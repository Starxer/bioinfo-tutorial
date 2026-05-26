# 03 — 环境管理：conda 与 mamba

> **学完本章你能**：用 conda 创建隔离的 Python/R 环境、安装生信软件、导出分享环境配置、区分 conda 和 pip 的用法

---

## 1. 为什么需要环境管理？

想象这个场景：

- 工具 A 需要 Python 3.8 + numpy 1.19
- 工具 B 需要 Python 3.10 + numpy 1.26

如果装在一起，必然有一方用不了。**环境管理**让你可以为每个项目创建独立的"工具箱"。

> **conda 和 mamba** 是同一类工具。mamba 用 C++ 重写了 conda 的依赖解析，速度快得多，命令基本兼容。**推荐直接用 mamba**。

---

## 2. conda / mamba 安装

如果你用 Miniconda 或 Miniforge，安装后打开终端试试：

```bash
# 验证是否已安装
conda --version
mamba --version
```

如果还没装，去下载 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 或 [Miniforge](https://github.com/conda-forge/miniforge)（推荐，包含 mamba）：

```bash
# Linux 安装 Miniforge
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

> **提示**：安装时选 Yes 初始化 conda。安装后关掉终端重新打开生效。

---

## 3. 核心命令——环境管理

```bash
# 创建环境（指定 Python 版本）
mamba create -n myenv python=3.10

# 创建环境并同时安装多个包
mamba create -n rnaseq python=3.9 fastqc multiqc star samtools

# 激活环境
mamba activate myenv

# 退出环境
mamba deactivate

# 列出所有环境
mamba env list

# 删除环境
mamba remove -n myenv --all

# 克隆环境
mamba create -n newenv --clone oldenv
```

> **命名规范**：环境名用英文，建议按项目或功能命名，如 `rnaseq`、`assembly`、`py310`。

---

## 4. 核心命令——包管理

激活环境后，安装软件包：

```bash
# 搜索包
mamba search samtools

# 安装包
mamba install samtools

# 从特定频道（channel）安装
mamba install -c bioconda samtools
mamba install -c conda-forge -c bioconda salmon

# 指定版本
mamba install samtools=1.20

# 更新包
mamba update samtools

# 列出当前环境已安装的包
mamba list
```

### 重要的频道（Channel）

| 频道 | 用途 | 例子 |
|------|------|------|
| `conda-forge` | 通用软件、Python 包 | `numpy`, `pandas`, `scipy` |
| `bioconda` | **生信软件的主阵地** | `samtools`, `bwa`, `fastqc` |
| `defaults` | Anaconda 官方 | 一般不优先用 |
| `r` | R 语言包 | `r-base`, `r-ggplot2` |

> **安装顺序建议**：`conda-forge` 优先，再 `bioconda`，最后 `defaults`。同时指定：`-c conda-forge -c bioconda`

---

## 5. 安装 R 和 R 包

```bash
# 创建 R 环境
mamba create -n r-env r-base=4.3

# 激活后安装 R 包
mamba install -c conda-forge r-tidyverse r-ggplot2 r-DESeq2

# 或进入 R 后 install.packages("包名")
```

> **注意**：R 包在 conda 里前缀是 `r-`。用 conda 装 R 包比 R 自带的 `install.packages()` 更稳定，因为依赖自动解决。

---

## 6. conda install vs pip install——什么时候用哪个？

这是新手最容易困惑的地方。

| 对比维度 | `conda install` | `pip install` |
|---------|----------------|--------------|
| **软件类型** | 任何软件（Python/R/C/二进制） | 仅 Python 包 |
| **依赖解析** | 自动处理非 Python 依赖（如 libssl） | 只解析 Python 包依赖 |
| **冲突处理** | 强（安装前会检查所有依赖） | 弱（可能装完发现冲突） |
| **速度** | 慢一些（但 mamba 快多了） | 快 |
| **来源** | conda channel（conda-forge/bioconda） | PyPI |

**最佳实践：**

```bash
# 优先 conda/mamba，覆盖不了的东西再用 pip
mamba install -c conda-forge -c bioconda pytables pandas numpy
pip install biopython  # bioconda 上版本不新时用 pip
# 或者更好的方式：在 environment.yml 里同时用 pip
```

---

## 7. 分享环境——environment.yml

写好这份文件，别人就能一秒复刻你的环境：

```yaml
name: rnaseq
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.10
  - fastqc=0.12
  - multiqc=1.20
  - star=2.7
  - samtools=1.20
  - subread=2.0   # featureCounts
  - r-base=4.3
  - r-deseq2
  - pip
  - pip:
    - pysam
    - cutadapt
```

别人拿到后：

```bash
mamba env create -f environment.yml
```

> **养成好习惯**：每个项目在根目录放一个 `environment.yml`，标注日期和用途。
> 导出当前环境用：`mamba env export > environment.yml`（导出的文件会包含具体版本号，更精确）

---

## 参考资料

- [conda 官方文档](https://docs.conda.io/en/latest/)
- [Miniforge 安装](https://github.com/conda-forge/miniforge)
- [bioconda 首页](https://bioconda.github.io/)
- [mamba 项目](https://github.com/mamba-org/mamba)

---

## 小结

- 环境管理解决"不同工具需要不同版本"的问题
- 常用命令：`create` → `activate` → `install` → `deactivate` → `env export`
- 频道顺序：`conda-forge` > `bioconda` > `defaults`
- conda 装任何软件，pip 只装 Python 包 — 先 conda 后 pip
- 每个项目配一个 `environment.yml`，方便复现

### 练练手

1. 创建一个 `biostudy` 环境（Python 3.10），安装 fastqc 和 multiqc
2. 激活环境后运行 `fastqc --version` 确认安装成功
3. 退出环境，再激活，试试 `mamba list` 看看装了哪些包
4. 导出当前环境为 `environment.yml`，看看内容
