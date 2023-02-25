import sys

from PyQt5.QtWidgets import QApplication, QDialog
from Ui_Create_event import *
app = QApplication(sys.argv)

class Create_Event(Ui_Create_event):
    def __init__(self):
        dialog2 = QDialog()
        super().setupUi(dialog2)
        dialog2.exec()


create_event = Create_Event()
sys.exit(app.exec())