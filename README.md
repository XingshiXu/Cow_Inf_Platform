# 🐮 Cattle Information Intelligent Display Platform | 牛只信息智能展示平台

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Backend Status](https://img.shields.io/badge/backend-Spring%20Boot-green.svg)]()
[![Frontend Status](https://img.shields.io/badge/frontend-Vue.js%202.0-brightgreen.svg)]()

> An integrated solution for non-contact cattle body dimension measurement and intelligent ranch management data visualization.
> 
> 一个集成了非接触式牛只体尺测量与智慧牧场管理数据可视化的综合解决方案。

---
**前言**：我们完成了一项新的工作，您可以在下面的海报中获得简要的信息：   
![工作海报](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/Poster.jpg)


## 🇨🇳 中文介绍 (Chinese Version)

### 📖 项目概述

欢迎访问 **牛只信息智能展示平台** 项目仓库。

我们开发了一套完整的配套系统，包含**智能采集设备**、**数据库系统**及**数据展示平台**。该系统旨在为现代牧场提供直观、全面的体尺数据数字化管理模式。

通过本平台，养殖者能够及时掌握奶牛个体层面与群体层面的信息，辅助科学决策，从而显著提升牧场管理的效率与智能化水平。

### ✨ 核心功能

*   **非接触式测量**：利用便携式终端设备，通过用户交互界面（GUI）便捷完成牛体尺的非接触式测量。[![点击查看滑块图像](https://imgsli.com/NDA3NjY5/thumb)](https://imgsli.com/NDA3NjY5)
*   **自动化数据流**：采集到的体尺数据自动传输至云端 MySQL 数据库。
*   **可视化管理平台**：基于 B/S 架构的 Web 平台，实现数据的可视化管理。
*   **个体追溯**：支持查询单头牛只的历史体尺数据。
*   **群体分析**：具备群体状态的统计与分析功能，并通过图表动态展示。

### 🏗️ 功能展示

本repo主要展示**边缘采集终端**和**数据展示平台**两部分。

#### 1. 体尺数据采集终端 (硬件)
  
> **![设备图片](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/Device.png)**
> <br>
> *(图： Body measurement device)*
  
#### 2. 数据展示平台 (数据库与界面)

平台基于 B/S 架构构建，前后端分离设计。

| 技术栈 | 采用技术 |
| :--- | :--- |
| **后端 (Backend)** | Java 语言, 集成 Spring Boot 与 MyBatis-Plus 框架 |
| **前端 (Frontend)** | JavaScript 语言, 结合 Vue 2.0 与 ECharts 等组件实现动态交互与数据可视化 |
| **数据库 (Database)**| MySQL |


> [![平台视频](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/视频播放.jpg?raw=true)](https://www.youtube.com/watch?v=IYBWnM-T8Yc)
> <br>
> **(视频： Information management platform （两分钟让您了解平台的主要功能）)**

>  **![设备图片](https://raw.githubusercontent.com/XingshiXu/Cow_Inf_Platform/main/PlatformFunction.gif)**
>  <br>
> **(GIF： 您同样可以通过动图快速简要的了解)**

### 🔄 系统工作流程

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
