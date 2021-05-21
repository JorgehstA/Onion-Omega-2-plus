import json

coord_total = []
i = 1 # índice de cada línea del fichero

def addToDic(values):
    coord = {}
    coord['x_' + str(i)] = values[0]
    coord['y_' + str(i)] = values[1]
    coord['z_' + str(i)] = values[2]
    return(coord)


f = open('C:/Users/HowDev/Desktop/GatewayBLE/Test/DatosDummy.txt', 'r')
for line in f:
    line = line.rstrip("\n") # Elimino \n sino me aparece en la lista junto al último valor
    #print(line)
    data = line.split(".") #Creo una lista
    #print(data)
    temp = addToDic(data) #Añado a un diccionario
    i += 1 # Incremento el índice de la siguiente línea
    coord_total.append(temp) #Añade el dicionario a una lista
    #print(temp)
    #print(coord_total)
file_coord = {
    'locations' : coord_total
}
#print(file_Coord)
f.close()

aux = json.dumps(file_coord, indent=4)
print(aux)


