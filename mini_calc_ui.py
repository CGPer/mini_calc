# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mini_calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.show_input = QtWidgets.QLineEdit(Form)
        self.show_input.setGeometry(QtCore.QRect(10, 10, 421, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_input.sizePolicy().hasHeightForWidth())
        self.show_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.show_input.setFont(font)
        self.show_input.setToolTip("")
        self.show_input.setStyleSheet("")
        self.show_input.setInputMask("")
        self.show_input.setText("")
        self.show_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.show_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.show_input.setObjectName("show_input")
        self.equal = QtWidgets.QPushButton(Form)
        self.equal.setGeometry(QtCore.QRect(10, 70, 124, 51))
        self.equal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.equal.setObjectName("equal")
        self.result = QtWidgets.QLineEdit(Form)
        self.result.setGeometry(QtCore.QRect(142, 71, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setMaxLength(12)
        self.result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(340, 70, 91, 51))
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("background-color:rgb(0, 255, 255)")
        self.clear.setObjectName("clear")

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.result.clear)
        self.clear.clicked.connect(self.show_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "迷你计算器"))
        self.show_input.setPlaceholderText(_translate("Form", "示例：sqrt(2)+sin(pi/2)+2**3-5/2"))
        self.equal.setText(_translate("Form", "＝"))
        self.equal.setShortcut(_translate("Form", "Enter"))
        self.clear.setText(_translate("Form", "清除"))
