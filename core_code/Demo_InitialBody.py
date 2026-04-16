# 这是一个Sample demo 用于输出体尺并进行可视化展示。

# 1: Nose             # 2: Head             # 3: Neck
# 4: Wither           # 5: Back             # 6: Buttock
# 7: Ischium          # 8: Shoulder_L       # 9: Shoulder_R
# 10: Elbow_L         # 11: Elbow_R         # 12: Wrist_L
# 13: Wrist_R         # 14: Front_hoof_L    # 15: Front_hoof_R
# 16: Stifle_L        # 17: Stifle_R        # 18: Hock_L
# 19: Hock_R          # 20: Rear_hoof_L     # 21: Rear_hoof_R

import open3d as o3d
import numpy as np
import json
import cv2
import pandas as pd
from pathlib import Path

def load_keypoints_from_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    keypoints = {}
    for shape in data['shapes']:
        label = shape['label']
        point = shape['points'][0]
        keypoints[label] = point
    return keypoints


def pixel_to_camera_coords(x, y, depth, fx, fy, cx, cy):
    z = depth
    x3d = (x - cx) * z / fx
    y3d = (y - cy) * z / fy
    return np.array([x3d, y3d, z], dtype=np.float32)


def fit_ground_plane(pcd, distance_threshold=0.01, ransac_n=3, num_iterations=1000):
    plane_model, inliers = pcd.segment_plane(distance_threshold=distance_threshold,
                                             ransac_n=ransac_n,
                                             num_iterations=num_iterations)
    # 地面点染为蓝色
    colors = np.asarray(pcd.colors)
    colors[inliers] = [0.0, 0.5, 1.0]
    pcd.colors = o3d.utility.Vector3dVector(colors)

    return plane_model, inliers

def get_point_to_plane_distance(point, plane_model):
    a, b, c, d = plane_model
    x, y, z = point
    return abs(a*x + b*y + c*z + d) / np.linalg.norm([a, b, c])

def compute_measurements(keypoints_3d, plane_model):
    def distance(a, b):
        return np.linalg.norm(a - b)
    results = {}

    # 体斜长
    if '1' in keypoints_3d and '7' in keypoints_3d:
        head_x = keypoints_3d['1'][0]
        ischium_x = keypoints_3d['7'][0]
        if head_x > ischium_x and '9' in keypoints_3d:
            results['体斜长'] = distance(keypoints_3d['7'], keypoints_3d['9'])
        elif '8' in keypoints_3d:
            results['体斜长'] = distance(keypoints_3d['7'], keypoints_3d['8'])

    # 体高（withers到地面）
    if '4' in keypoints_3d:
        results['体高'] = get_point_to_plane_distance(keypoints_3d['4'], plane_model)

    # 十字部高（buttock到地面）
    if '6' in keypoints_3d:
        results['十字部高'] = get_point_to_plane_distance(keypoints_3d['6'], plane_model)

    return results

def visualize_keypoints_on_pointcloud(pcd, keypoints_3d, plane_model=None):
    geometries = [pcd]

    for label in ["4", "6", "7", "8"]:
        if label in keypoints_3d:
            sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.02)
            sphere.paint_uniform_color([1, 0, 0])  # 红色
            sphere.translate(keypoints_3d[label])
            geometries.append(sphere)

    if plane_model is not None:
        a, b, c, d = plane_model
        normal = np.array([a, b, c])
        normal /= np.linalg.norm(normal)

        def project_point_to_plane(p, normal, d):
            distance = (np.dot(normal, p) + d)
            return p - distance * normal

        if "4" in keypoints_3d:
            p_withers = keypoints_3d["4"]
            p_proj_withers = project_point_to_plane(p_withers, normal, d)
            line_wither = o3d.geometry.LineSet(
                points=o3d.utility.Vector3dVector([p_withers, p_proj_withers]),
                lines=o3d.utility.Vector2iVector([[0, 1]])
            )
            line_wither.colors = o3d.utility.Vector3dVector([[1, 0, 0]])
            geometries.append(line_wither)

        if "6" in keypoints_3d:
            p_buttock = keypoints_3d["6"]
            p_proj_buttock = project_point_to_plane(p_buttock, normal, d)
            line_buttock = o3d.geometry.LineSet(
                points=o3d.utility.Vector3dVector([p_buttock, p_proj_buttock]),
                lines=o3d.utility.Vector2iVector([[0, 1]])
            )
            line_buttock.colors = o3d.utility.Vector3dVector([[0, 1, 0]])
            geometries.append(line_buttock)

        if "7" in keypoints_3d and "1" in keypoints_3d:
            p_ischium = keypoints_3d["7"]
            p_nose = keypoints_3d["1"]
            if p_nose[0] > p_ischium[0] and "9" in keypoints_3d:
                p_shoulder = keypoints_3d["9"]
            elif "8" in keypoints_3d:
                p_shoulder = keypoints_3d["8"]
            else:
                p_shoulder = None

            if p_shoulder is not None:
                line_body_length = o3d.geometry.LineSet(
                    points=o3d.utility.Vector3dVector([p_ischium, p_shoulder]),
                    lines=o3d.utility.Vector2iVector([[0, 1]])
                )
                line_body_length.colors = o3d.utility.Vector3dVector([[0, 0, 1]])
                geometries.append(line_body_length)

    o3d.visualization.draw_geometries(geometries)

