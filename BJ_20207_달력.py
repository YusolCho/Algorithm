N = int(input())
table = [] # 
for _ in range(N):
    s, e = map(int, input().split())
    l = s - e 
    table.append([s,l,e]) # 약속 시작 날짜, -(약속길이)
table.sort() # 약속 시작 날짜가 이르고 약속 길이가 긴 순서대로 정렬

# 약속이 있는 마지막 날짜
max_value = 0
for meeting in table:
    max_value = max(max_value, meeting[2])

# 약속 표시할 캘린더 생성(약속이 있는 마지막 날짜 x 모든 약속의 개수)
graph = [[0] * max_value for _ in range(N)]

# 캘린더에 약속 표시 
def fill_calendar(meeting):
    global graph
    s, e = meeting[0]-1 , meeting[2]-1

    q = [0]
    while q: # 각 층에 대해서 

        floor = q.pop()
        if floor >= len(graph):
            return
        
        if sum(graph[floor][s:e+1]) == 0: # 그래프의 i층의 시작~끝 인덱스가 만약 다 0이라면
            graph[floor][s:e+1] = [1]*(len(graph[floor][s:e+1])) # 1로 채운 다음 
            return # 중단
        else:
            q.append(floor+1)

# 모든 미팅에 대해 적용
for meeting in table:
    fill_calendar(meeting)

# 각 날짜별 약속 개수
column_sum = [sum(row) for row in zip(*graph)]+[0]

# 직사각형의 높이, 너비, 그리고 총 넓이 변수 지정
height, width, total_area = 0, 0, 0

# 넓이 계산 
for i in column_sum:
    if i !=0:
        width += 1
        height = max(height, i)
    
    if i == 0:
        total_area += width*height
        width, height = 0, 0

# 정답        
print(total_area)