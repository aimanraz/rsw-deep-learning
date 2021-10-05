# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsw_app_tool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
import tensorflow as tf
import levenberg_marquardt_new as lm
import scipy.spatial.transform._rotation_groups

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam,SGD

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import itertools


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/cropped-SMRI-logo-6.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_26.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_26.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_26)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_27.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_27.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_25.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 941, 884))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_3.addWidget(self.spinBox_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_4.addWidget(self.spinBox_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.checkBox_4)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBox_5 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_5.addWidget(self.spinBox_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_5.addWidget(self.checkBox_5)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox_6 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_6.addWidget(self.spinBox_6)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_6.addWidget(self.label_27)
        self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_6.addWidget(self.checkBox_6)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName("label_29")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spinBox_7 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_7.addWidget(self.spinBox_7)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_7.addWidget(self.label_30)
        self.comboBox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_7.addWidget(self.checkBox_7)
        self.formLayout.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName("label_31")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName("label_32")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinBox_8 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_8.addWidget(self.spinBox_8)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_8.addWidget(self.label_33)
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_8)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout_8.addWidget(self.checkBox_8)
        self.formLayout.setLayout(18, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.spinBox_9 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_9.setObjectName("spinBox_9")
        self.horizontalLayout_9.addWidget(self.spinBox_9)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_9.addWidget(self.label_36)
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_9)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout_9.addWidget(self.checkBox_9)
        self.formLayout.setLayout(20, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.comboBox_10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_10)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem20)
        self.formLayout.setLayout(21, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.comboBox_11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_11)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem21)
        self.formLayout.setLayout(22, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.comboBox_12 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_12)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem22)
        self.formLayout.setLayout(23, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName("label_43")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.FieldRole, self.label_43)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_14.addWidget(self.lineEdit)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem23)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem24)
        self.formLayout.setLayout(24, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_15.addWidget(self.lineEdit_2)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem25)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_15.addWidget(self.label_42)
        self.spinBox_10 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(1000)
        self.spinBox_10.setObjectName("spinBox_10")
        self.horizontalLayout_15.addWidget(self.spinBox_10)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem26)
        self.formLayout.setLayout(25, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 941, 558))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_44.setObjectName("label_44")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setObjectName("label_45")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem27)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_46.setObjectName("label_46")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setObjectName("label_47")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_47)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem28)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_17.addWidget(self.pushButton_4)
        spacerItem29 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem29)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_17)
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_48.setObjectName("label_48")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_49.setObjectName("label_49")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_49)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_50.setObjectName("label_50")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_51.setObjectName("label_51")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_51)
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_52.setObjectName("label_52")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_52)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_53.setObjectName("label_53")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_53)
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_54.setObjectName("label_54")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_16.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_16.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_16.addWidget(self.radioButton_3)
        spacerItem30 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem30)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_16.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_16.addWidget(self.pushButton_6)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem31)
        self.formLayout_2.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_16)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName("widget")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.gridLayout_6.addLayout(self.formLayout_2, 0, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_18.addWidget(self.textEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_19.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_19.addWidget(self.pushButton_8)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem32)
        self.gridLayout.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setVerticalSpacing(15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_55 = QtWidgets.QLabel(self.tab_5)
        self.label_55.setObjectName("label_55")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.label_56 = QtWidgets.QLabel(self.tab_5)
        self.label_56.setObjectName("label_56")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_20.addWidget(self.lineEdit_4)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem33)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.label_57 = QtWidgets.QLabel(self.tab_5)
        self.label_57.setObjectName("label_57")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_21.addWidget(self.lineEdit_5)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem34)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_21)
        self.label_58 = QtWidgets.QLabel(self.tab_5)
        self.label_58.setObjectName("label_58")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_22.addWidget(self.lineEdit_6)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem35)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_59 = QtWidgets.QLabel(self.tab_5)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_23.addWidget(self.label_59)
        self.formLayout_3.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_23)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushButton_10)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_8.clicked.connect(self.textEdit_2.clear)
        self.pushButton_10.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_10.clicked.connect(self.lineEdit_5.clear)
        self.pushButton_10.clicked.connect(self.lineEdit_6.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

######################################### Editing Started ###################################################### 
       
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.preprocess)
        self.pushButton_3.clicked.connect(self.outputLay)
        self.pushButton_3.clicked.connect(self.HL1)
        self.pushButton_3.clicked.connect(self.HL2)
        self.pushButton_3.clicked.connect(self.HL3)
        self.pushButton_3.clicked.connect(self.HL4)
        self.pushButton_3.clicked.connect(self.HL5)
        self.pushButton_3.clicked.connect(self.HL6)
        self.pushButton_3.clicked.connect(self.HL7)
        self.pushButton_3.clicked.connect(self.HL8)
        self.pushButton_3.clicked.connect(self.optim)
        self.pushButton_3.clicked.connect(self.los)
        self.pushButton_3.clicked.connect(self.metri)
        self.pushButton_3.clicked.connect(self.learn_btchsize)
        self.pushButton_3.clicked.connect(self.submitk)
        self.pushButton_4.clicked.connect(self.runFile)    

        self.pushButton_5.clicked.connect(self.plot_graph)
        self.pushButton_6.clicked.connect(self.clr)   
        self.pushButton_7.clicked.connect(self.WB)   
        self.pushButton_9.clicked.connect(self.pred)   
        self.pushButton_10.clicked.connect(self.clear)
        
        self.spinBox_3.setEnabled(False)
        self.spinBox_4.setEnabled(False)
        self.spinBox_5.setEnabled(False)
        self.spinBox_6.setEnabled(False)
        self.spinBox_7.setEnabled(False)
        self.spinBox_8.setEnabled(False)
        self.spinBox_9.setEnabled(False)

        self.comboBox_3.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        self.comboBox_5.setEnabled(False)
        self.comboBox_6.setEnabled(False)
        self.comboBox_7.setEnabled(False)
        self.comboBox_8.setEnabled(False)
        self.comboBox_9.setEnabled(False)
        
        self.comboBox_10.currentIndexChanged.connect(self.on_off)

        self.checkBox_2.stateChanged.connect(lambda:self.btnstate(self.checkBox_2))
        self.checkBox_3.stateChanged.connect(lambda:self.btnstate(self.checkBox_3))
        self.checkBox_4.stateChanged.connect(lambda:self.btnstate(self.checkBox_4))
        self.checkBox_5.stateChanged.connect(lambda:self.btnstate(self.checkBox_5))
        self.checkBox_6.stateChanged.connect(lambda:self.btnstate(self.checkBox_6))
        self.checkBox_7.stateChanged.connect(lambda:self.btnstate(self.checkBox_7))
        self.checkBox_8.stateChanged.connect(lambda:self.btnstate(self.checkBox_8))
        self.checkBox_9.stateChanged.connect(lambda:self.btnstate(self.checkBox_9))
        #self.radioButton.stateChanged.connect(lambda:self.btnstate(radioButton))
        #self.radioButton_2.stateChanged.connect(lambda:self.btnstate(radioButton_2))

