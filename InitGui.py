# ***************************************************************************
# *   Copyright (c) 2023 David Carter <dcarter@davidcarter.ca>              *
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

__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"

import FreeCAD
import FreeCADGui

# import Fem # Requires the FEM workbench to be loaded

class MaterialTestWorkbench ( Workbench ):
    "MaterialTest workbench object"
    Icon = FreeCAD.getUserAppDataDir() + "Mod/MaterialTest/Resources/icons/MaterialTestWorkbench.svg"
    MenuText = "MaterialTest"
    ToolTip = "MaterialTest workbench"

    def _loadMaterialModule(self):
        # import Material
        import MatGui
        # dummy usage to get flake8 and lgtm quiet
        # False if Material.__name__ else True
        False if MatGui.__name__ else True

    def Initialize(self):
        FreeCADGui.addLanguagePath(FreeCAD.getUserAppDataDir() + "Mod/MaterialTest/Resources/translations")

        # load the module
        import MaterialTestGui
        from PySide.QtCore import QT_TRANSLATE_NOOP

        self._loadMaterialModule()
        
        self.appendToolbar(QT_TRANSLATE_NOOP('MaterialTest', 'MaterialTest'),
                        ['MaterialTest_MaterialEditor', 'MaterialTest_NewMaterialEditor', "Materials_Edit", 'Separator', 'Materials_ModelSelect', 'Separator', 'MaterialTest_ValuesEditor', "Materials_ValueEdit"])

    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(MaterialTestWorkbench())
