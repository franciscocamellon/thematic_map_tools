# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThematicMapTools
                                 A QGIS plugin
 Tools for designing thematics maps
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-01-23
        git sha              : $Format:%H$
        copyright            : (C) 2021 by CamellONCase
        email                : camelloncase@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QObject, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QToolButton, QMenu, QAction

class GuiManager(QObject):

    def __init__(self, iface, parentMenu = None, toolbar = None):
        """Constructor.
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        super(GuiManager, self).__init__()
        self.iface = iface
        self.menu = parentMenu
        self.iconBasePath = ':/plugins/DsgTools/icons/'
        self.actions = []
        self.managerList = []
        self.menuList = []
        self.toolbar = toolbar