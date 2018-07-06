import sys
from math import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from mini_calc_ui import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.equal.clicked.connect(self.click_equal) #绑定等号按钮和回调函数

    def click_equal(self):                           #等号按钮的回调函数
        try:
            contain = eval(self.show_input.text())   #获取输入的文本并转换为表达式
            length = str(round(contain, 10))         #将精度设置为小数点后10位
            self.result.setText(length)              #将计算结果输出结果框
        except:
            self.result.setText('表达式错误')          #如果表达式无法计算，则报错


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
