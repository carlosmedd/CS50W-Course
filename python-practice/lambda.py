lista = [('Lucas', 42), ('Martina', 87), ('Joaquín', 12), ('Sofía', 94), ('Mateo', 58), ('Valentina', 21), ('Tomás', 76), ('Camila', 37), ('Benjamín', 63), ('Lucía', 49)]

lista.sort(key=lambda x: x[1], reverse=True)
print(lista)