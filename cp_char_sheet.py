# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cp_char_sheet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 10, 1101, 671))
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 159, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        self.CharMain = QtWidgets.QWidget()
        self.CharMain.setObjectName("CharMain")
        self.charSheetGroup = QtWidgets.QGroupBox(self.CharMain)
        self.charSheetGroup.setGeometry(QtCore.QRect(20, 30, 1051, 591))
        self.charSheetGroup.setObjectName("charSheetGroup")
        self.HandleInput = QtWidgets.QLineEdit(self.charSheetGroup)
        self.HandleInput.setGeometry(QtCore.QRect(160, 40, 301, 41))
        self.HandleInput.setStyleSheet("background-color: white;\n"
"font: 14pt \"OCR A Extended\";\n"
"border: 2px solid  rgb(244,0,0);\n"
"padding-left: 2px;")
        self.HandleInput.setObjectName("HandleInput")
        self.HumanityCurrent = QtWidgets.QLabel(self.charSheetGroup)
        self.HumanityCurrent.setGeometry(QtCore.QRect(10, 200, 61, 41))
        self.HumanityCurrent.setStyleSheet("border: 2px solid rgb(244,0,0);\n"
"font: 12pt \"OCR A Extended\";\n"
"padding-left: 2px;\n"
"text-align: center;\n"
"background: white;")
        self.HumanityCurrent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HumanityCurrent.setObjectName("HumanityCurrent")
        self.handleLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.handleLabel.setGeometry(QtCore.QRect(160, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.handleLabel.setFont(font)
        self.handleLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.handleLabel.setObjectName("handleLabel")
        self.RankLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.RankLabel.setGeometry(QtCore.QRect(400, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.RankLabel.setFont(font)
        self.RankLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.RankLabel.setObjectName("RankLabel")
        self.RoleAbilityDisplay = QtWidgets.QLabel(self.charSheetGroup)
        self.RoleAbilityDisplay.setGeometry(QtCore.QRect(160, 200, 242, 41))
        self.RoleAbilityDisplay.setStyleSheet("border: 2px solid rgb(244,0,0);\n"
"font: 12pt \"OCR A Extended\";\n"
"padding-left: 2px;\n"
"background: white;")
        self.RoleAbilityDisplay.setObjectName("RoleAbilityDisplay")
        self.CharacterImage = QtWidgets.QGraphicsView(self.charSheetGroup)
        self.CharacterImage.setGeometry(QtCore.QRect(10, 20, 131, 121))
        self.CharacterImage.setStyleSheet("border: 2px solid rgb(244,0,0);")
        self.CharacterImage.setObjectName("CharacterImage")
        self.HumanityMax = QtWidgets.QLabel(self.charSheetGroup)
        self.HumanityMax.setGeometry(QtCore.QRect(80, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HumanityMax.setFont(font)
        self.HumanityMax.setStyleSheet("border: 2px solid rgb(244,0,0);\n"
"font: 12pt \"OCR A Extended\";\n"
"padding-left: 2px;\n"
"background: white;")
        self.HumanityMax.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HumanityMax.setObjectName("HumanityMax")
        self.RoleLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.RoleLabel.setGeometry(QtCore.QRect(160, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.RoleLabel.setFont(font)
        self.RoleLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.RoleLabel.setObjectName("RoleLabel")
        self.RoleSelect = QtWidgets.QComboBox(self.charSheetGroup)
        self.RoleSelect.setGeometry(QtCore.QRect(160, 120, 301, 41))
        self.RoleSelect.setAutoFillBackground(False)
        self.RoleSelect.setStyleSheet("border: 2px solid rgb(244,0,0);\n"
"background-color: white;\n"
"font: 12pt \"OCR A Extended\";")
        self.RoleSelect.setObjectName("RoleSelect")
        self.HumanityLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.HumanityLabel.setGeometry(QtCore.QRect(10, 180, 131, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.HumanityLabel.setFont(font)
        self.HumanityLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.HumanityLabel.setObjectName("HumanityLabel")
        self.RoleAbilityRankInput = QtWidgets.QLineEdit(self.charSheetGroup)
        self.RoleAbilityRankInput.setGeometry(QtCore.QRect(400, 200, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RoleAbilityRankInput.setFont(font)
        self.RoleAbilityRankInput.setStyleSheet("background-color: white;\n"
"border: 2px solid rgb(244,0,0);\n"
"")
        self.RoleAbilityRankInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.RoleAbilityRankInput.setObjectName("RoleAbilityRankInput")
        self.ImagLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.ImagLabel.setGeometry(QtCore.QRect(10, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ImagLabel.setFont(font)
        self.ImagLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;\n"
"")
        self.ImagLabel.setObjectName("ImagLabel")
        self.HumanitySpacer = QtWidgets.QLabel(self.charSheetGroup)
        self.HumanitySpacer.setGeometry(QtCore.QRect(70, 200, 10, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.HumanitySpacer.setFont(font)
        self.HumanitySpacer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HumanitySpacer.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 8pt \"OCR A Extended\";\n"
"font-weight: bold;")
        self.HumanitySpacer.setObjectName("HumanitySpacer")
        self.RoleAbilityLabel = QtWidgets.QLabel(self.charSheetGroup)
        self.RoleAbilityLabel.setGeometry(QtCore.QRect(160, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.RoleAbilityLabel.setFont(font)
        self.RoleAbilityLabel.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.RoleAbilityLabel.setObjectName("RoleAbilityLabel")
        self.frame = QtWidgets.QFrame(self.charSheetGroup)
        self.frame.setGeometry(QtCore.QRect(10, 260, 691, 81))
        self.frame.setStyleSheet("background-color: rgb(244,0,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.IntelligenceInput = QtWidgets.QLineEdit(self.frame)
        self.IntelligenceInput.setGeometry(QtCore.QRect(10, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IntelligenceInput.setFont(font)
        self.IntelligenceInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.IntelligenceInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.IntelligenceInput.setObjectName("IntelligenceInput")
        self.IntelligenceLabel = QtWidgets.QLabel(self.frame)
        self.IntelligenceLabel.setGeometry(QtCore.QRect(10, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.IntelligenceLabel.setFont(font)
        self.IntelligenceLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.IntelligenceLabel.setObjectName("IntelligenceLabel")
        self.ReflexInput = QtWidgets.QLineEdit(self.frame)
        self.ReflexInput.setGeometry(QtCore.QRect(70, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ReflexInput.setFont(font)
        self.ReflexInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.ReflexInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ReflexInput.setObjectName("ReflexInput")
        self.ReflexLabel = QtWidgets.QLabel(self.frame)
        self.ReflexLabel.setGeometry(QtCore.QRect(70, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ReflexLabel.setFont(font)
        self.ReflexLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.ReflexLabel.setObjectName("ReflexLabel")
        self.DexterityInput = QtWidgets.QLineEdit(self.frame)
        self.DexterityInput.setGeometry(QtCore.QRect(130, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DexterityInput.setFont(font)
        self.DexterityInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.DexterityInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DexterityInput.setObjectName("DexterityInput")
        self.DexterityLabel = QtWidgets.QLabel(self.frame)
        self.DexterityLabel.setGeometry(QtCore.QRect(130, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.DexterityLabel.setFont(font)
        self.DexterityLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.DexterityLabel.setObjectName("DexterityLabel")
        self.TechInput = QtWidgets.QLineEdit(self.frame)
        self.TechInput.setGeometry(QtCore.QRect(190, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TechInput.setFont(font)
        self.TechInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.TechInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TechInput.setObjectName("TechInput")
        self.TechLabel = QtWidgets.QLabel(self.frame)
        self.TechLabel.setGeometry(QtCore.QRect(190, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.TechLabel.setFont(font)
        self.TechLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.TechLabel.setObjectName("TechLabel")
        self.CoolInput = QtWidgets.QLineEdit(self.frame)
        self.CoolInput.setGeometry(QtCore.QRect(250, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CoolInput.setFont(font)
        self.CoolInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.CoolInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CoolInput.setObjectName("CoolInput")
        self.BodyInput = QtWidgets.QLineEdit(self.frame)
        self.BodyInput.setGeometry(QtCore.QRect(430, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BodyInput.setFont(font)
        self.BodyInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.BodyInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BodyInput.setObjectName("BodyInput")
        self.CoolLabel = QtWidgets.QLabel(self.frame)
        self.CoolLabel.setGeometry(QtCore.QRect(250, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.CoolLabel.setFont(font)
        self.CoolLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.CoolLabel.setObjectName("CoolLabel")
        self.WillInput = QtWidgets.QLineEdit(self.frame)
        self.WillInput.setGeometry(QtCore.QRect(310, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WillInput.setFont(font)
        self.WillInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.WillInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.WillInput.setObjectName("WillInput")
        self.WillLabel = QtWidgets.QLabel(self.frame)
        self.WillLabel.setGeometry(QtCore.QRect(310, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.WillLabel.setFont(font)
        self.WillLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.WillLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.WillLabel.setObjectName("WillLabel")
        self.MoveInput = QtWidgets.QLineEdit(self.frame)
        self.MoveInput.setGeometry(QtCore.QRect(370, 29, 51, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MoveInput.setFont(font)
        self.MoveInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.MoveInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MoveInput.setObjectName("MoveInput")
        self.MoveLabel = QtWidgets.QLabel(self.frame)
        self.MoveLabel.setGeometry(QtCore.QRect(370, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.MoveLabel.setFont(font)
        self.MoveLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.MoveLabel.setObjectName("MoveLabel")
        self.BodyLabel = QtWidgets.QLabel(self.frame)
        self.BodyLabel.setGeometry(QtCore.QRect(430, 7, 51, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.BodyLabel.setFont(font)
        self.BodyLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.BodyLabel.setObjectName("BodyLabel")
        self.LuckLabel = QtWidgets.QLabel(self.frame)
        self.LuckLabel.setGeometry(QtCore.QRect(490, 7, 91, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.LuckLabel.setFont(font)
        self.LuckLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.LuckLabel.setObjectName("LuckLabel")
        self.LuckCurrentInput = QtWidgets.QLineEdit(self.frame)
        self.LuckCurrentInput.setGeometry(QtCore.QRect(490, 29, 41, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LuckCurrentInput.setFont(font)
        self.LuckCurrentInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.LuckCurrentInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LuckCurrentInput.setObjectName("LuckCurrentInput")
        self.LuckMaxInput = QtWidgets.QLineEdit(self.frame)
        self.LuckMaxInput.setGeometry(QtCore.QRect(540, 29, 41, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LuckMaxInput.setFont(font)
        self.LuckMaxInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.LuckMaxInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LuckMaxInput.setObjectName("LuckMaxInput")
        self.LuckSpacer = QtWidgets.QLabel(self.frame)
        self.LuckSpacer.setGeometry(QtCore.QRect(530, 29, 10, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.LuckSpacer.setFont(font)
        self.LuckSpacer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.LuckSpacer.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 8pt \"OCR A Extended\";\n"
"font-weight: bold;")
        self.LuckSpacer.setObjectName("LuckSpacer")
        self.EmpathySpacer = QtWidgets.QLabel(self.frame)
        self.EmpathySpacer.setGeometry(QtCore.QRect(630, 30, 10, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.EmpathySpacer.setFont(font)
        self.EmpathySpacer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.EmpathySpacer.setStyleSheet("background-color: rgb(244, 0, 0);\n"
"color: white;\n"
"font: 8pt \"OCR A Extended\";\n"
"font-weight: bold;")
        self.EmpathySpacer.setObjectName("EmpathySpacer")
        self.EmpathyMaxInput = QtWidgets.QLineEdit(self.frame)
        self.EmpathyMaxInput.setGeometry(QtCore.QRect(640, 30, 41, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EmpathyMaxInput.setFont(font)
        self.EmpathyMaxInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.EmpathyMaxInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.EmpathyMaxInput.setObjectName("EmpathyMaxInput")
        self.EmpathyLabel = QtWidgets.QLabel(self.frame)
        self.EmpathyLabel.setGeometry(QtCore.QRect(590, 8, 91, 25))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.EmpathyLabel.setFont(font)
        self.EmpathyLabel.setStyleSheet("background-color:white;\n"
"color: black;\n"
"font: 10pt \"OCR A Extended\";\n"
"font-weight: bold;\n"
"padding-left: 2px;")
        self.EmpathyLabel.setObjectName("EmpathyLabel")
        self.EmpathyCurrentInput = QtWidgets.QLineEdit(self.frame)
        self.EmpathyCurrentInput.setGeometry(QtCore.QRect(590, 30, 41, 45))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EmpathyCurrentInput.setFont(font)
        self.EmpathyCurrentInput.setStyleSheet("background-color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.EmpathyCurrentInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.EmpathyCurrentInput.setObjectName("EmpathyCurrentInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionReport_a_bug = QAction(MainWindow)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionDocumentation)
        self.menuAbout.addAction(self.actionReport_a_bug)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cyberpunk Red Character Sheet"))
        self.CharMain.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.charSheetGroup.setTitle(_translate("MainWindow", "filenamehere"))
        self.HumanityCurrent.setText(_translate("MainWindow", "23"))
        self.handleLabel.setText(_translate("MainWindow", "HANDLE"))
        self.RankLabel.setText(_translate("MainWindow", "RANK"))
        self.RoleAbilityDisplay.setText(_translate("MainWindow", "No role selected..."))
        self.HumanityMax.setText(_translate("MainWindow", "23"))
        self.RoleLabel.setText(_translate("MainWindow", "ROLES"))
        self.HumanityLabel.setText(_translate("MainWindow", "HUMANITY"))
        self.RoleAbilityRankInput.setText(_translate("MainWindow", "4"))
        self.ImagLabel.setText(_translate("MainWindow", "IMAGE"))
        self.HumanitySpacer.setText(_translate("MainWindow", "|"))
        self.RoleAbilityLabel.setText(_translate("MainWindow", "ROLE ABILITY"))
        self.IntelligenceInput.setText(_translate("MainWindow", "8"))
        self.IntelligenceLabel.setText(_translate("MainWindow", "INT"))
        self.ReflexInput.setText(_translate("MainWindow", "6"))
        self.ReflexLabel.setText(_translate("MainWindow", "REF"))
        self.DexterityInput.setText(_translate("MainWindow", "5"))
        self.DexterityLabel.setText(_translate("MainWindow", "DEX"))
        self.TechInput.setText(_translate("MainWindow", "8"))
        self.TechLabel.setText(_translate("MainWindow", "TECH"))
        self.CoolInput.setText(_translate("MainWindow", "5"))
        self.BodyInput.setText(_translate("MainWindow", "5"))
        self.CoolLabel.setText(_translate("MainWindow", "COOL"))
        self.WillInput.setText(_translate("MainWindow", "5"))
        self.WillLabel.setText(_translate("MainWindow", "WILL"))
        self.MoveInput.setText(_translate("MainWindow", "5"))
        self.MoveLabel.setText(_translate("MainWindow", "MOVE"))
        self.BodyLabel.setText(_translate("MainWindow", "BODY"))
        self.LuckLabel.setText(_translate("MainWindow", "LUCK"))
        self.LuckCurrentInput.setText(_translate("MainWindow", "7"))
        self.LuckMaxInput.setText(_translate("MainWindow", "7"))
        self.LuckSpacer.setText(_translate("MainWindow", "|"))
        self.EmpathySpacer.setText(_translate("MainWindow", "|"))
        self.EmpathyMaxInput.setText(_translate("MainWindow", "8"))
        self.EmpathyLabel.setText(_translate("MainWindow", "EMP"))
        self.EmpathyCurrentInput.setText(_translate("MainWindow", "7"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionReport_a_bug.setText(_translate("MainWindow", "Report a bug"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
