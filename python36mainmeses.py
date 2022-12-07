from clas36mes import Mes
#NUMEROS ALEATORIOS
import random
import datetime

#VAMOS A GENERAR NUMEROS ALEATORIOS
#RECUPERAMOS UN NUMERO ENTERO ENTRE 1 Y 50
#aleatorio = random.randint(1,50)

meses=[]

for i in range(1, 13):
    mes = Mes()
    fecha = datetime.datetime(2022, i ,1)
    nombreMes = fecha.strftime("%B")
    #mes.nombre= "Mes " + (str(i))
    mes.nombre = nombreMes.upper()
    mes.temperaturaMax = random.randint(20,50)
    mes.temperaturaMin = random.randint(1,20)
    meses.append(mes)


for mes in meses:
    print(mes)
