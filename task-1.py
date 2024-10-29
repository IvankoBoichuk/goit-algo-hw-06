import networkx as nx
from matplotlib import pyplot as plt
from utils import G


# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=9)
plt.title("Граф обласних центрів України")
plt.show()

# Аналіз графу: кількість вершин, ребер, ступінь вершин
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
print(degree_dict)