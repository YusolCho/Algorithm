import heapq
N, D = map(int,input().split()) # 지름길 수, 도착점까지 거리
graph = [[] for _ in range(D+1)]

for _ in range(N):
    s, e, c = map(int,input().split()) # 시작점, 도착점, 거리
    if e <= D:  
        graph[s].append((c, e)) # 거리, 도착점

for s in range(D):
    if s + 1 <= D:
        graph[s].append((1, s+1)) # 거리, 도착점

INF = int(1e9)
minimum_distance = [INF] * (D+1)

def dijkstra(start_node):
    q = []
    heapq.heappush(q,(0,start_node)) # 거리, 노드

    minimum_distance[start_node] = 0

    while q: 
        start_here_distance, here = heapq.heappop(q) # 거리, 노드 

        if start_here_distance > minimum_distance[here]:
            continue  # 현재 노드가 이미 더 짧은 경로로 방문된 경우


        for nearby_distance, nearby_node in graph[here]: # 거리, 노드 

            new_distance = start_here_distance + nearby_distance    

            if (new_distance < minimum_distance[nearby_node]):
                minimum_distance[nearby_node] = new_distance 
                heapq.heappush(q, (new_distance, nearby_node)) # 거리, 노드 

dijkstra(0)
print(minimum_distance[D])