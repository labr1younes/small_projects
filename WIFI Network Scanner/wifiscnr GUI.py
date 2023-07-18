from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem,QProgressBar
from PyQt6 import uic
import wifiscnr as scnr
import sys

class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        
        #load th UI file
        uic.loadUi("UI.ui",self)

        #define widgets
        self.scantBtn = self.findChild(QPushButton,"scan")
        self.table = self.findChild(QTableWidget,"mytableWidget")
        self.pbar = self.findChild(QProgressBar, "progressBar")

        # adding functions
        self.scantBtn.clicked.connect(self.fun_scan)

        self.setWindowTitle("Wi-Fi Scanner")
        self.setFixedSize(250,250)
        self.show()

    def load_data(self,tmp):
        row = 0
        self.table.setRowCount(len(tmp))
        keys = list(tmp.keys())

        for key in keys:
            self.table.setItem(row, 0, QTableWidgetItem(key))
            self.table.setItem(row, 1, QTableWidgetItem(tmp[key]))
            row += 1
        self.pbar.setValue(100)

    def fun_scan(self):
        self.pbar.setValue(0)
        t = scnr.detect_new_devices()
        self.load_data(t)

if  __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UI()
    app.exec()
