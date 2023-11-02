import nodo #Creación del Grafo del Mapa de Rumania 2 a usar en el programa

class costos:
    nodes = []
    num_Nodes = 0
    num_Edges = 0
    directed = False
    cost = False
    straight_Cost = {}

    def __init__(self, numNodes, numEdges, directed, cost, straight_Cost):
        self.num_Nodes = numNodes
        self.num_Edges = numEdges
        self.directed = directed
        self.cost = cost
        self.straight_Cost = straight_Cost

    def start_costos(self, cities):
        self.add_cities(cities)
        self.add_edges()


    def add_cities(self, cities):
        for i in cities:
            self.nodes.append(nodo.nodo(i))

    def add_edges(self):
        #Se añaden las ciudades vecinas.
        #Arad
        self.nodes[0].adjacent_Nodes.append({'Zerind':75})
        self.nodes[0].adjacent_Nodes.append({'Sibiu':140})
        self.nodes[0].adjacent_Nodes.append({'Timisoara':118})

        #Bucharest
        self.nodes[1].adjacent_Nodes.append({'Fagaras':211})
        self.nodes[1].adjacent_Nodes.append({'Pitesti':101})
        self.nodes[1].adjacent_Nodes.append({'Giurgiu':90})
        self.nodes[1].adjacent_Nodes.append({'Urziceni':85})

        #Craiova
        self.nodes[2].adjacent_Nodes.append({'Dobreta':120})
        self.nodes[2].adjacent_Nodes.append({'Rimnicu Vilcea':146})
        self.nodes[2].adjacent_Nodes.append({'Pitesti':138})

        #Dobreta
        self.nodes[3].adjacent_Nodes.append({'Craiova':120})
        self.nodes[3].adjacent_Nodes.append({'Mehadia':75})

        #Eforie
        self.nodes[4].adjacent_Nodes.append({'Hirsova':86})

        #Fagaras
        self.nodes[5].adjacent_Nodes.append({'Sibiu':99})
        self.nodes[5].adjacent_Nodes.append({'Bucharest':211})

        #Giurgiu
        self.nodes[6].adjacent_Nodes.append({'Bucharest':90})

        #Hirsova
        self.nodes[7].adjacent_Nodes.append({'Urziceni':98})
        self.nodes[7].adjacent_Nodes.append({'Eforie':86})

        #Iasi
        self.nodes[8].adjacent_Nodes.append({'Neamt':87})
        self.nodes[8].adjacent_Nodes.append({'Vaslui':92})

        #Lugoj
        self.nodes[9].adjacent_Nodes.append({'Timisoara':111})
        self.nodes[9].adjacent_Nodes.append({'Mehadia':70})

        #Mehadia
        self.nodes[10].adjacent_Nodes.append({'Lugoj':70})
        self.nodes[10].adjacent_Nodes.append({'Dobreta':75})

        #Neamt
        self.nodes[11].adjacent_Nodes.append({'Iasi':87})

        #Oradea
        self.nodes[12].adjacent_Nodes.append({'Zerind':71})
        self.nodes[12].adjacent_Nodes.append({'Sibiu':151})

        #Pitesti
        self.nodes[13].adjacent_Nodes.append({'Rimnicu Vilcea':97})
        self.nodes[13].adjacent_Nodes.append({'Craiova':138})
        self.nodes[13].adjacent_Nodes.append({'Bucharest':101})

        #Rimnicu
        self.nodes[14].adjacent_Nodes.append({'Sibiu':80})
        self.nodes[14].adjacent_Nodes.append({'Craiova':146})
        self.nodes[14].adjacent_Nodes.append({'Pitesti':97})

        #Sibiu
        self.nodes[15].adjacent_Nodes.append({'Oradea':151})
        self.nodes[15].adjacent_Nodes.append({'Arad':140})
        self.nodes[15].adjacent_Nodes.append({'Rimnicu Vilcea':80})
        self.nodes[15].adjacent_Nodes.append({'Fagaras':99})

        #Timisoara
        self.nodes[16].adjacent_Nodes.append({'Lugoj':111})
        self.nodes[16].adjacent_Nodes.append({'Arad':118})

        #Urziceni
        self.nodes[17].adjacent_Nodes.append({'Bucharest':85})
        self.nodes[17].adjacent_Nodes.append({'Hirsova':98})
        self.nodes[17].adjacent_Nodes.append({'Vaslui':142})

        #Vaslui
        self.nodes[18].adjacent_Nodes.append({'Iasi':92})
        self.nodes[18].adjacent_Nodes.append({'Urziceni':142})

        #Zerind
        self.nodes[19].adjacent_Nodes.append({'Oradea':71})
        self.nodes[19].adjacent_Nodes.append({'Arad':75})

