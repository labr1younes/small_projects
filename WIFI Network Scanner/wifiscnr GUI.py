from PyQt6.QtWidgets import QApplication, QWidget ,QLabel ,QPushButton ,QSpinBox, QListView,QHBoxLayout
from PyQt6 import uic
import wifiscnr as scnr
import sys

class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        
        #load th UI file
        uic.loadUi("UI.ui",self)

        #define widgets
        self.startBtn = self.findChild(QPushButton,"start")
        self.stopBtn = self.findChild(QPushButton,"stop")
        self.timeSpn = self.findChild(QSpinBox,"time")
        self.listView = self.findChild(QListView,"mylistView")

        # adding functions
        self.startBtn.clicked.connect(self.fun_start)
        self.stopBtn.clicked.connect(self.fun_stop)

        self.show()
        
    def fun_start(self):
        t = scnr.detect_new_devices()
        scnr.show(t)
        print(f"this is Start, and it s {tmp}")

    def fun_stop(self):
        tmp = self.timeSpn.value()
        print(f"this is Stop, and it s {tmp}")
        
        

        
        
if  __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UI()
    app.exec()
