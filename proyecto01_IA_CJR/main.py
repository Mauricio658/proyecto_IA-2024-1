# Importa las bibliotecas necesarias
import networkx as nx  # Para trabajar con grafos
import matplotlib.pyplot as plt  # Para visualizar el grafo
from nodo import *
from costos import *
import visitas

# Define la función principal del programa
def main():

    # Lista de ciudades disponibles
    cities = [
    'Oradea', 'Zerind', 'Arad', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia',
    'Dobreta', 'Craiova', 'Rimnicu Vilcea', 'Fagaras', 'Pitesti',
    'Bucharest', 'Giurgiu', 'Urziceni','Hirsova', 'Eforie', 'Vaslui',
    'Iasi', 'Neamt']

    # Imprime la lista de ciudades disponibles
    print("\n\t ****************************** Metodo de Busqueda A* usando Mapa de Rumania 2 ******************************\n")
    print("\n\t ========================================== Ciudades Disponibles =========================================\n\n")
    print(cities)
    print("\n\t ========================================================================================================\n\n")
    # Solicita al usuario que ingrese una ciudad de inicio válida
    flag = False
    while(flag == False):
        print()
        start = input('Ingresa el punto de partida: ').capitalize()
        end = "Bucharest"
        if(start in cities):
            flag = True
    print("\n")

    # Configuración del grafo
    numNodes = len(cities)
    numEdges = 23
    directed = False
    cost = True

    # Costos directos desde cada ciudad a Bucarest
    straight_Cost = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242,
        'Eforie':161, 'Fagaras':178, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226,
        'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':98,
        'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199,
        'Zerind':374}

    # Crear una instancia de la clase 'costos'
    Camino = costos(numNodes, numEdges, directed, cost, straight_Cost)
    Camino.start_costos(sorted(cities))

    # Si la ciudad de inicio es "Bucharest", muestra la información y termina
    if(start == "Bucharest"):
        print('Trayectoria: ', start)
        print('El costo total es: ', Camino.straight_Cost.get(start))
        return

    # Si la ciudad de inicio es diferente, muestra la información de inicio y ejecuta visitas
    else:
        print('Ciudad inicial', start)
        print('Costo: ', Camino.straight_Cost.get(start))
        visitas.visitas(Camino, start, 0, start ,end)

        # Crea un grafo utilizando networkx
        G = nx.Graph()

        # Agrega nodos y bordes al grafo desde la variable 'visitas.trajectory'
        for item in visitas.trajectory:
            cost, path = list(item.keys())[0], list(item.values())[0]
            cities_in_path = path.split('/')
            for i in range(len(cities_in_path) - 1):
                G.add_edge(cities_in_path[i], cities_in_path[i + 1], weight=cost)

        # Ajusta la posición de los nodos en el grafo y define etiquetas de bordes
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        # Dibuja el grafo y muestra las etiquetas de los bordes
        nx.draw(G, pos, with_labels=True,node_size=1000, node_color="lightblue", font_size=8, font_weight='bold', font_color="black")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Muestra el grafo
        plt.suptitle("Metodo Grafico A*")
        plt.show()

# Verifica si el código se ejecuta como un script principal
if __name__ == '__main__':
    import grafico_Rumania# mandamos el mapa para que el usuario observe la ciudad de inicio y tiene que cerrarlo para continuar
    main()
