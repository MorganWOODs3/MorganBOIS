from PyQt5.QtWidgets import *
from PyQt5 import uic
import socket
import sys
import time


class Chrono(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("Chronomètre")

        self.textEdit = QTextEdit("")
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Start")
        self.btnPress2 = QPushButton("Stop")
        self.btnPress3 = QPushButton("Connect")
        self.btnPress4 = QPushButton("Reset")
        self.btnPress5 = QPushButton("Quitter")

        layout = QVBoxLayout()
        p1 = layout.addWidget(self.textEdit)
        p2 = layout.addWidget(self.btnPress1)
        p3 = layout.addWidget(self.btnPress2)
        p4 = layout.addWidget(self.btnPress3)
        p5 = layout.addWidget(self.btnPress4)
        p6 = layout.addWidget(self.btnPress5)
        self.setLayout(layout)
        grid = QGridLayout()
        grid.addWidget(p1, 0, 0)
        grid.addWidget(p2, 1, 1)
        grid.addWidget(p3, 2, 0)
        grid.addWidget(p4, 3, 0)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
        self.btnPress4.clicked.connect(self.btnPress4_Clicked)
        self.btnPress5.clicked.connect(self.btnPress5_Clicked)

    def btnPress1_Clicked(self):
        # while:
        self.textEdit.append(f"{self.i}")
        self.i += 1
        time.sleep(1)
        print(self.i)



    def btnPress2_Clicked(self):
        pass


    def btnPress3_Clicked(self):
        host = "localhost"
        port = 10000

        message = 'Client'
        try:
            print(f"Ouverture de la socket sur le serveur {host} port {port}")
            client_socket = socket.socket()
            client_socket.connect((host, port))
            print("Serveur est connecté")

            while message != 'bye':
                message = input("\nCommande Server : ")
                client_socket.send(message.encode())
                message = client_socket.recv(1024).decode()
                print(f"Message du serveur : \n{message}\n")

            client_socket.close()
            print("Connexion arrêter : Server")

        except(ConnectionError):
            print("il y a une erreur de connection")

        # Fermeture de la socket du client


    def btnPress4_Clicked(self):
        self.textEdit.setPlainText("")

    def btnPress5_Clicked(self):
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Chrono()
    win.show()
    sys.exit(app.exec_())
