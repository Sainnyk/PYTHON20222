from class35coche import Coche

class Deportivo (Coche):
    def turbo(self):
        self.velocidad += 80
        print("Activando turbo")

    #OVERRIDE DEL METODO ORIGINAL
    def acelerar(self):
        self.velocidad += 60
        print("Velocidad atual de "+ self.marca + ": "+ str(self.velocidad))