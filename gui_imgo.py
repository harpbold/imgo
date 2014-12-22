#/usr/bin/env python

from PyQt4 import QtGui, QtCore
import sys
import os


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()
        self.recursion = True
        self.dir_name = ""

    def init_ui(self):
        self.setWindowTitle("IMGO")
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        cb1 = QtGui.QCheckBox("Recursive", self)
        cb1.setChecked(True)

        btn = QtGui.QPushButton("Select folder", self)
        btn.setToolTip("Select the folder on which the script will operate")

        btn_imgo = QtGui.QPushButton("Run IMGO", self)
        btn_imgo.setToolTip("Run IMGO(Iamge Organizer) script which will delete duplicate "
                       "files, \nfix wrong extensions and order images to folders by their dimension")

        self.label = QtGui.QLabel("Selected folder: <none>", self)
        grid.addWidget(self.label, 0, 0, 1, 2)
        grid.addWidget(btn, 1, 0)
        grid.addWidget(btn_imgo, 1, 1)
        grid.addWidget(cb1, 2, 0)

        btn.clicked.connect(self.select_file)
        btn_imgo.clicked.connect(self.run_imgo)
        cb1.pressed.connect(self.toggle_recursion)

        self.setFixedSize(self.sizeHint())
        self.center()
        self.show()

    def run_imgo(self):
        if self.dir_name == "":
            return
        s = 'python imgo.py '
        s += str(self.dir_name)
        if self.recursion:
            s += " -r"
        print s
        os.system(s)

    def select_file(self):
        self.dir_name = QtGui.QFileDialog.getExistingDirectory(self, 'Folder selection', '/')
        if self.dir_name != "":
            self.label.setText("Selected folder: " + self.dir_name)
        self.setFixedSize(self.sizeHint())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def toggle_recursion(self):
        self.recursion = not self.recursion


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
