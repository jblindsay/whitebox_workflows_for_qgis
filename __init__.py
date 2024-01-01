# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WhiteboxWorkflows
                                 A QGIS plugin
 Provides access to Whitebox Workflows within QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-03-09
        copyright            : (C) 2023 by Whitebox Geospatial Inc.
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
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Whitebox Geospatial Inc.'
__date__ = '2023-03-09'
__copyright__ = '(C) 2023 by Whitebox Geospatial Inc.'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WhiteboxWorkflows class from file WhiteboxWorkflows.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .whitebox_workflows_for_qgis import WhiteboxWorkflowsPlugin
    return WhiteboxWorkflowsPlugin()
