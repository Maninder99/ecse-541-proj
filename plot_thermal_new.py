import matplotlib.pyplot as plt
import numpy as np
import os

# Create figs folder automatically
os.makedirs("figs", exist_ok=True)

def read_temp_file(filename):
    """Read 3D-ICE node output file (skips all lines starting with %)"""
    data = np.loadtxt(filename, comments='%', skiprows=0)
    time = data[:, 0] * 1000   # convert seconds → milliseconds
    temp = data[:, 1]
    return time, temp

plt.rcParams.update({'font.size': 12, 'figure.figsize': (10, 6)})

# ====================== 1. Baseline 2-Tier ======================
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
plt.savefig("figs/baseline_2tier_temperature1.png", dpi=300)

# ====================== 2. 3-Tier Configuration ======================
time_3_1, temp_3_1 = read_temp_file("my_3tier_node1.txt")
time_3_2, temp_3_2 = read_temp_file("my_3tier_node2.txt")
time_3_3, temp_3_3 = read_temp_file("my_3tier_node3.txt")

plt.figure()
plt.plot(time_3_1, temp_3_1, label="Die 1 (bottom)", linewidth=2)
plt.plot(time_3_2, temp_3_2, label="Die 2", linewidth=2)
plt.plot(time_3_3, temp_3_3, label="Die 3 (top)", linewidth=2)
plt.title("3-Tier Liquid-Cooled 3D MPSoC")
plt.xlabel("Time (ms)")
plt.ylabel("Temperature (K)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figs/3tier_temperature1.png", dpi=300)

# ====================== 3. Custom 4-Tier ======================
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
plt.savefig("figs/custom_4tier_temperature1.png", dpi=300)

# ====================== 4. Flow Rate Sweep (New) ======================
# 4-tier with different coolant flow rates
time_f24_1, temp_f24_1 = read_temp_file("my_4tier_flow_24_node1.txt")
time_f72_1, temp_f72_1 = read_temp_file("my_4tier_flow_72_node1.txt")

plt.figure()
plt.plot(time_f24_1, temp_f24_1, label="Flow rate 24.0", linewidth=2, color='red')
plt.plot(time_f72_1, temp_f72_1, label="Flow rate 72.0", linewidth=2, color='green')
plt.title("4-Tier: Effect of Coolant Flow Rate on Bottom Die Temperature")
plt.xlabel("Time (ms)")
plt.ylabel("Temperature (K)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figs/flow_rate_sweep1.png", dpi=300)

# ====================== 5. Max Temperature Comparison (2/3/4-tier) ======================
plt.figure()
dies = ["Die 1", "Die 2", "Die 3", "Die 4"]
max_temps_2tier = [max(temp_b1), max(temp_b2), float('nan'), float('nan')]
max_temps_3tier = [max(temp_3_1), max(temp_3_2), max(temp_3_3), float('nan')]
max_temps_4tier = [max(temp_c1), max(temp_c2), max(temp_c3), max(temp_c4)]

x = np.arange(len(dies))
width = 0.25

plt.bar(x - width, max_temps_2tier, width, label="2-Tier Baseline", alpha=0.85)
plt.bar(x,       max_temps_3tier, width, label="3-Tier", alpha=0.85)
plt.bar(x + width, max_temps_4tier, width, label="4-Tier Custom", alpha=0.85)

plt.xticks(x, dies)
plt.ylabel("Maximum Temperature (K)")
plt.title("Max Temperature Comparison: 2-Tier vs 3-Tier vs 4-Tier")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figs/max_temp_comparison1.png", dpi=300)

print("\n All plots saved successfully!")
