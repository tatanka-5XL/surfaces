# gui.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import classes

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(802, 483)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelShape = QtWidgets.QLabel(self.centralwidget)
        self.labelShape.setGeometry(QtCore.QRect(20, 35, 180, 24))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelShape.setFont(font)
        self.labelShape.setObjectName("labelTvar")
        self.ComboShape = QtWidgets.QComboBox(self.centralwidget)
        self.ComboShape.setGeometry(QtCore.QRect(210, 35, 210, 24))
        self.ComboShape.setObjectName("boxTvar")
        self.ComboShape.addItem("")
        self.ComboShape.addItem("")
        self.ComboShape.addItem("")
        self.ComboShape.addItem("")
        self.ComboShape.addItem("")
        self.confirmShapeButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmShapeButton.setGeometry(QtCore.QRect(430, 35, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmShapeButton.setFont(font)
        self.confirmShapeButton.setObjectName("vyber")
        self.labelPic = QtWidgets.QLabel(self.centralwidget)
        self.labelPic.setGeometry(QtCore.QRect(20, 70, 697, 137))
        self.labelPic.setText("")
        self.labelPic.setPixmap(QtGui.QPixmap("src/img/ctverec.png"))
        self.labelPic.setObjectName("labelPic")
        self.labelParams = QtWidgets.QLabel(self.centralwidget)
        self.labelParams.setGeometry(QtCore.QRect(20, 220, 130, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelParams.setFont(font)
        self.labelParams.setObjectName("labelParams")
        self.lineEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(50, 250, 113, 20))
        self.lineEditA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditA.setObjectName("lineEditA")
        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setGeometry(QtCore.QRect(21, 249, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)  
        self.labelA.setFont(font)
        self.labelA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelA.setObjectName("inputA")
        self.lineEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(50, 280, 113, 20))
        self.lineEditB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditB.hide()
        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setGeometry(QtCore.QRect(20, 279, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelB.setFont(font)
        self.labelB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelB.setObjectName("inputB")
        self.labelB.hide()
        self.lineEditC = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditC.setGeometry(QtCore.QRect(50, 309, 113, 20))
        self.lineEditC.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditC.setObjectName("lineEditC")
        self.lineEditC.hide()
        self.labelC = QtWidgets.QLabel(self.centralwidget)
        self.labelC.setGeometry(QtCore.QRect(20, 308, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelC.setFont(font)
        self.labelC.setAlignment(QtCore.Qt.AlignCenter)
        self.labelC.setObjectName("inputC")
        self.labelC.hide()
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(560, 420, 141, 24))
        self.labelResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setFrameShape(QtWidgets.QFrame.Box)
        self.labelResult.setStyleSheet("background-color: white")
        self.labelResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.labelResultDesc = QtWidgets.QLabel(self.centralwidget)
        self.labelResultDesc.setGeometry(QtCore.QRect(500, 420, 60, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelResultDesc.setFont(font)
        self.labelResultDesc.setObjectName("labelResultDesc")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(710, 420, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setAutoDefault(True)
        self.lineEditA.returnPressed.connect(self.submitButton.click)
        self.lineEditB.returnPressed.connect(self.submitButton.click)
        self.lineEditC.returnPressed.connect(self.submitButton.click)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.confirmShapeButton.clicked.connect(self.select_shape)
        self.submitButton.clicked.connect(self.calculate)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Výpočet obsahu"))
        self.labelShape.setText(_translate("mainWindow", "Geometrický tvar:"))
        self.ComboShape.setItemText(0, _translate("mainWindow", "Čtverec"))
        self.ComboShape.setItemText(1, _translate("mainWindow", "Obdélník"))
        self.ComboShape.setItemText(2, _translate("mainWindow", "Trojúhelník"))
        self.ComboShape.setItemText(3, _translate("mainWindow", "Lichoběžník"))
        self.ComboShape.setItemText(4, _translate("mainWindow", "Kruh"))
        self.confirmShapeButton.setText(_translate("mainWindow", "Vybrat"))
        self.labelParams.setText(_translate("mainWindow", "Parametry výpočtu"))
        self.labelA.setText(_translate("mainWindow", "a"))
        self.labelResultDesc.setText(_translate("mainWindow", "Výsledek"))
        self.labelResult.setText(_translate("mainWindow", "0"))
        self.submitButton.setText(_translate("mainWindow", "Vypočítat"))
        self.labelB.setText(_translate("mainWindow", "c"))
        self.labelC.setText(_translate("mainWindow", "h"))

    def select_shape(self):
        shape = self.ComboShape.currentIndex()
        if shape == 0:
            self.labelPic.setPixmap(QtGui.QPixmap("src/img/ctverec.png"))
            self.lineEditA.clear()
            self.lineEditB.hide()
            self.lineEditC.hide()
            self.labelA.setText("a")
            self.labelB.hide()
            self.labelC.hide()
            self.labelResult.clear()

        elif shape == 1:
            self.labelPic.setPixmap(QtGui.QPixmap("src/img/obdelnik.png"))
            self.lineEditB.show()
            self.lineEditC.hide()
            self.labelA.setText("a")
            self.labelB.show()
            self.labelB.setText("b")
            self.labelC.hide()
            self.labelResult.clear()

        elif shape == 2:
            self.labelPic.setPixmap(QtGui.QPixmap("src/img/trojuhelnik.png"))
            self.lineEditA.clear()
            self.lineEditB.show()
            self.lineEditB.clear()
            self.lineEditC.hide()
            self.labelA.setText("a")
            self.labelB.show()
            self.labelB.setText("h")
            self.labelC.hide()
            self.labelResult.clear()

        elif shape == 3:
            self.labelPic.setPixmap(QtGui.QPixmap("src/img/lichobeznik.png"))
            self.lineEditA.clear()
            self.lineEditB.show()
            self.lineEditB.clear()
            self.lineEditC.show()
            self.lineEditC.clear()
            self.labelA.setText("a")
            self.labelB.show()
            self.labelB.setText("c")
            self.labelC.show()
            self.labelC.setText("h")
            self.labelResult.clear()

        else:
            self.labelPic.setPixmap(QtGui.QPixmap("src/img/kruh.png"))
            self.lineEditA.clear()
            self.lineEditB.hide()
            self.lineEditC.hide()
            self.labelA.setText("r")
            self.labelB.hide()
            self.labelC.hide()
            self.labelResult.clear()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Neplatný vstup")
        msg.setText("Musíte vložit kladné číslo")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def validate(self, input):
        try:
            float(input)
            if float(input) > 0:
                return True
            else:
                return False
        except ValueError:
            return False


    def calculate(self):
        shape = self.ComboShape.currentIndex()
        if shape == 0:
            a = self.lineEditA.text()
            if self.validate(a):
                sq = classes.Square(float(a))
                self.labelResult.setText(str(sq.surface()))
            else:
                self.show_popup()
        elif shape == 1:
            a = self.lineEditA.text()
            b = self.lineEditB.text()
            if self.validate(a) and self.validate(b):
                rect = classes.Rectangle(float(a), float(b))
                self.labelResult.setText(str(rect.surface()))
            else:
                self.show_popup()
        elif shape == 2:
            a = self.lineEditA.text()
            h = self.lineEditB.text()
            if self.validate(a) and self.validate(h):
                tri = classes.Triangle(float(a), float(h))
                self.labelResult.setText(str(tri.surface()))
            else:
                self.show_popup()
        elif shape == 3:
            a = self.lineEditA.text()
            c = self.lineEditB.text()
            h = self.lineEditC.text()
            if self.validate(a) and self.validate(c) and self.validate(h):
                trap = classes.Trapezoid(float(a), float(c), float(h))
                self.labelResult.setText(str(trap.surface()))
            else:
                self.show_popup()
        else:
            r = self.lineEditA.text()
            if self.validate(r):
                cir = classes.Circle(float(r))
                self.labelResult.setText(str(cir.surface()))
            else:
                self.show_popup()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = QtWidgets.QMainWindow()
#     ui = Ui_mainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())
