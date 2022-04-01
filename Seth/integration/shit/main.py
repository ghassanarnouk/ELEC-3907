from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys

import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, qApp

from qroundprogressbar import QRoundProgressBar

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("mainui.ui", self)
		self.layout = self.findChild(QGridLayout,"gridLayout")
		
		
		progress = QRoundProgressBar()
		progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)

		# style accordingly via palette
		palette = QPalette()
		brush = QBrush(QColor(0, 0, 255))
		brush.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Highlight, brush)

		progress.setPalette(palette)
		progress.setLayout(layout)
		
		self.show()
		# simulate delayed time that a process may take to execute
		# from demonstration purposes only
		

app = QApplication(sys.argv)
UIWindow= UI()
app.exec_()