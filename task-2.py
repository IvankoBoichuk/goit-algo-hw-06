# Вибір випадкових міст для прикладу
from utils import bfs_path, dfs_path
from utils import G

start_city = "Львів"
goal_city = "Донецьк"

# Пошук шляхів з використанням DFS та BFS
dfs_result = dfs_path(G, start_city, goal_city)
bfs_result = bfs_path(G, start_city, goal_city)

print(f"DFS: {dfs_result}")
print(f"BFS: {bfs_result}")