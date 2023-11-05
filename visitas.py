visit = []
trajectory = []
globCity = ''
h = 1

def visitas(objcostos, strCurrentCity, temp2, start, end):
    global visit, trajectory, globCity, h

    print(str(h)+".- : \n")
    visit.append(strCurrentCity) #La ciudad actual se añade a la lista de visitados.
    for i in objcostos.nodes: # El ciclo sirve para recorrer la lista de los nodos que son adyacentes.
        if(i.ciudad == strCurrentCity): # Si la ciudad de la lista es la misma a la que se le está pasando en la función entra al otro ciclo for
            for j in i.adjacent_Nodes: # Se busca el costo de los nodos vecinos a la ciudad actual por ejemplo SIBIU = FAG,RIMNI,ARAD, 0RAD
                if(str( list(j.keys())[0] ) in visit):  #Si los vecinos del nuevo nodo ya están en visitados no se vuelven a agregar.
                    continue                
                else: #Caso contrario los vecinos que no se han marcado como visitados se tienen que agregar en el diccionario.
                    tmp_city = str( list(j.keys())[0] ) # Se guarda temporalmente la ciudad vecina.
                    
                    if(h == 1):
                        tmp_city += '/'  + globCity + start # Solo sucede en la primera llamada a la función, sirve para agregar a Sibiu en la trayectoria.
                    
                    tmp_city += '/'  + globCity #Se actualiza la trayectoria de la ciudad -> EJEMPLO SIBIU/FAGARAS/CRAVIOTA.
                    tmp_distance = (int( list(j.values())[0])) + temp2 # Se suma la distancia de la arista y del origen(temp2) se actualiza antes de llamarse recursivamente.
                    tmp_total = tmp_distance      
                    tmp_total += objcostos.straight_Cost.get(str(list(j.keys())[0])) # Se suma el costo de línea directa de Bucharest.
                    print("Suma de la ciudad ", tmp_city, ": ", tmp_distance, " + ", objcostos.straight_Cost.get(str(list(j.keys())[0])), "=", tmp_total)
                    trajectory.append({tmp_total:tmp_city})                          # Se agrega en la lista el diccionario la ciudad y su costo.


    print("\nCiudades visitadas", visit)
    print('Nodos y distancias finales: ', trajectory)
    h += 1

    globCity, min_distance = minimum() #Se regresa el valor más pequeño de la lista junto con su ciudad.

    for j in trajectory: # Caso contrario al anterior for se va verificando si ya llegamos a Bucharest con la ruta mas óptima. 
        if(end in str( list(j.values())[0]) and min_distance == list(j.keys())[0]):
            print('\nTrayectoria: ', list(j.values())[0])
            print('El costo total es: ', list(j.keys())[0])
            return
    
    trajectory.remove({min_distance:globCity}) # Se borra la ciudad y su costo de la lista por que ya no pertece a la lista de nodos y distancias.
    min_city = globCity.split('/')[0] # Se obtiene únicamente la ciudad de menor distancia, no toda la trayectoria.
    min_distance -= objcostos.straight_Cost.get(min_city) # Para sumar los siguientes valores se tiene que restar el costo directo, esto sirve para sumarselos a las ciudades vecinas.

    print("\n-> Trayectoria con costo mínimo: '"+globCity+"'\n")
    visitas(objcostos, min_city, min_distance, start, end) #Se llama recursivamente la función.


def minimum(): # Función que regresa el valor mínimo de la ciudad en la lista trayectoría, con esto buscamos la forma más óptima para avanzar a la ciudad destino
    global trajectory
    strTmp = []
    intTmp = []
    for i in trajectory:
        intTmp.append(int( list(i.keys())[0] ))
        strTmp.append(str( list(i.values())[0] ))

    for j in trajectory:
        if(j.get(min(intTmp)) != None):
            return j.get(min(intTmp)), min(intTmp)