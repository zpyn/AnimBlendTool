from PySide2 import QtCore, QtWidgets, QtGui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from . import QtCustom
#reload(QtCustom)


class BlendAnimUI(MayaQWidgetDockableMixin,QtWidgets.QMainWindow):
    """
    Creates all the dialog window using widgets
    """
    
    def __init__(self, **kwargs):
        """
        """
        super(BlendAnimUI,self).__init__()
        self.setup_ui()
        self.set_basic_connections()

    def setup_ui(self):
        """
        This function initialize and build all the widgets needed fo the UI
        """
        self.btns_dict= dict()
        self.setWindowTitle('Constraint and Bake')
        main_widget = QtWidgets.QWidget()
        Title_lbl = QtWidgets.QLabel("Anim Blend Tool")
        Title_lbl.setFont(QtGui.QFont('MS Shell Dlg 2', 10))
        rigs_fl = QtCustom.FrameLayout("Anim")
        rigs_fl.setColor(102,141,145)
        # Qt Widgets
        controls_lbl = QtWidgets.QLabel("Controls")
        controls_spr = QtWidgets.QSpacerItem(35,10,QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.controls_le = QtWidgets.QLineEdit()
        self.controls_btn = QtWidgets.QPushButton()
        self.controls_btn .setObjectName("controls_btn")
        self.btns_dict["controls_btn"] = self.controls_le
        f_source_lbl = QtWidgets.QLabel("First Source")
        f_source_spr = QtWidgets.QSpacerItem(20,10,QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.f_source_le = QtWidgets.QLineEdit()
        self.f_source_btn = QtWidgets.QPushButton()
        self.f_source_btn.setObjectName("firstSource_btn")
        self.btns_dict["firstSource_btn"] = self.f_source_le 
        s_source_lbl = QtWidgets.QLabel("Second Source")
        s_source_spr = QtWidgets.QSpacerItem(4,10,QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.s_source_le = QtWidgets.QLineEdit()
        self.s_source_btn = QtWidgets.QPushButton()
        self.s_source_btn.setObjectName("secondSource_btn")
        self.btns_dict["secondSource_btn"] = self.s_source_le
        target_lbl = QtWidgets.QLabel("Target")
        target_spr = QtWidgets.QSpacerItem(48,10,QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.target_le = QtWidgets.QLineEdit()
        self.target_btn = QtWidgets.QPushButton()
        self.target_btn.setObjectName("target_btn")
        self.btns_dict["target_btn"] = self.target_le
        time_fl = QtCustom.FrameLayout("Blend Time Range")
        time_fl.setColor(102,141,145)
        t_range_lbl = QtWidgets.QLabel("Time Range")
        t_spacer = QtWidgets.QSpacerItem(20,10,QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.custom_rb = QtWidgets.QRadioButton("Custom")
        self.timeSlider_rb = QtWidgets.QRadioButton("Time Slider")
        t_spacer02 = QtWidgets.QSpacerItem(4,20,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        start_time_lbl = QtWidgets.QLabel("Start time")
        self.start_time_le = QtWidgets.QLineEdit()
        self.start_time_le.setEnabled(False)
        stat_time_spr_01 = QtWidgets.QSpacerItem(30,10,QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        stat_time_spr_02 = QtWidgets.QSpacerItem(100,10,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.start_time_le.setMaximumSize(80, 150)
        self.end_time_lbl = QtWidgets.QLabel("End time")
        self.end_time_le = QtWidgets.QLineEdit()
        self.end_time_le.setEnabled(False)
        end_time_spr_01 = QtWidgets.QSpacerItem(35,10,QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        end_time_spr_02 = QtWidgets.QSpacerItem(100,10,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.end_time_le.setMaximumSize(80, 150)
        bake_fl = QtCustom.FrameLayout("Bake")
        bake_fl.setColor(102,141,145)
        self.b_smartBake_rb = QtWidgets.QRadioButton("Smart Bake")
        Operation_fl = QtCustom.FrameLayout("Operation")
        Operation_fl.setColor(102,141,145)
        operation_spr_01 = QtWidgets.QSpacerItem(10,10,QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        operation_spr_02 = QtWidgets.QSpacerItem(100,10,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        operationTime_lbl = QtWidgets.QLabel("Operation Type")
        self.constraint_rb = QtWidgets.QRadioButton("Constraint")
        self.bake_rb = QtWidgets.QRadioButton("Bake")
        self.ConstraintBake_rb = QtWidgets.QRadioButton("Constraint and Bake")
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")
        self.delete_btn = QtWidgets.QPushButton("Delete Nodes")
        end_spacer = QtWidgets.QSpacerItem(0,0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        # Layouts
        main_lyt = QtWidgets.QVBoxLayout()
        header_lyt = QtWidgets.QHBoxLayout()
        controls_lyt = QtWidgets.QHBoxLayout()
        a_first_lyt = QtWidgets.QHBoxLayout()
        a_second_lyt = QtWidgets.QHBoxLayout()
        a_target_lyt = QtWidgets.QHBoxLayout()
        t_option_lyt = QtWidgets.QHBoxLayout()
        s_time_lyt = QtWidgets.QHBoxLayout()
        e_time_lyt = QtWidgets.QHBoxLayout()
        bake_lyt = QtWidgets.QHBoxLayout()
        operations_lyt = QtWidgets.QHBoxLayout()
        btn_lyt = QtWidgets.QHBoxLayout()
        # Anim Frame
        controls_lyt.addWidget(controls_lbl)
        controls_lyt.addSpacerItem(controls_spr)
        controls_lyt.addWidget(self.controls_le )
        controls_lyt.addWidget(self.controls_btn)
        a_first_lyt.addWidget(f_source_lbl)
        a_first_lyt.addSpacerItem(f_source_spr)
        a_first_lyt.addWidget(self.f_source_le)
        a_first_lyt.addWidget(self.f_source_btn)
        a_second_lyt.addWidget(s_source_lbl)
        a_second_lyt.addSpacerItem(s_source_spr)
        a_second_lyt.addWidget(self.s_source_le)
        a_second_lyt.addWidget(self.s_source_btn)
        a_target_lyt.addWidget(target_lbl)
        a_target_lyt.addSpacerItem(target_spr)
        a_target_lyt.addWidget(self.target_le)
        a_target_lyt.addWidget(self.target_btn)
        # Time Frame
        t_option_lyt.addWidget(t_range_lbl)
        t_option_lyt.addSpacerItem(t_spacer)
        t_option_lyt.addWidget(self.custom_rb)
        t_option_lyt.addWidget(self.timeSlider_rb)
        t_option_lyt.addSpacerItem(t_spacer02)
        s_time_lyt.addWidget(start_time_lbl)
        s_time_lyt.addSpacerItem( stat_time_spr_01)
        s_time_lyt.addWidget(self.start_time_le)
        s_time_lyt.addSpacerItem( stat_time_spr_02)
        e_time_lyt.addWidget(self.end_time_lbl)
        e_time_lyt.addSpacerItem(end_time_spr_01)
        e_time_lyt.addWidget(self.end_time_le)
        e_time_lyt.addSpacerItem(end_time_spr_02)
        # Bake
        bake_lyt.addWidget(self.b_smartBake_rb)
        # Ops
        operations_lyt.addWidget(operationTime_lbl)
        operations_lyt.addSpacerItem(operation_spr_01)
        operations_lyt.addWidget(self.constraint_rb)
        operations_lyt.addWidget(self.bake_rb)
        operations_lyt.addWidget(self.ConstraintBake_rb)
        operations_lyt.addSpacerItem(operation_spr_02)
        header_lyt.addWidget(Title_lbl)
        rigs_fl.addLayout(controls_lyt)
        rigs_fl.addLayout(a_first_lyt)
        rigs_fl.addLayout(a_second_lyt)
        rigs_fl.addLayout(a_target_lyt)
        time_fl.addLayout(t_option_lyt)
        time_fl.addLayout(s_time_lyt)
        time_fl.addLayout(e_time_lyt)
        bake_fl.addLayout(bake_lyt)
        Operation_fl.addLayout(operations_lyt)
        btn_lyt.addWidget(self.apply_btn)
        btn_lyt.addWidget(self.delete_btn )
        btn_lyt.addWidget(self.close_btn)
        main_lyt.addLayout(header_lyt)
        main_lyt.addWidget(rigs_fl)
        main_lyt.addWidget(time_fl)
        main_lyt.addWidget(bake_fl)
        main_lyt.addWidget(Operation_fl)
        main_lyt.addLayout(btn_lyt)
        main_lyt.addSpacerItem(end_spacer)
        main_widget.setLayout(main_lyt)
        self.setCentralWidget(main_widget)
    
    def set_basic_connections(self):
        """
        This function set some basic connections
        """
        # Enable Custom Time Line Edits
        self.custom_rb.toggled.connect(self.enable_time_selection)
        
    def enable_time_selection(self, value):
        """
        This function enables or disables widgets depending of the need
        """
        if value == True:
            self.start_time_le.setEnabled(True)
            self.end_time_le.setEnabled(True)
        else:
            self.start_time_le.setEnabled(False)
            self.end_time_le.setEnabled(False)


 

        








