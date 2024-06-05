from QtTest import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui

class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        #信号与槽
        self.OpenFileBtn.clicked.connect(self.loadImage)

    def loadImage(self):
        print("按钮被按下了")
        self.fname, _ = QFileDialog.getOpenFileName(self, caption='选择图片', directory='.', filter='图像文件(*.jpg *.png)')
        print(self.fname)
        pix = QtGui.QPixmap(self.fname).scaled(self.ImageLabel.width(), self.ImageLabel.height())
        self.ImageLabel.setPixmap(pix)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())