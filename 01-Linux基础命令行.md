# 01 — Linux 基础命令行

> **学完本章你能**：用 SSH 连接到服务器、认识 Linux 文件系统和基本命令、理解管道和重定向、用 vim 编辑文件

---

## 1. 为什么学生信要学 Linux？

生物信息学的运行环境绝大多数都是 Linux 系统。原因很简单：

- **服务器/集群**：大学和高性能计算中心（HPC）的服务器几乎全是 Linux
- **开源生态**：几乎所有生信软件（samtools, BWA, GATK, blast,...）首发的平台就是 Linux
- **命令行效率**：处理几千个测序文件，图形界面做不到，但一条 shell 命令就行
- **管道工作流**：把一个程序的输出直接接到下一个程序的输入，一步完成整个流程

> 对应到 Windows：Linux 里的终端 ≈ 你的 cmd/PowerShell，但强大得多。

---

## 2. 先认识终端

打开终端（Terminal），你会看到类似这样的提示符：

```
lyf@server:~$
```

各部分含义：

| 部分 | 含义 |
|------|------|
| `lyf` | 当前用户名 |
| `server` | 计算机名（主机名） |
| `~` | 当前所在目录（`~` = 家目录） |
| `$` | 普通用户的提示符（root 是 `#`） |

> **试试看**：打开终端，输入 `whoami` 看看你是谁，输入 `pwd` 看看你在哪。

---

## 3. SSH 连接——怎么连到服务器

生信分析不是在你自己的电脑上跑——而是连到**远程服务器或集群**上操作。SSH（Secure Shell）就是你通向服务器的"门"。

### 3.1 终端里直接用 ssh 命令

在 Linux / macOS 终端或 Windows PowerShell 里，一行命令就能连：

```bash
# 基本用法
ssh 用户名@服务器地址

# 示例：连到你实验室的服务器
ssh zhang@192.168.1.100

# 如果 SSH 端口不是默认的 22
ssh -p 2222 zhang@192.168.1.100
```

> **本教程提供在线练习服务器**，配好了 Ubuntu + conda + 常用生信工具，让你不用自己配机器。登录方式：
> ```bash
> ssh learner@starxer.cn -p 2222
> ```
> 密码联系管理员获取。

第一次连会问是否接受服务器密钥，输入 `yes` 然后回车，再输入密码就进去了。

### 3.2 SSH 客户端软件（图形界面，推荐新手用）

如果你更习惯图形界面，可以用专门的 SSH 客户端：

| 软件 | 平台 | 特点 | 推荐场景 |
|------|------|------|---------|
| **WindTerm** | Windows/Linux/macOS | 免费开源，界面现代，支持多标签、自动补全、文件传输 | ⭐ **首选推荐** |
| **Tabby (原 Terminus)** | Windows/Linux/macOS | 免费开源，颜值高，内置 SSH 管理 | 追求界面好看 |
| **PuTTY** | Windows 为主 | 老牌经典，轻量简单 | 快速临时连接 |
| **Windows Terminal** | Windows | 微软官方，支持多标签，配合 `ssh` 命令 | Windows 自带方案 |
| **Xterm** | Linux | Linux 原生 X 终端 | Linux 桌面用户 |

**推荐：WindTerm**
- 免费开源，功能完整
- 多标签页（同时连多个服务器）
- 内置文件管理器（拖拽上传/下载文件）
- 下载地址：https://github.com/kingToolbox/WindTerm

> **选哪个？** 在你自己电脑上，用 **WindTerm** 或 **Tabby** 最省心。到服务器上之后，vim 仍然是改配置文件的必会工具（后面会讲）。

### 3.3 ssh 密钥登录——不用每次输密码

每次都输密码很烦，配置密钥后免密登录：

```bash
# 1. 在本地生成密钥对（一直回车用默认）
ssh-keygen -t ed25519

# 2. 把公钥复制到服务器
ssh-copy-id ubuntu@123.207.3.78

# 3. 以后再 ssh 就不用密码了
ssh ubuntu@123.207.3.78
```

> 实验室集群和云服务器一般都支持密钥登录。特别是云服务器（腾讯云、阿里云）第一次创建时会让你设置密钥。

### 3.4 连接后做的第一件事

连上服务器后，先确认你在哪：

```bash
whoami    # 我是谁？
pwd       # 我在哪？
ls -la    # 这里有什么？
df -h     # 磁盘空间够不够？
free -h   # 内存还剩多少？
nproc     # 有几个 CPU 核心？
```

> **经验**：上服务器先跑 `df -h` 看磁盘，数据写到满盘就麻烦了。`/tmp` 空间通常不大，大文件不要放那里。

---

## 4. Linux 文件系统

Linux 里**一切皆文件**（目录也是文件）。所有文件从根`/`开始，形成一棵树。

![[imgs/linux-fhs-runob1.jpg]]

**生信常用目录速查：**

| 目录 | 用途 | 你什么时候会用到 |
|------|------|-----------------|
| `/home/你/` | 你的家目录 | **所有你的文件放这里** |
| `/tmp/` | 临时文件 | 跑流程时的中间文件扔这 |
| `/opt/` | 第三方软件 | conda/miniconda 装在这 |
| `/usr/local/` | 本地安装的程序 | 手动编译的生信工具 |
| `/etc/` | 系统配置文件 | 一般不改它 |

> **路径小提示**：绝对路径从 `/` 开始（如 `/home/lyf/data/`），相对路径不从 `/` 开始（如 `data/sample1.fastq`）。`.` 表示当前目录，`..` 表示上级目录。

---

## 5. 必会命令——文件和目录操作

以下命令是日常使用频率最高的，**必须掌握**：

