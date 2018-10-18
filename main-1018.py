import sys
import os
import vtk
import re
import math
from vtk.util.misc import vtkGetDataRoot
VTK_DATA_ROOT=vtkGetDataRoot()
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication,\
    QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, QApplication, QMainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MouseInteractorHighLightActor(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)
        self.AddObserver("CharEvent",self.OnCharEvent)
        self.LastPickedActor = None
        self.LastPickedProperty = vtk.vtkProperty()

    def OnCharEvent(self,obj,event):
        pass

    def leftButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()

        picker = vtk.vtkPropPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.GetDefaultRenderer())

        self.NewPickedActor = picker.GetActor()

        if self.NewPickedActor:
            if self.LastPickedActor:
                self.LastPickedActor.GetProperty().DeepCopy(self.LastPickedProperty)

            self.LastPickedProperty.DeepCopy(self.NewPickedActor.GetProperty())
            self.NewPickedActor.GetProperty().SetDiffuse(1.0)
            self.NewPickedActor.GetProperty().SetSpecular(0.0)
            self.NewPickedActor.GetProperty().SetOpacity(0.2)
            self.NewPickedActor.GetProperty().SetRepresentationToWireframe()
            self.NewPickedActor.GetProperty().SetColor(1,0,0)

            self.LastPickedActor = self.NewPickedActor

        self.OnLeftButtonDown()
        return

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 660)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.gridlayout = QtWidgets.QGridLayout(self.centralWidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menu_3)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menu_6)
        self.menu_7.setObjectName("menu_7")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionD = QtWidgets.QAction(MainWindow)
        self.actionD.setObjectName("actionD")
        self.action_1 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/1.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_1.setIcon(icon1)
        self.action_1.setObjectName("action_1")
        self.action_4 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/2.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_4.setIcon(icon2)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/3.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_5.setIcon(icon3)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon/4.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_6.setIcon(icon4)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon/5.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_7.setIcon(icon5)
        self.action_7.setObjectName("action_7")
        self.actionScale1 = QtWidgets.QAction(MainWindow)
        self.actionScale1.setObjectName("actionScale1")
        self.actionScale2 = QtWidgets.QAction(MainWindow)
        self.actionScale2.setObjectName("actionScale2")
        self.actionScale4 = QtWidgets.QAction(MainWindow)
        self.actionScale4.setObjectName("actionScale4")
        self.actionScale8 = QtWidgets.QAction(MainWindow)
        self.actionScale8.setObjectName("actionScale8")
        self.actionScale16 = QtWidgets.QAction(MainWindow)
        self.actionScale16.setObjectName("actionScale16")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action14 = QtWidgets.QAction(MainWindow)
        self.action14.setObjectName("action14")
        self.action15 = QtWidgets.QAction(MainWindow)
        self.action15.setObjectName("action15")
        self.action16 = QtWidgets.QAction(MainWindow)
        self.action16.setObjectName("action16")
        self.action17 = QtWidgets.QAction(MainWindow)
        self.action17.setObjectName("action17")
        self.action21 = QtWidgets.QAction(MainWindow)
        self.action21.setObjectName("action21")
        self.action22 = QtWidgets.QAction(MainWindow)
        self.action22.setObjectName("action22")
        self.action23 = QtWidgets.QAction(MainWindow)
        self.action23.setObjectName("action23")
        self.action25 = QtWidgets.QAction(MainWindow)
        self.action25.setObjectName("action25")
        self.action26 = QtWidgets.QAction(MainWindow)
        self.action26.setObjectName("action26")
        self.action27 = QtWidgets.QAction(MainWindow)
        self.action27.setObjectName("action27")
        self.action31 = QtWidgets.QAction(MainWindow)
        self.action31.setObjectName("action31")
        self.action32 = QtWidgets.QAction(MainWindow)
        self.action32.setObjectName("action32")
        self.action33 = QtWidgets.QAction(MainWindow)
        self.action33.setObjectName("action33")
        self.action34 = QtWidgets.QAction(MainWindow)
        self.action34.setObjectName("action34")
        self.action35 = QtWidgets.QAction(MainWindow)
        self.action35.setObjectName("action35")
        self.action36 = QtWidgets.QAction(MainWindow)
        self.action36.setObjectName("action36")
        self.action37 = QtWidgets.QAction(MainWindow)
        self.action37.setObjectName("action37")
        self.action41 = QtWidgets.QAction(MainWindow)
        self.action41.setObjectName("action41")
        self.action42 = QtWidgets.QAction(MainWindow)
        self.action42.setObjectName("action42")
        self.action43 = QtWidgets.QAction(MainWindow)
        self.action43.setObjectName("action43")
        self.action44 = QtWidgets.QAction(MainWindow)
        self.action44.setObjectName("action44")
        self.action45 = QtWidgets.QAction(MainWindow)
        self.action45.setObjectName("action45")
        self.action46 = QtWidgets.QAction(MainWindow)
        self.action46.setObjectName("action46")
        self.action47 = QtWidgets.QAction(MainWindow)
        self.action47.setObjectName("action47")
        self.action48 = QtWidgets.QAction(MainWindow)
        self.action48.setObjectName("action48")
        self.action49 = QtWidgets.QAction(MainWindow)
        self.action49.setObjectName("action49")
        self.action50 = QtWidgets.QAction(MainWindow)
        self.action50.setObjectName("action50")

        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.actionD)
        self.menu.addAction(self.action)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu_1.addAction(self.action_1)
        self.menu_1.addAction(self.action_4)
        self.menu_1.addAction(self.action_5)
        self.menu_1.addAction(self.action_6)
        self.menu_1.addAction(self.action_7)
        self.menu_4.addAction(self.actionScale1)
        self.menu_4.addAction(self.actionScale2)
        self.menu_4.addAction(self.actionScale4)
        self.menu_4.addAction(self.actionScale8)
        self.menu_4.addAction(self.actionScale16)
        self.menu_5.addAction(self.action_11)
        self.menu_5.addAction(self.action_12)
        self.menu_5.addAction(self.action_13)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.menu_5.menuAction())
        self.menu_7.addAction(self.action11)
        self.menu_7.addAction(self.action12)
        self.menu_7.addAction(self.action1)
        self.menu_7.addAction(self.action14)
        self.menu_7.addAction(self.action15)
        self.menu_7.addAction(self.action16)
        self.menu_7.addAction(self.action17)
        self.menu_7.addAction(self.action21)
        self.menu_7.addAction(self.action22)
        self.menu_7.addAction(self.action50)
        self.menu_7.addAction(self.action23)
        self.menu_7.addAction(self.action25)
        self.menu_7.addAction(self.action26)
        self.menu_7.addAction(self.action27)
        self.menu_7.addAction(self.action31)
        self.menu_7.addAction(self.action32)
        self.menu_7.addAction(self.action33)
        self.menu_7.addAction(self.action34)
        self.menu_7.addAction(self.action35)
        self.menu_7.addAction(self.action36)
        self.menu_7.addAction(self.action37)
        self.menu_7.addAction(self.action41)
        self.menu_7.addAction(self.action42)
        self.menu_7.addAction(self.action43)
        self.menu_7.addAction(self.action44)
        self.menu_7.addAction(self.action45)
        self.menu_7.addAction(self.action46)
        self.menu_7.addAction(self.action47)
        self.menu_3.addAction(self.action48)
        self.menu_3.addAction(self.action49)
        self.menu_6.addAction(self.action_14)
        self.menu_6.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_1)
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_5)
        self.toolBar.addAction(self.action_6)
        self.toolBar.addAction(self.action_7)
        self.toolBar.addAction(self.action_11)
        self.toolBar.addAction(self.action_12)
        self.toolBar.addAction(self.action_13)
        self.toolBar.addAction(self.action11)
        self.toolBar.addAction(self.action12)
        self.toolBar.addAction(self.action1)
        self.toolBar.addAction(self.action14)
        self.toolBar.addAction(self.action15)
        self.toolBar.addAction(self.action16)
        self.toolBar.addAction(self.action17)
        self.toolBar.addAction(self.action21)
        self.toolBar.addAction(self.action22)
        self.toolBar.addAction(self.action50)
        self.toolBar.addAction(self.action23)
        self.toolBar.addAction(self.action25)
        self.toolBar.addAction(self.action26)
        self.toolBar.addAction(self.action27)
        self.toolBar.addAction(self.action31)
        self.toolBar.addAction(self.action32)
        self.toolBar.addAction(self.action33)
        self.toolBar.addAction(self.action34)
        self.toolBar.addAction(self.action35)
        self.toolBar.addAction(self.action36)
        self.toolBar.addAction(self.action37)
        self.toolBar.addAction(self.action41)
        self.toolBar.addAction(self.action42)
        self.toolBar.addAction(self.action43)
        self.toolBar.addAction(self.action44)
        self.toolBar.addAction(self.action45)
        self.toolBar.addAction(self.action46)
        self.toolBar.addAction(self.action47)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tooth Visualization"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "导出"))
        self.menu_1.setTitle(_translate("MainWindow", "视图"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.menu_4.setTitle(_translate("MainWindow", "牙齿移动"))
        self.menu_5.setTitle(_translate("MainWindow", "牙颌显示"))
        self.menu_6.setTitle(_translate("MainWindow", "力值"))
        self.menu_7.setTitle(_translate("MainWindow", "牙位"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.action_3.setText(_translate("MainWindow", "图片"))
        self.actionD.setText(_translate("MainWindow", "动画"))
        self.action_1.setText(_translate("MainWindow", "视图1"))
        self.action_4.setText(_translate("MainWindow", "视图2"))
        self.action_5.setText(_translate("MainWindow", "视图3"))
        self.action_6.setText(_translate("MainWindow", "视图4"))
        self.action_7.setText(_translate("MainWindow", "视图5"))
        self.actionScale1.setText(_translate("MainWindow", "scale1"))
        self.actionScale2.setText(_translate("MainWindow", "scale2"))
        self.actionScale4.setText(_translate("MainWindow", "scale4"))
        self.actionScale8.setText(_translate("MainWindow", "scale8"))
        self.actionScale16.setText(_translate("MainWindow", "scale16"))
        self.action_11.setText(_translate("MainWindow", "上下颌"))
        self.action_12.setText(_translate("MainWindow", "上颌"))
        self.action_13.setText(_translate("MainWindow", "下颌"))
        self.action_14.setText(_translate("MainWindow", "整体"))
        self.action11.setText(_translate("MainWindow", "11"))
        self.action12.setText(_translate("MainWindow", "12"))
        self.action1.setText(_translate("MainWindow", "13"))
        self.action14.setText(_translate("MainWindow", "14"))
        self.action15.setText(_translate("MainWindow", "15"))
        self.action16.setText(_translate("MainWindow", "16"))
        self.action17.setText(_translate("MainWindow", "17"))
        self.action21.setText(_translate("MainWindow", "21"))
        self.action22.setText(_translate("MainWindow", "22"))
        self.action50.setText(_translate("MainWindow", "23"))
        self.action23.setText(_translate("MainWindow", "24"))
        self.action25.setText(_translate("MainWindow", "25"))
        self.action26.setText(_translate("MainWindow", "26"))
        self.action27.setText(_translate("MainWindow", "27"))
        self.action31.setText(_translate("MainWindow", "31"))
        self.action32.setText(_translate("MainWindow", "32"))
        self.action33.setText(_translate("MainWindow", "33"))
        self.action34.setText(_translate("MainWindow", "34"))
        self.action35.setText(_translate("MainWindow", "35"))
        self.action36.setText(_translate("MainWindow", "36"))
        self.action37.setText(_translate("MainWindow", "37"))
        self.action41.setText(_translate("MainWindow", "41"))
        self.action42.setText(_translate("MainWindow", "42"))
        self.action43.setText(_translate("MainWindow", "43"))
        self.action44.setText(_translate("MainWindow", "44"))
        self.action45.setText(_translate("MainWindow", "45"))
        self.action46.setText(_translate("MainWindow", "46"))
        self.action47.setText(_translate("MainWindow", "47"))
        self.action48.setText(_translate("MainWindow", "上颌牙位"))
        self.action49.setText(_translate("MainWindow", "下颌牙位"))

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ren = vtk.vtkRenderer()
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()
        self.InitialWindow()
        self.show()

        self.ui.action.triggered.connect(self.openFile)
        self.ui.action_3.triggered.connect(self.exportpicture)
        self.ui.actionD.triggered.connect(self.exportmovie)
        self.ui.action_1.triggered.connect(self.view1)
        self.ui.action_4.triggered.connect(self.view2)
        self.ui.action_5.triggered.connect(self.view3)
        self.ui.action_6.triggered.connect(self.view4)
        self.ui.action_7.triggered.connect(self.view5)
        
        self.ui.actionScale1.triggered.connect(self.scale1)
        self.ui.actionScale2.triggered.connect(self.scale2)
        self.ui.actionScale4.triggered.connect(self.scale4)
        self.ui.actionScale8.triggered.connect(self.scale8)
        self.ui.actionScale16.triggered.connect(self.scale16)
        self.ui.action_11.triggered.connect(self.shangxiahe)
        self.ui.action_12.triggered.connect(self.shanghe)
        self.ui.action_13.triggered.connect(self.xiahe)
        self.ui.action_14.triggered.connect(self.zhengti)
        self.ui.action11.triggered.connect(self.danya11)
        self.ui.action12.triggered.connect(self.danya12)
        self.ui.action1.triggered.connect(self.danya13)
        self.ui.action14.triggered.connect(self.danya14)
        self.ui.action15.triggered.connect(self.danya15)
        self.ui.action16.triggered.connect(self.danya16)
        self.ui.action17.triggered.connect(self.danya17)
        self.ui.action21.triggered.connect(self.danya21)
        self.ui.action22.triggered.connect(self.danya22)
        self.ui.action50.triggered.connect(self.danya23)
        self.ui.action23.triggered.connect(self.danya24)
        self.ui.action25.triggered.connect(self.danya25)
        self.ui.action26.triggered.connect(self.danya26)
        self.ui.action27.triggered.connect(self.danya27)
        self.ui.action31.triggered.connect(self.danya31)
        self.ui.action32.triggered.connect(self.danya32)
        self.ui.action33.triggered.connect(self.danya33)
        self.ui.action34.triggered.connect(self.danya34)
        self.ui.action35.triggered.connect(self.danya35)
        self.ui.action36.triggered.connect(self.danya36)
        self.ui.action37.triggered.connect(self.danya37)
        self.ui.action41.triggered.connect(self.danya41)
        self.ui.action42.triggered.connect(self.danya42)
        self.ui.action43.triggered.connect(self.danya43)
        self.ui.action44.triggered.connect(self.danya44)
        self.ui.action45.triggered.connect(self.danya45)
        self.ui.action46.triggered.connect(self.danya46)
        self.ui.action47.triggered.connect(self.danya47)
        self.ui.action48.triggered.connect(self.shangyawei)
        self.ui.action49.triggered.connect(self.xiayawei)

    def openFile(self):
        self.ren.RemoveAllViewProps()
        pathfile = QFileDialog.getExistingDirectory(self,"请选择文件夹","\\")
        actor = list()
        dirs = os.listdir(pathfile)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (270)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def exportpicture(self):
        pass

    def exportmovie(self):
        pass

    def shangxiahe(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (270)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def shanghe(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()   
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()


    def xiahe(self):        
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        if os.path.isfile("gumx.stl"):
            if os.path.isfile("gums.stl"):
                actorgs = actorgum[0]
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for i in actorxia:
                    self.ren.AddActor(i)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for i in actorxia:
                    self.ren.AddActor(i)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(-90)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (270)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()       
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()


    def InitialWindow(self):
        self.ren.RemoveAllViewProps()
        camera = vtk.vtkCamera()
        camera.Elevation (270)
        camera.OrthogonalizeViewUp ()
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def view1(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (360)
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def view2(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (270)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def view3(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (90)
        camera.OrthogonalizeViewUp ()
        camera.Azimuth(270)
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def view4(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (-130)
        camera.Elevation (90)
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def view5(self):
        self.ren.RemoveAllViewProps()
        actor = list()
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actor.append(stlactor)
        camera = vtk.vtkCamera()
        camera.Elevation (90)
        camera.OrthogonalizeViewUp ()
        camera.OrthogonalizeViewUp ()
        for i in actor:
            self.ren.AddActor(i)
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def shangyawei(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            actor2=[]
            t=(1,1,1)
            i=0
            while i < len(ids):
                text=vtk.vtkVectorText()
                text.SetText(ids[i])
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(float(o1s[i])-0.8*t[0],float(o2s[i])-0.1*t[0], float(o3s[i])+8*t[0])
                textActor.SetScale(t)
                actor2.append(textActor)
                i+=1
            for i in actor2:
                self.ren.AddActor(i)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)

        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()

    def xiayawei(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1

        if os.path.isfile("gumx.stl"):
            if os.path.isfile("gums.stl"):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for i in actorxia:
                    self.ren.AddActor(i)
                actor2=[]
                t=(1,1,1)
                i=0
                while i < len(idx):
                    text=vtk.vtkVectorText()
                    text.SetText(idx[i])
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(float(o1x[i])-0.8*t[0],float(o2x[i])-0.1*t[0], float(o3x[i])-8*t[0])
                    textActor.SetScale(t)
                    textActor.RotateX(180)
                    actor2.append(textActor)
                    i+=1
                for i in actor2:
                    self.ren.AddActor(i)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for i in actorxia:
                    self.ren.AddActor(i)
                actor2=[]
                t=(1,1,1)
                i=0
                while i < len(idx):
                    text=vtk.vtkVectorText()
                    text.SetText(idx[i])
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(float(o1x[i])-0.8*t[0],float(o2x[i])-0.1*t[0], float(o3x[i])-8*t[0])
                    textActor.SetScale(t)
                    textActor.RotateX(180)
                    actor2.append(textActor)
                    i+=1
                for i in actor2:
                    self.ren.AddActor(i)
            
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(180)
            textActor.RotateY(0)
            self.ren.AddActor(textActor)

        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.OrthogonalizeViewUp ()
        camera.Azimuth(360)    
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        self.ren.ResetCamera()
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.iren.Initialize()
		
    def scale1(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        Fhs,Fhx,Mhs,Mhx = [],[],[],[]
        for a,b,c in zip(fxs,fys,fzs):
            Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(fxx,fyx,fzx):
            Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxs,mys,mzs):
            Mhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxx,myx,mzx):
            Mhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))

        actorgum1 = []
        actorshang1 = []
        actorxia1 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum1.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang1.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia1.append(stlactor)

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorshang1):
                actorshang1[i].GetProperty().SetOpacity(0.5)
                actorshang1[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                if Fhs[i]<0.5:
                    transform.Translate(0,0,0)
                elif Fhs[i]>0.5 and Fhs[i]<=6:
                    transform.Translate(0.05*float(fxs[i]),0.05*float(fys[i]), 0.05*float(fzs[i]))
                elif Fhs[i]>6 and Fhs[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                else:
                    transform.Translate(0,0,0)
                if Mhs[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                elif Mhs[i]>0.05 and Mhs[i]<=0.6:
                    transform.RotateX(0.05*mxs[i])
                    transform.RotateY(0.05*mys[i])
                    transform.RotateZ(0.05*mzs[i])
                elif Mhs[i]>0.6 and Mhs[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                actorshang1[i].SetUserTransform(transform)
                i+=1
            for k in actorshang1:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            for i in actorxia:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorxia1):
                actorxia1[i].GetProperty().SetOpacity(0.5)
                actorxia1[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                if Fhx[i]<0.5:
                    transform.Translate(0,0,0)
                elif Fhx[i]>0.5 and Fhx[i]<=6:
                    transform.Translate(0.05*float(fxx[i]),0.05*float(fyx[i]), 0.05*float(fzx[i]))
                elif Fhx[i]>6 and Fhx[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                else:
                    transform.Translate(0,0,0)
                if Mhx[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                elif Mhx[i]>0.05 and Mhx[i]<=0.6:
                    transform.RotateX(0.05*mxx[i])
                    transform.RotateY(0.05*myx[i])
                    transform.RotateZ(0.05*mzx[i])
                elif Mhx[i]>0.6 and Mhx[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                actorxia1[i].SetUserTransform(transform)
                i+=1
            for k in actorxia1:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def scale2(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        Fhs,Fhx,Mhs,Mhx = [],[],[],[]
        for a,b,c in zip(fxs,fys,fzs):
            Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(fxx,fyx,fzx):
            Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxs,mys,mzs):
            Mhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxx,myx,mzx):
            Mhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))

        actorgum1 = []
        actorshang1 = []
        actorxia1 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum1.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang1.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia1.append(stlactor)

        actorgum2 = []
        actorshang2 = []
        actorxia2 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum2.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang2.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia2.append(stlactor)

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorshang1):
                actorshang1[i].GetProperty().SetOpacity(0.5)
                actorshang1[i].GetProperty().SetColor(0,0,1)
                actorshang2[i].GetProperty().SetOpacity(0.5)
                actorshang2[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                if Fhs[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                elif Fhs[i]>0.5 and Fhs[i]<=6:
                    transform.Translate(0.05*float(fxs[i]),0.05*float(fys[i]), 0.05*float(fzs[i]))
                    transform2.Translate(2*0.05*float(fxs[i]),2*0.05*float(fys[i]), 2*0.05*float(fzs[i]))
                elif Fhs[i]>6 and Fhs[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3, 2*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                if Mhs[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                elif Mhs[i]>0.05 and Mhs[i]<=0.6:
                    transform.RotateX(0.05*mxs[i])
                    transform.RotateY(0.05*mys[i])
                    transform.RotateZ(0.05*mzs[i])
                    transform2.RotateX(0.05*mxs[i])
                    transform2.RotateY(0.05*mys[i])
                    transform2.RotateZ(0.05*mzs[i])
                elif Mhs[i]>0.6 and Mhs[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                actorshang1[i].SetUserTransform(transform)
                actorshang2[i].SetUserTransform(transform2)
                i+=1
            for k in actorshang1:
                self.ren.AddActor(k)
            for k in actorshang2:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            for i in actorxia:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorxia1):
                actorxia1[i].GetProperty().SetOpacity(0.5)
                actorxia1[i].GetProperty().SetColor(0,0,1)
                actorxia2[i].GetProperty().SetOpacity(0.5)
                actorxia2[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                if Fhx[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                elif Fhx[i]>0.5 and Fhx[i]<=6:
                    transform.Translate(0.05*float(fxx[i]),0.05*float(fyx[i]), 0.05*float(fzx[i]))
                    transform2.Translate(2*0.05*float(fxx[i]),2*0.05*float(fyx[i]), 2*0.05*float(fzx[i]))
                elif Fhx[i]>6 and Fhx[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3,2*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                if Mhx[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                elif Mhx[i]>0.05 and Mhx[i]<=0.6:
                    transform.RotateX(0.05*mx[i])
                    transform.RotateY(0.05*my[i])
                    transform.RotateZ(0.05*mz[i])
                    transform2.RotateX(0.05*mx[i])
                    transform2.RotateY(0.05*my[i])
                    transform2.RotateZ(0.05*mz[i])
                elif Mhx[i]>0.6 and Mhx[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                actorxia1[i].SetUserTransform(transform)
                actorxia2[i].SetUserTransform(transform2)
                i+=1
            for k in actorxia1:
                self.ren.AddActor(k)
            for k in actorxia2:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def scale4(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        Fhs,Fhx,Mhs,Mhx = [],[],[],[]
        for a,b,c in zip(fxs,fys,fzs):
            Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(fxx,fyx,fzx):
            Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxs,mys,mzs):
            Mhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxx,myx,mzx):
            Mhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))

        actorgum1 = []
        actorshang1 = []
        actorxia1 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum1.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang1.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia1.append(stlactor)

        actorgum2 = []
        actorshang2 = []
        actorxia2 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum2.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang2.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia2.append(stlactor)

        actorgum3 = []
        actorshang3 = []
        actorxia3 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum3.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang3.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia3.append(stlactor)

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorshang1):
                actorshang1[i].GetProperty().SetOpacity(0.5)
                actorshang1[i].GetProperty().SetColor(0,0,1)
                actorshang2[i].GetProperty().SetOpacity(0.5)
                actorshang2[i].GetProperty().SetColor(0,0,1)
                actorshang3[i].GetProperty().SetOpacity(0.5)
                actorshang3[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                if Fhs[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                elif Fhs[i]>0.5 and Fhs[i]<=6:
                    transform.Translate(0.05*float(fxs[i]),0.05*float(fys[i]), 0.05*float(fzs[i]))
                    transform2.Translate(2*0.05*float(fxs[i]),2*0.05*float(fys[i]), 2*0.05*float(fzs[i]))
                    transform3.Translate(4*0.05*float(fxs[i]),4*0.05*float(fys[i]), 4*0.05*float(fzs[i]))
                elif Fhs[i]>6 and Fhs[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3, 2*0.3)
                    transform3.Translate(4*0.3,4*0.3, 4*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                if Mhs[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                elif Mhs[i]>0.05 and Mhs[i]<=0.6:
                    transform.RotateX(0.05*mxs[i])
                    transform.RotateY(0.05*mys[i])
                    transform.RotateZ(0.05*mzs[i])
                    transform2.RotateX(0.05*mxs[i])
                    transform2.RotateY(0.05*mys[i])
                    transform2.RotateZ(0.05*mzs[i])
                    transform3.RotateX(0.05*mxs[i])
                    transform3.RotateY(0.05*mys[i])
                    transform3.RotateZ(0.05*mzs[i])
                elif Mhs[i]>0.6 and Mhs[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                actorshang1[i].SetUserTransform(transform)
                actorshang2[i].SetUserTransform(transform2)
                actorshang3[i].SetUserTransform(transform3)
                i+=1
            for k in actorshang1:
                self.ren.AddActor(k)
            for k in actorshang2:
                self.ren.AddActor(k)
            for k in actorshang3:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            for i in actorxia:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorxia1):
                actorxia1[i].GetProperty().SetOpacity(0.5)
                actorxia1[i].GetProperty().SetColor(0,0,1)
                actorxia2[i].GetProperty().SetOpacity(0.5)
                actorxia2[i].GetProperty().SetColor(0,0,1)
                actorxia3[i].GetProperty().SetOpacity(0.5)
                actorxia3[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                if Fhx[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                elif Fhx[i]>0.5 and Fhx[i]<=6:
                    transform.Translate(0.05*float(fxx[i]),0.05*float(fyx[i]), 0.05*float(fzx[i]))
                    transform2.Translate(2*0.05*float(fxx[i]),2*0.05*float(fyx[i]), 2*0.05*float(fzx[i]))
                    transform3.Translate(4*0.05*float(fxx[i]),4*0.05*float(fyx[i]), 4*0.05*float(fzx[i]))
                elif Fhx[i]>6 and Fhx[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3,2*0.3)
                    transform3.Translate(4*0.3,4*0.3,4*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                if Mhx[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                elif Mhx[i]>0.05 and Mhx[i]<=0.6:
                    transform.RotateX(0.05*mx[i])
                    transform.RotateY(0.05*my[i])
                    transform.RotateZ(0.05*mz[i])
                    transform2.RotateX(0.05*mx[i])
                    transform2.RotateY(0.05*my[i])
                    transform2.RotateZ(0.05*mz[i])
                    transform3.RotateX(0.05*mx[i])
                    transform3.RotateY(0.05*my[i])
                    transform3.RotateZ(0.05*mz[i])
                elif Mhx[i]>0.6 and Mhx[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                actorxia1[i].SetUserTransform(transform)
                actorxia2[i].SetUserTransform(transform2)
                actorxia3[i].SetUserTransform(transform3)
                i+=1
            for k in actorxia1:
                self.ren.AddActor(k)
            for k in actorxia2:
                self.ren.AddActor(k)
            for k in actorxia3:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def scale8(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        Fhs,Fhx,Mhs,Mhx = [],[],[],[]
        for a,b,c in zip(fxs,fys,fzs):
            Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(fxx,fyx,fzx):
            Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxs,mys,mzs):
            Mhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxx,myx,mzx):
            Mhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))

        actorgum1 = []
        actorshang1 = []
        actorxia1 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum1.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang1.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia1.append(stlactor)

        actorgum2 = []
        actorshang2 = []
        actorxia2 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum2.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang2.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia2.append(stlactor)

        actorgum3 = []
        actorshang3 = []
        actorxia3 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum3.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang3.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia3.append(stlactor)

        actorgum4 = []
        actorshang4 = []
        actorxia4 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum4.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang4.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia4.append(stlactor)

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorshang1):
                actorshang1[i].GetProperty().SetOpacity(0.5)
                actorshang1[i].GetProperty().SetColor(0,0,1)
                actorshang2[i].GetProperty().SetOpacity(0.5)
                actorshang2[i].GetProperty().SetColor(0,0,1)
                actorshang3[i].GetProperty().SetOpacity(0.5)
                actorshang3[i].GetProperty().SetColor(0,0,1)
                actorshang4[i].GetProperty().SetOpacity(0.5)
                actorshang4[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                transform4 = vtk.vtkTransform()
                if Fhs[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                elif Fhs[i]>0.5 and Fhs[i]<=6:
                    transform.Translate(0.05*float(fxs[i]),0.05*float(fys[i]), 0.05*float(fzs[i]))
                    transform2.Translate(2*0.05*float(fxs[i]),2*0.05*float(fys[i]), 2*0.05*float(fzs[i]))
                    transform3.Translate(4*0.05*float(fxs[i]),4*0.05*float(fys[i]), 4*0.05*float(fzs[i]))
                    transform4.Translate(8*0.05*float(fxs[i]),8*0.05*float(fys[i]), 8*0.05*float(fzs[i]))
                elif Fhs[i]>6 and Fhs[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3, 2*0.3)
                    transform3.Translate(4*0.3,4*0.3, 4*0.3)
                    transform4.Translate(8*0.3,8*0.3, 8*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                if Mhs[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                    transform4.RotateX(0)
                    transform4.RotateY(0)
                    transform4.RotateZ(0)
                elif Mhs[i]>0.05 and Mhs[i]<=0.6:
                    transform.RotateX(0.05*mxs[i])
                    transform.RotateY(0.05*mys[i])
                    transform.RotateZ(0.05*mzs[i])
                    transform2.RotateX(0.05*mxs[i])
                    transform2.RotateY(0.05*mys[i])
                    transform2.RotateZ(0.05*mzs[i])
                    transform3.RotateX(0.05*mxs[i])
                    transform3.RotateY(0.05*mys[i])
                    transform3.RotateZ(0.05*mzs[i])
                    transform4.RotateX(0.05*mxs[i])
                    transform4.RotateY(0.05*mys[i])
                    transform4.RotateZ(0.05*mzs[i])
                elif Mhs[i]>0.6 and Mhs[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                    transform4.RotateX(3)
                    transform4.RotateY(3)
                    transform4.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                actorshang1[i].SetUserTransform(transform)
                actorshang2[i].SetUserTransform(transform2)
                actorshang3[i].SetUserTransform(transform3)
                actorshang4[i].SetUserTransform(transform4)
                i+=1
            for k in actorshang1:
                self.ren.AddActor(k)
            for k in actorshang2:
                self.ren.AddActor(k)
            for k in actorshang3:
                self.ren.AddActor(k)
            for k in actorshang4:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            for i in actorxia:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorxia1):
                actorxia1[i].GetProperty().SetOpacity(0.5)
                actorxia1[i].GetProperty().SetColor(0,0,1)
                actorxia2[i].GetProperty().SetOpacity(0.5)
                actorxia2[i].GetProperty().SetColor(0,0,1)
                actorxia3[i].GetProperty().SetOpacity(0.5)
                actorxia3[i].GetProperty().SetColor(0,0,1)
                actorxia4[i].GetProperty().SetOpacity(0.5)
                actorxia4[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                transform4 = vtk.vtkTransform()
                if Fhx[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                elif Fhx[i]>0.5 and Fhx[i]<=6:
                    transform.Translate(0.05*float(fxx[i]),0.05*float(fyx[i]), 0.05*float(fzx[i]))
                    transform2.Translate(2*0.05*float(fxx[i]),2*0.05*float(fyx[i]), 2*0.05*float(fzx[i]))
                    transform3.Translate(4*0.05*float(fxx[i]),4*0.05*float(fyx[i]), 4*0.05*float(fzx[i]))
                    transform4.Translate(8*0.05*float(fxx[i]),8*0.05*float(fyx[i]), 8*0.05*float(fzx[i]))
                elif Fhx[i]>6 and Fhx[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3,2*0.3)
                    transform3.Translate(4*0.3,4*0.3,4*0.3)
                    transform4.Translate(8*0.3,8*0.3,8*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                if Mhx[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                    transform4.RotateX(0)
                    transform4.RotateY(0)
                    transform4.RotateZ(0)
                elif Mhx[i]>0.05 and Mhx[i]<=0.6:
                    transform.RotateX(0.05*mx[i])
                    transform.RotateY(0.05*my[i])
                    transform.RotateZ(0.05*mz[i])
                    transform2.RotateX(0.05*mx[i])
                    transform2.RotateY(0.05*my[i])
                    transform2.RotateZ(0.05*mz[i])
                    transform3.RotateX(0.05*mx[i])
                    transform3.RotateY(0.05*my[i])
                    transform3.RotateZ(0.05*mz[i])
                    transform4.RotateX(0.05*mx[i])
                    transform4.RotateY(0.05*my[i])
                    transform4.RotateZ(0.05*mz[i])
                elif Mhx[i]>0.6 and Mhx[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                    transform4.RotateX(3)
                    transform4.RotateY(3)
                    transform4.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                actorxia1[i].SetUserTransform(transform)
                actorxia2[i].SetUserTransform(transform2)
                actorxia3[i].SetUserTransform(transform3)
                actorxia4[i].SetUserTransform(transform4)
                i+=1
            for k in actorxia1:
                self.ren.AddActor(k)
            for k in actorxia2:
                self.ren.AddActor(k)
            for k in actorxia3:
                self.ren.AddActor(k)
            for k in actorxia4:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()
        
    def scale16(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        Fhs,Fhx,Mhs,Mhx = [],[],[],[]
        for a,b,c in zip(fxs,fys,fzs):
            Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(fxx,fyx,fzx):
            Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxs,mys,mzs):
            Mhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
        for a,b,c in zip(mxx,myx,mzx):
            Mhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))

        actorgum1 = []
        actorshang1 = []
        actorxia1 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum1.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang1.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia1.append(stlactor)

        actorgum2 = []
        actorshang2 = []
        actorxia2 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum2.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang2.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia2.append(stlactor)

        actorgum3 = []
        actorshang3 = []
        actorxia3 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum3.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang3.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia3.append(stlactor)

        actorgum4 = []
        actorshang4 = []
        actorxia4 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum4.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang4.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia4.append(stlactor)

        actorgum5 = []
        actorshang5 = []
        actorxia5 = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum5.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang5.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia5.append(stlactor)

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorshang1):
                actorshang1[i].GetProperty().SetOpacity(0.5)
                actorshang1[i].GetProperty().SetColor(0,0,1)
                actorshang2[i].GetProperty().SetOpacity(0.5)
                actorshang2[i].GetProperty().SetColor(0,0,1)
                actorshang3[i].GetProperty().SetOpacity(0.5)
                actorshang3[i].GetProperty().SetColor(0,0,1)
                actorshang4[i].GetProperty().SetOpacity(0.5)
                actorshang4[i].GetProperty().SetColor(0,0,1)
                actorshang5[i].GetProperty().SetOpacity(0.5)
                actorshang5[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                transform4 = vtk.vtkTransform()
                transform5 = vtk.vtkTransform()
                if Fhs[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                elif Fhs[i]>0.5 and Fhs[i]<=6:
                    transform.Translate(0.05*float(fxs[i]),0.05*float(fys[i]), 0.05*float(fzs[i]))
                    transform2.Translate(2*0.05*float(fxs[i]),2*0.05*float(fys[i]), 2*0.05*float(fzs[i]))
                    transform3.Translate(4*0.05*float(fxs[i]),4*0.05*float(fys[i]), 4*0.05*float(fzs[i]))
                    transform4.Translate(8*0.05*float(fxs[i]),8*0.05*float(fys[i]), 8*0.05*float(fzs[i]))
                    transform5.Translate(16*0.05*float(fxs[i]),16*0.05*float(fys[i]), 16*0.05*float(fzs[i]))
                elif Fhs[i]>6 and Fhs[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3, 2*0.3)
                    transform3.Translate(4*0.3,4*0.3, 4*0.3)
                    transform4.Translate(8*0.3,8*0.3, 8*0.3)
                    transform5.Translate(16*0.3,16*0.3, 16*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                if Mhs[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                    transform4.RotateX(0)
                    transform4.RotateY(0)
                    transform4.RotateZ(0)
                    transform5.RotateX(0)
                    transform5.RotateY(0)
                    transform5.RotateZ(0)
                elif Mhs[i]>0.05 and Mhs[i]<=0.6:
                    transform.RotateX(0.05*mxs[i])
                    transform.RotateY(0.05*mys[i])
                    transform.RotateZ(0.05*mzs[i])
                    transform2.RotateX(0.05*mxs[i])
                    transform2.RotateY(0.05*mys[i])
                    transform2.RotateZ(0.05*mzs[i])
                    transform3.RotateX(0.05*mxs[i])
                    transform3.RotateY(0.05*mys[i])
                    transform3.RotateZ(0.05*mzs[i])
                    transform4.RotateX(0.05*mxs[i])
                    transform4.RotateY(0.05*mys[i])
                    transform4.RotateZ(0.05*mzs[i])
                    transform5.RotateX(0.05*mxs[i])
                    transform5.RotateY(0.05*mys[i])
                    transform5.RotateZ(0.05*mzs[i])
                elif Mhs[i]>0.6 and Mhs[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                    transform4.RotateX(3)
                    transform4.RotateY(3)
                    transform4.RotateZ(3)
                    transform5.RotateX(3)
                    transform5.RotateY(3)
                    transform5.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                actorshang1[i].SetUserTransform(transform)
                actorshang2[i].SetUserTransform(transform2)
                actorshang3[i].SetUserTransform(transform3)
                actorshang4[i].SetUserTransform(transform4)
                actorshang5[i].SetUserTransform(transform5)
                i+=1
            for k in actorshang1:
                self.ren.AddActor(k)
            for k in actorshang2:
                self.ren.AddActor(k)
            for k in actorshang3:
                self.ren.AddActor(k)
            for k in actorshang4:
                self.ren.AddActor(k)
            for k in actorshang5:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            for i in actorxia:
                self.ren.AddActor(i)            
            i=0
            while i < len(actorxia1):
                actorxia1[i].GetProperty().SetOpacity(0.5)
                actorxia1[i].GetProperty().SetColor(0,0,1)
                actorxia2[i].GetProperty().SetOpacity(0.5)
                actorxia2[i].GetProperty().SetColor(0,0,1)
                actorxia3[i].GetProperty().SetOpacity(0.5)
                actorxia3[i].GetProperty().SetColor(0,0,1)
                actorxia4[i].GetProperty().SetOpacity(0.5)
                actorxia4[i].GetProperty().SetColor(0,0,1)
                actorxia5[i].GetProperty().SetOpacity(0.5)
                actorxia5[i].GetProperty().SetColor(0,0,1)
                transform = vtk.vtkTransform()
                transform2 = vtk.vtkTransform()
                transform3 = vtk.vtkTransform()
                transform4 = vtk.vtkTransform()
                transform5 = vtk.vtkTransform()
                if Fhx[i]<0.5:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                elif Fhx[i]>0.5 and Fhx[i]<=6:
                    transform.Translate(0.05*float(fxx[i]),0.05*float(fyx[i]), 0.05*float(fzx[i]))
                    transform2.Translate(2*0.05*float(fxx[i]),2*0.05*float(fyx[i]), 2*0.05*float(fzx[i]))
                    transform3.Translate(4*0.05*float(fxx[i]),4*0.05*float(fyx[i]), 4*0.05*float(fzx[i]))
                    transform4.Translate(8*0.05*float(fxx[i]),8*0.05*float(fyx[i]), 8*0.05*float(fzx[i]))
                    transform5.Translate(16*0.05*float(fxx[i]),16*0.05*float(fyx[i]), 16*0.05*float(fzx[i]))
                elif Fhx[i]>6 and Fhx[i]<=10:
                    transform.Translate(0.3,0.3, 0.3)
                    transform2.Translate(2*0.3,2*0.3,2*0.3)
                    transform3.Translate(4*0.3,4*0.3,4*0.3)
                    transform4.Translate(8*0.3,8*0.3,8*0.3)
                    transform5.Translate(16*0.3,16*0.3,16*0.3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                if Mhx[i]<0.05:
                    transform.RotateX(0)
                    transform.RotateY(0)
                    transform.RotateZ(0)
                    transform2.RotateX(0)
                    transform2.RotateY(0)
                    transform2.RotateZ(0)
                    transform3.RotateX(0)
                    transform3.RotateY(0)
                    transform3.RotateZ(0)
                    transform4.RotateX(0)
                    transform4.RotateY(0)
                    transform4.RotateZ(0)
                    transform5.RotateX(0)
                    transform5.RotateY(0)
                    transform5.RotateZ(0)
                elif Mhx[i]>0.05 and Mhx[i]<=0.6:
                    transform.RotateX(0.05*mx[i])
                    transform.RotateY(0.05*my[i])
                    transform.RotateZ(0.05*mz[i])
                    transform2.RotateX(0.05*mx[i])
                    transform2.RotateY(0.05*my[i])
                    transform2.RotateZ(0.05*mz[i])
                    transform3.RotateX(0.05*mx[i])
                    transform3.RotateY(0.05*my[i])
                    transform3.RotateZ(0.05*mz[i])
                    transform4.RotateX(0.05*mx[i])
                    transform4.RotateY(0.05*my[i])
                    transform4.RotateZ(0.05*mz[i])
                    transform5.RotateX(0.05*mx[i])
                    transform5.RotateY(0.05*my[i])
                    transform5.RotateZ(0.05*mz[i])
                elif Mhx[i]>0.6 and Mhx[i]<=1:
                    transform.RotateX(3)
                    transform.RotateY(3)
                    transform.RotateZ(3)
                    transform2.RotateX(3)
                    transform2.RotateY(3)
                    transform2.RotateZ(3)
                    transform3.RotateX(3)
                    transform3.RotateY(3)
                    transform3.RotateZ(3)
                    transform4.RotateX(3)
                    transform4.RotateY(3)
                    transform4.RotateZ(3)
                    transform5.RotateX(3)
                    transform5.RotateY(3)
                    transform5.RotateZ(3)
                else:
                    transform.Translate(0,0,0)
                    transform2.Translate(0,0,0)
                    transform3.Translate(0,0,0)
                    transform4.Translate(0,0,0)
                    transform5.Translate(0,0,0)
                actorxia1[i].SetUserTransform(transform)
                actorxia2[i].SetUserTransform(transform2)
                actorxia3[i].SetUserTransform(transform3)
                actorxia4[i].SetUserTransform(transform4)
                actorxia5[i].SetUserTransform(transform5)
                i+=1
            for k in actorxia1:
                self.ren.AddActor(k)
            for k in actorxia2:
                self.ren.AddActor(k)
            for k in actorxia3:
                self.ren.AddActor(k)
            for k in actorxia4:
                self.ren.AddActor(k)
            for k in actorxia5:
                self.ren.AddActor(k)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def zhengti(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)
                    
        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1

        idf,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idf.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idfs,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idfx,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idf):
            if int(idf[i]) < 31:
                idfs.append(idf[i])
                fxs.append(fx[i])
                fys.append(fy[i])
                fzs.append(fz[i])
                mxs.append(mx[i])
                mys.append(my[i])
                mzs.append(mz[i])
            else:
                idfx.append(idf[i])
                fxx.append(fx[i])
                fyx.append(fy[i])
                fzx.append(fz[i])
                mxx.append(mx[i])
                myx.append(my[i])
                mzx.append(mz[i])
            i+=1

        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            Fhs=[]
            for a,b,c in zip(fxs,fys,fzs):
                Fhs.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
            α=list()
            β=list()
            γ=list()
            for a,b,c,d in zip(fxs,fys,fzs,Fhs):
                α.append(math.acos(float(a)/float(d))*180/3.14159)
                β.append(math.acos(float(b)/float(d))*180/3.14159)
                γ.append(math.acos(float(c)/float(d))*180/3.14159)

            i=0
            while i < len(idfs):
                if Fhs[i]<=0.5:
                    actorshang[i].GetProperty().SetColor(0,0,1)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>0.5 and Fhs[i]<=1:
                    actorshang[i].GetProperty().SetColor(0,0.7,1)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>1 and Fhs[i]<=1.5:
                    actorshang[i].GetProperty().SetColor(0,1,1)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>1.5 and Fhs[i]<=2:
                    actorshang[i].GetProperty().SetColor(0,1,0.7)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>2 and Fhs[i]<=2.5:
                    actorshang[i].GetProperty().SetColor(0.12,1,0)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>2.5 and Fhs[i]<=3:
                    actorshang[i].GetProperty().SetColor(0.71,1,0)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>3 and Fhs[i]<=3.5:
                    actorshang[i].GetProperty().SetColor(1,1,0)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                elif Fhs[i]>3.5 and Fhs[i]<=4:
                    actorshang[i].GetProperty().SetColor(1,0.7,0)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                else:
                    actorshang[i].GetProperty().SetColor(1,0,0)
                    actorshang[i].GetProperty().SetOpacity(0.6)
                i+=1
            for k in actorshang:
                self.ren.AddActor(k)
            
            actor1 = []
            i=0
            while i < len(idfs):
                lineSource = vtk.vtkLineSource()
                lineSource.SetPoint1(float(o1s[i]), float(o2s[i]), float(o3s[i]))
                lineSource.SetPoint2(float(o1s[i])+float(fxs[i]*8), float(o2s[i])+float(fys[i])*8, float(o3s[i])+float(fzs[i])*8)

                coneSource = vtk.vtkConeSource()
                coneSource.SetCenter(float(o1s[i])+float(fxs[i]*8), float(o2s[i])+float(fys[i])*8, float(o3s[i])+float(fzs[i])*8)
                coneSource.SetHeight(1.2)
                coneSource.SetRadius(0.6)
                coneSource.SetResolution (32)
                coneSource.SetDirection(float(fxs[i])*8,float(fys[i])*8,float(fzs[i])*8)

                axisWithArrow = vtk.vtkAppendPolyData()
                axisWithArrow.AddInputConnection(coneSource.GetOutputPort())
                axisWithArrow.AddInputConnection(lineSource.GetOutputPort())
                axisWithArrow.Update()

                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(axisWithArrow.GetOutputPort())

                actorPan = vtk.vtkActor()
                actorPan.SetMapper(mapper)
                actorPan.GetProperty().SetLineWidth(2)
                actorPan.GetProperty().SetColor(0, 0, 1)
                actor1.append(actorPan)
                i+=1
            for k in actor1:
                self.ren.AddActor(k)
                
            t=(1,1,1)
            actor2 = []
            i=0
            while i < len(idfs):
                text=vtk.vtkVectorText()
                text.SetText(str(round(Fhs[i],2)))
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(1,1,1)
                textActor.SetPosition(float(o1s[i])-0.8*t[0],float(o2s[i])-0.1*t[0], float(o3s[i])+8*t[0])
                textActor.SetScale(t)
                actor2.append(textActor)
                i+=1
            for k in actor2:
                self.ren.AddActor(k)

            camera = vtk.vtkCamera()
            reader = vtk.vtkBMPReader()
            reader.SetFileName("Icon/Color.bmp")
            reader.Update()
            actorbmp = vtk.vtkImageActor()
            actorbmp.SetInputData(reader.GetOutput())
            transformbmp = vtk.vtkTransform()
            transformbmp.Translate(-30,30,0)
            transformbmp.Scale(0.1,0.1,0.1)
            actorbmp.SetUserTransform(transformbmp)
            self.ren.AddActor(actorbmp)
        else:
            actorgx = actorgum[0]
            self.ren.AddActor(actorgx)
            Fhx=[]
            for a,b,c in zip(fxx,fyx,fzx):
                Fhx.append(math.sqrt((float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))))
            α=list()
            β=list()
            γ=list()
            for a,b,c,d in zip(fxx,fyx,fzx,Fhx):
                α.append(math.acos(float(a)/float(d))*180/3.14159)
                β.append(math.acos(float(b)/float(d))*180/3.14159)
                γ.append(math.acos(float(c)/float(d))*180/3.14159)

            i=0
            while i < len(idfx):
                if Fhx[i]<=0.5:
                    actorxia[i].GetProperty().SetColor(0,0,1)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>0.5 and Fhx[i]<=1:
                    actorxia[i].GetProperty().SetColor(0,0.7,1)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>1 and Fhx[i]<=1.5:
                    actorxia[i].GetProperty().SetColor(0,1,1)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>1.5 and Fhx[i]<=2:
                    actorxia[i].GetProperty().SetColor(0,1,0.7)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>2 and Fhx[i]<=2.5:
                    actorxia[i].GetProperty().SetColor(0.12,1,0)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>2.5 and Fhx[i]<=3:
                    actorxia[i].GetProperty().SetColor(0.71,1,0)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>3 and Fhx[i]<=3.5:
                    actorxia[i].GetProperty().SetColor(1,1,0)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                elif Fhx[i]>3.5 and Fhx[i]<=4:
                    actorxia[i].GetProperty().SetColor(1,0.7,0)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                else:
                    actorxia[i].GetProperty().SetColor(1,0,0)
                    actorxia[i].GetProperty().SetOpacity(0.6)
                i+=1
            for k in actorxia:
                self.ren.AddActor(k)
            
            actor1 = []
            i=0
            while i < len(idfx):
                lineSource = vtk.vtkLineSource()
                lineSource.SetPoint1(float(o1x[i]), float(o2x[i]), float(o3x[i]))
                lineSource.SetPoint2(float(o1x[i])+float(fxx[i]*10), float(o2x[i])+float(fyx[i])*10, float(o3x[i])+float(fzx[i])*10)

                coneSource = vtk.vtkConeSource()
                coneSource.SetCenter(float(o1x[i])+float(fxx[i]*10), float(o2x[i])+float(fyx[i])*10, float(o3x[i])+float(fzx[i])*10)
                coneSource.SetHeight(1.2)
                coneSource.SetRadius(0.6)
                coneSource.SetResolution (32)
                coneSource.SetDirection(float(fxx[i])*5,float(fyx[i])*10,float(fzx[i])*10)

                axisWithArrow = vtk.vtkAppendPolyData()
                axisWithArrow.AddInputConnection(coneSource.GetOutputPort())
                axisWithArrow.AddInputConnection(lineSource.GetOutputPort())
                axisWithArrow.Update()

                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(axisWithArrow.GetOutputPort())

                actorPan = vtk.vtkActor()
                actorPan.SetMapper(mapper)
                actorPan.GetProperty().SetLineWidth(2)
                actorPan.GetProperty().SetColor(0, 0, 1)
                actor1.append(actorPan)
                i+=1
            for k in actor1:
                self.ren.AddActor(k)
                
            t=(1,1,1)
            actor2 = []
            i=0
            while i < len(idfx):
                text=vtk.vtkVectorText()
                text.SetText(str(round(Fhx[i],2)))
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(1,1,1)
                textActor.SetPosition(float(o1x[i])-0.8*t[0],float(o2x[i])-0.1*t[0], float(o3x[i])+8*t[0])
                textActor.SetScale(t)
                actor2.append(textActor)
                i+=1
            for k in actor2:
                self.ren.AddActor(k)
            reader = vtk.vtkBMPReader()
            reader.SetFileName("Icon/Color.bmp")
            reader.Update()
            actorbmp = vtk.vtkImageActor()
            actorbmp.SetInputData(reader.GetOutput())
            transformbmp = vtk.vtkTransform()
            transformbmp.Translate(-30,-35,0)
            transformbmp.Scale(0.1,0.1,0.1)
            transformbmp.RotateX(180)
            actorbmp.SetUserTransform(transformbmp)
            self.ren.AddActor(actorbmp)
            camera = vtk.vtkCamera()
            camera.Elevation (180)
            camera.OrthogonalizeViewUp ()
            camera.Azimuth(360)
            

        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(14)
        self.ren.ResetCamera()
        self.iren.Initialize() 

    def danya11(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth11.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth11.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth11.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 11:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya12(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth12.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth12.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth12.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 12:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya13(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth13.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth13.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth13.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 13:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya14(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth14.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth14.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth14.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 14:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya15(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth15.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth15.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth15.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 15:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya16(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth16.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth16.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth16.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 16:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya17(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth17.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth17.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth17.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 17:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya21(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth21.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth21.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth21.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 21:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya22(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth22.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth22.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth22.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 22:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya23(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth23.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth23.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth23.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 23:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya24(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth24.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth24.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth24.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 24:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya25(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth25.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth25.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth25.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 25:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya26(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth26.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth26.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth26.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 26:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya27(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth27.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i <  'tooth31.stl' and i != 'tooth27.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        θ= list()
        for i in q3:
            θ.append((180/3.14159)*2*(math.acos((float(i)))))
        x= list()
        y= list()
        z= list()
        for a,b,c,d in zip(q0,q1,q2,θ):
            x.append(float(a)/(math.sin(0.5*d)))
            y.append(float(b)/(math.sin(0.5*d)))
            z.append(float(c)/(math.sin(0.5*d)))

        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))
        
        if os.path.isfile("gums.stl"):
            actorgs = actorgum[0]
            self.ren.AddActor(actorgs)
            for i in actorshang:
                self.ren.AddActor(i)
            if os.path.isfile('tooth27.stl'):
                actor1 = []
                i = 0
                while i < len(idli):
                    if int(idli[i]) == 27:
                        axes = vtk.vtkAxesActor()
                        axes.SetTotalLength(6*abs(float(fx[i])),6*abs(float(fy[i])),6*abs(float(fz[i])))
                        axes.SetShaftTypeToCylinder ()
                        axes.AxisLabelsOff ()
                        transform = vtk.vtkTransform()
                        transform.Translate(float(o1[i]),float(o2[i]), float(o3[i])+4)
                        transform.RotateWXYZ(θ[i],x[i],y[i],z[i])
                        axes.SetUserTransform(transform)
                        actor1.append(axes)

                        bitter1 = vtk.vtkFloatArray()
                        bitter1.SetNumberOfTuples(3)
                        bitter1.SetTuple1(0, fx[i])
                        bitter1.SetTuple1(1, fy[i])
                        bitter1.SetTuple1(2, fz[i])
                        dobj1 = vtk.vtkDataObject()
                        dobj1.GetFieldData().AddArray(bitter1)

                        actorpie = vtk.vtkPieChartActor()
                        actorpie.SetInputData(dobj1)
                        actorpie.SetTitle("号牙力值")
                        actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                        actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                        actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie.GetLegendActor().SetNumberOfEntries(3)
                        actorpie.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie.SetPieceColor(2,0.35,0.52,0.69)
                        if fx[i] < 0:
                            actorpie.SetPieceLabel(0,"F-yuanzhong")
                        else:
                            actorpie.SetPieceLabel(0,"F-jinzhong")
                        if fy[i] < 0:
                            actorpie.SetPieceLabel(1,"F-shece")
                        else:
                            actorpie.SetPieceLabel(1,"F-chunjiace")
                        if fz[i] < 0:
                            actorpie.SetPieceLabel(2,"F-yaru")
                        else:
                            actorpie.SetPieceLabel(2,"F-shenchang")
                        actorpie.LegendVisibilityOff()

                        actorpie.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetColor(1,0,0)
                        actorpie.GetLabelTextProperty().SetFontSize(5)
                        actor1.append(actorpie)

                        bitter2 = vtk.vtkFloatArray()
                        bitter2.SetNumberOfTuples(3)
                        bitter2.SetTuple1(0, mx[i])
                        bitter2.SetTuple1(1, my[i])
                        bitter2.SetTuple1(2, mz[i])
                        dobj2 = vtk.vtkDataObject()
                        dobj2.GetFieldData().AddArray(bitter2)

                        actorpie2 = vtk.vtkPieChartActor()
                        actorpie2.SetInputData(dobj2)
                        actorpie2.SetTitle("号牙力值")
                        actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                        actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                        actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                        actorpie2.GetLegendActor().SetNumberOfEntries(3)
                        actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                        actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                        actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                        if mx[i] < 0:
                            actorpie2.SetPieceLabel(0,"guanshexiang")
                        else:
                            actorpie2.SetPieceLabel(0,"guanchunxiang")
                        if my[i] < 0:
                            actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                        else:
                            actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                        if mz[i] < 0:
                            actorpie2.SetPieceLabel(2,"jinzhongshece")
                        else:
                            actorpie2.SetPieceLabel(2,"yuanzhongshece")
                        actorpie2.LegendVisibilityOff()

                        actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                        actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                        actor1.append(actorpie2)
                        for k in actor1:
                            self.ren.AddActor(k)
                    i+=1
            else:
                text=vtk.vtkVectorText()
                text.SetText('No such tooth')
                textMapper=vtk.vtkPolyDataMapper()
                textMapper.SetInputConnection(text.GetOutputPort())
                textActor=vtk.vtkFollower()
                textActor.SetMapper(textMapper)
                textActor.GetProperty().SetColor(0,0,1)
                textActor.SetPosition(-25,35,0)
                textActor.SetScale(5)
                self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no maxillary')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya31(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i > 'tooth31.stl' and i != 'tooth31.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth31.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 31:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth31.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 31:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()
		
    def danya32(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth32.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth32.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth32.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 32:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth32.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 32:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya33(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth33.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth33.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth33.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 33:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth33.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 33:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya34(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth34.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth34.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth34.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 34:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth34.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 34:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya35(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth35.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth35.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth35.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 35:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth35.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 35:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya36(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth36.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth36.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth36.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 36:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth36.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 36:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya37(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth37.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth37.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth37.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 37:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth37.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 37:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya41(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth41.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth41.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth41.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 41:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth41.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 41:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()
		
    def danya42(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth42.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth42.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth42.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 42:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth42.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 42:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya43(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth43.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth43.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth43.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 43:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth43.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 43:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya44(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth44.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth44.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth44.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 44:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth44.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 44:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya45(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth45.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth45.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth45.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 45:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth45.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 45:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya46(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth46.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth46.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth46.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 46:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth46.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 46:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

    def danya47(self):
        self.ren.RemoveAllViewProps()
        count = 0
        actorgum = []
        actorshang = []
        actorxia = []
        path = os.getcwd()
        dirs = os.listdir(path)
        for i in dirs:
            if os.path.splitext(i)[1] == ".stl":
                count += 1
                sr=vtk.vtkSTLReader()
                sr.SetFileName(i)
                if i == 'tooth47.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetOpacity(0.3)
                    stlactor.GetProperty().SetColor(1,1,1)
                    stlactor.SetMapper(stlmapper)
                    self.ren.AddActor(stlactor)
                elif i == 'gums.stl' or i == 'gumx.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.87,0.51,0.49)
                    stlactor.SetMapper(stlmapper)
                    actorgum.append(stlactor)
                elif i >= 'tooth31.stl' and i != 'tooth47.stl':
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorxia.append(stlactor)                                        
                else:
                    stlmapper=vtk.vtkPolyDataMapper()
                    stlmapper.SetInputConnection(sr.GetOutputPort())
                    stlactor=vtk.vtkActor()
                    stlactor.GetProperty().SetColor(0.91,0.85,0.80)
                    stlactor.SetMapper(stlmapper)
                    actorshang.append(stlactor)

        id,q0,q1,q2,q3,o1,o2,o3=[],[],[],[],[],[],[],[]
        with open("TeethAxis.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                id.append(tmp[0])
                q1.append(tmp[1])
                q2.append(tmp[2])
                q3.append(tmp[3])
                q0.append(tmp[4])
                o1.append(tmp[5])
                o2.append(tmp[6])
                o3.append(tmp[7])

        ids,q0s,q1s,q2s,q3s,o1s,o2s,o3s=[],[],[],[],[],[],[],[]
        idx,q0x,q1x,q2x,q3x,o1x,o2x,o3x=[],[],[],[],[],[],[],[]
        i=0
        while i < len(id):
            if int(id[i]) < 31:
                ids.append(id[i])
                q0s.append(q0[i])
                q1s.append(q1[i])
                q2s.append(q2[i])
                q3s.append(q3[i])
                o1s.append(o1[i])
                o2s.append(o2[i])
                o3s.append(o3[i])
            else:
                idx.append(id[i])
                q0x.append(q0[i])
                q1x.append(q1[i])
                q2x.append(q2[i])
                q3x.append(q3[i])
                o1x.append(o1[i])
                o2x.append(o2[i])
                o3x.append(o3[i])
            i+=1


        θs= list()
        for i in q3s:
            θs.append((180/3.14159)*2*(math.acos((float(i)))))
        xs= list()
        ys= list()
        zs= list()
        for a,b,c,d in zip(q0s,q1s,q2s,θs):
            xs.append(float(a)/(math.sin(0.5*d)))
            ys.append(float(b)/(math.sin(0.5*d)))
            zs.append(float(c)/(math.sin(0.5*d)))

        θx= list()
        for i in q3x:
            θx.append((180/3.14159)*2*(math.acos((float(i)))))
        xx= list()
        yx= list()
        zx= list()
        for a,b,c,d in zip(q0x,q1x,q2x,θx):
            xx.append(float(a)/(math.sin(0.5*d)))
            yx.append(float(b)/(math.sin(0.5*d)))
            zx.append(float(c)/(math.sin(0.5*d)))



        idli,fx,fy,fz,mx,my,mz=[],[],[],[],[],[],[]
        with open("rcforc.txt") as A:
            for eachline in A:
                tmp=re.split("\s+",eachline)
                idli.append(round(float(tmp[0]),3))
                fx.append(round(float(tmp[1]),3))
                fy.append(round(float(tmp[2]),3))
                fz.append(round(float(tmp[3]),3))
                mx.append(round(float(tmp[4]),3))
                my.append(round(float(tmp[5]),3))
                mz.append(round(float(tmp[6]),3))

        idlis,fxs,fys,fzs,mxs,mys,mzs=[],[],[],[],[],[],[]
        idlix,fxx,fyx,fzx,mxx,myx,mzx=[],[],[],[],[],[],[]
        i=0
        while i < len(idli):
            if int(id[i]) < 31:
                idlis.append(id[i])
                fxs.append(q0[i])
                fys.append(q1[i])
                fzs.append(q2[i])
                mxs.append(q3[i])
                mys.append(o1[i])
                mzs.append(o2[i])
            else:
                idlix.append(id[i])
                fxx.append(float(q0[i]))
                fyx.append(float(q1[i]))
                fzx.append(float(q2[i]))
                mxx.append(float(q3[i]))
                myx.append(float(o1[i]))
                mzx.append(float(o2[i]))
            i+=1
        
        if os.path.isfile("gumx.stl"):
            if os.path.isfile('gums.stl'):
                actorgx = actorgum[1]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth47.stl'): 
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 47:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if fxx[i] < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
            else:
                actorgx = actorgum[0]
                self.ren.AddActor(actorgx)
                for k in actorxia:
                    self.ren.AddActor(k)
                if os.path.isfile('tooth47.stl'):
                    actor1 = []
                    i = 0
                    while i < len(idlix):
                        if int(idlix[i]) == 47:
                            axes = vtk.vtkAxesActor()
                            axes.SetTotalLength(6*abs(float(fxx[i])),6*abs(float(fyx[i])),6*abs(float(fzx[i])))
                            axes.SetShaftTypeToCylinder ()
                            axes.AxisLabelsOff ()
                            transform = vtk.vtkTransform()
                            transform.Translate(float(o1x[i]),float(o2x[i]), float(o3x[i])-4)
                            transform.RotateWXYZ(θx[i],xx[i],yx[i],zx[i])
                            axes.SetUserTransform(transform)
                            actor1.append(axes)

                            bitter1 = vtk.vtkFloatArray()
                            bitter1.SetNumberOfTuples(3)
                            bitter1.SetTuple1(0, fxx[i])
                            bitter1.SetTuple1(1, fyx[i])
                            bitter1.SetTuple1(2, fzx[i])
                            dobj1 = vtk.vtkDataObject()
                            dobj1.GetFieldData().AddArray(bitter1)

                            actorpie = vtk.vtkPieChartActor()
                            actorpie.SetInputData(dobj1)
                            actorpie.SetTitle("号牙力值")
                            actorpie.GetPositionCoordinate().SetValue(-0.1,0.1,0.0)
                            actorpie.GetPosition2Coordinate().SetValue(0.5,0.3,0.0)
                            actorpie.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie.GetLegendActor().SetNumberOfEntries(3)
                            actorpie.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie.SetPieceColor(2,0.35,0.52,0.69)
                            if float(fxx[i]) < 0:
                                actorpie.SetPieceLabel(0,"F-yuanzhong")
                            else:
                                actorpie.SetPieceLabel(0,"F-jinzhong")
                            if fyx[i] < 0:
                                actorpie.SetPieceLabel(1,"F-shece")
                            else:
                                actorpie.SetPieceLabel(1,"F-chunjiace")
                            if fzx[i] < 0:
                                actorpie.SetPieceLabel(2,"F-yaru")
                            else:
                                actorpie.SetPieceLabel(2,"F-shenchang")
                            actorpie.LegendVisibilityOff()

                            actorpie.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetColor(1,0,0)
                            actorpie.GetLabelTextProperty().SetFontSize(5)
                            actor1.append(actorpie)

                            bitter2 = vtk.vtkFloatArray()
                            bitter2.SetNumberOfTuples(3)
                            bitter2.SetTuple1(0, mxx[i])
                            bitter2.SetTuple1(1, myx[i])
                            bitter2.SetTuple1(2, mzx[i])
                            dobj2 = vtk.vtkDataObject()
                            dobj2.GetFieldData().AddArray(bitter2)

                            actorpie2 = vtk.vtkPieChartActor()
                            actorpie2.SetInputData(dobj2)
                            actorpie2.SetTitle("号牙力值")
                            actorpie2.GetPositionCoordinate().SetValue(0.5,0.1,0.0)
                            actorpie2.GetPosition2Coordinate().SetValue(1.1,0.3,0.0)
                            actorpie2.GetProperty().SetColor(0.1,0.1,0.1)
                            actorpie2.GetLegendActor().SetNumberOfEntries(3)
                            actorpie2.SetPieceColor(0,0.62,0.36,0.35)
                            actorpie2.SetPieceColor(1,0.33,0.61,0.49)
                            actorpie2.SetPieceColor(2,0.35,0.52,0.69)
                            if mxx[i] < 0:
                                actorpie2.SetPieceLabel(0,"guanshexiang")
                            else:
                                actorpie2.SetPieceLabel(0,"guanchunxiang")
                            if myx[i] < 0:
                                actorpie2.SetPieceLabel(1,"yuanzhongqingxie")
                            else:
                                actorpie2.SetPieceLabel(1,"jinzhongqingxie")
                            if mzx[i] < 0:
                                actorpie2.SetPieceLabel(2,"jinzhongshece")
                            else:
                                actorpie2.SetPieceLabel(2,"yuanzhongshece")
                            actorpie2.LegendVisibilityOff()

                            actorpie2.GetTitleTextProperty().SetColor(1,0,0)
                            actorpie2.GetLabelTextProperty().SetColor(1,0,0)
                            actor1.append(actorpie2)
                            for k in actor1:
                                self.ren.AddActor(k)
                        i+=1
                else:
                    text=vtk.vtkVectorText()
                    text.SetText('No such tooth')
                    textMapper=vtk.vtkPolyDataMapper()
                    textMapper.SetInputConnection(text.GetOutputPort())
                    textActor=vtk.vtkFollower()
                    textActor.SetMapper(textMapper)
                    textActor.GetProperty().SetColor(0,0,1)
                    textActor.SetPosition(25,35,0)
                    textActor.RotateX(0)
                    textActor.RotateY(180)
                    textActor.SetScale(5)
                    self.ren.AddActor(textActor)
        else:
            text=vtk.vtkVectorText()
            text.SetText('There is no Mandible')
            textMapper=vtk.vtkPolyDataMapper()
            textMapper.SetInputConnection(text.GetOutputPort())
            textActor=vtk.vtkFollower()
            textActor.SetMapper(textMapper)
            textActor.GetProperty().SetColor(0,0,1)
            textActor.SetPosition(0,0,0)
            textActor.SetScale(5)
            textActor.RotateX(0)
            textActor.RotateY(180)
            self.ren.AddActor(textActor)
            
        camera = vtk.vtkCamera()
        camera.Elevation (180)
        camera.Azimuth(360)
        camera.OrthogonalizeViewUp ()
        self.ren.SetBackground(1, 1, 1)
        self.ren.SetBackground2(0.95, 0.95, 0.95)
        self.ren.SetGradientBackground(1)
        self.ren.SetActiveCamera(camera)
        cam1=self.ren.GetActiveCamera()
        cam1.Zoom(1.4)
        self.ren.ResetCamera()
        self.iren.Initialize()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
