#EJEMPLO NUMEROS PARES
print("Inserte el numero inicial: ")
inicio = int(input())

print("Inserte el numero final: ")
final= int(input())

for i in range(inicio,final+1): #ya que si final es 6 acabaría en 5 por el fin - 1 de python
    if(i % 2 == 0):
        print(i)