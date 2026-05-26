"""
绘制 Linux 文件系统层级结构图 (FHS)
mmx 第四轮：极简 L2，宽画布，大间距
输出：../imgs/linux-filesystem.svg
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

# === Colors ===
C = {
    'root':   ('#1565C0', '#1565C0', '#FFFFFF'),
    'system': ('#E3F2FD', '#90CAF9', '#333333'),
    'user':   ('#FFF3E0', '#FFB74D', '#E65100'),
    'file':   ('#F3E5F5', '#CE93D8', '#6A1B9A'),
}

# === Nodes: widely spaced ===
# format: name -> (x, y, tag)
N = {
    # Root
    '/':       (6.0, 8.5, 'root'),
    # L1 — 1 unit apart
    'bin':     (1.0, 6.5, 'system'),
    'boot':    (2.2, 6.5, 'system'),
    'dev':     (3.4, 6.5, 'system'),
    'etc':     (4.6, 6.5, 'system'),
    'home':    (6.0, 6.5, 'user'),
    'opt':     (7.4, 6.5, 'user'),
    'tmp':     (8.6, 6.5, 'system'),
    'usr':     (9.8, 6.5, 'system'),
    'var':     (11.0, 6.5, 'system'),
    # L2 — only 1 child per parent except home (2)
    'fstab':   (4.6, 4.5, 'file'),     # etc child
    'user':    (5.4, 4.5, 'user'),     # home child 1
    'project': (6.6, 4.5, 'user'),     # home child 2
    'miniconda':(7.4, 4.5, 'user'),    # opt child
    'bin2':    (9.2, 4.5, 'system'),   # usr child (/usr/bin)
    'local':   (10.4, 4.5, 'system'),  # usr child (/usr/local)
    'log':     (11.0, 4.5, 'system'),  # var child
}

# === Edges ===
edges = [
    ('/', 'bin'), ('/', 'boot'), ('/', 'dev'), ('/', 'etc'),
    ('/', 'home'), ('/', 'opt'), ('/', 'tmp'), ('/', 'usr'), ('/', 'var'),
    ('etc', 'fstab'),
    ('home', 'user'), ('home', 'project'),
    ('opt', 'miniconda'),
    ('usr', 'bin2'), ('usr', 'local'),
    ('var', 'log'),
]

# --- Draw ---
for name, (x, y, tag) in N.items():
    bg, border, tc = C[tag]
    ls = '--' if tag == 'file' else '-'
    display = 'bin' if name == 'bin2' else name
    fs = 15 if name == '/' else (13 if y > 5.5 else 11)
    fw = 'bold' if name == '/' or y > 5.5 else 'normal'
    ax.text(x, y, display, fontsize=fs, ha='center', va='center',
            fontweight=fw, color=tc,
            bbox=dict(boxstyle='round,pad=0.35', facecolor=bg, edgecolor=border,
                      linewidth=1.5 if name == '/' else 1.0, linestyle=ls))

# --- Edges ---
for p, c in edges:
    px, py, _ = N[p]
    cx, cy, _ = N[c]
    mid = (py + cy) / 2
    ax.plot([px, px], [py-0.3, mid], color='#BDBDBD', linewidth=0.8)
    ax.plot([px, cx], [mid, mid], color='#BDBDBD', linewidth=0.8)
    ax.plot([cx, cx], [mid, cy+0.35], color='#BDBDBD', linewidth=0.8)

# --- Title ---
ax.text(6.0, 9.1, 'Linux Filesystem Hierarchy (FHS)', fontsize=15, fontweight='bold',
        ha='center', color='#222')

# --- Legend ---
items = [
    ("System dirs\n(bin, usr, var…)", '#E3F2FD', '#90CAF9', '-'),
    ("User dirs\n(home, opt)", '#FFF3E0', '#FFB74D', '-'),
    ("Config files\n(fstab, hosts…)", '#F3E5F5', '#CE93D8', '--'),
]
for i, (desc, bg, border, ls) in enumerate(items):
    x0 = 0.4 + i * 3.0
    rect = mpatches.FancyBboxPatch((x0, 1.0), 2.5, 1.0, boxstyle="round,pad=0.1",
                                    facecolor=bg, edgecolor=border, linewidth=1, linestyle=ls)
    ax.add_patch(rect)
    ax.text(x0 + 1.25, 1.5, desc, fontsize=8, ha='center', va='center', color='#333')

# --- Quick reference ---
ref = ("/bin — Commands    /home — Your files    /etc — Config\n"
       "/opt — Software    /tmp — Temporary     /usr — Resources\n"
       "/var — Logs & data")
ax.text(6.0, 2.5, ref, fontsize=8, va='bottom', ha='center',
       bbox=dict(boxstyle='round', facecolor='#FAFAFA', edgecolor='#E0E0E0', pad=0.5),
       fontfamily='monospace', color='#555')

plt.tight_layout(pad=0.3)
plt.savefig('../imgs/linux-filesystem.svg', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("OK: ../imgs/linux-filesystem.svg")
