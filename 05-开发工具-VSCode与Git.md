# 05 — 开发工具：VS Code、Markdown 与 Git

> **学完本章你能**：用 VS Code 在服务器上写代码、用 Markdown 写笔记和文档、用 Git 跟踪代码变化、用 Obsidian/Notion 管理科研笔记

---

## 1. VS Code：一个编辑器管所有事

VS Code（Visual Studio Code）是目前最流行的代码编辑器。对生信来说，它的三个核心功能：

### 功能一：代码编辑 + 语法高亮

- 支持 Python、R、Shell、Markdown、JSON 等**几乎所有格式**
- 自动缩进、括号匹配、智能提示
- 自带终端（不用来回切窗口）

### 功能二：Remote-SSH——连到服务器上写代码

这是生信最常用的功能——你的 VS Code 在本地，但文件在服务器上。

1. 安装 Remote - SSH 扩展（Extension）
2. 按 `F1` → 输入 `Remote-SSH: Connect to Host...`
3. 输入服务器地址如 `ssh ubuntu@123.207.3.78`
4. 连上后左侧文件浏览器显示服务器上的文件

> **VS Code 也能写 Markdown**：新建 `.md` 文件就能写，右侧即时预览。写生信流程文档、实验记录非常方便。

### 功能三：集成的 Git 界面

左侧的"源代码管理"（Source Control）选项卡，可以图形化完成 add → commit → push，不用记 git 命令。

