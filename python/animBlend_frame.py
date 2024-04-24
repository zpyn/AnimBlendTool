from functools import partial
#import importlib

from . import animBlend_ui
from . import animBlend_core


class AnimWidget(animBlend_ui.BlendAnimUI):
    """
    Anim Blend Dialog Widget, presents options to blend and bake animation 
    of two source rigs into a target rig.
    """
    def __init__(self, **kwargs):
        super(AnimWidget,self).__init__()
        self.maya_operations = animBlend_core.MayaOperations()
        self.set_connections()
    
    def set_connections(self):
        """
        This functions connects all widgets with their particular function.
        """
        self.controls_btn.clicked.connect(partial(self.load_content, 
                                                  self.controls_btn))
        self.f_source_btn.clicked.connect(partial(self.load_content, 
                                                  self.f_source_btn))
        self.s_source_btn.clicked.connect(partial(self.load_content, 
                                                  self.s_source_btn))
        self.target_btn.clicked.connect(partial(self.load_content, 
                                                self.target_btn))
        self.apply_btn.clicked.connect(self.run)
        self.delete_btn.clicked.connect(self.delete)
        self.close_btn.clicked.connect(self.close)
    
    def load_content(self, button):
        """
        This functions sets the text of the correspongin line edit.
        of the pressed button 

        Args:
            button (QtPushButton): Button that has been pressed
        """
        lineEdit =self.btns_dict[button.objectName()]
        selection = self.maya_operations.get_selection()
        lineEdit.setText(selection)
    
    def delete(self):
        """
        Calls the break connection function from the Maya operations.
        """
        controls = self.controls_le.text().split(",")
        self.maya_operations.break_connection(controls)

    def run(self):
        """
        Collects the data from the UI and execute 
        the selected Operation (contraint, bake, constraint and bake)
        """
        controls = self.controls_le.text().split(",")
        first_source = self.f_source_le.text()
        second_sources = self.s_source_le.text()
        target = self.target_le.text()
        time_type = self.get_time_type()
        smart_type = self.b_smartBake_rb.isChecked()
        operation_type = self.get_operation_type()

        if time_type == 0:
            time_ = (self.start_time_le.text(),self.end_time_le.text())
        elif time_type == 1:
            time_ =  self.maya_operations.get_frameRange()
        
        if operation_type == 0:
            self.maya_operations.drop_message(t="Invalid Operation Type", 
                                              m="Please select a operation type!")
        elif operation_type == 1:
            self.maya_operations.blend_animation(controls,first_source,second_sources,target,time_)
        elif operation_type == 2:
            self.maya_operations.bake_controls(controls, smart_bake = smart_type)
        elif operation_type == 3:
            self.maya_operations.blend_animation(controls,first_source,second_sources,target,time_)
            self.maya_operations.bake_controls(controls, smart_bake = smart_type)

    def get_operation_type(self):
        """
        Evaluate wich Radial button of the operations is checked.

        Returns:
            option (int): 

        """
        if self.constraint_rb.isChecked():
            return 1
        elif self.bake_rb.isChecked():
            return 2
        elif self.ConstraintBake_rb.isChecked():
            return 3
        
        return 0

    def get_time_type(self):
        """
         Evaluate wich Radial button of the blend time options is checked

         Returns:
            operation (int): 
        """
        if self.custom_rb.isChecked():
            return 0
        elif self.timeSlider_rb.isChecked():
            return 1
        return False
    
    

