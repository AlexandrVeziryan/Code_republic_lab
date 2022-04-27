
from cProfile import label
from cgitb import text
from ctypes import pointer
from PyQt5 import QtCore, QtGui, QtWidgets

can_clear = False    
memory = 0
point_size = 30

# len_to_size = {}
# size = 30
# for i in range(20):
#     if i < 11:
#         len_to_size[i] = size
#     else:
#         size -= 2
#         len_to_size[i] = size


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(287, 518)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.memory_recall = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("mr"))
        self.memory_recall.setGeometry(QtCore.QRect(220, 100, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.memory_recall.setFont(font)
        self.memory_recall.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.memory_recall.setObjectName("memory_recall")
        self.memory_minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("m-"))
        self.memory_minus.setGeometry(QtCore.QRect(150, 100, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.memory_minus.setFont(font)
        self.memory_minus.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.memory_minus.setObjectName("memory_minus")
        self.devide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.devide.setGeometry(QtCore.QRect(220, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.devide.setFont(font)
        self.devide.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(233, 185, 110);")
        self.devide.setObjectName("devide")
        self.percent = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.percent.setGeometry(QtCore.QRect(150, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.percent.setFont(font)
        self.percent.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.percent.setObjectName("percent")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.multiply.setGeometry(QtCore.QRect(220, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(233, 185, 110);")
        self.multiply.setObjectName("multiply")
        self.num_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.num_9.setGeometry(QtCore.QRect(150, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_9.setFont(font)
        self.num_9.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_9.setObjectName("num_9")
        self.num_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.num_6.setGeometry(QtCore.QRect(150, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_6.setFont(font)
        self.num_6.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_6.setObjectName("num_6")
        self.minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minus.setGeometry(QtCore.QRect(220, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.minus.setFont(font)
        self.minus.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(233, 185, 110);")
        self.minus.setObjectName("minus")
        self.memory_plus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("m+"))
        self.memory_plus.setGeometry(QtCore.QRect(80, 100, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.memory_plus.setFont(font)
        self.memory_plus.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.memory_plus.setObjectName("memory_plus")
        self.square_root = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("√"))
        self.square_root.setGeometry(QtCore.QRect(80, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.square_root.setFont(font)
        self.square_root.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.square_root.setObjectName("square_root")
        self.num_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.num_8.setGeometry(QtCore.QRect(80, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_8.setFont(font)
        self.num_8.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_8.setObjectName("num_8")
        self.num_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.num_5.setGeometry(QtCore.QRect(80, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_5.setFont(font)
        self.num_5.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_5.setObjectName("num_5")
        self.memory_clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("mc"))
        self.memory_clear.setGeometry(QtCore.QRect(10, 100, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.memory_clear.setFont(font)
        self.memory_clear.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.memory_clear.setObjectName("memory_clear")
        self.all_clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("AC"))
        self.all_clear.setGeometry(QtCore.QRect(10, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.all_clear.setFont(font)
        self.all_clear.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.all_clear.setObjectName("all_clear")
        self.num_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.num_7.setGeometry(QtCore.QRect(10, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_7.setFont(font)
        self.num_7.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_7.setObjectName("num_7")
        self.num_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.num_4.setGeometry(QtCore.QRect(10, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_4.setFont(font)
        self.num_4.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_4.setObjectName("num_4")
        global point_size
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(30)# point_size
        print(point_size)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.num_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.num_2.setGeometry(QtCore.QRect(80, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_2.setFont(font)
        self.num_2.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_2.setObjectName("num_2")
        self.num_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.num_3.setGeometry(QtCore.QRect(150, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_3.setFont(font)
        self.num_3.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_3.setObjectName("num_3")
        self.plus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.plus.setGeometry(QtCore.QRect(220, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(233, 185, 110);")
        self.plus.setObjectName("plus")
        self.num_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.num_1.setGeometry(QtCore.QRect(10, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_1.setFont(font)
        self.num_1.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_1.setObjectName("num_1")
        self.dot = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("."))
        self.dot.setGeometry(QtCore.QRect(80, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dot.setFont(font)
        self.dot.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.dot.setObjectName("dot")
        self.squar_degree = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("x^2"))
        self.squar_degree.setGeometry(QtCore.QRect(80, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.squar_degree.setFont(font)
        self.squar_degree.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.squar_degree.setObjectName("squar_degree")
        self.pi = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3.14"))
        self.pi.setGeometry(QtCore.QRect(10, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pi.setFont(font)
        self.pi.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.pi.setObjectName("pi")
        self.plus_minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+/-"))
        self.plus_minus.setGeometry(QtCore.QRect(150, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.plus_minus.setFont(font)
        self.plus_minus.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.plus_minus.setCheckable(False)
        self.plus_minus.setObjectName("plus_minus")
        self.round_to_0_decimals = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.round_to_0_decimals.setGeometry(QtCore.QRect(220, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.round_to_0_decimals.setFont(font)
        self.round_to_0_decimals.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.round_to_0_decimals.setObjectName("round_to_0_decimals")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("="))
        self.equal.setGeometry(QtCore.QRect(220, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(233, 185, 110);")
        self.equal.setObjectName("equal")
        self.num_0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.num_0.setGeometry(QtCore.QRect(10, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.num_0.setFont(font)
        self.num_0.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(211, 215, 207);")
        self.num_0.setObjectName("num_0")
        self.round_to_2_decimals = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.round_to_2_decimals.setGeometry(QtCore.QRect(150, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.round_to_2_decimals.setFont(font)
        self.round_to_2_decimals.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(136, 138, 133);")
        self.round_to_2_decimals.setObjectName("round_to_2_decimals")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
    
    def press_it(self, pressed):
        global can_clear    
        global memory    
        global point_size    
        if can_clear and pressed in "3.140256789":
            self.label.setText("0")
        can_clear = False
        if pressed in "%/*-+"and self.label.text()[-1] in "%/*-+":
            self.label.setText(self.label.text()[:-1] + pressed)
        elif pressed == "AC":
            self.label.setText("0")
            can_clear = True
        elif pressed == "3.14":
            self.label.setText("3.14")
        elif pressed == "√":
            self.label.setText(f"{float(self.label.text()) ** 0.5:.2f}")
            can_clear = True
        elif pressed == "mc":
            memory = 0
            self.label.setText("0")
            can_clear = True
        elif pressed == "m+":
            can_clear = True
            try:
                memory += eval(self.label.text())
            except:            
                self.label.setText("error")
        elif pressed == "m-":
            can_clear = True
            try:
                memory -= eval(self.label.text())
            except:            
                self.label.setText("error")
        elif pressed == "mr":
            self.label.setText(f"{memory}")
            can_clear = True
        elif pressed == "x^2":
            self.label.setText(f"{float(self.label.text()) ** 2:.2f}")
            can_clear = True
        elif pressed == "=":
            try:
                text = self.label.text()
                if text[-1] in "%/*-+":
                    text = text[:-1]
                strr = str(eval(text))
            except:
                strr = "error"            
            self.label.setText(strr)
            can_clear = True
        elif pressed == "+/-":
            try:
                strr = str(eval(self.label.text()) * -1)
            except:
                strr = "error"            
            self.label.setText(strr)
            can_clear = True
        else:
            #Chechink if starts with 0
            if self.label.text() == "0":
                self.label.setText("")
            if len(self.label.text()) < 11:    
                self.label.setText(f'{self.label.text()}{pressed}')

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.memory_recall.setText(_translate("Calculator", "mr"))
        self.memory_minus.setText(_translate("Calculator", "m-"))
        self.devide.setText(_translate("Calculator", "/"))
        self.percent.setText(_translate("Calculator", "%"))
        self.multiply.setText(_translate("Calculator", "*"))
        self.num_9.setText(_translate("Calculator", "9"))
        self.num_6.setText(_translate("Calculator", "6"))
        self.minus.setText(_translate("Calculator", "-"))
        self.memory_plus.setText(_translate("Calculator", "m+"))
        self.square_root.setText(_translate("Calculator", "√x"))
        self.num_8.setText(_translate("Calculator", "8"))
        self.num_5.setText(_translate("Calculator", "5"))
        self.memory_clear.setText(_translate("Calculator", "mc"))
        self.all_clear.setText(_translate("Calculator", "AC"))
        self.num_7.setText(_translate("Calculator", "7"))
        self.num_4.setText(_translate("Calculator", "4"))
        self.label.setText(_translate("Calculator", "0"))
        self.num_2.setText(_translate("Calculator", "2"))
        self.num_3.setText(_translate("Calculator", "3"))
        self.plus.setText(_translate("Calculator", "+"))
        self.num_1.setText(_translate("Calculator", "1"))
        self.dot.setText(_translate("Calculator", "."))
        self.squar_degree.setText(_translate("Calculator", "x^2"))
        self.pi.setText(_translate("Calculator", "兀"))
        self.plus_minus.setText(_translate("Calculator", "+/-"))
        self.round_to_0_decimals.setText(_translate("Calculator", "R0"))
        self.equal.setText(_translate("Calculator", "="))
        self.num_0.setText(_translate("Calculator", "0"))
        self.round_to_2_decimals.setText(_translate("Calculator", "R2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
