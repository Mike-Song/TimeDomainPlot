# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tasks\Work\TimeDomainPlot\TimeDomainPlot.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1300, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTimDomain = QtWidgets.QWidget()
        self.tabTimDomain.setObjectName("tabTimDomain")
        self.groupBox_TimeDomain = QtWidgets.QGroupBox(self.tabTimDomain)
        self.groupBox_TimeDomain.setGeometry(QtCore.QRect(0, 10, 131, 161))
        self.groupBox_TimeDomain.setObjectName("groupBox_TimeDomain")
        self.comboBox_TriggerDomain = QtWidgets.QComboBox(self.groupBox_TimeDomain)
        self.comboBox_TriggerDomain.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.comboBox_TriggerDomain.setObjectName("comboBox_TriggerDomain")
        self.comboBox_TriggerDomain.addItem("")
        self.comboBox_TriggerDomain.addItem("")
        self.label_Trigger_2 = QtWidgets.QLabel(self.groupBox_TimeDomain)
        self.label_Trigger_2.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_Trigger_2.setObjectName("label_Trigger_2")
        self.label_SampleNumber = QtWidgets.QLabel(self.groupBox_TimeDomain)
        self.label_SampleNumber.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_SampleNumber.setObjectName("label_SampleNumber")
        self.label = QtWidgets.QLabel(self.groupBox_TimeDomain)
        self.label.setGeometry(QtCore.QRect(80, 90, 31, 21))
        self.label.setObjectName("label")
        self.label_SampleNumber_6 = QtWidgets.QLabel(self.groupBox_TimeDomain)
        self.label_SampleNumber_6.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_SampleNumber_6.setObjectName("label_SampleNumber_6")
        self.comboBox_SampleRate = QtWidgets.QComboBox(self.groupBox_TimeDomain)
        self.comboBox_SampleRate.setGeometry(QtCore.QRect(10, 91, 61, 21))
        self.comboBox_SampleRate.setObjectName("comboBox_SampleRate")
        self.comboBox_SampleRate.addItem("")
        self.comboBox_SampleRate.addItem("")
        self.comboBox_SampleRate.addItem("")
        self.comboBox_RecordLength = QtWidgets.QComboBox(self.groupBox_TimeDomain)
        self.comboBox_RecordLength.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.comboBox_RecordLength.setEditable(False)
        self.comboBox_RecordLength.setMaxVisibleItems(100)
        self.comboBox_RecordLength.setObjectName("comboBox_RecordLength")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.comboBox_RecordLength.addItem("")
        self.widget_Signal_TimeDomain = QtWidgets.QWidget(self.tabTimDomain)
        self.widget_Signal_TimeDomain.setGeometry(QtCore.QRect(139, 40, 1120, 620))
        self.widget_Signal_TimeDomain.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget_Signal_TimeDomain.setObjectName("widget_Signal_TimeDomain")
        self.pushButton_Stop_TimeDomain = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Stop_TimeDomain.setEnabled(False)
        self.pushButton_Stop_TimeDomain.setGeometry(QtCore.QRect(10, 560, 101, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Stop_TimeDomain.sizePolicy().hasHeightForWidth())
        self.pushButton_Stop_TimeDomain.setSizePolicy(sizePolicy)
        self.pushButton_Stop_TimeDomain.setMinimumSize(QtCore.QSize(82, 23))
        self.pushButton_Stop_TimeDomain.setObjectName("pushButton_Stop_TimeDomain")
        self.pushButton_Start_TimeDomain = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Start_TimeDomain.setEnabled(True)
        self.pushButton_Start_TimeDomain.setGeometry(QtCore.QRect(10, 530, 101, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Start_TimeDomain.sizePolicy().hasHeightForWidth())
        self.pushButton_Start_TimeDomain.setSizePolicy(sizePolicy)
        self.pushButton_Start_TimeDomain.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_Start_TimeDomain.setObjectName("pushButton_Start_TimeDomain")
        self.groupBox_TimeDomain_2 = QtWidgets.QGroupBox(self.tabTimDomain)
        self.groupBox_TimeDomain_2.setGeometry(QtCore.QRect(0, 180, 131, 141))
        self.groupBox_TimeDomain_2.setObjectName("groupBox_TimeDomain_2")
        self.label_SampleNumber_2 = QtWidgets.QLabel(self.groupBox_TimeDomain_2)
        self.label_SampleNumber_2.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label_SampleNumber_2.setObjectName("label_SampleNumber_2")
        self.lineEdit_VolScale = QtWidgets.QLineEdit(self.groupBox_TimeDomain_2)
        self.lineEdit_VolScale.setGeometry(QtCore.QRect(10, 50, 51, 20))
        self.lineEdit_VolScale.setToolTip("")
        self.lineEdit_VolScale.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_VolScale.setPlaceholderText("")
        self.lineEdit_VolScale.setObjectName("lineEdit_VolScale")
        self.label_2 = QtWidgets.QLabel(self.groupBox_TimeDomain_2)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 41, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Offset = QtWidgets.QLineEdit(self.groupBox_TimeDomain_2)
        self.lineEdit_Offset.setGeometry(QtCore.QRect(10, 110, 51, 20))
        self.lineEdit_Offset.setToolTip("")
        self.lineEdit_Offset.setPlaceholderText("")
        self.lineEdit_Offset.setObjectName("lineEdit_Offset")
        self.label_SampleNumber_3 = QtWidgets.QLabel(self.groupBox_TimeDomain_2)
        self.label_SampleNumber_3.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_SampleNumber_3.setObjectName("label_SampleNumber_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_TimeDomain_2)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 31, 20))
        self.label_4.setObjectName("label_4")
        self.groupBox_TimeDomain_3 = QtWidgets.QGroupBox(self.tabTimDomain)
        self.groupBox_TimeDomain_3.setGeometry(QtCore.QRect(0, 330, 131, 91))
        self.groupBox_TimeDomain_3.setObjectName("groupBox_TimeDomain_3")
        self.label_FrameNum = QtWidgets.QLabel(self.groupBox_TimeDomain_3)
        self.label_FrameNum.setEnabled(False)
        self.label_FrameNum.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_FrameNum.setObjectName("label_FrameNum")
        self.checkBox_FrameMode = QtWidgets.QCheckBox(self.groupBox_TimeDomain_3)
        self.checkBox_FrameMode.setEnabled(False)
        self.checkBox_FrameMode.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.checkBox_FrameMode.setObjectName("checkBox_FrameMode")
        self.lineEdit_FrameNum = QtWidgets.QLineEdit(self.groupBox_TimeDomain_3)
        self.lineEdit_FrameNum.setEnabled(False)
        self.lineEdit_FrameNum.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.lineEdit_FrameNum.setObjectName("lineEdit_FrameNum")
        self.pushButton_Save_TimeDomain = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Save_TimeDomain.setEnabled(False)
        self.pushButton_Save_TimeDomain.setGeometry(QtCore.QRect(10, 590, 101, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Save_TimeDomain.sizePolicy().hasHeightForWidth())
        self.pushButton_Save_TimeDomain.setSizePolicy(sizePolicy)
        self.pushButton_Save_TimeDomain.setMinimumSize(QtCore.QSize(82, 23))
        self.pushButton_Save_TimeDomain.setObjectName("pushButton_Save_TimeDomain")
        self.radioButton_CHA = QtWidgets.QRadioButton(self.tabTimDomain)
        self.radioButton_CHA.setGeometry(QtCore.QRect(10, 450, 101, 21))
        self.radioButton_CHA.setChecked(True)
        self.radioButton_CHA.setObjectName("radioButton_CHA")
        self.radioButton_CHB = QtWidgets.QRadioButton(self.tabTimDomain)
        self.radioButton_CHB.setGeometry(QtCore.QRect(10, 480, 101, 21))
        self.radioButton_CHB.setObjectName("radioButton_CHB")
        self.pushButton_Home = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Home.setEnabled(True)
        self.pushButton_Home.setGeometry(QtCore.QRect(490, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Home.sizePolicy().hasHeightForWidth())
        self.pushButton_Home.setSizePolicy(sizePolicy)
        self.pushButton_Home.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_Home.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_Back = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Back.setEnabled(True)
        self.pushButton_Back.setGeometry(QtCore.QRect(550, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Back.sizePolicy().hasHeightForWidth())
        self.pushButton_Back.setSizePolicy(sizePolicy)
        self.pushButton_Back.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_Back.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Forward = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Forward.setEnabled(True)
        self.pushButton_Forward.setGeometry(QtCore.QRect(610, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Forward.sizePolicy().hasHeightForWidth())
        self.pushButton_Forward.setSizePolicy(sizePolicy)
        self.pushButton_Forward.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_Forward.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_Forward.setObjectName("pushButton_Forward")
        self.pushButton_Pan = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Pan.setEnabled(True)
        self.pushButton_Pan.setGeometry(QtCore.QRect(670, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Pan.sizePolicy().hasHeightForWidth())
        self.pushButton_Pan.setSizePolicy(sizePolicy)
        self.pushButton_Pan.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_Pan.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_Pan.setObjectName("pushButton_Pan")
        self.pushButton_Zoom = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_Zoom.setEnabled(True)
        self.pushButton_Zoom.setGeometry(QtCore.QRect(730, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Zoom.sizePolicy().hasHeightForWidth())
        self.pushButton_Zoom.setSizePolicy(sizePolicy)
        self.pushButton_Zoom.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_Zoom.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_Zoom.setObjectName("pushButton_Zoom")
        self.pushButton_SavePic = QtWidgets.QPushButton(self.tabTimDomain)
        self.pushButton_SavePic.setEnabled(True)
        self.pushButton_SavePic.setGeometry(QtCore.QRect(790, 10, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SavePic.sizePolicy().hasHeightForWidth())
        self.pushButton_SavePic.setSizePolicy(sizePolicy)
        self.pushButton_SavePic.setMinimumSize(QtCore.QSize(50, 23))
        self.pushButton_SavePic.setMaximumSize(QtCore.QSize(50, 23))
        self.pushButton_SavePic.setObjectName("pushButton_SavePic")
        self.groupBox_TimeDomain_4 = QtWidgets.QGroupBox(self.tabTimDomain)
        self.groupBox_TimeDomain_4.setGeometry(QtCore.QRect(0, 430, 131, 81))
        self.groupBox_TimeDomain_4.setObjectName("groupBox_TimeDomain_4")
        self.groupBox_TimeDomain_4.raise_()
        self.groupBox_TimeDomain.raise_()
        self.widget_Signal_TimeDomain.raise_()
        self.pushButton_Stop_TimeDomain.raise_()
        self.pushButton_Start_TimeDomain.raise_()
        self.groupBox_TimeDomain_2.raise_()
        self.groupBox_TimeDomain_3.raise_()
        self.pushButton_Save_TimeDomain.raise_()
        self.radioButton_CHA.raise_()
        self.radioButton_CHB.raise_()
        self.pushButton_Home.raise_()
        self.pushButton_Back.raise_()
        self.pushButton_Forward.raise_()
        self.pushButton_Pan.raise_()
        self.pushButton_Zoom.raise_()
        self.pushButton_SavePic.raise_()
        self.tabWidget.addTab(self.tabTimDomain, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action3G = QtWidgets.QAction(MainWindow)
        self.action3G.setCheckable(True)
        self.action3G.setObjectName("action3G")
        self.action100M = QtWidgets.QAction(MainWindow)
        self.action100M.setCheckable(True)
        self.action100M.setObjectName("action100M")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setCheckable(True)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setCheckable(True)
        self.actionStop.setObjectName("actionStop")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time-Domain Plot"))
        self.groupBox_TimeDomain.setTitle(_translate("MainWindow", " Horizontal Setting"))
        self.comboBox_TriggerDomain.setItemText(0, _translate("MainWindow", "Auto"))
        self.comboBox_TriggerDomain.setItemText(1, _translate("MainWindow", "External"))
        self.label_Trigger_2.setText(_translate("MainWindow", "Trigger:"))
        self.label_SampleNumber.setText(_translate("MainWindow", "Sample Rate:"))
        self.label.setText(_translate("MainWindow", "MS/s"))
        self.label_SampleNumber_6.setText(_translate("MainWindow", "Record Length:"))
        self.comboBox_SampleRate.setItemText(0, _translate("MainWindow", "500"))
        self.comboBox_SampleRate.setItemText(1, _translate("MainWindow", "1000"))
        self.comboBox_SampleRate.setItemText(2, _translate("MainWindow", "1250"))
        self.comboBox_RecordLength.setItemText(0, _translate("MainWindow", "1K"))
        self.comboBox_RecordLength.setItemText(1, _translate("MainWindow", "2K"))
        self.comboBox_RecordLength.setItemText(2, _translate("MainWindow", "4K"))
        self.comboBox_RecordLength.setItemText(3, _translate("MainWindow", "8K"))
        self.comboBox_RecordLength.setItemText(4, _translate("MainWindow", "16K"))
        self.comboBox_RecordLength.setItemText(5, _translate("MainWindow", "32K"))
        self.comboBox_RecordLength.setItemText(6, _translate("MainWindow", "64K"))
        self.comboBox_RecordLength.setItemText(7, _translate("MainWindow", "128K"))
        self.comboBox_RecordLength.setItemText(8, _translate("MainWindow", "256K"))
        self.comboBox_RecordLength.setItemText(9, _translate("MainWindow", "512K"))
        self.comboBox_RecordLength.setItemText(10, _translate("MainWindow", "1M"))
        self.comboBox_RecordLength.setItemText(11, _translate("MainWindow", "2M"))
        self.comboBox_RecordLength.setItemText(12, _translate("MainWindow", "4M"))
        self.comboBox_RecordLength.setItemText(13, _translate("MainWindow", "8M"))
        self.comboBox_RecordLength.setItemText(14, _translate("MainWindow", "16M"))
        self.comboBox_RecordLength.setItemText(15, _translate("MainWindow", "32M"))
        self.comboBox_RecordLength.setItemText(16, _translate("MainWindow", "64M"))
        self.comboBox_RecordLength.setItemText(17, _translate("MainWindow", "128M"))
        self.pushButton_Stop_TimeDomain.setText(_translate("MainWindow", "Stop"))
        self.pushButton_Start_TimeDomain.setText(_translate("MainWindow", "Start"))
        self.groupBox_TimeDomain_2.setTitle(_translate("MainWindow", " Vertical Setting"))
        self.label_SampleNumber_2.setText(_translate("MainWindow", "Voltage Scale:"))
        self.lineEdit_VolScale.setText(_translate("MainWindow", "3000"))
        self.label_2.setText(_translate("MainWindow", "mV/Div"))
        self.lineEdit_Offset.setText(_translate("MainWindow", "0"))
        self.label_SampleNumber_3.setText(_translate("MainWindow", "Offset:"))
        self.label_4.setText(_translate("MainWindow", "mV"))
        self.groupBox_TimeDomain_3.setTitle(_translate("MainWindow", " Frame Mode:"))
        self.label_FrameNum.setText(_translate("MainWindow", " Number:"))
        self.checkBox_FrameMode.setText(_translate("MainWindow", "Enable"))
        self.lineEdit_FrameNum.setText(_translate("MainWindow", "1"))
        self.pushButton_Save_TimeDomain.setText(_translate("MainWindow", "Save"))
        self.radioButton_CHA.setText(_translate("MainWindow", "Channel A"))
        self.radioButton_CHB.setText(_translate("MainWindow", "Channel B"))
        self.pushButton_Home.setToolTip(_translate("MainWindow", "Rest original view"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        self.pushButton_Back.setToolTip(_translate("MainWindow", "Back to previous view"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.pushButton_Forward.setToolTip(_translate("MainWindow", "Forward to next view"))
        self.pushButton_Forward.setText(_translate("MainWindow", "Forward"))
        self.pushButton_Pan.setToolTip(_translate("MainWindow", "Pan axes with left mouse, zoom with right"))
        self.pushButton_Pan.setText(_translate("MainWindow", "Pan"))
        self.pushButton_Zoom.setToolTip(_translate("MainWindow", "Zoom with rectange"))
        self.pushButton_Zoom.setText(_translate("MainWindow", "Zoom"))
        self.pushButton_SavePic.setToolTip(_translate("MainWindow", "Save the  picutue"))
        self.pushButton_SavePic.setText(_translate("MainWindow", "Save Pic"))
        self.groupBox_TimeDomain_4.setTitle(_translate("MainWindow", "Channel Selection:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTimDomain), _translate("MainWindow", "Time-Domain Plot"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.action3G.setText(_translate("MainWindow", "3G"))
        self.action100M.setText(_translate("MainWindow", "100M"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

