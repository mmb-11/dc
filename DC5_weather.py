import csv
from datetime import datetime
from collections import defaultdict

def map_function(row):
    year = datetime.strptime(row[0], "%Y-%m-%d").year
    return year, (float(row[2]), float(row[3]), 1)

def reduce_function(mapped):
    reduced = defaultdict(lambda: [0, 0, 0])
    for year, (tmax, tmin, count) in mapped:
        reduced[year][0] += tmax
        reduced[year][1] += tmin
        reduced[year][2] += count
    return reduced

with open("DC5_weather.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    mapped = [map_function(row) for row in reader]

reduced = reduce_function(mapped)

result = [(year, data[0] / data[2], data[1] / data[2]) for year, data in reduced.items()]
hottest_year, max_avg_temp = max(result, key=lambda x: x[1])[:2]
coolest_year, min_avg_temp = min(result, key=lambda x: x[2])[:2]

print(f"Hottest Year: {hottest_year} with avg max temperature {max_avg_temp:.2f}°C")
print(f"Coolest Year: {coolest_year} with avg min temperature {min_avg_temp:.2f}°C")
