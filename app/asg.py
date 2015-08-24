# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'as.ui'
#
# Created: Fri Aug  7 14:08:01 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main_window(object):
    def setupUi(self, Main_window):
        Main_window.setObjectName(_fromUtf8("Main_window"))
        Main_window.resize(825, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main_window.sizePolicy().hasHeightForWidth())
        Main_window.setSizePolicy(sizePolicy)
        Main_window.setMinimumSize(QtCore.QSize(825, 582))
        Main_window.setMaximumSize(QtCore.QSize(825, 582))
        Main_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget = QtGui.QWidget(Main_window)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.table_networks = QtGui.QTableWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_networks.sizePolicy().hasHeightForWidth())
        self.table_networks.setSizePolicy(sizePolicy)
        self.table_networks.setMinimumSize(QtCore.QSize(0, 350))
        self.table_networks.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_networks.setSizeIncrement(QtCore.QSize(0, 0))
        self.table_networks.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.table_networks.setObjectName(_fromUtf8("table_networks"))
        self.table_networks.setColumnCount(8)
        self.table_networks.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table_networks.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.table_networks)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 26, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_rescan_networks = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rescan_networks.sizePolicy().hasHeightForWidth())
        self.button_rescan_networks.setSizePolicy(sizePolicy)
        self.button_rescan_networks.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_rescan_networks.setObjectName(_fromUtf8("button_rescan_networks"))
        self.horizontalLayout.addWidget(self.button_rescan_networks)
        self.button_attack = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_attack.sizePolicy().hasHeightForWidth())
        self.button_attack.setSizePolicy(sizePolicy)
        self.button_attack.setObjectName(_fromUtf8("button_attack"))
        self.horizontalLayout.addWidget(self.button_attack)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.text_output = QtGui.QTextEdit(self.widget)
        self.text_output.setObjectName(_fromUtf8("text_output"))
        self.verticalLayout.addWidget(self.text_output)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        Main_window.setCentralWidget(self.widget)

        QtCore.QObject.connect(self.button_rescan_networks, QtCore.SIGNAL(_fromUtf8("clicked()")), self.scan_process)
        QtCore.QObject.connect(self.button_attack, QtCore.SIGNAL(_fromUtf8("clicked()")), self.check_network)

        self.retranslateUi(Main_window)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        Main_window.setWindowTitle(_translate("Main_window", "WifiFactoryPass-GreekTool", None))
        item = self.table_networks.horizontalHeaderItem(0)
        item.setText(_translate("Main_window", "Essid", None))
        item = self.table_networks.horizontalHeaderItem(1)
        item.setText(_translate("Main_window", "Bssid", None))
        item = self.table_networks.horizontalHeaderItem(2)
        item.setText(_translate("Main_window", "Channel", None))
        item = self.table_networks.horizontalHeaderItem(3)
        item.setText(_translate("Main_window", "Signal", None))
        item = self.table_networks.horizontalHeaderItem(4)
        item.setText(_translate("Main_window", "Enc", None))
        item = self.table_networks.horizontalHeaderItem(5)
        item.setText(_translate("Main_window", "Cypher", None))
        item = self.table_networks.horizontalHeaderItem(6)
        item.setText(_translate("Main_window", "Auth", None))
        item = self.table_networks.horizontalHeaderItem(7)
        item.setText(_translate("Main_window", "Mb", None))
        self.button_rescan_networks.setText(_translate("Main_window", "Scan networks", None))
        self.button_attack.setText(_translate("Main_window", "Attack Current Network", None))

