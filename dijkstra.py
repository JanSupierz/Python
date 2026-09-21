import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import sys
import heapq

def dijkstra(G:nx.Graph, source:int, target:int):
    queue = []
    dist = [sys.maxsize] * len(G)
    paths = [-1] * len(G)

    dist[source]=0
    paths[source]=source

    heapq.heappush(queue, (dist[source], source))

    while queue:
        d,n = heapq.heappop(queue)

        if d > dist[n]:
            continue

        if n == target:
            break
            
        for i in G.neighbors(n):
            if dist[i] > dist[n] + 1:
                dist[i] = dist[n] + 1
                paths[i] = n
                heapq.heappush(queue, (dist[i], i))

    def get_path(t:int) -> list:
        if t == source:
            return [source]
        elif t == -1:
            return []

        return get_path(paths[t]) + [t]
    
    return get_path(target)

def main():
    seed = 10
    random.seed(seed)
    G = nx.Graph()

    nodes = list(range(10)) #0 to 9
    random.shuffle(nodes)

    while len(nodes) > 1:

        for _ in range(random.randint(1,3)):
            G.add_edge(nodes[-1], random.choice(nodes))

        nodes.pop()
    start, end = 0,7
    path_nodes = dijkstra(G, start, end)
    pos = nx.spring_layout(G, seed=seed)

    fig, (ax1, ax2) = plt.subplots(2,1)

    path_edges = list(zip(path_nodes, path_nodes[1:]))
    P = G.edge_subgraph(path_edges)

    path_colors = ["lightgreen" if n == start else "red" if n == end else "yellow" for n in P.nodes]

    nx.draw(P, ax=ax2, with_labels=True, node_color=path_colors)
    ax2.set_title("Path")

    anim = FuncAnimation(fig, update, fargs=(ax1, path_nodes, pos, G), frames=len(path_nodes), interval=1000, repeat=True)
    plt.show()
    anim.save("path.gif", writer="pillow", fps=1)

def update(frame:int, ax:plt.axes, path:list[int], pos, G:nx.Graph):
    ax.clear()

    start, end = path[0], path[-1]
    colors = {n: "lightblue" for n in G.nodes}
    colors[start]="lightgreen"
    colors[end]="gray"

    for n in path[1:frame+1]:
        if n == end:
            colors[n] = "red"
        else: 
            colors[n] = "yellow"
        
    nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=list(colors.values()))
    ax.set_title("Graph")

if __name__== "__main__":
    main()