# ***************************************************************************
# *   Copyright (c) 2021-2023 David Carter <dcarter@davidcarter.ca>         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************
"""Class for editing materials"""

__title__ = "FreeCAD Materials"
__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"
    
import FreeCADGui

from DraftTools import translate

class CmdMaterialEditor:
    def Activated(self):
        FreeCADGui.addModule("MaterialEditor")
        FreeCADGui.doCommand("MaterialEditor.openEditor()")

    def IsActive(self):
        return True
        
    def GetResources(self):
        return {'MenuText': translate("Rocket", 'Material editor'),
                'ToolTip': translate("Rocket", 'Opens the FreeCAD material editor'),
                'Pixmap': "Arch_Material" }

class CmdNewMaterialEditor:
    def Activated(self):
        FreeCADGui.addModule("Materials")
        FreeCADGui.doCommand("Materials.openEditor()")

    def IsActive(self):
        return True
        
    def GetResources(self):
        return {'MenuText': translate("Rocket", 'Material editor'),
                'ToolTip': translate("Rocket", 'Opens the FreeCAD material editor'),
                'Pixmap': "Arch_Material" }

class CmdValuesEditor:
    def Activated(self):
        FreeCADGui.addModule("ValueEditor")
        FreeCADGui.doCommand("ValueEditor.openEditor()")

    def IsActive(self):
        return True
        
    def GetResources(self):
        return {'MenuText': translate("Rocket", 'Material editor'),
                'ToolTip': translate("Rocket", 'Opens the FreeCAD material editor'),
                'Pixmap': "Arch_Material" }
