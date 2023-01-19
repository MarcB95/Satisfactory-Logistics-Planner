# -*- coding: utf-8 -*-
import PyQt5.QtWidgets as qtw
from PyQt5 import QtGui, QtCore
import pandas as pd
import os, re

# contains all items as dataframe
Item_df = pd.read_csv('Recipes.csv', delimiter=',')
Item_df = Item_df.where(Item_df.notnull(), None)
basic_resources = Item_df.index[Item_df['tier'] == 0].tolist()

# returns dataframe index as int
def getIndex(name):
    name = name.replace(' ', '_')
    return Item_df.loc[Item_df['name'] == name].first_valid_index()

# returns single value inside dataframe
def getAttribute(idx, attr):
    return Item_df.iloc[idx][attr]

# returns dict for processed item, str for basic resource
def getDict(idx):
    itemDict = Item_df.iloc[[idx]].to_dict()
    for attr in itemDict:
        for x in itemDict[attr]:
            itemDict[attr] = itemDict[attr][x]
        if itemDict['tier'] == 0:
            return itemDict['name']
        else:
            return itemDict

def getItemPoolNames(tier, format='_'):
    itemPool_df = Item_df.loc[Item_df['tier'].between(1, tier)]
    itemPool_names = itemPool_df['name'].tolist()
    if format == '_':
        return itemPool_names
    else:
        return [name.replace('_', ' ') for name in itemPool_names]

# check for invalid input numbers
def inputError(input):
    invalid_character = re.search('[^\d\.]', input)
    if invalid_character:
        return True, re.sub('[^\d\.]', '', input)
    dots = len(re.findall('[\.]', input))
    if dots > 1:
        parts = input.split('.')
        parts[1:] = [''.join(parts[1:])]
        return True, parts[0] +'.'+ parts[1]
    leading_zero = re.match('[0][\d]', input)
    if leading_zero:
            input = re.sub('[0]*', '', input, count=1)
    if input == '':
        return True, '0'
    return False, input

