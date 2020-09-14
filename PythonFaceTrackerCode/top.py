# Aditya Gopinath
# ESD 2
# Project Nighthawk
# top.py

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from faceTracker import *
from calibration import *
from globals import globals
import ctypes

# main window class that holds everything
class MainWindow(QMainWindow):
  def fullscreen(self):
    self.showFullScreen() #sets the window fullscreen
  
  def maximized(self):
    self.showMaximized() #exits fullscreen and sets the window maximized
        
  def __init__(self):
    super(MainWindow, self).__init__()
    
    self.setWindowTitle("Project Nighthawk")
    self.settings=QSettings("RIT", "DrKaputa")
    
    #************************************Added by me************************************
    app_icon = 'nighthawk_icon.png'
    self.setWindowIcon(QIcon(app_icon)) #set icon on top left of window
    if(sys.platform == "win32"): #only do this if the OS is Windows (breaks on Linux)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_icon) #set icon on Windows taskbar
    
    fsAction = QtGui.QAction("&Fullscreen", self)
    fsAction.setShortcut("Ctrl+F")
    fsAction.setStatusTip('Go Fullscreen')
    fsAction.triggered.connect(self.fullscreen)
    
    maxAction = QtGui.QAction("&Maximize", self)
    maxAction.setShortcut("Ctrl+E")
    maxAction.setStatusTip('Exit Fullscreen, Set Window Maximized')
    maxAction.triggered.connect(self.maximized)
    
    self.statusBar()
    
    mainMenu = self.menuBar()
    fileMenu = mainMenu.addMenu('&File')
    fileMenu.addAction(fsAction)
    fileMenu.addAction(maxAction)
    #***********************************************************************************
    
    # open default file
    fileName = 'parameters.txt'
    with open(fileName) as f:
      globals.comPort                 = int(f.readline().split("= ")[1])
      globals.baudRate                = int(f.readline().split("= ")[1])
      globals.Brightness              = int(f.readline().split("= ")[1])
      globals.phi_face                = float(f.readline().split("= ")[1])
      globals.zone                    = float(f.readline().split("= ")[1])
      globals.FOV                     = float(f.readline().split("= ")[1])
      globals.faceTrackingWidth       = float(f.readline().split("= ")[1])
      globals.faceTrackingHeight      = float(f.readline().split("= ")[1])
      globals.faceTrackingHysteresis  = float(f.readline().split("= ")[1])
      globals.hysteresis              = float(f.readline().split("= ")[1])
      globals.offset                  = float(f.readline().split("= ")[1])
      globals.zoneWidth               = float(f.readline().split("= ")[1])
 
    # instantiate the dock widgets
    self.faceTracker = FaceTrackerHolder(self)
    self.calibration = Calibration(self)
 
    # load in the docks
    self.setupDocks()
    
    # load in the style sheet
    styleFile ="styleSheet.txt"
    with open(styleFile,"r") as fh:
      self.setStyleSheet(fh.read())
      
    # restore dock locations
    if self.settings.value("state"):
      self.restoreGeometry(self.settings.value("geometry").toByteArray())
      self.restoreState(self.settings.value("state").toByteArray())
      self.move(self.settings.value("windowPos", QVariant(QPoint(50, 50))).toPoint())
      self.resize(self.settings.value("windowSize", QVariant(QSize(555, 550))).toSize())
      self.setWindowState(Qt.WindowState(self.settings.value("windowState").toInt()[0]))
    
  def setupDocks(self):
    self.faceTrackerDock = QDockWidget(self)
    self.faceTrackerDock.setWidget(self.faceTracker)
    self.faceTrackerDock.setWindowTitle("Camera")
    self.faceTrackerDock.setObjectName("Camera")
    self.faceTrackerDock.setContentsMargins(0, 0, 0, 0) #sets left top right and bottom margins
    self.faceTrackerDock.setFeatures(QDockWidget.AllDockWidgetFeatures)
    self.faceTrackerDock.setAllowedAreas(Qt.AllDockWidgetAreas)
    self.addDockWidget(Qt.LeftDockWidgetArea, self.faceTrackerDock)
    
    self.calibrationDock = QDockWidget(self)
    self.calibrationDock.setWidget(self.calibration)
    self.calibrationDock.setWindowTitle("Buttons")
    self.calibrationDock.setObjectName("Buttons")
    self.calibrationDock.setContentsMargins(0, 0, 0, 0)
    self.calibrationDock.setFeatures(QDockWidget.AllDockWidgetFeatures)
    self.calibrationDock.setAllowedAreas(Qt.AllDockWidgetAreas)
    self.addDockWidget(Qt.LeftDockWidgetArea, self.calibrationDock)
    
    DOCKOPTIONS = QMainWindow.AllowTabbedDocks
    DOCKOPTIONS = DOCKOPTIONS|QMainWindow.AllowNestedDocks
    DOCKOPTIONS = DOCKOPTIONS|QMainWindow.AnimatedDocks
    self.setDockOptions(DOCKOPTIONS)
    self.setTabPosition(Qt.AllDockWidgetAreas,QTabWidget.North)
   
  def closeEvent(self, event):
    self.settings.setValue('geometry', self.saveGeometry())
    self.settings.setValue('state', self.saveState())
    self.settings.setValue("windowState", QVariant(self.windowState()))
    self.settings.setValue("windowSize", QVariant(self.size()))
    self.settings.setValue("windowPos", QVariant(self.pos()))
    self.settings.sync()
    QMainWindow.closeEvent(self, event)

# start of the program that instantiates a MainWindow class
def main():
  app = QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  
  sys.exit(app.exec_())

if __name__ == '__main__':
    main()