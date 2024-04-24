"""
This module provides utility functions with maya commands for the AnimBlend Tool
"""
import re

import maya.cmds as cmds

class MayaOperations():
    """
    Present Functions for cosntraint, bake and other process needed
    to blend animation inside Autodesk Maya software
    """
    def __init__(self):
        pass

    def bake_controls(self, controls, smart_bake = False):
        """
        Bake the simulation for the selected controls with the option for smart baking.
        
        Args:
            smart_bake (bool): Whether to execute it with smart bake or not.

        Returns:
            None

        """
        time_ = self.get_frameRange()
        cmds.bakeResults(controls, simulation=1, t=(time_[0], time_[1]), 
                         sampleBy=1, at=["tx","ty","tz","rx","ry","rz"], 
                         smart=smart_bake)

    def blend_animation(self, controls, first_source, second_source, target, time):
        """
        Executes the two main functions to constraint and blend the animation.

        Args:
            controls (list) : List of rig controls.
            first_source (str): First rig root node name that will be taken 
                                for the blend.
            second_source (str): Second rig root node name that will be taken 
                                 for the blend.
            target (str): Target rig root node that will be driven by 
                          the first and second source.
            time (tuple): Blend time range (start frame, end frame).

        Returns:
            None

        """
        # Create and Key Constraints
        constraints_ls = self.constraint_controls(
            controls, first_source, second_source, target)
        self.key_constraints(constraints_ls,time)

    def constraint_controls(self, controls, first_source, second_source, target):
        """
        This function constraints each control of the given list and skips locked channels if needed.

        Args:
            contorls (list): List of rig controls to constraint.
            first_source (str): First rig root node that containts the controls that will drive the target.
            second_source (str): Second rig root node that containts the controls that will drive the target.
            target (str) :  traget Rig which controls will be driven by first 2.
        
        Returns:
            list (str):  List with the created parent constraint nodes.

        """
        first_source_ns = first_source.split(":")[0]
        second_source_ns = second_source.split(":")[0]
        target_ns = target.split(":")[0]
        constraint_ls = list()
        ax_ls = ['x','y','z']

        for ctrl in controls:
            ctrl_name = ctrl.split(":")[1]     
            # Skip locked attributes      
            skip_t = [ax for ax in ax_ls
                       if cmds.getAttr("{0}.t{1}".format(target_ns+":"+ctrl_name, ax),lock=True)
                     ]
            skip_r = [ax for ax in ax_ls 
                      if cmds.getAttr("{0}.r{1}".format(target_ns+":"+ctrl_name, ax),lock=True)
                     ]

            pc =cmds.parentConstraint("{}:".format(first_source_ns)+ctrl_name, 
                                      "{}:".format(second_source_ns)+ctrl_name, 
                                      "{}:".format(target_ns)+ctrl_name, 
                                      skipTranslate=skip_t,
                                      skipRotate=skip_r, mo=0
                                      )
            constraint_ls.append(pc)
        return constraint_ls
    
    def key_constraints(self, constraint_ls, time):
        """
        This function adds keyframes to the constraint nodes to blend the animation

        Args:
            constraint_ls (list): List of constraint nodes.
            time (tuple):  Blend time range (start frame, end frame).

        Returns:
            None
        """
        for con in constraint_ls:
            for attr in cmds.listAttr(con):
                if re.search(r'[W[0-9]', attr):
                    if "W0" in attr:
                        cmds.setKeyframe(con, 
                                         t=time[0], 
                                         v=1, 
                                         attribute=attr, 
                                         inTangentType="linear", 
                                         outTangentType= "linear"
                                         )
                        cmds.setKeyframe(con,
                                         t=time[1],
                                         v=0,
                                         attribute=attr,
                                         inTangentType="linear", 
                                         outTangentType= "linear"
                                         )  
                    elif "W1" in attr:
                        cmds.setKeyframe(con,t=time[0],
                                         v=0,
                                         attribute=attr,
                                         inTangentType="linear",
                                         outTangentType= "linear"
                                         )
                        cmds.setKeyframe(con,
                                         t=time[1],
                                         v=1,
                                         attribute=attr,
                                         inTangentType="linear",
                                         outTangentType="linear"
                                         )

    def break_connection(self, ctrl_ls):
        """
        This functions removes parent constraint nodes and animation curves connected to the selected controls

        Args:
            ctrl_ls (list): List of rig controls that will be cleaned.
        
        Returns:
            None

        """
        for ctrl in ctrl_ls:
            if cmds.listConnections(ctrl, type="parentConstraint", s=1, d=0):
                parentConstraint_ls = cmds.listConnections(ctrl, 
                                                           type="parentConstraint", 
                                                           s=1,d=0
                                                           )
                cmds.delete(list(dict.fromkeys(parentConstraint_ls)))
        
            if cmds.listConnections(ctrl, type="animCurve", s=1, d=0):
                animCurves_ls= cmds.listConnections(ctrl,
                                                    type="animCurve",
                                                    s=1,d=0
                                                    )
                cmds.delete(animCurves_ls)
    
    def get_frameRange(self):
        """
        This functions querys the start and end frame of the timeline.
        Args:
            None

        Returns:
            tuple (int): (start_frame, end_frame)
        """
        start_frame = int(cmds.playbackOptions(minTime=1, q=1))
        end_frame = int(cmds.playbackOptions(maxTime=1, q=1))
        return(start_frame, end_frame)

    def get_selection(self):
        """
        This function get the selected node inside Maya
        Args:
            None

        Returns:
            string : A string of all selected nodes separeted by commas.
        
        """
        selection_ls = cmds.ls(selection=1)
        selection_str = (",").join(selection_ls)
        return selection_str
    
    def drop_message(self, m= "", t=""):
        """
        This funtion calls the Maya confirm dialog for user feedback.
        Args:
            m (str): Message to display.
            t (str): Title for the dialog window.
        Returns:
            None
        """
        cmds.confirmDialog(t=t,m=m)


    