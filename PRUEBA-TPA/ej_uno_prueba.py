import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Ejercicio 1 sección práctica prueba individual")
        self.setFixedSize(QSize(600,300))
        #caja = QHBoxLayout()
        caja_grande = QVBoxLayout()
        caja_av = QGridLayout()
        caja_ti = QGridLayout()
    

        #Componentes de la interfaz
        nUsuario = QLabel("NOMBRE USUARIO")
        #masa = QLabel("Masa (kg)")
        atributo_uno = QLabel("Atributo 1")
        atributo_dos = QLabel("Atributo 2")
        atributo_tres= QLabel("Atributo 3")
        atributo_cuatro = QLabel("Atributo 4")
        atributo_cinco = QLabel("Atributo 5")
        atributo_seis = QLabel("Atributo 6")
        valor_uno = QLabel("Valor 1")
        valor_dos = QLabel("Valor 2")
        valor_tres= QLabel("Valor 3")
        valor_cuatro = QLabel("Valor 4")
        valor_cinco = QLabel("Valor 5")
        valor_seis = QLabel("Valor 6")
        text = QLabel("Texto descripción usuario")
        img = QLabel("Imagen")
        ok = QLabel("Ok")
        vacio = QLabel("   ")
   
        self.entrada_masa = QLineEdit()
        self.entrada_estatura = QLineEdit()
        self.resultado = QLabel("")
        

        # Se agregan los componentes al layout definido
        
        caja_ti.addWidget(text, 2,0)
        caja_av.addWidget(atributo_uno, 1,6)
        caja_ti.addWidget(img, 3,0)
        caja_av.addWidget(vacio, 2,1)
        caja_av.addWidget(atributo_dos, 2,6)
        caja_av.addWidget(atributo_tres, 3,6)
        caja_av.addWidget(atributo_cuatro, 4,6)
        caja_av.addWidget(atributo_cinco, 5,6)
        caja_av.addWidget(atributo_seis, 6,6)
        caja_av.addWidget(valor_uno, 1,7)
        caja_av.addWidget(valor_dos, 2,7)
        caja_av.addWidget(valor_tres, 3,7)
        caja_av.addWidget(valor_cuatro, 4,7)
        caja_av.addWidget(valor_cinco, 5,7)
        caja_av.addWidget(valor_seis, 6,7)
        

        
        caja_grande.addWidget(nUsuario)
        caja_grande.addLayout(caja_ti)
        caja_grande.addLayout(caja_av)
        caja_grande.addWidget(ok)
        
   
        caja_grande.addWidget(self.resultado)
   

        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        
        

        

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()