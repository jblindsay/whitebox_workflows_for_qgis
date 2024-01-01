# -*- coding: utf-8 -*-

"""
/***************************************************************************
 WhiteboxWorkflows
                                 A QGIS plugin
 Provides access to Whitebox Workflows within QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-03-09
        copyright            : (C) 2023 by John Lindsay, Whitebox Geospatial Inc.
        email                : support@whiteboxgeo.com
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

__author__ = 'John Lindsay, Whitebox Geospatial Inc.'
__date__ = '2024-01-01'
__copyright__ = '(C) 2024 by Whitebox Geospatial Inc.'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .whitebox_workflows_for_qgis_provider import WhiteboxWorkflowsProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class WhiteboxWorkflowsPlugin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = WhiteboxWorkflowsProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
