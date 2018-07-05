import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from mini_calc_ui import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.equal.clicked.connect(self.click_equal) #绑定等号按钮和回调函数

    def click_equal(self):                           #等号按钮的回调函数
        try:
            contain = str(eval(self.show_input.text()))  #获取输入的文本并转换为表达式
            if len(contain) > 12:                        #如果计算结果大于12位
                self.result.setText('结果大于12位')        #则显示结果无法显示
            else:
                self.result.setText(contain)             #计算结果小于12位则将计算结果输出结果框
        except:
            self.result.setText('表达式错误')             #如果表达式无法计算，则报错


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
