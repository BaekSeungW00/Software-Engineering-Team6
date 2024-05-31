# Form implementation generated from reading ui file 'voca_select_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VocaSelect(object):
    def setupUi(self, VocaSelect):
        VocaSelect.setObjectName("VocaSelect")
        VocaSelect.resize(1000, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=VocaSelect)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 240, 991, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hackersButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.hackersButton.setMinimumSize(QtCore.QSize(300, 70))
        self.hackersButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hackersButton.setFont(font)
        self.hackersButton.setObjectName("hackersButton")
        self.horizontalLayout.addWidget(self.hackersButton)
        self.wordMasterButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.wordMasterButton.setMinimumSize(QtCore.QSize(300, 70))
        self.wordMasterButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.wordMasterButton.setFont(font)
        self.wordMasterButton.setObjectName("wordMasterButton")
        self.horizontalLayout.addWidget(self.wordMasterButton)
        self.amazingTalkerButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.amazingTalkerButton.setMinimumSize(QtCore.QSize(300, 70))
        self.amazingTalkerButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.amazingTalkerButton.setFont(font)
        self.amazingTalkerButton.setObjectName("amazingTalkerButton")
        self.horizontalLayout.addWidget(self.amazingTalkerButton)
        self.label = QtWidgets.QLabel(parent=VocaSelect)
        self.label.setGeometry(QtCore.QRect(304, 167, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(VocaSelect)
        QtCore.QMetaObject.connectSlotsByName(VocaSelect)

    def retranslateUi(self, VocaSelect):
        _translate = QtCore.QCoreApplication.translate
        VocaSelect.setWindowTitle(_translate("VocaSelect", "Dialog"))
        self.hackersButton.setText(_translate("VocaSelect", "해커스"))
        self.wordMasterButton.setText(_translate("VocaSelect", "워드 마스터"))
        self.amazingTalkerButton.setText(_translate("VocaSelect", "어메이징 토커"))
        self.label.setText(_translate("VocaSelect", "단어장을 선택하세요"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VocaSelect = QtWidgets.QDialog()
    ui = Ui_VocaSelect()
    ui.setupUi(VocaSelect)
    VocaSelect.show()
    sys.exit(app.exec())