class MainWindow(qtw.QMainWindow):
    # imported ui file
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color:rgb(70, 70, 80)")
        self.centralwidget = qtw.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = qtw.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 851, 92))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_top = qtw.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_top.setContentsMargins(14, 0, 0, 0)
        self.layout_top.setSpacing(6)
        self.layout_top.setObjectName("layout_top")
        self.label = qtw.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(140, 0))
        self.label.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setFrameShape(qtw.QFrame.NoFrame)
        self.label.setFrameShadow(qtw.QFrame.Plain)
        self.label.setObjectName("label")
        self.layout_top.addWidget(self.label)
        self.button1 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button1.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button1.setFont(font)
        self.button1.setStyleSheet("background-color:#fa9549;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: rgb(190, 110, 55);\n"
"selection-background-color: yellow;")
        self.button1.setCheckable(False)
        self.button1.setChecked(False)
        self.button1.setObjectName("button1")
        self.layout_top.addWidget(self.button1)
        self.button2 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button2.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button2.setFont(font)
        self.button2.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button2.setCheckable(False)
        self.button2.setObjectName("button2")
        self.layout_top.addWidget(self.button2)
        self.button3 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button3.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button3.setFont(font)
        self.button3.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button3.setCheckable(False)
        self.button3.setObjectName("button3")
        self.layout_top.addWidget(self.button3)
        self.button4 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button4.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button4.setFont(font)
        self.button4.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button4.setCheckable(False)
        self.button4.setObjectName("button4")
        self.layout_top.addWidget(self.button4)
        self.button5 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button5.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button5.setFont(font)
        self.button5.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button5.setCheckable(False)
        self.button5.setObjectName("button5")
        self.layout_top.addWidget(self.button5)
        self.button6 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button6.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button6.setFont(font)
        self.button6.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button6.setCheckable(False)
        self.button6.setObjectName("button6")
        self.layout_top.addWidget(self.button6)
        self.button7 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button7.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button7.setFont(font)
        self.button7.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button7.setCheckable(False)
        self.button7.setObjectName("button7")
        self.layout_top.addWidget(self.button7)
        self.button8 = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button8.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button8.setFont(font)
        self.button8.setStyleSheet("background-color: lightgray;\n"
"border-style: outset;\n"
"border-width: 6px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button8.setCheckable(False)
        self.button8.setObjectName("button8")
        self.layout_top.addWidget(self.button8)
        spacerItem = qtw.QSpacerItem(8, 0, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Minimum)
        self.layout_top.addItem(spacerItem)
        self.button_clear = qtw.QPushButton(self.horizontalLayoutWidget)
        self.button_clear.setMinimumSize(QtCore.QSize(90, 50))
        self.button_clear.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("background-color: lightgray;\n"
"border-style:outset;\n"
"border-width: 4px;\n"
"border-radius: 8px;\n"
"border-color: darkgray;\n"
"selection-background-color: yellow;")
        self.button_clear.setObjectName("button_clear")
        self.layout_top.addWidget(self.button_clear)
        self.seperator_top = qtw.QFrame(self.centralwidget)
        self.seperator_top.setEnabled(True)
        self.seperator_top.setGeometry(QtCore.QRect(0, 100, 1920, 20))
        self.seperator_top.setStyleSheet("background-color:none;")
        self.seperator_top.setFrameShadow(qtw.QFrame.Plain)
        self.seperator_top.setLineWidth(5)
        self.seperator_top.setFrameShape(qtw.QFrame.HLine)
        self.seperator_top.setObjectName("seperator_top")
        self.seperator_left = qtw.QFrame(self.centralwidget)
        self.seperator_left.setGeometry(QtCore.QRect(303, 110, 20, 951))
        self.seperator_left.setStyleSheet("background-color:none;")
        self.seperator_left.setFrameShadow(qtw.QFrame.Plain)
        self.seperator_left.setLineWidth(5)
        self.seperator_left.setFrameShape(qtw.QFrame.VLine)
        self.seperator_left.setObjectName("seperator_left")
        self.verticalLayoutWidget = qtw.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 129, 291, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_left_header = qtw.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_left_header.setContentsMargins(0, 0, 0, 0)
        self.layout_left_header.setObjectName("layout_left_header")
        self.label_searchbar = qtw.QLabel(self.verticalLayoutWidget)
        self.label_searchbar.setMinimumSize(QtCore.QSize(0, 25))
        self.label_searchbar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_searchbar.setStyleSheet("")
        self.label_searchbar.setObjectName("label_searchbar")
        self.layout_left_header.addWidget(self.label_searchbar)
        self.line_searchbar = qtw.QLineEdit(self.verticalLayoutWidget)
        self.line_searchbar.setMinimumSize(QtCore.QSize(0, 0))
        self.line_searchbar.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_searchbar.setFont(font)
        self.line_searchbar.setStyleSheet("background-color:white")
        self.line_searchbar.setObjectName("line_searchbar")
        self.layout_left_header.addWidget(self.line_searchbar)
        self.layout_target = qtw.QHBoxLayout()
        self.layout_target.setSpacing(6)
        self.layout_target.setObjectName("layout_target")
        self.label_main_target = qtw.QLabel(self.verticalLayoutWidget)
        self.label_main_target.setMinimumSize(QtCore.QSize(0, 25))
        self.label_main_target.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_main_target.setObjectName("label_main_target")
        self.layout_target.addWidget(self.label_main_target)
        spacerItem1 = qtw.QSpacerItem(0, 0, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)
        self.layout_target.addItem(spacerItem1)
        self.line_main_target = qtw.QLineEdit(self.verticalLayoutWidget)
        self.line_main_target.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_main_target.setFont(font)
        self.line_main_target.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_main_target.setStyleSheet("background-color:white")
        self.line_main_target.setMaxLength(6)
        self.line_main_target.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_main_target.setObjectName("line_main_target")
        self.layout_target.addWidget(self.line_main_target)
        self.label_per_min = qtw.QLabel(self.verticalLayoutWidget)
        self.label_per_min.setMinimumSize(QtCore.QSize(33, 25))
        self.label_per_min.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_per_min.setObjectName("label_per_min")
        self.layout_target.addWidget(self.label_per_min)
        self.layout_left_header.addLayout(self.layout_target)
        self.verticalLayoutWidget_2 = qtw.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 289, 311, 711))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_resources = qtw.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_resources.setContentsMargins(0, 0, 0, 0)
        self.layout_resources.setObjectName("layout_resources")
        self.scrollArea = qtw.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(329, 129, 1570, 870))
        self.scrollArea.setMinimumSize(QtCore.QSize(1570, 870))
        self.scrollArea.setMaximumSize(QtCore.QSize(1570, 870))
        self.scrollArea.setStyleSheet("color: darkgray;")
        self.scrollArea.setFrameShape(qtw.QFrame.Box)
        self.scrollArea.setFrameShadow(qtw.QFrame.Plain)
        self.scrollArea.setLineWidth(4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea_content = qtw.QWidget()
        self.scrollArea_content.setGeometry(QtCore.QRect(0, 0, 1562, 862))
        self.scrollArea_content.setObjectName("scrollArea_content")
        self.scrollArea.setWidget(self.scrollArea_content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = qtw.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fa9549;\">Tier:</span></p></body></html>"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.label_searchbar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#fa9549;\">Item Name:</span></p></body></html>"))
        self.label_main_target.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#fa9549;\">Target:</span></p></body></html>"))
        self.line_main_target.setText(_translate("MainWindow", "1"))
        self.label_per_min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#fa9549;\">/min</span></p></body></html>"))

    def __init__(self):
        super(MainWindow, self).__init__()
        #uic.loadUi("Logistics-Planner.ui", self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/Logo.png'))
        self.retranslateUi(self)

        # tier button list
        self.Button_list=[self.button1, self.button2,
                    self.button3, self.button4,
                    self.button5, self.button6,
                    self.button7, self.button8]

        self.active_style = self.button1.styleSheet()
        self.inactive_style = self.button2.styleSheet()
        self.clear_style = self.button_clear.styleSheet()
        pressed_style = """background-color: #9f9f9f;
            border-style: inset;
            border-width: 4px;
            border-radius: 8px;
            border-color: gray;"""
        self.current_item = None
        self.scrollArea.setWidgetResizable(True)

        # auto completer
        self.completer = Completer(self.centralwidget)
        self.completer.setCaseSensitivity(0)
        self.line_searchbar.setCompleter(self.completer)

        # tier buttons
        self.button1.clicked.connect(lambda: self.buttonPress(1))
        self.button2.clicked.connect(lambda: self.buttonPress(2))
        self.button3.clicked.connect(lambda: self.buttonPress(3))
        self.button4.clicked.connect(lambda: self.buttonPress(4))
        self.button5.clicked.connect(lambda: self.buttonPress(5))
        self.button6.clicked.connect(lambda: self.buttonPress(6))
        self.button7.clicked.connect(lambda: self.buttonPress(7))
        self.button8.clicked.connect(lambda: self.buttonPress(8))

        self.button_clear.pressed.connect(
            lambda b=self.button_clear: b.setStyleSheet(pressed_style))
        self.button_clear.released.connect(self.clearWidgets)

        self.line_searchbar.editingFinished.connect(self.itemConfirmed)
        self.line_main_target.textChanged[str].connect(lambda: self.targetChanged())

    # target value is being edited
    def targetChanged(self):
        target = self.line_main_target.text()

        # invalid input handling
        isError, target = inputError(target)
        self.line_main_target.setText(target)
        if isError:
            self.line_main_target.setStyleSheet(
                'background-color:white; border: 2px solid red;')
            return
        else: self.line_main_target.setStyleSheet(
                'background-color:white;')

        if self.current_item == None: return
        target = float(target)
        for widget in self.Display_widgets:
            widget.update(target)
        for widget in self.Resource_widgets:
            widget.update(target)

    # a tier button is pressed
    def buttonPress(self, tier):
        if tier == self.completer.active_tier: return
        for i in range(1, len(self.Button_list)):
            if i < tier:
                self.Button_list[i].setStyleSheet(
                    self.active_style)
            else:
                self.Button_list[i].setStyleSheet(
                    self.inactive_style)
        self.completer.update(tier)

    # delete current item and production tree widgets
    def clearWidgets(self):
        self.button_clear.setStyleSheet(self.clear_style)
        dummy = qtw.QWidget()
        self.scrollArea.setWidget(dummy)
        for i in reversed(range(self.layout_resources.count()-1)):
            self.layout_resources.itemAt(i).widget().setParent(None)
        if self.layout_resources.count() == 1:
            self.layout_resources.takeAt(0)
        self.current_item = None
        self.line_searchbar.setText('')

    # when item name is confirmed in the searchbar
    def itemConfirmed(self):
        line_input = self.line_searchbar.text()
        line_input = line_input.replace(' ', '_')
        tier = self.completer.active_tier
        itemPool_names = getItemPoolNames(tier, '_')

        if line_input not in itemPool_names: return
        if line_input == self.current_item: return

        self.clearWidgets()
        self.current_item = line_input
        target = float(self.line_main_target.text())
        ProductionTree = TreeNode(getIndex(line_input))
        NodeList = []
        ProductionTree.getNodeList(NodeList)

        # find deepest level and total demand factor
        mainDict = {}
        max_depth = 0
        for node in NodeList:
            idx = node.item_idx
            depth = node.level
            demand = node.demand

            if idx not in mainDict:
                mainDict[idx] = {'depth':depth, 'demand':0}
            elif mainDict[idx]['depth'] < depth:
                mainDict[idx]['depth'] = depth
            mainDict[idx]['demand'] += demand
            max_depth = max(max_depth, depth)

        self.Display_widgets = []
        self.Resource_widgets = []
        occupied_space = [0]*(max_depth+1)
        grid_display = qtw.QGridLayout()
        grid_display.setSpacing(6)

        # create and place custom widgets
        for item in mainDict:
            column = mainDict[item]['depth']
            demand = mainDict[item]['demand']
            if column == -1:
                newWidget = ResourceWidget(self.centralwidget, item, demand)
                self.Resource_widgets.append(newWidget)
                self.layout_resources.addWidget(newWidget)
                newWidget.update(target)
                continue
            row = occupied_space[column]
            newWidget = DisplayWidget(self.centralwidget, item, demand)
            self.Display_widgets.append(newWidget)
            grid_display.addWidget(newWidget, row, max_depth - column, QtCore.Qt.AlignCenter)
            occupied_space[column] += 1
            newWidget.update(target)

        self.layout_resources.addStretch(1)
        grid_display.setColumnStretch(max_depth+1, 1)
        grid_display.setRowStretch(max(occupied_space)+1, 1)
        frame = qtw.QFrame()
        frame.setLayout(grid_display)
        self.scrollArea.setWidget(frame)


# auto completer for the searchbar
class Completer(qtw.QCompleter):
    def __init__(self, parent):
        super(Completer, self).__init__(parent)
        self.active_tier = 1
        self.content = QtCore.QStringListModel()
        itemPool_names = getItemPoolNames(self.active_tier, ' ')
        self.content.setStringList(itemPool_names)
        self.setModel(self.content)

    # update item pool based on confirmed tier
    def update(self, tier):
        if tier == self.active_tier: return
        self.active_tier = tier
        itemPool_names = getItemPoolNames(tier, ' ')
        self.content.setStringList(itemPool_names)

# item-specific ancestry data structure
class TreeNode:
    def __init__(self, item_idx, demand=1.0, level=0):
        self.item_idx = item_idx
        self.level = level
        self.children = []
        self.parent = None
        self.demand = demand
        rate = getAttribute(item_idx, 'rate')
        self.biproduct = None

        biproduct_name = getAttribute(item_idx, 'biproduct')
        if biproduct_name is not None:
            self.biproduct = biproduct_name
            self.bi_ratio = getAttribute(item_idx, 'bi_rate') / rate

        # recursively add children
        for i in range(4):
            resource = getAttribute(item_idx, 'resource'+str(i))
            if resource is None:
                break
            else:
                child_idx = getIndex(resource)
                consumption_rate = getAttribute(item_idx, 'demand'+str(i))
                child_demand = demand * consumption_rate / rate
                if child_idx in basic_resources:
                    newChild = TreeNode(child_idx, child_demand, -1)
                else:
                    newChild = TreeNode(child_idx, child_demand, level+1)
                newChild.parent = self
                self.children.append(newChild)

    # append all TreeNodes into NodeList
    def getNodeList(self, NodeList):
        NodeList.append(self)
        if len(self.children) > 0:
            for child in self.children:
                child.getNodeList(NodeList)

# shown in the middle
class DisplayWidget(qtw.QFrame):
    def __init__(self, parent, item_idx, demand):
        super(DisplayWidget, self).__init__(parent)
        self.setSizePolicy(qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Minimum)
        self.setStyleSheet(
            "background-color:black; border: 1px solid black;")
        self.item_idx = item_idx
        self.demand = demand
        biproduct = getAttribute(item_idx, 'biproduct')
        grid = qtw.QGridLayout()
        grid.setSpacing(1)
        grid.setContentsMargins(1,1,1,1)

        # pixmap onto label
        building_bmp = getAttribute(item_idx, 'building') + '.bmp'
        building_pixmap = QtGui.QPixmap(os.path.join('images', building_bmp))
        img_building = self.addLabel(grid, 0)
        img_building.setPixmap(building_pixmap)
        img_building.setScaledContents(True)

        item_bmp = getAttribute(item_idx, 'name') + '.bmp'
        item_pixmap = QtGui.QPixmap(os.path.join('images', item_bmp))
        img_item = self.addLabel(grid, 1)
        img_item.setPixmap(item_pixmap)
        img_item.setScaledContents(True)

        # line edit under label
        self.line_building = self.addLine(grid, 0)
        self.line_item = self.addLine(grid, 1)

        if biproduct is not None:
            bi_pixmap = QtGui.QPixmap(os.path.join('images', biproduct))
            img_bi = self.addLabel(grid, 2, True)
            img_bi.setPixmap(bi_pixmap)
            img_bi.setScaledContents(True)

            self.line_bi = self.addLine(grid, 2)

        self.setLayout(grid)

    # create label and add to grid
    def addLabel(self, grid, pos, isBiproduct=False):
        label = qtw.QLabel()
        label.setFixedHeight(80)
        label.setFixedWidth(80)
        if isBiproduct:
            label.setStyleSheet("background-color:#9873ac;")
        else:
            label.setStyleSheet("background-color:#fa9549;")
        grid.addWidget(label, 0, pos)
        return label

    # create line edit and add to grid
    def addLine(self, grid, pos):
        line = qtw.QLineEdit()
        line.setFixedHeight(24)
        line.setFixedWidth(80)
        line.setReadOnly(True)
        f = line.font()
        f.setPointSize(12)
        line.setFont(f)
        line.setText('0')
        line.setStyleSheet('background-color:white; color:black;')
        grid.addWidget(line, 1, pos)
        return line

    # update production values based on target input
    def update(self, target):

        # round value and setText
        def setLineText(value, lineEdit):
            value = round(value, 2)
            if len(str(value)) > 8:
                value = 'A LOT'
            elif value.is_integer():
                value = int(value)
            lineEdit.setText(str(value))

        demand_target = self.demand * target
        rate = getAttribute(self.item_idx, 'rate')
        if hasattr(self, 'line_bi'):
            bi_rate = getAttribute(self.item_idx, 'bi_rate')
            bi_ratio = bi_rate / rate
            bi_target = bi_ratio * demand_target
            setLineText(bi_target, self.line_bi)
        setLineText(demand_target/rate, self.line_building)
        setLineText(demand_target, self.line_item)

# basic resources (shown left)
class ResourceWidget(qtw.QWidget):
    def __init__(self, parent, item_idx, demand):        
        super(ResourceWidget, self).__init__(parent)
        self.item_idx = item_idx
        self.demand = demand
        item_name = getAttribute(item_idx, 'name')
        item_name = item_name.replace('_', ' ')

        # add widgets to horizontal box layout
        HBox = qtw.QHBoxLayout()
        HBox.addWidget(self.addLabel(item_name+':'))
        HBox.addStretch()
        self.resource_target = self.addLineEdit()
        HBox.addWidget(self.resource_target)
        HBox.addWidget(self.addLabel('/min', 12))
        self.setLayout(HBox)

    # create label
    def addLabel(self, text, size=16):
        label = qtw.QLabel()
        label.setText(text)
        label.setFixedHeight(30)
        label.setStyleSheet('color: #fa9549;')
        f = label.font()
        f.setPointSize(size)
        f.setBold(True)
        label.setFont(f)
        label.adjustSize()
        return label

    # create line edit
    def addLineEdit(self):
        line = qtw.QLineEdit()
        line.setText(str(round(self.demand, 2)))
        line.setFixedHeight(30)
        line.setFixedWidth(80)
        line.setStyleSheet('background-color: white;')
        f = line.font()
        f.setPointSize(12)
        line.setFont(f)
        line.setReadOnly(True)
        line.setAlignment(QtCore.Qt.AlignRight)
        return line

    # update basic resources
    def update(self, target):
        demand_target = self.demand*target
        demand_target = round(demand_target, 2)
        if len(str(demand_target)) > 8:
            demand_target = 'A LOT'
        elif demand_target.is_integer():
            demand_target = int(demand_target)
        self.resource_target.setText(str(demand_target))


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    sys.exit(app.exec_())