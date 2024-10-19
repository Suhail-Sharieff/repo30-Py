import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont,QFontDatabase


class DigClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dig Clock")
        self.setGeometry(600,600,400,200)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:140px;" 
                                       "color:hsl(111,100%,50%);")

        self.setStyleSheet("background-color:black;")

        fontId=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        fontFam=QFontDatabase.applicationFontFamilies(fontId)[0]
        my_font=QFont(fontFam,140)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.setTime)
        self.timer.start(1000)
         
        self.setTime()

    def setTime(self):
        currTime=QTime.currentTime().toString("hh : mm : ss AP")
        self.time_label.setText(currTime)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigClock()
    clock.show()
    sys.exit(app.exec_())
