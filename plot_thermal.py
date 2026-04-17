import matplotlib.pyplot as plt
import numpy as np
import os

# Create figs folder automatically
os.makedirs("figs", exist_ok=True)

def read_temp_file(filename):
    """Read 3D-ICE node output file (skips all lines starting with %)"""
    data = np.loadtxt(filename, comments='%', skiprows=0)
    time = data[:, 0] * 1000          # convert seconds to  milliseconds
    temp = data[:, 1]
    return time, temp

plt.rcParams.update({'font.size': 12, 'figure.figsize': (10, 6)})

# Baseline 2-tier (paper)
time_b1, temp_b1 = read_temp_file("mc4rm/transient/background_node1.txt")
time_b2, temp_b2 = read_temp_file("mc4rm/transient/background_node2.txt")

plt.figure()
plt.plot(time_b1, temp_b1, label="Die 1 (bottom)", linewidth=2)
plt.plot(time_b2, temp_b2, label="Die 2 (top)", linewidth=2)
plt.title("Baseline 2-Tier Liquid-Cooled 3D MPSoC (Paper Replication)")
plt.xlabel("Time (ms)")
plt.ylabel("Temperature (K)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figs/baseline_2tier_temperature.png", dpi=300)
print("Saved to figs/baseline_2tier_temperature.png")

# Custom 4-tier (4-tier)
time_c1, temp_c1 = read_temp_file("my_4tier_node1.txt")
time_c2, temp_c2 = read_temp_file("my_4tier_node2.txt")
time_c3, temp_c3 = read_temp_file("my_4tier_node3.txt")
time_c4, temp_c4 = read_temp_file("my_4tier_node4.txt")

plt.figure()
plt.plot(time_c1, temp_c1, label="Die 1 (bottom)", linewidth=2)
plt.plot(time_c2, temp_c2, label="Die 2", linewidth=2)
plt.plot(time_c3, temp_c3, label="Die 3", linewidth=2)
plt.plot(time_c4, temp_c4, label="Die 4 (top)", linewidth=2)
plt.title("Custom 4-Tier Liquid-Cooled 3D MPSoC (Our Extension)")
plt.xlabel("Time (ms)")
plt.ylabel("Temperature (K)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figs/custom_4tier_temperature.png", dpi=300)
print("Saved to figs/custom_4tier_temperature.png")

# Comparison plot (max temperature)
plt.figure()
dies = ["Die 1", "Die 2", "Die 3", "Die 4"]
max_temps_baseline = [max(temp_b1), max(temp_b2), float('nan'), float('nan')]
max_temps_custom   = [max(temp_c1), max(temp_c2), max(temp_c3), max(temp_c4)]

x = np.arange(len(dies))
width = 0.35
plt.bar(x - width/2, max_temps_baseline, width, label="2-Tier Baseline", alpha=0.8)
plt.bar(x + width/2, max_temps_custom,   width, label="4-Tier Custom", alpha=0.8)
plt.xticks(x, dies)
plt.ylabel("Maximum Temperature (K)")
plt.title("Max Temperature Comparison: 2-Tier vs 4-Tier")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figs/max_temp_comparison.png", dpi=300)
print("Saved to figs/max_temp_comparison.png")
