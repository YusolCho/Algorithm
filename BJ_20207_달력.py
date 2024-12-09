import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
table = [(int(data[i]), int(data[i + 1])) for i in range(1, len(data), 2)]
table.sort()

max_value = max(e for _, e in table)
graph = [0] * max_value

for s, e in table:
    for i in range(s - 1, e):
        graph[i] += 1

# 총면적 계산
total_area, i = 0, 0
while i < max_value:
    if graph[i] == 0:
        i += 1
        continue

    start = i
    max_height = 0
    while i < max_value and graph[i] > 0:
        max_height = max(max_height, graph[i])
        i += 1

    total_area += (i - start) * max_height

# 답 출력
print(total_area) 