#IMPORTAMOS LA CLASE PERSONA
from class34persona import Persona

print("EJEMPLO CLASE PERSONA")

#Instanciamos (creamos) un objeto de la clase persona
person = Persona()
print("Pais: " + person.pais)
#Incluimos datos para la persona 1
person.pais = "España"
person.nombre = "Alumno"
person.apellidos = "Python"
person.email = "alumnopython@gmail.com"
person.anyonacimiento = 2001

#Persona 2
person2 = Persona()
print("Pais persona 2: " + person2.pais)

#LLAMAMOS A LOS METODOS
print("Nombre completo" + person.getNombreCompleto())
print("Edad: " + str(person.getEdad()))
print(person)
print(person.getDescripcion("Castaño ojos verdes"))