```bash
# 查看当前位置
pwd                        # 显示当前绝对路径

# 列出文件
ls                         # 列出当前目录
ls -lh                     # 详细格式（-l）+ 人类可读大小（-h）
ls -la                     # 包括隐藏文件（以.开头的）
ls *.fastq                 # 只显示 .fastq 结尾的文件

# 切换目录
cd /path/to/dir            # 进入指定目录
cd ~                       # 回家目录
cd ..                      # 返回上级目录
cd -                       # 回到上一个目录

# 创建/删除目录
mkdir data                 # 创建目录
mkdir -p data/raw/fastq    # 递归创建多层目录
rmdir empty_dir            # 删除空目录

# 复制/移动/删除文件
cp file1.txt file2.txt     # 复制文件
cp -r dir1/ dir2/          # 复制整个目录（-r = recursive）
mv old.txt new.txt         # 移动或重命名
rm file.txt                # 删除文件（谨慎！没有回收站）
rm -rf dir/                # 删除目录及其所有内容（极其危险！）

# 查看文件
cat file.txt               # 显示完整文件内容
head -n 20 file.txt        # 显示前20行
tail -n 10 file.txt        # 显示后10行
less file.txt              # 分页浏览（Q退出，/搜索）
```

> **安全警告**：`rm -rf` 一旦执行无法撤销。`rm -rf /` 会删除整个系统。**永远不要在不确定时运行 rm -rf**。

---

## 6. 文件权限

Linux 里每个文件都有三组权限：

```bash
-rwxr-xr--  1 lyf lyf  1234  May 20 10:00  script.sh
|  |  |  |    |   |      |         |         |
|  用户 组    链接 属主 属组    大小       修改时间   文件名
|  rwx 其它
文件类型
```

三组权限 `r`（读=4）`w`（写=2）`x`（执行=1），数字累加：

```bash
chmod 755 script.sh        # 用户rwx(7)，组rx(5)，其它rx(5)
chmod +x script.sh         # 给所有人加执行权限
chmod 644 data.txt         # 用户rw(6)，组r(4)，其它r(4)
```

---

## 7. 重定向和管道——生信最核心的"组合拳"

这是 Linux 区别于图形界面的核心优势——**把小工具串成流水线**。

### 重定向（保存输出）

```bash
# > 把输出写入文件（覆盖原内容）
ls -lh > file_list.txt

# >> 追加到文件末尾
echo "新的一行" >> log.txt

# < 从文件读取输入
sort < unsorted.txt

# 2> 重定向错误信息
grep "ERROR" log.txt 2> errors.log
```

### 管道（把一个程序的输出给另一个程序）

管道的符号是竖线 `|`，含义是"把左边命令的输出，作为右边命令的输入"。

```bash
# 例1：查看当前目录下有多少个 .fastq 文件
ls *.fastq | wc -l

# 例2：看前10行中哪些行包含 "ATCG"
head -100 reads.fastq | grep "ATCG"

# 例3：查看最大的5个文件
ls -lhS | head -5

# 例4：生信真实场景——看fastq文件有多少条序列
echo $(( $(wc -l < sample.fastq) / 4 ))
# fastq 每条序列占4行，所以行数÷4 = 序列数
```

> **管道是生信的精髓**。GATK、samtools、bedtools 等工具的输入输出都在 stdin/stdout，你可以把十几个工具串成一条命令来处理数据。

---

## 8. vim——终端里的文本编辑器

在服务器上写脚本、改配置文件，你离不开 vim（或 nano）。

![[imgs/vim-workmodel.png]]

**新手只需要记三个场景：**

```bash
# 1. 打开文件
vim script.sh

# 2. 进入输入模式（打字）按 i
# 3. 退出输入模式按 ESC
# 4. 保存退出 -> 输入 :wq 再回车
# 5. 不保存退出 -> 输入 :q! 再回车
```

> 就这么简单。以后用得多了再学搜索替换、复制粘贴等进阶操作。先能"进去、打字、保存退出来"就够了。

---

## 参考资料

- [菜鸟教程 Linux 基础](https://www.runoob.com/linux/linux-tutorial.html)
- [Linux 文件系统结构](https://www.runoob.com/linux/linux-system-contents.html)
- [Vim 教程](https://www.runoob.com/linux/linux-vim.html)
- [Linux 文件权限](https://www.runoob.com/linux/linux-file-attr-permission.html)
- [WindTerm（SSH 客户端）](https://github.com/kingToolbox/WindTerm)
- [Tabby（SSH 客户端，原 Terminus）](https://github.com/Eugeny/tabby)
- [ssh-keygen 密钥配置指南](https://www.runoob.com/w3cnote/set-ssh-login-key.html)

---

## 小结

- Linux 是生信的基础——服务器、集群都用它
- 用 **SSH** 连接服务器：`ssh 用户@地址`，推荐 **WindTerm** 做图形客户端
- 记住 6 个核心命令：`pwd` `ls` `cd` `cp` `mv` `rm`
- 文件权限三组（用户/组/其它）× 三种（读/写/执行）
- `|` 管道可以把命令串起来，这是生信工作流的核心
- vim 先会三个操作：按 i 输入 → ESC 退出 → `:wq` 保存

### 练练手

1. 安装 **WindTerm**（或 Terminus），配置一个 SSH 连接到你实验室的服务器
2. 用终端里的 `ssh` 命令连接服务器，连上后输入 `df -h` 看磁盘空间
3. 配置 ssh 密钥登录，让下次连接不用输密码
4. 在家目录下创建一个 `biostudy/` 目录，在里面创建 `data/` 和 `scripts/`
5. 用 `echo "Hello bioinfo" > hello.txt` 创建一个文件，然后用 `cat` 查看
6. 试试 `ls -lh | wc -l`——猜猜这个组合命令输出的数字是什么意思
