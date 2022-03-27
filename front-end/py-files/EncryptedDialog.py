import sys
import os

path = "E:\\NSI\\projets\\steganography"

os.chdir(path)
sys.path.append(f"{os.getcwd()}\\front-end\\py-files")
sys.path.append(f"{os.getcwd()}\\front-end\\ui-files")
sys.path.append(f"{os.getcwd()}\\back-end")
from PyQt5 import QtWidgets
from PyQt5 import uic

class EncryptedDialog(QtWidgets.QDialog):
    """
    Classe permettant de créer la fenêtre de dialogue de fin d'encryptage.
    """
    def __init__(self):
        super().__init__()
        uic.loadUi(f"{os.getcwd()}\\front-end\\ui-files\\encryptedDialog.ui", self) # On importe l'interface graphique liée à ce constructeur.

        self.imagePathLabel.setText(f"{os.getcwd()}") # On change le texte du label imagePathLabel pour y mettre le chemin d'acces de l'image générée.