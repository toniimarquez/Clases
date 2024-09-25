import random
def centros_al_cuadrado(semilla, cantidad):
    numeros = []
    for _ in range(cantidad):
        semilla = str(semilla**2).zfill(8)  
        centro = semilla[2:6]
        numeros.append(int(centro))
        semilla = int(centro)
    return numeros
def medios_cuadrados(semilla, cantidad):
    numeros = []
    for _ in range(cantidad):
        semilla = str(semilla**2).zfill(8)
        inicio = len(semilla) // 2 - 2
        centro = semilla[inicio:inicio+4]
        numeros.append(int(centro))
        semilla = int(centro)
    return numeros
semilla_centro = random.randint(1000, 9999) 
semilla_medio = random.randint(1000, 9999)
numeros_centros = centros_al_cuadrado(semilla_centro, 100)
numeros_medios = medios_cuadrados(semilla_medio, 100)
print("Números generados por el método de Centros al Cuadrado:")
print(numeros_centros)
print("\nNúmeros generados por el método de Medios Cuadrados:")
print(numeros_medios)
