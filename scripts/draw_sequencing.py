"""
绘制 Sanger vs NGS 测序对比图
最终版：Sanger高斯波形峰图、NGS可见泳道
输出：../imgs/sequencing-comparison.svg
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(10, 5))

# ===== Sanger (left) =====
ax1 = fig.add_axes([0.05, 0.08, 0.40, 0.88])
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 7)
ax1.axis('off')
ax1.set_title('Sanger Sequencing (1977)', fontsize=13, fontweight='bold', pad=12, color='#333')

# Reaction components
ax1.text(0.3, 6.4, 'DNA Template', fontsize=9, color='#222', fontweight='bold')
ax1.text(0.3, 5.7, 'Primer', fontsize=8.5, color='#D84315')
ax1.text(0.3, 5.2, 'DNA Pol + dNTPs', fontsize=8, color='#444')
ax1.text(0.3, 4.7, '+ fluorescent ddNTPs', fontsize=7.5, color='#00838F')

# Capillary electrophoresis box
cap_rect = mpatches.FancyBboxPatch((0.15, 2.4), 1.5, 2.0, boxstyle="round,pad=0.15",
                                    facecolor='#FFF8E1', edgecolor='#F9A825', linewidth=1.3)
ax1.add_patch(cap_rect)
ax1.text(0.9, 3.8, 'Capillary', fontsize=8.5, ha='center', color='#F57F17', fontweight='bold')
ax1.text(0.9, 3.3, 'Electro-', fontsize=7, ha='center', color='#F57F17')
ax1.text(0.9, 3.0, 'phoresis', fontsize=7, ha='center', color='#F57F17')

# Arrow → chromatogram
ax1.annotate('', xy=(2.2, 2.4), xytext=(2.2, 1.6),
            arrowprops=dict(arrowstyle='->', color='#F9A825', lw=1.5))

# ===== CHROMATOGRAM: 4 channels, Gaussian peaks =====
base_colors = {'A': '#4CAF50', 'T': '#E53935', 'C': '#1E88E5', 'G': '#616161'}
np.random.seed(42)

# Generate ~30 base calls (dense)
bases = np.random.choice(['A', 'T', 'C', 'G'], 30)
x_positions = np.linspace(0.3, 5.7, 100)
chrom_y = 0.9

# For each channel, create combined Gaussian signal
for base, color in base_colors.items():
    signal = np.zeros(100)
    for i, b in enumerate(bases):
        if b == base:
            idx = int(6 + i * 2.98)
            if 0 <= idx < 100:
                sigma = 0.35
                for j in range(100):
                    signal[j] += np.exp(-(j - idx)**2 / (2 * sigma**2))
    offset = {'A': 0.0, 'C': 0.35, 'T': 0.7, 'G': 1.05}[base]
    ax1.plot(x_positions, signal * 0.22 + chrom_y - 0.4 + offset, color=color, linewidth=1.2, alpha=0.85)
    
# Channel labels
for base, yoff in [('A', 0.0), ('C', 0.35), ('T', 0.7), ('G', 1.05)]:
    ax1.text(5.7, chrom_y - 0.4 + yoff + 0.12, base, fontsize=7, 
             fontweight='bold', color=base_colors[base], ha='left', va='center')

ax1.text(3.0, chrom_y - 0.6, '4-channel fluorescence chromatogram', ha='center', fontsize=7.5, color='#333')
ax1.text(0.3, chrom_y - 0.6, '~1000 bp / read', fontsize=6.5, color='#999', fontstyle='italic')

# ===== NGS (right) =====
ax2 = fig.add_axes([0.50, 0.08, 0.48, 0.88])
ax2.set_xlim(0, 6)
ax2.set_ylim(0, 7)
ax2.axis('off')
ax2.set_title('NGS — Illumina (2007)', fontsize=13, fontweight='bold', pad=12, color='#333')

# Step 1
ax2.text(0.3, 6.4, 'Step 1', fontsize=8.5, fontweight='bold', color='#1976D2')
ax2.text(0.3, 5.9, 'Library Prep', fontsize=10.5, fontweight='bold', color='#1565C0')
ax2.text(0.3, 5.2, 'Fragment DNA\nAdd adapters', fontsize=8.5, color='#444')

# Step 2
ax2.text(2.1, 6.4, 'Step 2', fontsize=8.5, fontweight='bold', color='#1976D2')
ax2.text(2.1, 5.9, 'Cluster Gen.', fontsize=10.5, fontweight='bold', color='#1565C0')
ax2.text(2.1, 5.2, 'Bridge PCR on\nflow cell surface', fontsize=8.5, color='#444')

# Step 3
ax2.text(4.0, 6.4, 'Step 3', fontsize=8.5, fontweight='bold', color='#1976D2')
ax2.text(4.0, 5.9, 'Seq by Synth.', fontsize=10.5, fontweight='bold', color='#1565C0')
ax2.text(4.0, 5.2, 'Reversible terminator\nfluorescent NTPs', fontsize=8.5, color='#C62828')

# ===== FLOW CELL WITH VISIBLE LANES =====
fc_rect = mpatches.FancyBboxPatch((0.3, 0.3), 5.4, 4.3, boxstyle="round,pad=0.15",
                                    facecolor='#F5F5F5', edgecolor='#43A047', linewidth=1.5)
ax2.add_patch(fc_rect)
ax2.text(3.0, 4.15, 'Flow Cell — Top View', fontsize=9, ha='center', color='#2E7D32', fontweight='bold')

# Draw 6 lanes
lane_colors = ['#E8F5E9', '#C8E6C9', '#E8F5E9', '#C8E6C9', '#E8F5E9', '#C8E6C9']
np.random.seed(123)
for lane in range(6):
    y0 = 3.6 - lane * 0.55
    y1 = y0 - 0.4
    # Lane background
    rect = Rectangle((0.5, y1), 5.0, 0.45, facecolor=lane_colors[lane], 
                      edgecolor='#A5D6A7', linewidth=0.5)
    ax2.add_patch(rect)
    # Lane label
    ax2.text(0.3, (y0+y1)/2, f'L{lane+1}', fontsize=6, ha='right', va='center', color='#888')
    
    # Clusters as colored dots along each lane
    for i in range(18):
        cx = 0.65 + i * 0.27 + np.random.random() * 0.05
        cy = y1 + 0.08 + np.random.random() * 0.28
        clr = np.random.choice(['#4CAF50', '#E53935', '#1E88E5', '#FFB300'])
        ax2.scatter(cx, cy, s=5, color=clr, alpha=0.6, edgecolors='none')

# Annotation: cluster
ax2.annotate('Each dot = one\namplified cluster', xy=(2.5, 1.9), xytext=(4.5, 2.2),
            arrowprops=dict(arrowstyle='->', color='#555', lw=1),
            fontsize=7, color='#333', ha='center')

# Bottom: summary
ax2.text(3.0, 0.05, '6 lanes × millions of clusters = billions of reads per run',
         fontsize=8, ha='center', color='#1B5E20', fontweight='bold')

# Comparison arrow between Sanger and NGS
fig.text(0.47, 0.5, '→', fontsize=20, color='#CCC', ha='center', va='center')

plt.savefig('../imgs/sequencing-comparison.svg', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("OK: ../imgs/sequencing-comparison.svg")