> 参考：[菜鸟教程 VS Code](https://www.runoob.com/vscode/vscode-tutorial.html)

---

## 2. Markdown——写文档和笔记的通用语言

**Markdown** 是一种轻量级标记语言，让你用纯文本写出带格式的文档。你现在看到的这篇教程就是 Markdown 写的。

### 为什么要学 Markdown？

- **纯文本格式**：永远不依赖某个软件（VS Code、Obsidian、Typora 都能打开）
- **生信标配**：GitHub 的 README、Snakemake 注释、项目文档全是 Markdown
- **跟代码共存**：和脚本放在同一个仓库里，版本控制一起管理

### 10 分钟学会 Markdown

```markdown
# 一级标题
## 二级标题
### 三级标题

**加粗**  *斜体*  `行内代码`

- 无序列表项
- 另一项

1. 有序列表
2. 第二项

[链接文字](https://example.com)

![图片说明](图片路径.png)

> 引用块——用来写重要提示

`​``bash
# 代码块——用来贴命令或代码
echo "Hello bioinfo"
`​``

| 列1 | 列2 |
|-----|-----|
| 单元格 | 单元格 |
```

**在 VS Code 里写 Markdown**：
- 新建 `xxx.md` 文件，直接写
- 按 `Ctrl+Shift+V` 打开实时预览
- 安装 Markdown All in One 扩展，自动补全表格、目录

### Markdown + 笔记软件

Markdown 文件可以用各种软件来管理和浏览：

| 软件 | 平台 | 定位 | 适合做什么 |
|------|------|------|-----------|
| **VS Code** | 全平台 | 编辑器 | 写 README、方法文档，跟代码放一起 |
| **Obsidian** | 全平台 | 知识管理 | **科研笔记、文献笔记、双向链接知识库** |
| **Notion** | 全平台 | 协作+数据库 | 实验记录、项目看板、团队协作 |
| **Typora** | 全平台 | 所见即所得 | 快速写漂亮的 Markdown 文档 |

---

## 3. Obsidian——搭建你的生信知识库

**适合场景**：个人笔记、文献整理、建立知识点之间的关联。

### Obsidian 的核心能力

- **纯本地 Markdown 文件**：所有笔记存成 `.md` 文件，不依赖云服务
- **双向链接**：`[[另一篇笔记]]` 可以链接到任何其他笔记，自动生成知识图谱
- **标签系统**：用 `#标签名` 分类组织
- **图谱视图**：可视化展示笔记之间的关联（适合发现知识盲区）

### 科研笔记的典型用法

```
你的 Obsidian 仓库/
├── 文献笔记/          # 读过的论文
│   ├── 2024-Smith-RNA-seq方法.md
│   └── 2025-Li-家蚕免疫.md
├── 实验记录/          # 实验步骤和结果
│   ├── RNA提取-2025-03-20.md
│   └── 差异表达分析-2025-04-01.md
├── 会议/              # 讲座和组会笔记
│   └── 2025-04-15-组会-转录组方案.md
├── 生信入门教程/       # 各种学习资料
│   └── 01-Linux基础命令行.md
└── 概念/              # 关键概念解释
    ├── 转录组学.md
    └── 差异表达分析.md
```

```markdown
# 在笔记里链接其他笔记
这篇文章使用了 [[STAR 比对器]] 进行比对，
然后通过 [[DESeq2]] 做差异表达分析。
See also: [[RNA-seq 分析流程]]
```

> **Obsidian 的杀手锏**：笔记之间的 `[[双向链接]]` 形成一个知识网络，当你复习"差异表达分析"时，能看到所有跟它关联的文献、实验记录和方法笔记。

---

## 4. Notion——团队协作和项目管理

**适合场景**：多人协作的实验记录、项目进度追踪。

### Notion 和 Obsidian 的区别

| 对比 | Obsidian | Notion |
|------|----------|--------|
| 文件存储 | 本地 `.md` 文件 | 云端数据库 |
| 离线使用 | 完全离线 | 需要网络 |
| 协作 | 自己用，或通过 Git 同步 | 多人实时编辑 |
| 灵活性 | 自由度高，插件多 | 模板丰富，结构更规整 |
| 适用场景 | 个人知识管理 | 团队项目协作 |

> **简单建议**：个人的学习笔记和文献整理用 Obsidian；实验记录和数据如果需跟同门分享，用 Notion 建个共享页面。

---

## 5. Git：版本控制——"后悔药"和"时间机器"

Git 是程序员用的版本控制系统。核心功能：

- **记录每次修改**，随时可以回退到任意历史版本
- **分支开发**，互不干扰（但生信新手可以先不碰分支）
- **GitHub/GitLab**：把代码存在云端，方便分享和协作

### Git 最小工作流

你只需要记住 5 个命令：

```bash
# 1. 在项目目录初始化仓库（只需一次）
cd /path/to/your/project
git init

# 2. 看看哪些文件被修改了
git status

# 3. 把文件加入暂存区（"我要备份这个文件"）
git add script.py
git add .              # 添加所有文件（谨慎！别提交大文件）

# 4. 提交（"拍照存档"）
git commit -m "添加了差异表达分析脚本"

# 5. 同步到 GitHub（如果需要）
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```

**新手的典型一天：**

```bash
# 早上开始干活
git status                # 看看昨天干到哪了

# 写代码…写完一部分
git add script.py
git commit -m "完成了DESeq2差异分析"

# 继续写…发现写错了
git checkout -- script.py # 撤销修改，回到上次commit的状态
```

### .gitignore——别提交没用的文件

在项目根目录创建 `.gitignore` 文件：

```
# 不要提交这些
__pycache__/
*.pyc
.DS_Store
*.fastq
*.bam
*.vcf
data/raw/
results/
```

> **为什么大数据文件不能提交到 Git？** Git 会把每个版本的文件完整保存，几个 GB 的 fastq 文件提交几次后仓库会膨胀到几十 GB。

### 互动学习

- [Learn Git Branching](https://learngitbranching.js.org/) — 在浏览器里交互式学 Git，**强烈推荐**
- [菜鸟教程 Git](https://www.runoob.com/git/git-tutorial.html)

---

## 6. 项目目录组织——让以后的自己和合作者能看懂

一个良好的项目结构，比你用多么复杂的工具都重要。

```
project-name/
├── README.md              # 项目简介（做什么、怎么做）
├── environment.yml        # 环境配置（一键复现）
├── .gitignore             # Git 忽略规则
├── data/
│   ├── raw/               # 原始数据（只读，绝不修改）
│   └── processed/         # 清洗/预处理后的数据
├── scripts/               # 分析脚本
│   ├── 01_quality_control.sh
│   ├── 02_alignment.sh
│   └── 03_differential_expression.R
├── results/               # 输出结果（图表、表格）
│   ├── figures/
│   └── tables/
├── docs/                  # 文档
│   └── methods.md
└── src/                   # 可复用的模块/函数
    └── utils.py
```

**关键原则：**

| 原则 | 说明 |
|------|------|
| **原始数据只读** | `data/raw/` 下的文件永不手动修改，保证可追溯 |
| **脚本可重复** | 从 `data/raw/` → `results/` 的整个流程，一键运行 |
| **结果不提交 Git** | results/ 加到 .gitignore，看结果看文件本身就行 |
| **README 写清楚** | 项目目标、数据来源、步骤说明，方便半年后的自己 |

> 这个结构不是死的——小项目可以简化，大项目会更复杂。关键是"**别人（包括未来的你）能看懂**"。

---

## 7. 写一个简单的 Snakefile（工作流管理简介）

当你需要跑多个步骤（质控 → 比对 → 定量 → 差异分析），手动一步步跑容易出错。工作流管理工具可以自动处理依赖和并行。

**Snakemake**（基于 Python 的工作流工具）：

```python
# Snakefile 示例
rule all:
    input: "results/diff_expression.csv"

rule fastqc:
    input: "data/raw/sample1.fastq"
    output: "results/qc/sample1_fastqc.html"
    shell: "fastqc {input} -o results/qc/"

rule align:
    input: "data/raw/sample1.fastq"
    output: "results/aligned/sample1.bam"
    shell: "bwa mem reference.fa {input} | samtools sort -o {output}"
```

然后一行命令跑完整条流水线：

```bash
snakemake --cores 8
```

Snakemake 会自动判断哪个步骤需要跑、哪个步骤已有结果。**这就是"可重复性"的实践。**

---

## 参考资料

- [Markdown 教程](https://www.runoob.com/markdown/md-tutorial.html)
- [Obsidian 官方文档](https://help.obsidian.md/)
- [Notion 教程](https://www.notion.so/help)
- [VS Code 官方文档](https://code.visualstudio.com/docs)
- [VS Code Remote-SSH](https://code.visualstudio.com/docs/remote/ssh)
- [菜鸟教程 Git](https://www.runoob.com/git/git-tutorial.html)
- [Learn Git Branching 互动教程](https://learngitbranching.js.org/)
- [Snakemake 官方文档](https://snakemake.readthedocs.io/)

---

## 小结

- **Markdown** 是纯文本格式语言，你看到的这篇教程就是 MD 写的——学会它，啥笔记软件都能用
- **Obsidian**：个人知识管理，双向链接构建科研知识网络
- **Notion**：团队协作、实验记录共享
- **VS Code + Remote-SSH**：本地编辑服务器文件，效率翻倍
- **Git** 只需记 5 个命令：`init` → `add` → `commit` → `push` → `status`
- 项目组织三要素：README、environment.yml、data/scripts/results/ 分离
- 工作流管理（Snakemake）让你的分析可复现

### 练练手

1. 新建一个 `test.md`，用 Markdown 写一段带标题、列表、代码块、链接的笔记
2. 在 VS Code 里按 `Ctrl+Shift+V` 预览你的 Markdown
3. 用 Obsidian 创建一个笔记，用 `[[另一篇笔记]]` 做一次双向链接
4. 在服务器上创建一个空项目目录，`git init` 初始化
5. 按教程的项目结构创建 data/ scripts/ results/ 等子目录
6. 把 `test.md` 复制进来，`git add` 然后 `git commit`
7. 试试 `learngitbranching.js.org` 的交互式教程
