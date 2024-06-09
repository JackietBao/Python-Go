from QtTest import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtGui

class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        #信号与槽
        self.OpenFileBtn.clicked.connect(self.loadImage)
        self.actionOpen.triggered.connect(self.loadImage)
        self.actionexit.triggered.connect(self.exit)
        self.actionabout.triggered.connect(self.about)

    def loadImage(self):
        #print("按钮被按下了")
        #self.ifolabel.setText("打开文件按钮被按下了")
        self.fname, _ = QFileDialog.getOpenFileName(self, caption='选择图片', directory='.', filter='图像文件(*.jpg *.png)')
        print(self.fname)
        pix = QtGui.QPixmap(self.fname).scaled(self.ImageLabel.width(), self.ImageLabel.height())
        self.ImageLabel.setPixmap(pix)

    def exit(self):
        sys.exit(app.exec_())

    def about(self):
        self.ifolabel.setText("帮助文件按钮被按下了")
        QMessageBox.information(self, '软件说明', '该软件由JackietBao制作而成，软件版本为 1.0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())