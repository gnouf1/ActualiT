# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/GUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1049, 762)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("* {\n"
"    font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"/*QPushButton*/\n"
"QPushButton {\n"
"    color: #fff;\n"
"    border: 0px solid rgba(255, 255, 255, 0);\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"/*MediumGray*/\n"
"QPushButton{\n"
"    background-color: #aab2bd;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ccd1d9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #ccd1d9,\n"
"    stop: 0.8 #aab2bd);\n"
"}\n"
"\n"
"/*DarkGray*/\n"
"QPushButton[class=\"DarkGray\"] {\n"
"    background-color: #434a54;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"DarkGray\"] {\n"
"    background-color: #656d78;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"DarkGray\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #656d78,\n"
"    stop: 0.8 #434a54);\n"
"}\n"
"\n"
"/*BlueJeans*/\n"
"QPushButton[class=\"BlueJeans\"] {\n"
"    background-color: #4a89dc;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"BlueJeans\"] {\n"
"    background-color: #5d9cec;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"BlueJeans\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #5d9cec,\n"
"    stop: 0.8 #4a89dc);\n"
"}\n"
"\n"
"/*Aqua*/\n"
"QPushButton[class=\"Aqua\"] {\n"
"    background-color: #3bafda;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Aqua\"] {\n"
"    background-color: #4fc1e9;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Aqua\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #4fc1e9,\n"
"    stop: 0.8 #3bafda);\n"
"}\n"
"\n"
"/*Mint*/\n"
"QPushButton[class=\"Mint\"] {\n"
"    background-color: #37bc9b;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Mint\"] {\n"
"    background-color: #48cfad;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Mint\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #48cfad,\n"
"    stop: 0.8 #37bc9b);\n"
"}\n"
"\n"
"/*Grass*/\n"
"QPushButton[class=\"Grass\"] {\n"
"    background-color: #8cc152;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Grass\"] {\n"
"    background-color: #a0d468;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Grass\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #a0d468,\n"
"    stop: 0.8 #8cc152);\n"
"}\n"
"\n"
"/*Sunflower*/\n"
"QPushButton[class=\"Sunflower\"] {\n"
"    background-color: #f6bb42;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Sunflower\"] {\n"
"    background-color: #ffce54;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Sunflower\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #ffce54,\n"
"    stop: 0.8 #f6bb42);\n"
"}\n"
"\n"
"/*Bittersweet*/\n"
"QPushButton[class=\"Bittersweet\"] {\n"
"    background-color: #e9573f;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Bittersweet\"] {\n"
"    background-color: #fc6e51;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Bittersweet\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #fc6e51,\n"
"    stop: 0.8 #e9573f);\n"
"}\n"
"\n"
"/*Grapefruit*/\n"
"QPushButton[class=\"Grapefruit\"] {\n"
"    background-color: #da4453;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Grapefruit\"] {\n"
"    background-color: #ed5565;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Grapefruit\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #ed5565,\n"
"    stop: 0.8 #da4453);\n"
"}\n"
"\n"
"/*Lavender*/\n"
"QPushButton[class=\"Lavender\"] {\n"
"    background-color: #967adc;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"Lavender\"] {\n"
"    background-color: #ac92ec;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"Lavender\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #ac92ec,\n"
"    stop: 0.8 #967adc);\n"
"}\n"
"\n"
"/*PinkRose*/\n"
"QPushButton[class=\"PinkRose\"] {\n"
"    background-color: #d770ad;\n"
"}\n"
"\n"
"QPushButton:hover[class=\"PinkRose\"] {\n"
"    background-color: #ec87c0;\n"
"}\n"
"\n"
"QPushButton:pressed[class=\"PinkRose\"] {\n"
"    background: qradialgradient(cx:0.5,\n"
"    cy: 0.5,\n"
"    fx: 0.5,\n"
"    fy: 0.5,\n"
"    radius: 1.5,\n"
"    stop: 0.2 #ec87c0,\n"
"    stop: 0.8 #d770ad);\n"
"}\n"
"\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"    border: 1px solid #aab2bd;\n"
"    border-radius: 4px;\n"
"    font-size: 12px;\n"
"    padding: 5px 8px;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3bafda;\n"
"}\n"
"\n"
"/*QComboBox*/\n"
"QComboBox {\n"
"    border: 1px solid #aab2bd;\n"
"    border-radius: 4px;\n"
"    font-size: 12px;\n"
"    padding: 5px 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\"%PATH%/img/more.png\");\n"
"    padding-right: 10px;\n"
"    padding-top: 2px;\n"
"\n"
"}\n"
"\n"
"QComboBox::!editable:on {\n"
"    border: 1px solid #3bafda;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    border: 2px solid #e6e9ed;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"    height: 35px;\n"
"    border-bottom: 1px solid #e6e9ed;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover{\n"
"    background-color: #3bafda;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected{\n"
"    background-color: #3bafda;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/*QListWidget,QListView*/\n"
"QListWidget,QListView {\n"
"    border: 1px solid #ccd1d9;\n"
"    outline: none;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QListWidget::item,QListView::item {\n"
"    height: 35px;\n"
"    padding-left: 5px;\n"
"    border-bottom: 1px solid #e6e9ed;\n"
"}\n"
"\n"
"QListWidget::item:hover,QListView::item:hover{\n"
"    background-color: #3bafda;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget::item:selected,QListView::item:selected{\n"
"    background-color: #3bafda;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/*QTableWidget,QTableView*/\n"
"QHeaderView{\n"
"    height: 40px;\n"
"    border: 0 solid rgba(255, 255, 255, 0);\n"
"    background-color: #fff;\n"
"    border-bottom: 2px solid #e6e9ed;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    height: 40px;\n"
"    border: 0 solid rgba(255, 255, 255, 0);\n"
"    background-color: #fff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QTableWidget,QTableView{\n"
"    border: 1px solid #ccd1d9;\n"
"    alternate-background-color: #f1f2f6;\n"
"    background-color: #fff;\n"
"    selection-background-color : #3bafda;\n"
"}\n"
"\n"
"/*QProgressBar*/\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: #e6e9ed;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar::chunk[class=\"Aqua\"] {\n"
"    background-color: #3bafda;\n"
"}\n"
"\n"
"QProgressBar::chunk[class=\"Grass\"] {\n"
"    background-color: #8cc152;\n"
"}\n"
"\n"
"QProgressBar::chunk[class=\"Sunflower\"] {\n"
"    background-color: #f6bb42;\n"
"}\n"
"\n"
"QProgressBar::chunk[class=\"Grapefruit\"] {\n"
"    background-color: #da4453;\n"
"}\n"
"\n"
"/*QCheckBox*/\n"
"QCheckBox::indicator:unchecked {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border: 1px solid #ccd1d9;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #3bafda;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #fff;\n"
"    image: url(\'%PATH%/img/checkbox_checked.png\');\n"
"}\n"
"\n"
"/*QRadioButton*/\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(\'%PATH%/img/Raidobox_unchecked.png\');\n"
"    /*background-color: #fff;*/\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(\'%PATH%/img/Raidobox_unchecked_hover.png\');\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(\'%PATH%/img/Raidobox_checked.png\');\n"
"}\n"
"\n"
"/*QTabWidget*/\n"
"QTabWidget{\n"
"    border:1px solid #ccd1d9;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    border-radius: 3px;\n"
"    border-top-left-radius: 0;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    padding: 8px 30px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    border-left: 1px solid #ccd1d9;\n"
"    background-color: #e6e9ed;\n"
"}\n"
"\n"
"/*QMenu*/\n"
"QMenu{\n"
"    padding:5px;\n"
"    background:white;\n"
"    border:1px solid #ccd1d9;\n"
" }\n"
"\n"
"QMenu::item{\n"
"    padding:0px 40px 0px 30px;\n"
"    height:25px;\n"
"}\n"
"\n"
"QMenu::item:selected:enabled{\n"
"    background-color: #3bafda;\n"
"    color:white;\n"
"}\n"
"\n"
"QMenu::item:selected:!enabled{\n"
"    background:transparent;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"    height:1px;\n"
"    background:lightgray;\n"
"    margin:5px 0px 5px 0px;\n"
"}\n"
"\n"
"/*QScrollBar*/\n"
"QScrollBar:vertical {\n"
"    max-width: 13px;\n"
"    padding-top: 0;\n"
"    padding-bottom: 0;\n"
"    border-bottom: 1px solid #ccd1d9;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #cdced1;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a9b2bd;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background-color: #ccd1d9;\n"
"\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"    background-color: #e6e9ed;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-height: 13px;\n"
"    padding-top: 0;\n"
"    padding-bottom: 0;\n"
"    border-right: 1px solid #ccd1d9;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #cdced1;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #a9b2bd;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    background-color: #ccd1d9;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"    background-color: #e6e9ed;\n"
"}\n"
"\n"
"/*QSlider*/\n"
"QSlider::groove:horizontal{\n"
"    border:0px;\n"
"    height:8px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"    background:white;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background:lightgray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background:white;\n"
"    width:10px;\n"
"    border-radius:5px;\n"
"    margin:-3px 0px -3px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"    border:0px;\n"
"    width:8px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical{\n"
"    background:white;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"    background:lightgray;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    background:white;\n"
"    height:10px;\n"
"    border-radius:5px;\n"
"    margin:0px -3px 0px -3px;\n"
"}\n"
"\n"
"/*QCalendarWidget*/\n"
"QCalendarWidget{\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"      height: 60px;\n"
"      color: white;\n"
"      font-size: 18px;\n"
"    font-weight: 700;\n"
"      icon-size: 20px, 20px;\n"
"    background-color: #3bafda;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover{\n"
"    border: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:pressed{\n"
"    border: transparent;\n"
"    background-color: #4fc1e9;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth{\n"
"    qproperty-icon: url(\'%PATH%/img/arrow-left.png\');\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth{\n"
"    qproperty-icon: url(\'%PATH%/img/arrow-right.png\');\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton::menu-indicator{\n"
"    background-color: #3bafda;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton::menu-indicator:pressed{\n"
"    background-color: #4fc1e9;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #3bafda;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    padding: 11px;\n"
"    font-size:14px;\n"
"    outline: none;\n"
"    selection-color: #FFF;\n"
"}\n"
"\n"
"/*QSpinBox*/\n"
"QSpinBox {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccd1d9;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    height: 14px;\n"
"    border-image: url(\'%PATH%/img/spinbox_up.png\');\n"
"    border-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed{\n"
"    border-image: url(\'%PATH%/img/spinbox_up_pressed.png\');\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 16px;\n"
"    height: 14px;\n"
"    border-image: url(\'%PATH%/img/spinbox_down.png\');\n"
"    border-width: 1px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed{\n"
"    border-image: url(\'%PATH%/img/spinbox_down_pressed.png\');\n"
"}\n"
"\n"
"/*QTreeWidget*/\n"
"QTreeWidget,TreeView {\n"
"    outline: none;\n"
"    border: 1px solid #d9d9d9;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    margin-right: 2px;\n"
"    border: 1px solid #d9d9d9;\n"
"    height: 30px;\n"
"    border-radius: 1px;\n"
"    padding-left: 2px;\n"
"    font-size: 12px;\n"
"    border-left: 0 solid transparent;\n"
"    selection-color: #FFF;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #3bafda;\n"
"    border: 1px solid #3bafda;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background: palette(base);\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    border: 1px solid #d9d9d9;\n"
"    border-right: 0 solid transparent;\n"
"    margin-bottom: 2px;\n"
"    image: url(\'%PATH%/img/minus.png\');\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    border: 1px solid #d9d9d9;\n"
"    border-right: 0 solid transparent;\n"
"    margin-bottom: 2px;\n"
"    image: url(\'%PATH%/img/minus.png\');\n"
"}\n"
"\n"
"QTreeWidget::branch:closed:has-children:has-siblings {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    image: url(\'%PATH%/img/plus.png\');\n"
"\n"
"}\n"
"\n"
"QTreeWidget::branch:has-children:!has-siblings:closed {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    border: 1px solid #d9d9d9;\n"
"    border-right: 0 solid transparent;\n"
"    margin-bottom: 2px;\n"
"    image: url(\'%PATH%/img/plus.png\');\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children:has-siblings {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    image: url(\'%PATH%/img/minus.png\');\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    margin-top: 2px;\n"
"    margin-left: 2px;\n"
"    border: 1px solid #d9d9d9;\n"
"    border-right: 0 solid transparent;\n"
"    margin-bottom: 2px;\n"
"    image: url(\'%PATH%/img/minus.png\');\n"
"}\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalDock = QtWidgets.QWidget(self.centralwidget)
        self.verticalDock.setMinimumSize(QtCore.QSize(183, 0))
        self.verticalDock.setMaximumSize(QtCore.QSize(183, 16777215))
        self.verticalDock.setObjectName("verticalDock")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalDock)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.refreshButton = QtWidgets.QPushButton(self.verticalDock)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.refreshButton.setFont(font)
        self.refreshButton.setFlat(False)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout.addWidget(self.refreshButton)
        self.toolBox = QtWidgets.QToolBox(self.verticalDock)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setItalic(False)
        self.toolBox.setFont(font)
        self.toolBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.RSS_Button = QtWidgets.QWidget()
        self.RSS_Button.setGeometry(QtCore.QRect(0, 0, 173, 214))
        self.RSS_Button.setObjectName("RSS_Button")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.RSS_Button)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RSS_manage = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.RSS_manage.setObjectName("RSS_manage")
        self.verticalLayout_2.addWidget(self.RSS_manage)
        self.toolBox.addItem(self.RSS_Button, "")
        self.Reddit_button = QtWidgets.QWidget()
        self.Reddit_button.setGeometry(QtCore.QRect(0, 0, 173, 214))
        self.Reddit_button.setObjectName("Reddit_button")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Reddit_button)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Reddit_manage = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Reddit_manage.setObjectName("Reddit_manage")
        self.verticalLayout_3.addWidget(self.Reddit_manage)
        self.toolBox.addItem(self.Reddit_button, "")
        self.Twitter_button = QtWidgets.QWidget()
        self.Twitter_button.setGeometry(QtCore.QRect(0, 0, 173, 214))
        self.Twitter_button.setObjectName("Twitter_button")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Twitter_button)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Twitter_manage = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Twitter_manage.setObjectName("Twitter_manage")
        self.verticalLayout_4.addWidget(self.Twitter_manage)
        self.toolBox.addItem(self.Twitter_button, "")
        self.Primi_Button = QtWidgets.QWidget()
        self.Primi_Button.setGeometry(QtCore.QRect(0, 0, 173, 214))
        self.Primi_Button.setObjectName("Primi_Button")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Primi_Button)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.NAC_manage = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.NAC_manage.setEnabled(True)
        self.NAC_manage.setObjectName("NAC_manage")
        self.verticalLayout_5.addWidget(self.NAC_manage)
        self.toolBox.addItem(self.Primi_Button, "")
        self.verticalLayout.addWidget(self.toolBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.toolButton = QtWidgets.QToolButton(self.verticalDock)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.gridLayout.addWidget(self.verticalDock, 0, 0, 3, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainCol = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.mainCol.setFont(font)
        self.mainCol.setStyleSheet("")
        self.mainCol.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainCol.setLineWidth(10)
        self.mainCol.setObjectName("mainCol")
        self.horizontalLayout_2.addWidget(self.mainCol)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.articleShower = QtWidgets.QTextBrowser(self.centralwidget)
        self.articleShower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.articleShower.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.articleShower.setOpenExternalLinks(True)
        self.articleShower.setObjectName("articleShower")
        self.horizontalLayout_2.addWidget(self.articleShower)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(3)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Reddit_manage, self.Twitter_manage)
        MainWindow.setTabOrder(self.Twitter_manage, self.NAC_manage)
        MainWindow.setTabOrder(self.NAC_manage, self.toolButton)
        MainWindow.setTabOrder(self.toolButton, self.RSS_manage)
        MainWindow.setTabOrder(self.RSS_manage, self.refreshButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.RSS_manage.setText(_translate("MainWindow", "Manage"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.RSS_Button), _translate("MainWindow", "RSS"))
        self.Reddit_manage.setText(_translate("MainWindow", "Manage"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Reddit_button), _translate("MainWindow", "Reddit"))
        self.Twitter_manage.setText(_translate("MainWindow", "Manage"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Twitter_button), _translate("MainWindow", "Twitter"))
        self.NAC_manage.setText(_translate("MainWindow", "Manage"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Primi_Button), _translate("MainWindow", "Source Primitive"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.articleShower.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto\'; font-size:15pt;\"><br /></p></body></html>"))
