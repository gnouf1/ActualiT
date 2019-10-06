# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1428, 885)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.articleShower = QtWidgets.QTextBrowser(self.centralwidget)
        self.articleShower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.articleShower.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.articleShower.setOpenExternalLinks(True)
        self.articleShower.setObjectName("articleShower")
        self.gridLayout.addWidget(self.articleShower, 0, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        self.mainCol = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.mainCol.setFont(font)
        self.mainCol.setStyleSheet("font: 15pt \"Montserrat\";\n"
"QListWidget.item : padding 10px;\n"
"")
        self.mainCol.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainCol.setLineWidth(10)
        self.mainCol.setObjectName("mainCol")
        self.gridLayout.addWidget(self.mainCol, 0, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 9, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 8, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1428, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuRSS = QtWidgets.QMenu(self.menuBar)
        self.menuRSS.setObjectName("menuRSS")
        self.menuTwitter = QtWidgets.QMenu(self.menuBar)
        self.menuTwitter.setObjectName("menuTwitter")
        self.menuReddit = QtWidgets.QMenu(self.menuBar)
        self.menuReddit.setObjectName("menuReddit")
        self.menuSources_Primitives = QtWidgets.QMenu(self.menuBar)
        self.menuSources_Primitives.setObjectName("menuSources_Primitives")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAjouter_Supprimer = QtWidgets.QAction(MainWindow)
        self.actionAjouter_Supprimer.setObjectName("actionAjouter_Supprimer")
        self.actionAjouter_Supprimer_2 = QtWidgets.QAction(MainWindow)
        self.actionAjouter_Supprimer_2.setObjectName("actionAjouter_Supprimer_2")
        self.actionAjouter_Supprimer_3 = QtWidgets.QAction(MainWindow)
        self.actionAjouter_Supprimer_3.setObjectName("actionAjouter_Supprimer_3")
        self.actionD_sactiver = QtWidgets.QAction(MainWindow)
        self.actionD_sactiver.setObjectName("actionD_sactiver")
        self.menuRSS.addAction(self.actionAjouter_Supprimer)
        self.menuTwitter.addAction(self.actionAjouter_Supprimer_2)
        self.menuReddit.addAction(self.actionAjouter_Supprimer_3)
        self.menuSources_Primitives.addAction(self.actionD_sactiver)
        self.menuBar.addAction(self.menuRSS.menuAction())
        self.menuBar.addAction(self.menuTwitter.menuAction())
        self.menuBar.addAction(self.menuReddit.menuAction())
        self.menuBar.addAction(self.menuSources_Primitives.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.articleShower.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto\'; font-size:15pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.menuRSS.setTitle(_translate("MainWindow", "RSS"))
        self.menuTwitter.setTitle(_translate("MainWindow", "Twitter"))
        self.menuReddit.setTitle(_translate("MainWindow", "Reddit"))
        self.menuSources_Primitives.setTitle(_translate("MainWindow", "Sources Primitives"))
        self.actionAjouter_Supprimer.setText(_translate("MainWindow", "Ajouter/Supprimer"))
        self.actionAjouter_Supprimer_2.setText(_translate("MainWindow", "Ajouter/Supprimer"))
        self.actionAjouter_Supprimer_3.setText(_translate("MainWindow", "Ajouter/Supprimer"))
        self.actionD_sactiver.setText(_translate("MainWindow", "Désactiver"))
