# Empezando el proyecto Rapidito con pyqt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

#Crear la clase de la ventana principal
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Mi segunda aplicacion con PyQt6")
        self.setGeometry(100, 100, 280, 80)

        # Crear un widget de texto
        label = QLabel("Hola PyQt6", self)
        label.move(60 ,30)

#iniciar la aplicacion
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()