import csv
from collections import defaultdict

temps = defaultdict(lambda: [0, 0, 0])  # [sum_max, sum_min, count]

with open("weather.csv") as f:
    next(f)
    for r in csv.reader(f):
        try:
            y = r[0][:4]
            tmax, tmin = float(r[2]), float(r[3])
            temps[y][0] += tmax
            temps[y][1] += tmin
            temps[y][2] += 1
        except:
            continue

hot, cool = "", ""
hot_val, cool_val = -1e9, 1e9

print("Yearly Average Temperatures:")
for y in sorted(temps):
    smax, smin, c = temps[y]
    avg_max = smax / c
    avg_min = smin / c
    print(f"{y}: {avg_temps[y]:.2f}°C")
    if avg_max > hot_val: hot, hot_val = y, avg_max
    if avg_min < cool_val: cool, cool_val = y, avg_min

print(f"\nHottest Year: {hot} → {hot_val:.2f}°C")
print(f"Coolest Year: {cool} → {cool_val:.2f}°C")