def main(image_path, depth_path, label_path, csv_output_path,
         fx=1067.870, fy=1067.840, cx=969.510, cy=537.386):
    # 读取图像和深度图
    color_img = cv2.imread(str(image_path))
    color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
    depth_map = np.load(str(depth_path)).astype(np.float32) / 1000.0  # mm -> m

    H, W = depth_map.shape

    keypoints_2d = load_keypoints_from_json(label_path)
    keypoints_3d = {}

    # 取参考关键点深度（Head(2), Neck(3), Wither(4)）
    ref_labels = ['2', '3', '4']
    ref_depths = []
    for rl in ref_labels:
        if rl in keypoints_2d:
            x_ref, y_ref = keypoints_2d[rl]
            x_int_ref, y_int_ref = int(round(x_ref)), int(round(y_ref))
            if 0 <= x_int_ref < W and 0 <= y_int_ref < H:
                z_ref = depth_map[y_int_ref, x_int_ref]
                if z_ref > 0:
                    ref_depths.append(z_ref)
    ref_depth_median = np.median(ref_depths) if len(ref_depths) > 0 else None

    # 获取肩膀关键点深度(Shoulder_L=8, Shoulder_R=9)
    shoulder_depths = {}
    for shoulder_label in ['8', '9']:
        if shoulder_label in keypoints_2d:
            x_s, y_s = keypoints_2d[shoulder_label]
            x_int_s, y_int_s = int(round(x_s)), int(round(y_s))
            if 0 <= x_int_s < W and 0 <= y_int_s < H:
                z_s = depth_map[y_int_s, x_int_s]
                if z_s > 0:
                    shoulder_depths[shoulder_label] = z_s

    for label, (x, y) in keypoints_2d.items():
        x_int, y_int = int(round(x)), int(round(y))
        if not (0 <= x_int < W and 0 <= y_int < H):
            continue
        z = depth_map[y_int, x_int]
        if z <= 0:
            continue

        print(f"关键点 {label} 深度: {z:.3f} m")  # 打印原始深度
        keypoints_3d[label] = pixel_to_camera_coords(x, y, z, fx, fy, cx, cy)

    # 点云生成和地平面拟合
    u, v = np.meshgrid(np.arange(W), np.arange(H))
    valid = (depth_map > 0) & (depth_map < 10.0)
    Z = depth_map[valid]
    X = (u[valid] - cx) * Z / fx
    Y = (v[valid] - cy) * Z / fy
    points = np.stack([X, Y, Z], axis=-1)
    colors = color_img[v[valid], u[valid]] / 255.0
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    plane_model, inliers = fit_ground_plane(pcd)

    measurements = compute_measurements(keypoints_3d, plane_model)

    print("\n🐄 体尺测量结果：")
    for k, v in measurements.items():
        print(f"{k}: {v:.3f} m")

    visualize_keypoints_on_pointcloud(pcd, keypoints_3d, plane_model)

    df = pd.DataFrame([measurements])
    df.to_csv(csv_output_path, index=False)
    print(f"✅ 测量结果已保存: {csv_output_path}")

# ========== 示例路径配置 ==========
image_path = Path(r"Your\Path\Left_image\000001017.png")
depth_path = Path(r"Your\Path\Depth_image\000001017.npy")
label_path = Path(r"Your\Path\Label\000001017.json")
csv_output_path = Path(r"Your\Path\XXXX.csv")

main(image_path, depth_path, label_path, csv_output_path)
