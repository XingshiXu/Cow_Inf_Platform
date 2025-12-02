# 🐮 Cattle Information Intelligent Display Platform | 牛只信息智能展示平台

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Backend Status](https://img.shields.io/badge/backend-Spring%20Boot-green.svg)]()
[![Frontend Status](https://img.shields.io/badge/frontend-Vue.js%202.0-brightgreen.svg)]()

> An integrated solution for non-contact cattle body dimension measurement and intelligent ranch management data visualization.
> 
> 一个集成了非接触式牛只体尺测量与智慧牧场管理数据可视化的综合解决方案。

---

## 🇬🇧 English Version

### 📖 Overview

Welcome to the **Cattle Information Intelligent Display Platform** repository.

To further promote the practical application of advanced agricultural models, we have developed a comprehensive ecosystem comprising intelligent data acquisition hardware, a robust database system, and an interactive web-based data display platform. This system aims to provide intuitive and comprehensive digital management for modern ranching.

Through this platform, farmers can realize real-time understanding of herd dynamics and receive support for scientific decision-making, significantly improving the efficiency and intelligence level of ranch management.

### ✨ Key Features

*   **Non-Contact Measurement:** Utilizes portable terminal devices for rapid, non-contact measurement of cattle body dimensions via a user-friendly GUI.
*   **Automated Data Pipeline:** Collected data is automatically transmitted from the edge device to a central MySQL database.
*   **Visual Management Platform:** A B/S architecture web platform for visualizing cattle data.
*   **Individual Tracking:** Supports querying historical body dimension data for single cattle.
*   **Herd Analysis:** Provides statistical analysis and visualization of the entire herd's status.

### 🏗️ System Architecture

The system is composed of two main parts: the **Edge Acquisition Terminal** and the **Data Display Platform**.

#### 1. Edge Acquisition Terminal (Hardware)

The proposed measurement model is deployed on a custom-designed terminal device. The design references our previous work *(Xu et al., 2024)*.

*   **Deployment Modes:** Can be carried by a farmer (backpack mode) or fixed on a tripod.
*   **Core Hardware:**
    *   **Compute:** Nvidia Jetson AGX Orin (for AI model inference)
    *   **Sensors:** Binocular Camera
    *   **Interaction:** Touchscreen Display
    *   **Power & Aux:** Dedicated power supply and auxiliary modules.

> **[Place Holder for Figure 13(a): Image of the Device]**
> <br>
> *(Figure 1: The intelligent data acquisition terminal device)*

#### 2. Data Display Platform (Software Stack)

The platform is built on a B/S (Browser/Server) architecture.

| Stack | Technology Used |
| :--- | :--- |
| **Backend** | Java, Spring Boot, MyBatis-Plus |
| **Frontend** | JavaScript, Vue 2.0, ECharts (for data visualization) |
| **Database**| MySQL |

### 🔄 Workflow

1.  **Data Acquisition:** The operator uses the terminal device (Jetson AGX Orin + Camera) to measure cattle via the GUI.
2.  **Data Transmission:** Measurement results are automatically uploaded to the server.
3.  **Data Storage:** Data is securely stored in the MySQL database.
4.  **Data Visualization:** Users access the web platform to view individual animal history and herd statistics via dynamic ECharts dashboards.

### 📚 References & Further Information

*   **Hardware Design Reference:** Xu et al., 2024 (Citation details to be updated).
*   **More Information & Future Iterations:**
    *   Please check here for the latest updates and documentation: [Link to Project Website / Wiki / Related Paper]

---

## 🇨🇳 中文介绍 (Chinese Version)

### 📖 项目概述

欢迎访问 **牛只信息智能展示平台** 项目仓库。

为进一步推动所提 AI 模型在畜牧业的实际应用，我们开发了一套完整的配套系统，包含**智能采集设备**、**数据库系统**及**数据展示平台**。该系统旨在为现代牧场提供直观、全面的体尺数据数字化管理模式。

通过本平台，养殖者能够及时掌握牛群动态，辅助科学决策，从而显著提升牧场管理的效率与智能化水平。

### ✨ 核心功能

*   **非接触式测量**：利用便携式终端设备，通过用户交互界面（GUI）便捷完成牛体尺的非接触式测量。
*   **自动化数据流**：采集到的体尺数据自动传输至云端 MySQL 数据库。
*   **可视化管理平台**：基于 B/S 架构的 Web 平台，实现数据的可视化管理。
*   **个体追踪**：支持查询单头牛只的历史体尺数据。
*   **群体分析**：具备群体状态的统计与分析功能，并通过图表动态展示。

### 🏗️ 功能展示

本系统主要由**边缘采集终端**和**数据展示平台**两部分组成。

#### 1. 体尺数据采集终端 (硬件)



> **[此处放置硬件设备图片，例如原文中的图13(a)]**
> <br>
> *(图1：智能数据采集终端设备原型)*

#### 2. 数据展示平台 (软件技术栈)

平台基于 B/S 架构构建，前后端分离设计。

| 技术栈 | 采用技术 |
| :--- | :--- |
| **后端 (Backend)** | Java 语言, 集成 Spring Boot 与 MyBatis-Plus 框架 |
| **前端 (Frontend)** | JavaScript 语言, 结合 Vue 2.0 与 ECharts 等组件实现动态交互与数据可视化 |
| **数据库 (Database)**| MySQL |

### 🔄 工作流程

1.  **数据采集**：操作者通过终端设备（Jetson AGX Orin + 双目相机）的 GUI 界面完成牛只测量。
2.  **数据传输**：测量结果自动上传至服务器。
3.  **数据存储**：数据安全存储于 MySQL 数据库中。
4.  **数据可视化**：用户通过 Web 平台访问，查看个体牛只历史数据以及基于 ECharts 的群体统计大屏。

### 📚 参考文献与更多信息

*   **硬件设计参考**：Xingshi Xu, et. al., (2024), Boosting cattle face recognition under uncontrolled scenes by embedding enhancement and optimization, Applied Soft Computing, 164.111951。
*   **更多信息**：
    *   请在此处查找我们的更多工作：[链接](https://github.com/XingshiXu/TeamWorks)

---
<p align="center">
  Created with ❤️ by XingshiXu (NWAFU & KU Lueven)
</p>
