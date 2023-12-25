#Napisati funkciju koja određuje listu grana u grafu koje je neophodno obrisati da bi se ciklični
# graf transformisao u aciklični (da bi se u njemu eliminisali ciklusi).
#Ako DFS naiđe na čvor koji je već označen kao posećen, to znači da postoji ciklus u grafu.
def find_cycle(graph):
    visited = set()
    stack = []
    rec_stack = set()


    def dfs(node):
        if node in rec_stack:
            return rec_stack #postoji ciklus
        if node in visited:
            return set() #ne postoji ciklus

        visited.add(node)
        rec_stack.add(node)
        stack.append(node)

        for neighbor in graph[node]:
            cycle = dfs(neighbor)
            if cycle:
                return cycle

        rec_stack.remove(node)
        stack.pop()
        return set()

    for vertex in graph: #ostali cvorovi
        cycle = dfs(vertex)
        if cycle:
            return cycle #ima ciklusa
    return set() #nema ciklusa

def edges_to_remove(graph):
    cycle = find_cycle(graph)
    edges = set()

    if not cycle:
        return edges

    cycle_list = list(cycle)
    cycle_list.append(cycle_list[0])

    edge = (cycle_list[-2], cycle_list[-1])
    edges.add(edge)
    return edges

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': ['A']
# }
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': [],
    'F': ['G'],
    'G': ['C']
}
edges_to_remove = edges_to_remove(graph)
print("Grane koje treba ukloniti:", edges_to_remove)

