# 生信入门教程 🧬

面向**零基础**的生物信息学入门系列教程。

> **文字简洁、多图、重实操** —— 每篇 15–30 分钟，配合真实测序数据示例。

---

## 📚 教程结构

| # | 标题 | 你会学到 | 时间 |
|---|------|---------|------|
| 00 | [教程大纲与导航](00-教程大纲与导航.md) | 学习路线、参考合集 | 5 min |
| 01 | [Linux 基础命令行](01-Linux基础命令行.md) | SSH 连接、文件系统、管道、vim | 40 min |
| 02 | [测序技术入门](02-测序技术入门.md) | Sanger/NGS/TGS、FASTQ+FASTA 真实数据 | 20 min |
| 03 | [环境管理](03-环境管理-conda与mamba.md) | conda/mamba、频道配置、environment.yml | 20 min |
| 04 | [公共数据库与序列比对](04-公共数据库与序列比对.md) | NCBI/Ensembl/UCSC、BLAST 比对 | 25 min |
| 05 | [开发工具](05-开发工具-VSCode与Git.md) | VS Code Remote-SSH、Markdown、Git、Obsidian | 35 min |

**第二阶段（实战分析）** 计划中：

- 06 — Python 和 R 画图（火山图、进化树等）
- 07 — 完整运行一次转录组分析流程

---

## 🚀 快速开始

### 在线练习环境（无需本地安装）

教程提供在线练习服务器，配好 Ubuntu + conda + 常用生信工具，直接 SSH 连接即可上手：

```bash
ssh learner@starxer.cn -p 2222
```

> 联系管理员（微信/邮件/Issue）获取密码。练习环境仅供学习，请勿用于生产任务。

### 方式一：Obsidian（推荐）

```bash
git clone https://github.com/Starxer/bioinfo-tutorial.git
```

在 Obsidian 中「打开其他仓库」→ 选择克隆的文件夹，即可获得**双向链接 + 知识图谱**体验。

### 方式二：任意 Markdown 编辑器

VS Code、Typora、Notion 导入均可阅读。图片和链接全部本地化，无需联网。

---

## 🗺️ 推荐学习路线

```
01 → 02 → 03 → 04 → 05
```

先学会**连上服务器操作文件**（01），再理解**要处理的数据是什么**（02），然后**装工具**（03）、**找数据**（04），最后学会**规范管理项目和写文档**（05）。

> 有基础可以跳读：会 Linux 跳过 01，只想装环境看 03。

---

## 📸 教程特点

- **真实数据示例**：FASTQ 截取自家蚕（*Bombyx mori*）Illumina PE150 测序数据；FASTA 来自 NCBI 家蚕参考基因组 GCF_014905235.1
- **实物照片**：Illumina 流动池（Flow Cell）8 泳道实物照
- **矢量图示**：FASTQ 格式图解、Sanger vs NGS 鸟枪法对比（Metaso 来源）

> 图片仅用于教学，版权归原始出处所有。

---

---

## 🤝 反馈与贡献

教程有错误、建议或想补充内容？欢迎 [提 Issue](https://github.com/Starxer/bioinfo-tutorial/issues) 或直接 PR。

---

## 🤖 AIGC 声明

本教程由 **Hermes Agent** 调用 **DeepSeek V4 Flash** 语言模型辅助编写，配图经 **MiniMax mmx** 生成与验证。所有内容均经人工审核、修正和确认。

> 如发现由 AI 引入的错误，欢迎提 Issue 指正。

---

## 📄 许可

本教程文字内容采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 许可。引用的图片版权归原始出处所有，仅限教学使用。
