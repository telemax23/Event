# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Analisis_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Analisis_docs(object):
    def setupUi(self, Analisis_docs):
        Analisis_docs.setObjectName("Analisis_docs")
        Analisis_docs.resize(1400, 560)
        self.gridLayout = QtWidgets.QGridLayout(Analisis_docs)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget_analysis = QtWidgets.QTreeWidget(Analisis_docs)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.treeWidget_analysis.setFont(font)
        self.treeWidget_analysis.setObjectName("treeWidget_analysis")
        self.gridLayout.addWidget(self.treeWidget_analysis, 7, 0, 1, 9)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout.addLayout(self.formLayout, 9, 8, 1, 1)
        self.label_username_login_role = QtWidgets.QLabel(Analisis_docs)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 1, 0, 1, 9)
        self.pushButton_update_table = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_update_table.setObjectName("pushButton_update_table")
        self.gridLayout.addWidget(self.pushButton_update_table, 6, 0, 1, 1)
        self.pushButton_open_analisis_doc = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_open_analisis_doc.setObjectName("pushButton_open_analisis_doc")
        self.gridLayout.addWidget(self.pushButton_open_analisis_doc, 6, 2, 1, 1)
        self.pushButton_template_survey = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_template_survey.setObjectName("pushButton_template_survey")
        self.gridLayout.addWidget(self.pushButton_template_survey, 9, 2, 1, 1)
        self.pushButton_template_contract = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_template_contract.setObjectName("pushButton_template_contract")
        self.gridLayout.addWidget(self.pushButton_template_contract, 9, 3, 1, 1)
        self.label_update_temlate = QtWidgets.QLabel(Analisis_docs)
        self.label_update_temlate.setObjectName("label_update_temlate")
        self.gridLayout.addWidget(self.label_update_temlate, 8, 0, 1, 1)
        self.pushButton_template_agreement = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_template_agreement.setObjectName("pushButton_template_agreement")
        self.gridLayout.addWidget(self.pushButton_template_agreement, 9, 0, 1, 1)
        self.pushButton_template_act = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_template_act.setObjectName("pushButton_template_act")
        self.gridLayout.addWidget(self.pushButton_template_act, 9, 4, 1, 1)
        self.pushButton_template_report = QtWidgets.QPushButton(Analisis_docs)
        self.pushButton_template_report.setObjectName("pushButton_template_report")
        self.gridLayout.addWidget(self.pushButton_template_report, 9, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 6, 1, 1)
        self.label_analysis_download_docs = QtWidgets.QLabel(Analisis_docs)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_analysis_download_docs.setFont(font)
        self.label_analysis_download_docs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_analysis_download_docs.setObjectName("label_analysis_download_docs")
        self.gridLayout.addWidget(self.label_analysis_download_docs, 2, 0, 1, 9)
        self.buttonBox = QtWidgets.QDialogButtonBox(Analisis_docs)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 7, 1, 1)

        self.retranslateUi(Analisis_docs)
        self.buttonBox.accepted.connect(Analisis_docs.accept) # type: ignore
        self.buttonBox.rejected.connect(Analisis_docs.reject) # type: ignore
        self.pushButton_open_analisis_doc.clicked.connect(Analisis_docs.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Analisis_docs)

    def retranslateUi(self, Analisis_docs):
        _translate = QtCore.QCoreApplication.translate
        Analisis_docs.setWindowTitle(_translate("Analisis_docs", "Логистик"))
        self.treeWidget_analysis.headerItem().setText(0, _translate("Analisis_docs", "Телефон"))
        self.treeWidget_analysis.headerItem().setText(1, _translate("Analisis_docs", "Фамилия"))
        self.treeWidget_analysis.headerItem().setText(2, _translate("Analisis_docs", "Имя"))
        self.treeWidget_analysis.headerItem().setText(3, _translate("Analisis_docs", "Отчетство"))
        self.treeWidget_analysis.headerItem().setText(4, _translate("Analisis_docs", "Паспорт"))
        self.treeWidget_analysis.headerItem().setText(5, _translate("Analisis_docs", "Прописка"))
        self.treeWidget_analysis.headerItem().setText(6, _translate("Analisis_docs", "ИНН"))
        self.treeWidget_analysis.headerItem().setText(7, _translate("Analisis_docs", "СНИЛС"))
        self.treeWidget_analysis.headerItem().setText(8, _translate("Analisis_docs", "Диплом"))
        self.treeWidget_analysis.headerItem().setText(9, _translate("Analisis_docs", "Сертификат"))
        self.treeWidget_analysis.headerItem().setText(10, _translate("Analisis_docs", "Согласие"))
        self.treeWidget_analysis.headerItem().setText(11, _translate("Analisis_docs", "Анкета"))
        self.treeWidget_analysis.headerItem().setText(12, _translate("Analisis_docs", "Договор"))
        self.treeWidget_analysis.headerItem().setText(13, _translate("Analisis_docs", "Акт"))
        self.treeWidget_analysis.headerItem().setText(14, _translate("Analisis_docs", "Отчет"))
        self.label_username_login_role.setText(_translate("Analisis_docs", "username_login_role"))
        self.pushButton_update_table.setText(_translate("Analisis_docs", "Обновить данные"))
        self.pushButton_open_analisis_doc.setText(_translate("Analisis_docs", "Открыть док-ты"))
        self.pushButton_template_survey.setText(_translate("Analisis_docs", "Анкета"))
        self.pushButton_template_contract.setText(_translate("Analisis_docs", "Договор"))
        self.label_update_temlate.setText(_translate("Analisis_docs", "Обновить шаблон:"))
        self.pushButton_template_agreement.setText(_translate("Analisis_docs", "Согласие"))
        self.pushButton_template_act.setText(_translate("Analisis_docs", "Акт"))
        self.pushButton_template_report.setText(_translate("Analisis_docs", "Отчет"))
        self.label_analysis_download_docs.setText(_translate("Analisis_docs", "Анализ полученных документов"))