#################################################      
        self.lay = QHBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.lay.addWidget(self.canvas)
        self.widget.setLayout(self.lay)
        self.widget.setFixedWidth(610) #310
        self.widget.setFixedHeight(490) #290                 
##################################################

    def on_off(self):
        if self.comboBox_10.currentText()=="LM":
            self.comboBox_12.setEnabled(True)
            if self.checkBox_2.isChecked():
                pass
                #self.comboBox_12.setCurrentIndex(4)
            else:
                pass
                #self.comboBox_12.setCurrentIndex(0)
        else:
            self.comboBox_12.setEnabled(True)       

    def openFile (self):
        url = QFileDialog.getOpenFileName(self,"Open a file","","All Files(*);;*CSV")
        fileUrl=url[0]
        self.datasets = pd.read_csv(fileUrl)
        self.label_5.setText("Data URL : "+fileUrl) 
        
        file =open(fileUrl,'r')
        content = file.read()
        self.textEdit.setText(content)
    
    def preprocess(self):
        self.x = self.datasets.iloc[:, :-1 ].values #or [:, [2,3]]
        self.y = self.datasets.iloc[:, 3].values
        
        self.xx = np.size(self.x,1)
        self.disp = self.xx
        self.label_8.setText("Number of Neuron:  " + str(self.disp))
        self.label_6.setText("Data Progress: Preprocessing Completed!") 
        
        if (self.checkBox.isChecked()):
            label_encoder_y = LabelEncoder()
            self.y = label_encoder_y.fit_transform(self.y)
            self.y= to_categorical(self.y)
        
        elif self.checkBox_2.isChecked():
            self.y = self.y.reshape(-1,1)
            self.sc_y = StandardScaler()
            self.y = self.sc_y.fit_transform(self.y)

        else:
            label_encoder_y = LabelEncoder()
            self.y = label_encoder_y.fit_transform(self.y)
            self.y= to_categorical(self.y)
            self.y= np.argmax(self.y, axis = 1)
    
    def outputLay(self,comboBox): 
        if self.comboBox.currentText()=="softmax":
            self.var1= 'softmax'        
        elif self.comboBox.currentText()=="sigmoid":
            self.var1= 'sigmoid'
        else:
            self.var1= 'linear'
    
    def HL1(self,comboBox_2):
        self.val1=self.spinBox_2.value()   
        if self.comboBox_2.currentText()=="relu":
            self.var2= 'relu'           
        elif self.comboBox_2.currentText()=="softmax":
            self.var2= 'softmax'        
        else:
            self.var2= 'sigmoid'    

    def HL2(self,comboBox_3):
        self.val2=self.spinBox_3.value()    
        if self.comboBox_3.currentText()=="relu":
            self.var3= 'relu'    
        elif self.comboBox_3.currentText()=="softmax":
            self.var3= 'softmax'           
        else:
            self.var3= 'sigmoid'
            
    def HL3(self,comboBox_4): #val6 var7
        self.val3=self.spinBox_4.value()    
        if self.comboBox_4.currentText()=="relu":
            self.var4= 'relu'    
        elif self.comboBox_4.currentText()=="softmax":
            self.var4= 'softmax'           
        else:
            self.var4= 'sigmoid'            
            
    def HL4(self,comboBox_5):
        self.val4=self.spinBox_5.value()    
        if self.comboBox_5.currentText()=="relu":
            self.var5= 'relu'    
        elif self.comboBox_5.currentText()=="softmax":
            self.var5= 'softmax'           
        else:
            self.var5= 'sigmoid'
            
    def HL5(self,comboBox_6):
        self.val5=self.spinBox_6.value()    
        if self.comboBox_6.currentText()=="relu":
            self.var6= 'relu'    
        elif self.comboBox_6.currentText()=="softmax":
            self.var6= 'softmax'           
        else:
            self.var6= 'sigmoid'   
            
    def HL6(self,comboBox_7):
        self.val6=self.spinBox_7.value()    
        if self.comboBox_7.currentText()=="relu":
            self.var7= 'relu'    
        elif self.comboBox_7.currentText()=="softmax":
            self.var7= 'softmax'           
        else:
            self.var7= 'sigmoid'

    def HL7(self,comboBox_8):
        self.val7=self.spinBox_8.value()    
        if self.comboBox_8.currentText()=="relu":
            self.var8= 'relu'    
        elif self.comboBox_8.currentText()=="softmax":
            self.var8= 'softmax'           
        else:
            self.var8= 'sigmoid'
            
    def HL8(self,comboBox_9):
        self.val8=self.spinBox_9.value()    
        if self.comboBox_9.currentText()=="relu":
            self.var9= 'relu'    
        elif self.comboBox_9.currentText()=="softmax":
            self.var9= 'softmax'           
        else:
            self.var9= 'sigmoid' 
            
    def optim(self,comboBox_10):
        if self.comboBox_10.currentText()=="LM":
            self.var10= SGD
            self.var14=True
        elif self.comboBox_10.currentText()=="GD":   
            self.var10=SGD
            self.var14=False
        else:
            self.var10= SGD
            self.var14=True


    def los(self,comboBox_11):
        
        if self.comboBox_11.currentText()=="BinaryCrossentropy":
            self.var11='binary_crossentropy'
            self.var13=lm.BinaryCrossentropy(from_logits=True)    
            
        elif self.comboBox_11.currentText()=="SparseCategoricalCrossentropy":
            self.var11='sparse_categorical_crossentropy'
            self.var13=lm.SparseCategoricalCrossentropy() 
            
        elif self.comboBox_11.currentText()=="CategoricalCrossentropy":
            self.var11='categorical_crossentropy'
            self.var13=lm.CategoricalCrossentropy() 
            
        else:
            self.var11=tf.keras.losses.MeanSquaredError()
            self.var13=lm.MeanSquaredError()

    def metri(self,comboBox_12):

        if self.comboBox_12.currentText()=="Accuracy":
            self.var12= 'acc'
            self.varval='val_acc'
        elif self.comboBox_12.currentText()=="BinaryAccuracy":
            self.var12= 'binary_accuracy'
            self.varval='val_binary_accuracy'
        elif self.comboBox_12.currentText()=="CategoricalAccuracy":
            self.var12= 'categorical_accuracy'
            self.varval='val_categorical_accuracy'
        elif self.comboBox_12.currentText()=="SparseCategoricalAccuracy":
            self.var12= 'sparse_categorical_accuracy'
            self.varval='val_categorical_accuracy'
        else:
            self.var12= tf.keras.metrics.MeanSquaredError()
            
    def learn_btchsize(self):
        if self.lineEdit.text() == "":
            self.lr=0.01
        else:
            self.lr=float(self.lineEdit.text())
            
        self.val9=self.spinBox_10.value()
            
    def btnstate(self,b):
        
        if b.text() == "Linear Regression":
            if b.isChecked() == True:
                self.checkBox.setEnabled(False)
                self.checkBox.setChecked(False)
            else:
                self.checkBox.setEnabled(True)

        if b.text() == "HL 2":        
            if b.isChecked() == True:
                self.comboBox_3.setEnabled(True)
                self.spinBox_3.setEnabled(True)
            else:
                self.comboBox_3.setEnabled(False)
                self.spinBox_3.setEnabled(False)
                
        if b.text() == "HL 3":        
            if b.isChecked() == True:
                self.comboBox_4.setEnabled(True)
                self.spinBox_4.setEnabled(True)
            else:
                self.comboBox_4.setEnabled(False)
                self.spinBox_4.setEnabled(False)                  
                
        if b.text() == "HL 4":        
            if b.isChecked() == True:
                self.comboBox_5.setEnabled(True)
                self.spinBox_5.setEnabled(True)
            else:
                self.comboBox_5.setEnabled(False)
                self.spinBox_5.setEnabled(False)                  
                
        if b.text() == "HL 5":        
            if b.isChecked() == True:
                self.comboBox_6.setEnabled(True)
                self.spinBox_6.setEnabled(True)
            else:
                self.comboBox_6.setEnabled(False)
                self.spinBox_6.setEnabled(False)  
                
        if b.text() == "HL 6":        
            if b.isChecked() == True:
                self.comboBox_7.setEnabled(True)
                self.spinBox_7.setEnabled(True)
            else:
                self.comboBox_7.setEnabled(False)
                self.spinBox_7.setEnabled(False)                  
                
        if b.text() == "HL 7":        
            if b.isChecked() == True:
                self.comboBox_8.setEnabled(True)
                self.spinBox_8.setEnabled(True)
            else:
                self.comboBox_8.setEnabled(False)
                self.spinBox_8.setEnabled(False)                  
 
        if b.text() == "HL 8":        
            if b.isChecked() == True:
                self.comboBox_9.setEnabled(True)
                self.spinBox_9.setEnabled(True)
            else:
                self.comboBox_9.setEnabled(False)
                self.spinBox_9.setEnabled(False)     
    
    def submitk (self):
        self.label_5.setText("Data Progress:") 
        self.yy = self.spinBox.value()
        self.classifier = Sequential()
        self.classifier.add(Dense(units=self.val1 , input_shape=(self.xx,), activation=self.var2))
        self.klop = 2
        
        if (self.checkBox_3.isChecked()):
            self.classifier.add(Dense(units=self.val2 , activation=self.var3))
            self.klop = 3

        else:
            pass

        if (self.checkBox_4.isChecked()):
            self.classifier.add(Dense(units=self.val3 , activation=self.var4))
            self.klop = 4
        else:
            pass
        
        if (self.checkBox_5.isChecked()):
            self.classifier.add(Dense(units=self.val4 , activation=self.var5))
            self.klop = 5
        else:
            pass
        
        if (self.checkBox_6.isChecked()):
            self.classifier.add(Dense(units=self.val5 , activation=self.var6))
            self.klop = 6
        else:
            pass
        
        if (self.checkBox_7.isChecked()):
            self.classifier.add(Dense(units=self.val6 , activation=self.var7))
            self.klop = 7
        else:
            pass
        
        if (self.checkBox_8.isChecked()):
            self.classifier.add(Dense(units=self.val7 , activation=self.var8))
            self.klop = 8
        else:
            pass
        
        if (self.checkBox_9.isChecked()):
            self.classifier.add(Dense(units=self.val8, activation=self.var9))
            self.klop = 9
        else:
            pass
              
        self.classifier.add(Dense(units=self.yy , activation=self.var1))
        self.classifier.compile(optimizer= self.var10(learning_rate=self.lr), loss= self.var11 , metrics= [self.var12])        
        
        if self.comboBox_10.currentText()=="LM" and self.comboBox_11.currentText()=="MSE":
            self.model_wrapper = lm.ModelWrapper(tf.keras.models.clone_model(self.classifier))
            self.model_wrapper.compile(
                        optimizer=tf.keras.optimizers.SGD(learning_rate=self.lr),
                        loss=self.var13,
                        metrics=['MSE'])
                        
            
        elif self.comboBox_10.currentText()=="LM" and self.comboBox_11.currentText()!="MSE":
            self.model_wrapper = lm.ModelWrapper(tf.keras.models.clone_model(self.classifier))
            self.model_wrapper.compile(
                        optimizer=tf.keras.optimizers.SGD(learning_rate=self.lr),
                        loss=self.var13,
                        solve_method='solve',
                        metrics=[self.var12])

            #self.classifier.compile(optimizer= self.var10(learning_rate=self.lr), loss= self.var11 , metrics= [self.var12])
        self.label_43.setText("Model : Submitted !")

    def runFile (self):
        
        self.label_43.setText("Model :")
        if self.lineEdit_3.text() == "":
            self.testsize = 0.20
            self.label_47.setText("20.0 %")
        else:
            self.trainsize = float(self.lineEdit_3.text())
            self.testsize = 100 - self.trainsize
            self.label_47.setText(str(self.testsize) + " %")
            self.testsize = self.testsize/100
           
        x_train,x_test,self.y_train, self.y_test = train_test_split(self.x,self.y, test_size =self.testsize, random_state = 45)
        
        self.sc_x = StandardScaler()
        self.x_train = self.sc_x.fit_transform(x_train)
        self.x_test = self.sc_x.transform(x_test) 
        
        e = 0
        if self.lineEdit_2.text() == "":
            self.epocs=100
            self.progressBar.setMaximum(self.epocs - 2)
        else:
            self.epocs=int(self.lineEdit_2.text()) 
            self.progressBar.setMaximum(self.epocs - 2)
            
        if self.comboBox_10.currentText()=="LM": 
            self.remains = []
            self.histo = None
            t1_start = time.perf_counter()
            for e in range(self.epocs):
                #t1_start = time.perf_counter()
                self.histo = self.model_wrapper.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test),epochs=1, batch_size=self.val9, verbose=0)
                #t1_stop = time.perf_counter()
                self.remains.append(self.histo.history)
                
                self.progressBar.setValue(e) 
                #if self.progressBar.text() == "100%":
                #please check the indent back
                if self.comboBox_11.currentText()=="MSE":
                        self.label_50.setText('Mean Squared Error (Train):')
                        self.label_52.setText('Mean Squared Error (Test):')  
                        scores_0 = self.model_wrapper.history.history['mean_squared_error']
                        scores_0 = np.around((min(scores_0)*100), decimals= 3)
                        self.label_51.setText(str(scores_0)+"%")                        

                        scores = self.model_wrapper.evaluate(x=self.x_test, y=self.y_test)
                        self.content2 = scores[1]*100
                        self.label_53.setText(str(np.around(self.content2, decimals = 3))+"%")  
                        
                else:

                        self.label_50.setText('Overall Training Set Accuracy : ')
                        self.label_52.setText('Test Set Accuracy : ')
                        #self.label_46.setText(str(np.around(np.mean(self.classifier.history.history[self.var12])*100, decimals=2))+"%")
                        scores_0 = self.model_wrapper.history.history[self.var12]
                        scores_0 = np.around((max(scores_0)*100), decimals= 3)
                        self.label_51.setText(str(scores_0)+"%")
                            
                        scores = self.model_wrapper.evaluate(x=self.x_test, y=self.y_test)
                        self.content2 = scores[1]*100
                        self.label_53.setText(str(np.around(self.content2, decimals = 3))+"%")
            t1_stop = time.perf_counter()
            self.label_49.setText(str(np.around((t1_stop - t1_start), decimals=4))+' second')
            #print(self.remains)              
        else:
            self.remains = []
            self.histo = None
            t1_start = time.perf_counter()
            for e in range(self.epocs):
                #t1_start = time.perf_counter()
                self.histo = self.classifier.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test),epochs=1, batch_size=self.val9, verbose=0, shuffle=self.var14)
                #t1_stop = time.perf_counter()
                self.remains.append(self.histo.history)
                
                self.progressBar.setValue(e) 
                
                #if self.progressBar.text() == "100%":
                #please check the indent back
                if self.comboBox_11.currentText()=="MSE":
                        self.label_50.setText('Mean Squared Error (Train):')
                        self.label_52.setText('Mean Squared Error (Test):')
                        #scores_0 = (np.around(np.mean(self.classifier.history.history['mean_squared_error'])*100, decimals=2))
                        scores_0 = self.classifier.history.history['mean_squared_error']
                        scores_0 = np.around((min(scores_0)*100), decimals= 3)
                        self.label_51.setText(str(scores_0)+"%")
                        
                        scores = self.classifier.evaluate(self.x_test, self.y_test)
                        self.content2 = scores[1]*100
                        self.label_53.setText(str(np.around(self.content2, decimals = 3))+"%")      
                        
                else:
                        self.label_50.setText('Overall Training Set Accuracy : ')
                        self.label_52.setText('Test Set Accuracy : ')    
                        scores_0 = self.classifier.history.history[self.var12]
                        scores_0 = np.around((max(scores_0)*100), decimals= 3)                        
                        self.label_51.setText(str(scores_0)+"%")
                        #self.label_46.setText(str(np.around(np.mean(self.classifier.history.history[self.var12])*100, decimals=2))+"%")
                    
                        scores = self.classifier.evaluate(self.x_test, self.y_test)
                        self.content2 = scores[1]*100
                        self.label_53.setText(str(np.around(self.content2, decimals = 3))+"%")
            t1_stop = time.perf_counter()
            self.label_49.setText(str(np.around((t1_stop - t1_start), decimals=4))+' second')
            #print(self.remains)     
    def pred(self):

        self.forc=float(self.lineEdit_4.text())
        self.tim=float(self.lineEdit_5.text())
        self.curr=float(self.lineEdit_6.text())
        
        pred_val =np.array([[self.tim,self.curr,self.forc]]) 
        pred_val = self.sc_x.transform(pred_val)
        
        if self.comboBox_10.currentText()=="LM":
            y_pred = self.model_wrapper.predict(pred_val)
        else:
            y_pred = self.classifier.predict(pred_val)
            
        y_check = np.size(y_pred,1)
        
        if y_check == 3:

            y_pred = (y_pred == y_pred.max(axis=1)[:,None]).astype(int)
            y_pred = y_pred.reshape(-1,1)
            if y_pred[0] == 1:
                self.label_59.setText("Result : BAD")
                
            
            if y_pred[1] == 1:
                self.label_59.setText("Result : GOOD")
                
            
            if y_pred[2] == 1:
                self.label_59.setText("Result : WORST")
                
        elif y_check == 2:

            y_pred = (y_pred == y_pred.max(axis=1)[:,None]).astype(int)
            y_pred = y_pred.reshape(-1,1)
            if y_pred[0] == 1:
                self.label_59.setText("Result : BAD")
                
            
            if y_pred[1] == 1:
                self.label_59.setText("Result : GOOD")
                
        elif y_check == 1 and self.var1 == 'sigmoid':
            
            y_pred = y_pred.round()
            y_pred = y_pred.reshape(-1,1)
            if y_pred == 0:
                self.label_59.setText("Result : BAD")
                
            
            if y_pred == 1:
                self.label_59.setText("Result : GOOD")  
        
        else:
            y_pred = self.sc_y.inverse_transform(y_pred)
            y_pred = y_pred[0]
            self.label_59.setText("Result : "+str(y_pred)) 
            
        

    def WB (self):
        
        #if self.comboBox_10.currentText()=="LM":
        
            # for lop in range (self.klop):
        
            #     self.layer_weights = self.model_wrapper.layers[lop].get_weights()[0]
            #     self.layer_biases  = self.model_wrapper.layers[lop].get_weights()[1]            
             
            #     self.textEdit_2.append("\nHidden layer weight: \n")
            #     self.textEdit_2.append(str(self.layer_weights))
                
            #     self.textEdit_2.append("\nHidden layer bias: \n")
            #     self.textEdit_2.append(str(self.layer_biases))
        #else:

            for lop in range (self.klop):
        
                self.layer_weights = self.classifier.layers[lop].get_weights()[0]
                self.layer_biases  = self.classifier.layers[lop].get_weights()[1]            
             
                self.textEdit_2.append("\nHidden layer weight: \n")
                self.textEdit_2.append(str(self.layer_weights))
                
                self.textEdit_2.append("\nHidden layer bias: \n")
                self.textEdit_2.append(str(self.layer_biases))            

    def clr(self):
        self.figure.clear()
        self.canvas.draw()
    
    def clear(self):
        self.label_59.setText("Result: ")
    
    def plot_graph (self):
        df = pd.DataFrame(self.remains)
        if self.radioButton.isChecked():
            
        
            self.figure.clear()
            if self.yy > 2 and self.checkBox.isChecked() and self.comboBox_10.currentText() !="LM":
                target_n = ['0', '1', '2']
                prediction = self.classifier.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = np.argmax(self.y_test, axis =1)
    
            elif self.yy > 2 and (self.var12 == 'sparse_categorical_accuracy' or self.var12 == 'acc') and self.comboBox_10.currentText() !="LM":
                target_n = ['0', '1', '2']
                prediction = self.classifier.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = self.y_test
    
            elif self.yy == 2 and self.comboBox_10.currentText() !="LM":
                target_n = ['0', '1']
                prediction = self.classifier.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = np.argmax(self.y_test, axis =1)
    
            elif self.yy == 1 and self.var1 == 'sigmoid' and self.comboBox_10.currentText() !="LM":
                target_n = ['0', '1']
                prediction = self.classifier.predict(self.x_test)
                predictions = prediction.round()
                y_test_labels = self.y_test  
                
            elif self.var11 == 'categorical_crossentropy' and self.comboBox_10.currentText() =="LM":
                target_n = ['0', '1', '2']
                prediction = self.model_wrapper.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = np.argmax(self.y_test, axis =1)
            
            elif self.var11 == 'sparse_categorical_crossentropy' and self.comboBox_10.currentText() =="LM":
                target_n = ['0', '1', '2']
                prediction = self.model_wrapper.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = self.y_test
                
            elif self.yy == 2 and self.comboBox_10.currentText() =="LM":
                target_n = ['0', '1']
                prediction = self.model_wrapper.predict(self.x_test)
                predictions = np.argmax(prediction, axis = 1)
                y_test_labels = np.argmax(self.y_test, axis =1)  
                
            elif self.yy == 1 and self.var1 == 'sigmoid' and self.comboBox_10.currentText() =="LM":
                target_n = ['0', '1']
                prediction = self.model_wrapper.predict(self.x_test)
                predictions = prediction.round()
                y_test_labels = self.y_test  
                
            cm = confusion_matrix(y_test_labels, predictions)   
            
            def plot_confusion_matrix(cm,
                                   target_names,
                                   title='Confusion matrix',
                                   cmap=None,
                                   normalize=True):
                
                 
                 accuracy = np.trace(cm) / float(np.sum(cm))
                 misclass = 1 - accuracy       
                 if cmap is None:
                     cmap =  plt.get_cmap('Blues')
                 plt.imshow(cm, interpolation='nearest', cmap=cmap)
                 plt.title(title)
                 plt.colorbar()   
                 if target_names is not None:
                     tick_marks = np.arange(len(target_names))
                     plt.xticks(tick_marks, target_names, rotation=45)
                     plt.yticks(tick_marks, target_names)      
                 if normalize:
                     cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] 
                     
                 thresh = cm.max() / 1.5 if normalize else cm.max() / 2
                 for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
                     if normalize:
                         plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                                  horizontalalignment="center",
                                  color="white" if cm[i, j] > thresh else "black")     
                     else:        
                         plt.text(j, i, "{:,}".format(cm[i, j]),
                                  horizontalalignment="center",
                                  color="white" if cm[i, j] > thresh else "black")
                 plt.tight_layout()
                 plt.ylabel('True label')
                 plt.xlabel('Predicted label\nAccuracy={:0.4f}; Misclass={:0.4f}'.format(accuracy, misclass))
                 #plt.show()
                
            plot_confusion_matrix(cm, 
                                       
                                       
                                       normalize    = False,
                                       target_names = target_n,
                                       title        = "Confusion Matrix")        
            self.figure.tight_layout()
            self.canvas.draw()
        
        elif self.radioButton_2.isChecked():
            
            self.figure.clear()
            
            df['loss'] = df['loss'].str.get(0)
            df['val_loss'] = df['val_loss'].str.get(0)
            
            plt.plot(df['loss'])
            plt.plot(df['val_loss']
                            )        
            plt.title('Learning curve', loc='left', weight='bold')
            plt.ylabel('Loss')
            plt.xlabel('Epoch')
            plt.legend(['train', 'test'], loc='upper right')
    
            self.figure.tight_layout()
            self.canvas.draw()
        
        elif self.radioButton_3.isChecked():
            
            self.figure.clear()
            
            df[self.var12] = df[self.var12].str.get(0)
            df[self.varval] = df[self.varval].str.get(0)
            
            plt.plot(df[self.var12])
            plt.plot(df[self.varval]
                            )        
            plt.title('Model Accuracy', loc='left', weight='bold')
            plt.ylabel('Accuracy')
            plt.xlabel('Epoch')
            plt.legend(['Train', 'Test'], loc='upper right')
    
            self.figure.tight_layout()
            self.canvas.draw()           
        
        else:
            pass

