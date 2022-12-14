# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_file


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 680)
        MainWindow.setMinimumSize(QtCore.QSize(480, 680))
        MainWindow.setMaximumSize(QtCore.QSize(480, 680))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setWindowIcon(QtGui.QIcon(':/calc.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.zero_button.setObjectName("zero_button")
        self.gridLayout.addWidget(self.zero_button, 5, 0, 1, 1)
        self.seven_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.seven_button.setFont(font)
        self.seven_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.seven_button.setObjectName("seven_button")
        self.gridLayout.addWidget(self.seven_button, 2, 0, 1, 1)
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.output_label.setFont(font)
        self.output_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.gridLayout.addWidget(self.output_label, 0, 0, 1, 4)
        self.eight_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.eight_button.sizePolicy().hasHeightForWidth())
        self.eight_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eight_button.setFont(font)
        self.eight_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.eight_button.setObjectName("eight_button")
        self.gridLayout.addWidget(self.eight_button, 2, 1, 1, 1)
        self.two_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.two_button.setFont(font)
        self.two_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.two_button.setObjectName("two_button")
        self.gridLayout.addWidget(self.two_button, 4, 1, 1, 1)
        self.dot_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.dot_button.sizePolicy().hasHeightForWidth())
        self.dot_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dot_button.setFont(font)
        self.dot_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.dot_button.setObjectName("dot_button")
        self.gridLayout.addWidget(self.dot_button, 5, 1, 1, 1)
        self.five_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.five_button.setFont(font)
        self.five_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.five_button.setObjectName("five_button")
        self.gridLayout.addWidget(self.five_button, 3, 1, 1, 1)
        self.one_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.one_button.setFont(font)
        self.one_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.one_button.setObjectName("one_button")
        self.gridLayout.addWidget(self.one_button, 4, 0, 1, 1)
        self.nine_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nine_button.setFont(font)
        self.nine_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.nine_button.setObjectName("nine_button")
        self.gridLayout.addWidget(self.nine_button, 2, 2, 1, 1)
        self.division_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.division_button.sizePolicy().hasHeightForWidth())
        self.division_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.division_button.setFont(font)
        self.division_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.division_button.setObjectName("division_button")
        self.gridLayout.addWidget(self.division_button, 1, 3, 1, 1)
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.multiply_button.sizePolicy().hasHeightForWidth())
        self.multiply_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.multiply_button.setFont(font)
        self.multiply_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.multiply_button.setObjectName("multiply_button")
        self.gridLayout.addWidget(self.multiply_button, 2, 3, 1, 1)
        self.six_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.six_button.setFont(font)
        self.six_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.six_button.setObjectName("six_button")
        self.gridLayout.addWidget(self.six_button, 3, 2, 1, 1)
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.subtract_button.sizePolicy().hasHeightForWidth())
        self.subtract_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subtract_button.setFont(font)
        self.subtract_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.subtract_button.setObjectName("subtract_button")
        self.gridLayout.addWidget(self.subtract_button, 3, 3, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 4, 3, 1, 1)
        self.three_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.three_button.setFont(font)
        self.three_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.three_button.setObjectName("three_button")
        self.gridLayout.addWidget(self.three_button, 4, 2, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 1, 2, 1, 1)
        self.four_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.four_button.setFont(font)
        self.four_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.four_button.setObjectName("four_button")
        self.gridLayout.addWidget(self.four_button, 3, 0, 1, 1)
        self.equal_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(7, 189, 255);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 147, 221);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(7, 189, 255);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.equal_button.setObjectName("equal_button")
        self.gridLayout.addWidget(self.equal_button, 5, 2, 1, 2)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80,80,80);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(50, 50, 50);\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);}")
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.one_button.clicked.connect(self.one_method)
        self.two_button.clicked.connect(self.two_method)
        self.three_button.clicked.connect(self.three_method)
        self.four_button.clicked.connect(self.four_method)
        self.five_button.clicked.connect(self.five_method)
        self.six_button.clicked.connect(self.six_method)
        self.seven_button.clicked.connect(self.seven_method)
        self.eight_button.clicked.connect(self.eight_method)
        self.nine_button.clicked.connect(self.nine_method)
        self.zero_button.clicked.connect(self.zero_method)
        self.dot_button.clicked.connect(self.dot_method)

        self.add_button.clicked.connect(self.add_method)
        self.subtract_button.clicked.connect(self.subtract_method)
        self.multiply_button.clicked.connect(self.multiply_method)
        self.division_button.clicked.connect(self.division_method)

        self.equal_button.clicked.connect(self.equal_method)
        self.clear_button.clicked.connect(self.clear_method)
        self.delete_button.clicked.connect(self.delete_method)

        self.equal_pressed = False

    def check_equal(self, value):
        if self.equal_pressed == True:
            self.output_label.setText(value)
            self.equal_pressed = False

    def one_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()

        if current_text == "0":
             self.output_label.setText("1")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"1")
        else:
            self.output_label.setText(current_text+"1")

    def two_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("2")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"2")
        else:
            self.output_label.setText(current_text+"2")

    def three_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("3")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"3")
        else:
            self.output_label.setText(current_text+"3")

    def four_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("4")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"4")
        else:
            self.output_label.setText(current_text+"4")

    def five_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("5")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"5")
        else:
            self.output_label.setText(current_text+"5")

    def six_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("6")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"6")
        else:
            self.output_label.setText(current_text+"6")

    def seven_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("7")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"7")
        else:
            self.output_label.setText(current_text+"7")

    def eight_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("8")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"8")
        else:
            self.output_label.setText(current_text+"8")

    def nine_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("9")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"9")
        else:
            self.output_label.setText(current_text+"9")

    def zero_method(self):
        self.check_equal("0")
        current_text = self.output_label.text()
        if current_text == "0":
             self.output_label.setText("0")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"0")
        else:
            self.output_label.setText(current_text+"0")


    def add_method(self):
        self.equal_pressed = False
        current_text = self.output_label.text()
        if current_text.endswith(("+", "-", "x", "??")):
            self.output_label.setText(current_text[:-1] + "+")
        else:
            self.output_label.setText(current_text + "+")

    def subtract_method(self):
        self.equal_pressed = False
        current_text = self.output_label.text()
        if current_text.endswith(("+", "-", "x", "??")):
            self.output_label.setText(current_text[:-1] + "-")
        else:
            self.output_label.setText(current_text + "-")

    def multiply_method(self):
        self.equal_pressed = False
        current_text = self.output_label.text()
        if current_text.endswith(("+", "-", "x", "??")):
            self.output_label.setText(current_text[:-1] + "x")
        else:
            self.output_label.setText(current_text + "x")

    def division_method(self):
        self.equal_pressed = False
        current_text = self.output_label.text()
        if current_text.endswith(("+", "-", "x", "??")):
            self.output_label.setText(current_text[:-1] + "??")
        else:
            self.output_label.setText(current_text + "??")

    def equal_method(self):
        current_text = self.output_label.text()
        if current_text.endswith(("+", "-", "x", "??")):
            current_text = current_text[:-1]
        if "x" in current_text:
            multiply = current_text.replace("x", "*")
            if "??" in multiply:
                division = multiply.replace("??", "/")
                result = str(round(eval(division),6))
            else:
                result = str(round(eval(multiply),6))
        elif "??" in current_text:
            division = current_text.replace("??", "/")
            if "x" in division:
                multiply = division.replace("x", "*")
                result = str(round(eval(multiply),6))
            else:
                result = str(round(eval(division),6))
        else:
            result = str(round(eval(current_text),6))
        self.output_label.setText(result)
        self.equal_pressed = True

    def clear_method(self):
        self.output_label.setText("0")

    def delete_method(self):
        current_text = self.output_label.text()
        current_text = current_text[:-1]
        if current_text == "":
            self.output_label.setText("0")
        else:
            self.output_label.setText(current_text)

    def dot_method(self):
        self.check_equal("0.")
        current_text = self.output_label.text()
        if current_text.endswith("."):
            self.output_label.setText(current_text[:-1]+".")
        elif current_text.endswith(("+", "-", "x", "??")):
            self.output_label.setText(current_text+"0.")
        elif current_text == "0":
             self.output_label.setText("0.")
        elif current_text.endswith(("+0", "-0", "x0", "??0")):
            self.output_label.setText(current_text[:-1]+"0.")
        else:
            self.output_label.setText(current_text+".")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.zero_button.setShortcut(_translate("MainWindow", "0"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.seven_button.setShortcut(_translate("MainWindow", "7"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.eight_button.setShortcut(_translate("MainWindow", "8"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.two_button.setShortcut(_translate("MainWindow", "2"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.dot_button.setShortcut(_translate("MainWindow", "."))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.five_button.setShortcut(_translate("MainWindow", "5"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.one_button.setShortcut(_translate("MainWindow", "1"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.nine_button.setShortcut(_translate("MainWindow", "9"))
        self.division_button.setText(_translate("MainWindow", "??"))
        self.division_button.setShortcut(_translate("MainWindow", "/"))
        self.multiply_button.setText(_translate("MainWindow", "x"))
        self.multiply_button.setShortcut(_translate("MainWindow", "*"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.six_button.setShortcut(_translate("MainWindow", "6"))
        self.subtract_button.setText(_translate("MainWindow", "-"))
        self.subtract_button.setShortcut(_translate("MainWindow", "-"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.add_button.setShortcut(_translate("MainWindow", "+"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.three_button.setShortcut(_translate("MainWindow", "3"))
        self.delete_button.setText(_translate("MainWindow", "<<"))
        self.delete_button.setShortcut(_translate("MainWindow", "Backspace"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.four_button.setShortcut(_translate("MainWindow", "4"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.equal_button.setShortcut(_translate("MainWindow", "Enter"))
        self.clear_button.setText(_translate("MainWindow", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
