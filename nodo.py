class nodo: #Clase Nodo.
    adjacent_Nodes = []
    ciudad = ""

    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.adjacent_Nodes = []
