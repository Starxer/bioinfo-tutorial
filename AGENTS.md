# 生信入门教程 — Agent Context

## 项目概述

面向**零基础**的生物信息学入门系列教程。中文学，重实操，15–30 分钟一篇。
GitHub: `Starxer/bioinfo-tutorial`

## 目录结构

```
生信入门教程/
├── 00-教程大纲与导航.md          # 学习路线、参考合集
├── 01-Linux基础命令行.md          # SSH、文件系统、管道、vim
├── 02-测序技术入门.md             # Sanger/NGS/TGS、FASTQ/FASTA
├── 03-环境管理-conda与mamba.md   # conda/mamba、频道、env.yml
├── 04-公共数据库与序列比对.md     # NCBI/Ensembl/UCSC、BLAST
├── 05-开发工具-VSCode与Git.md    # Remote-SSH、Markdown、Git
├── 生信讨论小组大纲.md            # 讨论组规划
├── imgs/                          # 配图 (SVG/JPG/PNG ~30张)
├── scripts/                       # 配图生成脚本 (Python/matplotlib→SVG)
├── README.md
└── AGENTS.md
```

## 内容规范

- **数据来源**: 实测数据截取自家蚕 (*Bombyx mori*) Illumina PE150
- **配图流程**: Python/matplotlib → SVG（矢量），mmx vision 验证评分 ≥ 8/10
  - 避免用 mmx image generate（AI文字乱码）
  - 墙内搜图用 Metaso.cn，图从 files.metaso.cn CDN 下载
- **语言**: 中文为主，中英混术语
- **风格**: 文字简洁、多图、重实操，零基础可读

## 技术栈

| 用途 | 工具 |
|------|------|
| AI 写作辅助 | Hermes Agent + DeepSeek V4 Flash |
| 配图生成/验证 | MiniMax mmx (Vision) |
| 配图脚本 | Python + matplotlib → SVG |
| 本地渲染 | pandoc + xelatex (Noto Sans CJK SC) |

## Git 工作流

- 墙内环境，`git push` 超时 → 用 GitHub Contents API 或 Git Data API 绕过
- gh CLI 已登录可用：`gh api repos/.../contents/... -X PUT`
- 也可用 token 直连：`git push https://Starxer:token@github.com/...`
- 分支: `main`，直接推送（单人项目）

## AIGC 声明

教程已包含 AIGC 声明（README.md 底部），新章节也需自查更新。

## Obsidian 集成

本仓库位于 Obsidian vault 内，Markdown 文件支持双向链接和知识图谱。
