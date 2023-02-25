# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Create_event.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_event(object):
    def setupUi(self, Create_event):
        Create_event.setObjectName("Create_event")
        Create_event.setWindowModality(QtCore.Qt.NonModal)
        Create_event.resize(500, 282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Create_event.sizePolicy().hasHeightForWidth())
        Create_event.setSizePolicy(sizePolicy)
        Create_event.setMinimumSize(QtCore.QSize(500, 282))
        Create_event.setMaximumSize(QtCore.QSize(500, 282))
        self.gridLayout = QtWidgets.QGridLayout(Create_event)
        self.gridLayout.setObjectName("gridLayout")
        self.event_data = QtWidgets.QDateEdit(Create_event)
        self.event_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.event_data.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 30), QtCore.QTime(23, 59, 59)))
        self.event_data.setMinimumDate(QtCore.QDate(1752, 9, 15))
        self.event_data.setObjectName("event_data")
        self.gridLayout.addWidget(self.event_data, 6, 0, 1, 1)
        self.pushButton_select_organization = QtWidgets.QPushButton(Create_event)
        self.pushButton_select_organization.setObjectName("pushButton_select_organization")
        self.gridLayout.addWidget(self.pushButton_select_organization, 5, 3, 1, 1)
        self.lineEdit_type_event = QtWidgets.QLineEdit(Create_event)
        self.lineEdit_type_event.setObjectName("lineEdit_type_event")
        self.gridLayout.addWidget(self.lineEdit_type_event, 7, 0, 1, 1)
        self.event_city = QtWidgets.QLineEdit(Create_event)
        self.event_city.setObjectName("event_city")
        self.gridLayout.addWidget(self.event_city, 7, 3, 1, 1)
        self.event_country = QtWidgets.QLineEdit(Create_event)
        self.event_country.setObjectName("event_country")
        self.gridLayout.addWidget(self.event_country, 6, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 2, 1, 1)
        self.event_name = QtWidgets.QLineEdit(Create_event)
        self.event_name.setObjectName("event_name")
        self.gridLayout.addWidget(self.event_name, 3, 0, 1, 4)
        self.lineEdit_selected_organization = QtWidgets.QLineEdit(Create_event)
        self.lineEdit_selected_organization.setObjectName("lineEdit_selected_organization")
        self.gridLayout.addWidget(self.lineEdit_selected_organization, 5, 0, 1, 2)
        self.event_time = QtWidgets.QTimeEdit(Create_event)
        self.event_time.setTime(QtCore.QTime(10, 0, 0))
        self.event_time.setObjectName("event_time")
        self.gridLayout.addWidget(self.event_time, 6, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Create_event)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 3, 1, 1)
        self.event_theme = QtWidgets.QLineEdit(Create_event)
        self.event_theme.setObjectName("event_theme")
        self.gridLayout.addWidget(self.event_theme, 4, 0, 1, 4)
        self.event_comment = QtWidgets.QLineEdit(Create_event)
        self.event_comment.setObjectName("event_comment")
        self.gridLayout.addWidget(self.event_comment, 9, 0, 1, 4)
        self.label_create_event = QtWidgets.QLabel(Create_event)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_event.setFont(font)
        self.label_create_event.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_event.setObjectName("label_create_event")
        self.gridLayout.addWidget(self.label_create_event, 1, 0, 1, 4)
        self.label_username_login_role = QtWidgets.QLabel(Create_event)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username_login_role.setFont(font)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 2, 1, 2)

        self.retranslateUi(Create_event)
        self.buttonBox.accepted.connect(Create_event.accept) # type: ignore
        self.buttonBox.rejected.connect(Create_event.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Create_event)
        Create_event.setTabOrder(self.event_name, self.event_theme)
        Create_event.setTabOrder(self.event_theme, self.lineEdit_selected_organization)
        Create_event.setTabOrder(self.lineEdit_selected_organization, self.pushButton_select_organization)
        Create_event.setTabOrder(self.pushButton_select_organization, self.event_data)
        Create_event.setTabOrder(self.event_data, self.event_time)
        Create_event.setTabOrder(self.event_time, self.lineEdit_type_event)
        Create_event.setTabOrder(self.lineEdit_type_event, self.event_country)
        Create_event.setTabOrder(self.event_country, self.event_city)
        Create_event.setTabOrder(self.event_city, self.event_comment)

    def retranslateUi(self, Create_event):
        _translate = QtCore.QCoreApplication.translate
        Create_event.setWindowTitle(_translate("Create_event", "Логистик"))
        self.pushButton_select_organization.setText(_translate("Create_event", "Выбрать организацию"))
        self.lineEdit_type_event.setPlaceholderText(_translate("Create_event", "НИР"))
        self.event_city.setPlaceholderText(_translate("Create_event", "Город..."))
        self.event_country.setPlaceholderText(_translate("Create_event", "Страна..."))
        self.event_name.setPlaceholderText(_translate("Create_event", "Наименование мероприятия..."))
        self.lineEdit_selected_organization.setPlaceholderText(_translate("Create_event", "Организация..."))
        self.event_theme.setPlaceholderText(_translate("Create_event", "Тема мероприятия..."))
        self.event_comment.setPlaceholderText(_translate("Create_event", "Комментарий..."))
        self.label_create_event.setText(_translate("Create_event", "Создание нового мероприятия"))
        self.label_username_login_role.setText(_translate("Create_event", "username_login_role"))