#BUCLEEEEEES

contador= 0

#--------------------------- FOR -------------------------

for i in range(5): #RANGE - 1
        print("Valor de i "+ str(i))

for i in range(1,6): # for i in range(INICIO, FIN-1)
        print("Valor de i "+ str(i))


    #--------------------------- WHILE -------------------------
while(contador <=5):
    print("Contador "+ str(contador))
    if(contador == 3):
        #Salimos del bucle
        break
    #  continue vuelve al while y como contador = 3 entra el if y asi infinitamente
    contador += 1

