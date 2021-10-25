from pyvis.network import Network


def dfs(grafo, vertice, camino=[]):

    camino = camino + [vertice]

    for vecino in grafo[vertice]:

        if vecino not in camino:

            camino = dfs(grafo, vecino, camino)

    return camino

matriz = {1: [2, 3], 2: [4, 5],

                    3: [5], 4: [6], 5: [6],

                    6: [7], 7: []}

print(dfs(matriz, 3))

net = Network()
net.add_nodes(matriz)

net.add_edge(1, 2)
net.add_edge(1, 3)
net.add_edge(2, 4)
net.add_edge(2, 5)
net.add_edge(3, 5)
net.add_edge(4, 6)
net.add_edge(5, 6)
net.add_edge(6, 7)



net.toggle_physics(True)
net.show('mygraph.html')