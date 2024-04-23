""" Custome QT Widgets """
from PySide2 import QtCore, QtWidgets, QtGui

class FrameLayout(QtWidgets.QGroupBox):
    """
    This Function creates a custiom QWidget that mimics the function
    of Maya's native Frame Layout
    """
    def __init__(self, title):
        super(FrameLayout,self).__init__(title)
        self.setCheckable(True)
        self.setChecked(True)

        self.layout= QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.colorR= 100
        self.colorG= 100
        self.colorB= 100
        self.clicked.connect(self.collapse)

    def collapse(self):
        '''
        Toggles the QGroupBoxs maximum height to achieve a collapsing effect. 
        '''
        if self.isChecked():
            self.setMaximumHeight(167777)
        else:
            self.setMaximumHeight(19)
    
    def setColor(self,r,g,b):
        """
        """
        self.r=r
        self.g=g
        self.b=b
        self.setFrameLayoutStylesheet()
    
    def setFrameLayoutStylesheet(self):
        """
        """
        self.setStyleSheet('''
                                QGroupBox { 
                                    background-color: rgb(%s,%s,%s); 
                                    padding-top:20px; 
                                    border: 1px solid #0F1317; 
                                    border-radius: 0px; 
                                    margin-top: 0px;
                                    font-size: 12px;
                                    font-weight: bold;
                                    outline: 0px;
                                } 
                                QGroupBox::title { 
                                    subcontrol-origin: margin; 
                                    left: 0px; 
                                    top: 1px;
                                    background: rgb(92, 89, 81);
                                    padding: 0 8000px 0 0px;
                                    border: 1px solid black;
                                } 
                                QGroupBox::indicator {
                                    margin-left: 4px;
                                    width: 12px; 
                                    height: 12px;
                                    border: 1px;
                                    image: url(:/teDownArrow.png);
                                }
                                QGroupBox::indicator:unchecked {
                                    width: 16px; 
                                    height: 16px;
                                    border: 1px;
                                    image: url(:/teRightArrow.png);
                                }
                                QLineEdit{
                                    background-color: rgb(%s,%s,%s);
                                }
                                QRadioButton::indicator:unchecked{
                                    width: 16px;
                                    height: 16px;
                                    border-radius: 8px; 
                                    background-color: rgb(%s,%s,%s);
                                }
                                QPushButton {
                                    background-color: rgb(%s,%s,%s);
                                }
                                QPushButton:hover {
                                    background-color: rgb(%s,%s,%s);
                                }
                                QPushButton:pressed {
                                    background-color: rgb(%s,%s,%s);
                                    border: 1px solid black;
                                }''' %   (
                    self.r, self.g, self.b,
                    self.r-35, self.g-35, self.b-35,
                    self.r-35, self.g-35, self.b-35,
                    self.r+20, self.g+20, self.b+20,
                    
                    self.r+100, self.g+100, self.b+100,
                    self.r-10, self.g-10, self.b-10)
        )
    def addWidget(self, widget):
        '''
        This function receives a widget to add to its internal vertical layout.
        '''
        self.layout.addWidget(widget)
    
    def addLayout(self, layout):
        '''
        This function receives a layout to add to its internal vertical layout.
        '''
        self.layout.addLayout(layout)



