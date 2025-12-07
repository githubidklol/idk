import sys

from PyQt6.QtWidgets import QApplication

from PasswordGenerator import PassGenWindow

app = QApplication(sys.argv)
window = PassGenWindow()
window.show()
app.exec()