from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from datetime import date


import sys
from lib import api
app = QApplication(sys.argv)

class AvailableCharts:

    def __init__(self):
        self.cov_chart = QWidget()
        self.cov_chart.setWindowTitle('Cov19 Pychart')
        self.cov_chart.setGeometry(500, 500, 500, 500)
        self.cov_chart.move(100, 150)

    def demo_chart(self):
        one_chart = QLabel(parent=self.cov_chart)
        pixmap = QPixmap(f"{date.today()}.png")
        one_chart.setPixmap(pixmap)
        one_chart.setScaledContents(True)
        one_chart.setMaximumSize(500, 500)

    def show_chart(self):
        self.demo_chart()
        self.cov_chart.show()
        sys.exit(app.exec_())

AvailableCharts().show_chart()