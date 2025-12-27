# 🐮 Cattle Information Intelligent Display Platform | 牛只信息智能展示平台

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Backend Status](https://img.shields.io/badge/backend-Spring%20Boot-green.svg)]()
[![Frontend Status](https://img.shields.io/badge/frontend-Vue.js%202.0-brightgreen.svg)]()

> An integrated solution for non-contact cattle body dimension measurement and intelligent ranch management data visualization.
> 
> 一个集成了非接触式牛只体尺测量与智慧牧场管理数据可视化的综合解决方案。

---

**🐮🐮🐮 Preface**: We have recently completed a new research project. A concise overview of this work can be found in the poster below.  

**🐮🐮🐮 前言**：我们近期完成了一项新的研究工作，您可以从下方海报中获取该研究的简要概述： 
<p align="center">
  <img src="https://raw.githubusercontent.com/XingshiXu/Cow_Inf_Platform/main/动物骨架.gif" alt="动物骨架 GIF" width=200">
</p>

![工作海报](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/Poster.jpg)

## 🇨🇳 🇬🇧 中文与英文介绍
~~*(The English version is currently being organized and will be released shortly.)*  --2025.11.05~~  
*(This document is bilingual. The English version precedes the Chinese version below.)*--2025.12.27

### 📖 Project Overview

Welcome to the **Intelligent Cattle Information Platform** project repository.

We have developed a complete supporting system, including a **smart acquisition device**, a **database system**, and a **data visualization platform**. This system aims to provide modern dairy farms with an intuitive and comprehensive digital management solution for body size data.

Through this platform, farmers can access real-time information at both individual and herd levels, enabling data-driven decision-making and significantly enhancing the efficiency and intelligence of farm management.

---

### 📖 项目概述

欢迎访问 **牛只信息智能展示平台** 项目仓库。

我们开发了一套完整的配套系统，包含**智能采集设备**、**数据库系统**及**数据展示平台**。该系统旨在为现代牧场提供直观、全面的体尺数据数字化管理模式。

通过本平台，养殖者能够及时掌握奶牛个体层面与群体层面的信息，辅助科学决策，从而显著提升牧场管理的效率与智能化水平。

***

### ✨ Core Features

*   **Non-Contact Measurement**: Easily perform non-contact body size measurements of cattle through a Graphical User Interface (GUI) on a portable terminal device. [![Click to view slider image](https://imgsli.com/NDA3NjY5/thumb)](https://imgsli.com/NDA3NjY5)
*   **Automated Data Flow**: Collected body size data is automatically transmitted to a cloud-based MySQL database.
*   **Visualized Management Platform**: A web platform based on a Browser-Server (B/S) architecture for visualized data management.
*   **Individual Tracking**: Supports querying the historical body size data of a single cow.
*   **Herd-level Analysis**: Provides statistical and analytical functions for the herd's status, dynamically displayed through charts.

---

### ✨ 核心功能

*   **非接触式测量**：利用便携式终端设备，通过用户交互界面（GUI）便捷完成牛体尺的非接触式测量。 [![点击查看滑块图像](https://imgsli.com/NDA3NjY5/thumb)](https://imgsli.com/NDA3NjY5)
*   **自动化数据流**：采集到的体尺数据自动传输至云端 MySQL 数据库。
*   **可视化管理平台**：基于 B/S 架构的 Web 平台，实现数据的可视化管理。
*   **个体追溯**：支持查询单头牛只的历史体尺数据。
*   **群体分析**：具备群体状态的统计与分析功能，并通过图表动态展示。

***

### 🏗️ Showcase

This repository primarily showcases two components: the **Edge Acquisition Terminal** and the **Data Visualization Platform**.

#### 1. Body Size Acquisition Terminal (Hardware)

> ![Device Image](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/Device.png)
> <br>
> *(Image: Body measurement device)*

#### 2. Data Visualization Platform (Database & Interface)

The platform is built on a B/S architecture with a frontend-backend separation design.

| Technology Stack | Technologies Used |
| :--- | :--- |
| **Backend** | Java, integrating Spring Boot & MyBatis-Plus frameworks |
| **Frontend** | JavaScript, using Vue 2.0 & ECharts for dynamic interaction and data visualization |
| **Database**| MySQL |

> [![Platform Video](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/视频播放.jpg?raw=true)](https://www.youtube.com/watch?v=dJ8z9_nfSyc)
> <br>
> *(Video: Information management platform (A two-minute overview of the main features))*

> ![Platform GIF](https://raw.githubusercontent.com/XingshiXu/Cow_Inf_Platform/main/PlatformFunction.gif)
> <br>
> *(GIF: A quick overview of the platform)*

---

### 🏗️ 功能展示

本repo主要展示**边缘采集终端**和**数据展示平台**两部分。

#### 1. 体尺数据采集终端 (硬件)

> ![设备图片](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/Device.png)
> <br>
> *(图： Body measurement device)*

#### 2. 数据展示平台 (数据库与界面)

平台基于 B/S 架构构建，前后端分离设计。

| 技术栈 | 采用技术 |
| :--- | :--- |
| **后端 (Backend)** | Java 语言, 集成 Spring Boot 与 MyBatis-Plus 框架 |
| **前端 (Frontend)** | JavaScript 语言, 结合 Vue 2.0 与 ECharts 等组件实现动态交互与数据可视化 |
| **数据库 (Database)**| MySQL |

> [![平台视频](https://github.com/XingshiXu/Cow_Inf_Platform/blob/main/视频播放.jpg?raw=true)](https://www.youtube.com/watch?v=dJ8z9_nfSyc)
> <br>
> *(视频： Information management platform （两分钟让您了解平台的主要功能）)*

> ![平台动图](https://raw.githubusercontent.com/XingshiXu/Cow_Inf_Platform/main/PlatformFunction.gif)
> <br>
> *(GIF： 您同样可以通过动图快速简要的了解)*

***

### 🔄 System Workflow

1.  **Data Acquisition**: The operator performs measurements on cattle via the GUI of the terminal device (Jetson AGX Orin + Stereo Camera).
2.  **Data Transmission**: Measurement results are automatically uploaded to the server.
3.  **Data Storage**: Data is securely stored in the MySQL database.
4.  **Data Visualization**: Users access the web platform to view historical data for individual cattle and a herd-level statistical dashboard powered by ECharts.

---

### 🔄 系统工作流程

1.  **数据采集**：操作者通过终端设备（Jetson AGX Orin + 双目相机）的 GUI 界面完成牛只测量。
2.  **数据传输**：测量结果自动上传至服务器。
3.  **数据存储**：数据安全存储于 MySQL 数据库中。
4.  **数据可视化**：用户通过 Web 平台访问，查看个体牛只历史数据以及基于 ECharts 的群体统计大屏。

***

### 🔬 Practical Application & User Feedback

Practical application tests provided valuable insights into the system's performance and usability in real-world scenarios. In a test where the device was carried by an operator, they were able to complete the measurement and data upload for a batch of 10 cooperative cattle within approximately 3 minutes. This demonstrated the system's potential for high operational efficiency in real-world farm settings.

However, these tests also highlighted practical limitations. The current battery life of approximately 2 hours indicates that for continuous, large-scale deployment, power management optimizations or a wired power source would be necessary. Furthermore, informal feedback from farm operators was highly encouraging. They appreciated the non-intrusive nature of the measurement process and found the data visualization platform to be intuitive. A recurring suggestion was the desire for a more lightweight and ruggedized hardware design for ease of use. Operators also expressed strong interest in potential future functions, such as automated lameness detection and Body Condition Scoring (BCS), which confirms the practical value of expanding the platform's capabilities. These findings are invaluable for guiding the future iterations of our system.

---

### 🔬 实际应用与用户反馈

实际应用测试为我们系统的性能和在真实场景中的可用性提供了宝贵的见解。在一次由操作员背负设备的测试中，我们能够在大约3分钟内完成对10头配合牛只的测量和数据上传。这展示了该系统在真实牧场环境中具有很高的操作效率潜力。

然而，这些测试也凸显了一些实际的局限性。目前大约2小时的电池续航表明，对于连续、大规模的部署，电源管理的优化或有线电源将是必要的。此外，来自农场操作人员的交流反馈非常令人鼓舞。他们欣赏该测量过程的非侵入性，并认为数据可视化平台非常直观。一个反复出现的建议是希望硬件能有更轻便、更坚固耐用的设计，以方便使用。操作人员还对未来的潜在功能（如自动化跛行检测和体况评分BCS）表达了强烈兴趣，这证实了扩展平台功能的实用价值。这些发现对于指导我们系统的未来迭代至关重要。

***

### 📚 References & More Information

*   **Hardware Design Reference**: Xingshi Xu, et. al., (2024), "Boosting cattle face recognition under uncontrolled scenes by embedding enhancement and optimization," *Applied Soft Computing*, 164, 111951.
*   **More Information**:
    *   Find more of our work here: [Link](https://github.com/XingshiXu/TeamWorks) ✨

---

### 📚 参考文献与更多信息

*   **硬件设计参考**：Xingshi Xu, et. al., (2024), Boosting cattle face recognition under uncontrolled scenes by embedding enhancement and optimization, *Applied Soft Computing*, 164.111951。
*   **更多信息**：
    *   在此处查找我们的更多工作：[链接](https://github.com/XingshiXu/TeamWorks)✨

---

<p align="center">
  Created with ❤️ by XingshiXu (NWAFU & KU Lueven)
</p>
