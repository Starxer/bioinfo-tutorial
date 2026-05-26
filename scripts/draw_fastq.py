"""
绘制 FASTQ 格式完整示例图
mmx 审查后优化版：完整4行、等宽字体、质量热力图、数学公式
输出：../imgs/fastq-format.svg
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis('off')

# --- FASTQ data (correct: 'I' = Q40 = best, not 'F') ---
# Read 1
r1_id = '@SEQ_ID:001:FLOWCELL:1'
r1_seq = 'G A T T T G G G G T T C A A A G C A G T A T C G A T C A A A T A G T A G'
r1_qual_raw = 'I I I I I I I I I I I I I G G D D < 9 ? 6 < 9 / A = < ? I * I - * + '

# Parse quality chars
def qscore(c):
    """Phred+33 quality score"""
    return ord(c) - 33

def qcolor(c):
    q = qscore(c)
    if q >= 35: return '#1B5E20'   # excellent (Q35+, dark green)
    elif q >= 30: return '#388E3C' # good (Q30-34, green)
    elif q >= 20: return '#F9A825' # ok (Q20-29, orange)
    else: return '#D32F2F'         # poor (<Q20, red)

# Draw read title
ax.text(0.3, 10.3, 'FASTQ Format: Each read = 4 lines', fontsize=13, fontweight='bold', color='#222')

# --- Read 1 ---
y0 = 9.2
# Line 1: ID
ax.text(0.3, y0, r1_id, fontsize=9, fontfamily='monospace', color='#1976D2', fontweight='bold')
ax.text(10.8, y0, '← Sequence ID (@ line)', fontsize=7.5, color='#777')

# Line 2: Sequence
y = y0 - 1.0
x_start = 0.3
ax.text(x_start, y, 'Sequence:', fontsize=8, color='#555', fontweight='bold')
bases = r1_seq.split()
for i, base in enumerate(bases):
    if base == ' ':
        continue
    x = x_start + 3.0 + i * 0.48
    # Base color
    bc = {'A': '#4CAF50', 'T': '#E53935', 'C': '#1E88E5', 'G': '#616161'}.get(base, '#333')
    ax.text(x, y, base, fontsize=9, fontfamily='monospace', color=bc, ha='center', fontweight='bold')

# Line 3: Separator
y = y0 - 1.5
ax.text(0.3, y, '+                    ← Separator (+)', fontsize=9, fontfamily='monospace', color='#999')

# Line 4: Quality scores
y = y0 - 2.1
ax.text(x_start, y, 'Quality: ', fontsize=8, color='#555', fontweight='bold')
qual_chars = r1_qual_raw.split()
for i, ch in enumerate(qual_chars):
    if ch == ' ':
        continue
    x = x_start + 3.0 + i * 0.48
    qc = qcolor(ch)
    ax.text(x, y, ch, fontsize=9, fontfamily='monospace', color=qc, ha='center', fontweight='bold')

# --- Read 2 (shorter) ---
r2_id = '@SEQ_ID:002:FLOWCELL:1'
r2_seq = 'C G T A C G T A C G T A C G T A C G T A C G T A C G'
r2_qual_raw = 'D D 7 ; = 9 D F G I I F H H G F D D 9 6 < ; 8 / 9 B '

y0 = 4.8
ax.text(0.3, y0, r2_id, fontsize=9, fontfamily='monospace', color='#1976D2', fontweight='bold')

y = y0 - 1.0
ax.text(x_start, y, 'Sequence:', fontsize=8, color='#555', fontweight='bold')
bases2 = r2_seq.split()
for i, base in enumerate(bases2):
    if base == ' ':
        continue
    x = x_start + 3.0 + i * 0.48
    bc = {'A': '#4CAF50', 'T': '#E53935', 'C': '#1E88E5', 'G': '#616161'}.get(base, '#333')
    ax.text(x, y, base, fontsize=9, fontfamily='monospace', color=bc, ha='center', fontweight='bold')

y = y0 - 1.5
ax.text(0.3, y, '+', fontsize=9, fontfamily='monospace', color='#999')

y = y0 - 2.1
ax.text(x_start, y, 'Quality: ', fontsize=8, color='#555', fontweight='bold')
qual_chars2 = r2_qual_raw.split()
for i, ch in enumerate(qual_chars2):
    if ch == ' ':
        continue
    x = x_start + 3.0 + i * 0.48
    qc = qcolor(ch)
    ax.text(x, y, ch, fontsize=9, fontfamily='monospace', color=qc, ha='center', fontweight='bold')

# --- Annotation bracket for Read 1 ---
from matplotlib.patches import FancyBboxPatch
rect = FancyBboxPatch((0.15, 5.6), 13.5, 3.7, boxstyle="round,pad=0.15",
                       facecolor='none', edgecolor='#FF9800', linewidth=1.5, linestyle='--')
ax.add_patch(rect)
ax.text(0.5, 9.5, 'Read 1 (4 lines)', fontsize=8, color='#E65100', fontweight='bold')

# --- Quality legend ---
legend_x = 9.8
legend_y = 2.2
ax.text(legend_x, legend_y, 'Quality Legend', fontsize=8, fontweight='bold', color='#333')
items = [
    ('I = Q40 (99.99%)', '#1B5E20'),
    ('G = Q38 (99.98%)', '#388E3C'),
    ('D = Q35', '#388E3C'),
    ('9 = Q24', '#F9A825'),
    ('< = Q27', '#D32F2F'),
]
for i, (label, color) in enumerate(items):
    ax.text(legend_x, legend_y - 0.4 - i*0.35, label, fontsize=7, fontfamily='monospace', color=color)

# --- Formula ---
ax.text(0.3, 0.4, 'Formula', fontsize=8, fontweight='bold', color='#333')
ax.text(0.3, -0.05, 'Q = -10 × log₁₀(P)      Phred+33: ASCII = Q + 33', 
        fontsize=7.5, fontfamily='monospace', color='#444')
ax.text(0.3, -0.45, 'Ex: char "I" = 73, Q = 73-33 = 40,  P(error) = 10⁻⁴ = 0.01%', 
        fontsize=7.5, fontfamily='monospace', color='#444')

# --- Arrow from base to its quality char (just one example) ---
# 6th base of Read 1: G at x≈2.3, quality G at below
ax.annotate('', xy=(x_start + 3.0 + 5*0.48, y0 - 2.1 + 0.25), 
            xytext=(x_start + 3.0 + 5*0.48, y0 - 1.0 - 0.25),
            arrowprops=dict(arrowstyle='<->', color='#888', lw=0.6, alpha=0.4))
ax.text(x_start + 3.0 + 5*0.48 + 0.25, y0 - 1.55, '1:1', fontsize=6, color='#888', alpha=0.6)

plt.tight_layout(pad=0.3)
plt.savefig('../imgs/fastq-format.svg', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("OK: ../imgs/fastq-format.svg")
