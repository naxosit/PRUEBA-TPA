from PyQt6 import QtWidgets


class VentanaSecundaria(QtWidgets.QMainWindow):
    def __init__(self, mascota):
        super(VentanaSecundaria, self).__init__()
        self.mascota = mascota
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Información de Mascota")
        self.setGeometry(100, 100, 400, 200)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 300, 100)
        self.label.setText(str(self.mascota))