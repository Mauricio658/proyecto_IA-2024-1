#Se crea el grafo aparte,para unicamente lectura por parte del usuario
import networkx as nx
import matplotlib.pyplot as plt


# Define la clase nodo
class Nodo:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.adjacent_Nodes = []

# Define la clase costos
class Costos:
    def __init__(self):
        self.nodes = []

    def add_city(self, ciudad, conexiones):
        node = Nodo(ciudad)
        for conexion, peso in conexiones.items():
            node.adjacent_Nodes.append((conexion, peso))
        self.nodes.append(node)

# Crear una instancia de la clase Costos
mapa_rumania = Costos()

# Agregar ciudades y conexiones
mapa_rumania.add_city("Arad", {"Zerind": 75, "Sibiu": 140, "Timisoara": 118})
mapa_rumania.add_city("Bucharest", {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85})
mapa_rumania.add_city("Craiova", {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138})
mapa_rumania.add_city("Dobreta", {"Craiova": 120, "Mehadia": 75})
mapa_rumania.add_city("Eforie", {"Hirsova": 86})
mapa_rumania.add_city("Fagaras", {"Sibiu": 99, "Bucharest": 211})
mapa_rumania.add_city("Giurgiu", {"Bucharest": 90})
mapa_rumania.add_city("Hirsova", {"Urziceni": 98, "Eforie": 86})
mapa_rumania.add_city("Iasi", {"Neamt": 87, "Vaslui": 92})
mapa_rumania.add_city("Lugoj", {"Timisoara": 111, "Mehadia": 70})
mapa_rumania.add_city("Mehadia", {"Lugoj": 70, "Dobreta": 75})
mapa_rumania.add_city("Neamt", {"Iasi": 87})
mapa_rumania.add_city("Oradea", {"Zerind": 71, "Sibiu": 151})
mapa_rumania.add_city("Pitesti", {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101})
mapa_rumania.add_city("Rimnicu Vilcea", {"Sibiu": 80, "Craiova": 146, "Pitesti": 97})
mapa_rumania.add_city("Sibiu", {"Oradea": 151, "Arad": 140, "Rimnicu Vilcea": 80, "Fagaras": 99})
mapa_rumania.add_city("Timisoara", {"Lugoj": 111, "Arad": 118})
mapa_rumania.add_city("Urziceni", {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142})
mapa_rumania.add_city("Vaslui", {"Iasi": 92, "Urziceni": 142})
mapa_rumania.add_city("Zerind", {"Oradea": 71, "Arad": 75})

# Crear un objeto grafo de NetworkX
G = nx.Graph()

# Agregar nodos y aristas al grafo
for node in mapa_rumania.nodes:
    G.add_node(node.ciudad)
    for conexion, peso in node.adjacent_Nodes:
        G.add_edge(node.ciudad, conexion, weight=peso)

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=8, font_weight='bold', font_color="black")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Mapa de Rumania")
plt.suptitle("Mapa de Rumania 2")

plt.show()
