import sys
from PyQt6 import QtWidgets, uic
from VentanaPrincipal import Ui_VentanaPrincipal
import VentanaSecundaria
mascotas = []
class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."

class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)

    def guardar_mascota(self):
        global mascotas
        nombre = self.entrada_nombre.text()
        especie = self.entrada_especie.text()
        edad = self.entrada_edad.text()
        peso = self.entrada_peso.text()
        

        u = Mascota(nombre, especie, edad, peso)
        mascotas.append(u)

        # Crear y mostrar la ventana secundaria
        ventana_secundaria = VentanaSecundaria(u)
        ventana_secundaria.show()

        # Verificar la lista de mascotas
        print("Lista de mascotas")
        for i in mascotas:
            print(i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()