####################################################### EDITING END ###################################################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application of ANN in RSW"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:18pt; font-weight:600;\">APPLICATION OF ARTIFICIAL NEURAL NETWORK USING PYTHON</span></p><p align=\"center\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:18pt; font-weight:600;\">(MANUFACTURING RESEARCH FIELD: RESISTANCE SPOT WELDING)</span></p><p align=\"center\"><br/><span style=\" font-family:\'Times New Roman,serif\'; font-size:18pt; font-weight:600; font-style:italic;\">Q-Check (Beta version)</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; font-weight:600;\">DEVELOPED BY:</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; font-weight:600;\">MUHAMAD AIMAN RAZIQ</span></p><p align=\"center\"><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Intro"))
        self.label_4.setText(_translate("MainWindow", "Please select the CSV file :"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        self.label_5.setText(_translate("MainWindow", "Data URL :"))
        self.checkBox.setToolTip(_translate("MainWindow", "Let say 2 classes list [1,0,1] to [[0,1],[1,0],[0,1]] one_hot form"))
        self.checkBox.setText(_translate("MainWindow", "Transform target value to One_Hot form"))
        self.checkBox_2.setText(_translate("MainWindow", "Linear Regression"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.label_6.setText(_translate("MainWindow", "Data Progress :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Select File"))
        self.label_7.setText(_translate("MainWindow", "Input Layer:"))
        self.label_8.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_9.setText(_translate("MainWindow", "Output Layer:"))
        self.label_10.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_11.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox.setItemText(0, _translate("MainWindow", "sigmoid"))
        self.comboBox.setItemText(1, _translate("MainWindow", "softmax"))
        self.comboBox.setItemText(2, _translate("MainWindow", "linear"))
        self.label_12.setText(_translate("MainWindow", "1. Hidden Layer"))
        self.label_13.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_14.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "softmax"))
        self.label_15.setText(_translate("MainWindow", "2. Hidden Layer"))
        self.label_16.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_17.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_3.setText(_translate("MainWindow", "HL 2"))
        self.label_18.setText(_translate("MainWindow", "3. Hidden Layer"))
        self.label_19.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_20.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_4.setText(_translate("MainWindow", "HL 3"))
        self.label_21.setText(_translate("MainWindow", "4. Hidden Layer"))
        self.label_23.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_24.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_5.setText(_translate("MainWindow", "HL 4"))
        self.label_25.setText(_translate("MainWindow", "5. Hidden Layer"))
        self.label_26.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_27.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_6.setText(_translate("MainWindow", "HL 5"))
        self.label_28.setText(_translate("MainWindow", "6. Hidden Layer"))
        self.label_29.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_30.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_7.setText(_translate("MainWindow", "HL 6"))
        self.label_31.setText(_translate("MainWindow", "7. Hidden Layer"))
        self.label_32.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_33.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_8.setText(_translate("MainWindow", "HL 7"))
        self.label_34.setText(_translate("MainWindow", "8. Hidden Layer"))
        self.label_35.setText(_translate("MainWindow", "Number of Neuron:"))
        self.label_36.setText(_translate("MainWindow", "Activation Function : "))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "relu"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "sigmoid"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "softmax"))
        self.checkBox_9.setText(_translate("MainWindow", "HL 8"))
        self.label_37.setText(_translate("MainWindow", "Optimizer :"))
        self.label_38.setText(_translate("MainWindow", "Loss : "))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "GD"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "SGD"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "LMA"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "BinaryCrossentropy"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "CategoricalCrossentropy"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "SparseCategoricalCrossentropy"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "MSE"))
        self.label_39.setText(_translate("MainWindow", "Metrics : "))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Accuracy"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "BinaryAccuracy"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "CategoricalAccuracy"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "SparseCategoricalAccuracy"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "MSE"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.label_43.setText(_translate("MainWindow", "Model : Not Submitted !"))
        self.label_40.setText(_translate("MainWindow", "Learning rate : "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "By default, 0.01"))
        self.label_41.setText(_translate("MainWindow", "Epochs : "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "By default, 100"))
        self.label_42.setText(_translate("MainWindow", "Batch Size : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Model Setup"))
        self.label_44.setText(_translate("MainWindow", "Insert The Train Set Size (%) :"))
        self.label_45.setText(_translate("MainWindow", "Train Size :"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "By default, 80%"))
        self.label_46.setText(_translate("MainWindow", "Test Size :"))
        self.label_47.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "Train data"))
        self.label_48.setText(_translate("MainWindow", "Elapsed time : "))
        self.label_49.setText(_translate("MainWindow", "-"))
        self.label_50.setText(_translate("MainWindow", "Overall Training Set Accuracy : "))
        self.label_51.setText(_translate("MainWindow", "-"))
        self.label_52.setText(_translate("MainWindow", "Test Set Accuracy : "))
        self.label_53.setText(_translate("MainWindow", "-"))
        self.label_54.setText(_translate("MainWindow", "Model Graph : "))
        self.radioButton.setText(_translate("MainWindow", "Confusion matrix"))
        self.radioButton_2.setText(_translate("MainWindow", "Loss"))
        self.radioButton_3.setText(_translate("MainWindow", "Accuracy"))
        self.pushButton_5.setText(_translate("MainWindow", "Plot"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear"))
        self.label_22.setText(_translate("MainWindow", "Progress :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Train"))
        self.pushButton_7.setText(_translate("MainWindow", "Get Weight and Bias"))
        self.pushButton_8.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Weight and Biases"))
        self.label_55.setText(_translate("MainWindow", "Please Insert The Input Value "))
        self.label_56.setText(_translate("MainWindow", "Applied Force (N) :"))
        self.label_57.setText(_translate("MainWindow", "Welding time (cycle time) : "))
        self.label_58.setText(_translate("MainWindow", "Welding current (kA) : "))
        self.label_59.setText(_translate("MainWindow", "Result : "))
        self.pushButton_9.setText(_translate("MainWindow", "Submit"))
        self.pushButton_10.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Prediction"))

import backg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

