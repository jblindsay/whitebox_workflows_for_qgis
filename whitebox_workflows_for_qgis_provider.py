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
__date__ = '2023-03-09'
__copyright__ = '(C) 2023 by Whitebox Geospatial Inc.'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import glob, os, platform, zipfile, urllib.request
from qgis.PyQt.QtGui import QIcon
from qgis.core import Qgis, QgsProcessingProvider, QgsMessageLog, QgsApplication
from processing.core.ProcessingConfig import ProcessingConfig, Setting
from .whitebox_workflows_for_qgis_algorithm import WhiteboxWorkflowsAlgorithm
# from .algorithms.aspect import Aspect
import pip

pluginPath = os.path.dirname(__file__)


class WhiteboxWorkflowsProvider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        self.FLOATING_LICENSE_ID = 'FLOATING_LICENSE_ID'
        self.WBW_COMPRESS_RASTERS = 'WBW_COMPRESS_RASTERS'
        self.WBW_MAX_THREADS = 'WBW_MAX_THREADS'

        # import urllib.request
        # url = "https://www.whiteboxgeo.com/wbw_wheels/whitebox_workflows-1.2.0-cp38-abi3-macosx_11_0_arm64.whl"
        # (s, msg) = urllib.request.urlretrieve(url, "whitebox_workflows-1.2.0-cp38-abi3-macosx_11_0_arm64.whl")
        # print(s)
        # print(msg)



        # The following code will identify the appropriate wbw whl file
        # for the system and unzips it for local use.
        this_dir = os.path.dirname(os.path.realpath(__file__))
        wb_dir = os.path.join(this_dir, 'whitebox_workflows')
        if not os.path.isdir(wb_dir):
            # # First, find all the wheel files in this_dir
            # path = os.path.join(this_dir, '*.whl')
            # whl_files = glob.glob(path)
            # if len(whl_files) == 0:
            #     print("Error: No whl files have been located in the plugin directory.")
            #     QgsMessageLog.logMessage("Error: No whl files have been located in the plugin directory.", level=Qgis.Critical)
            
            QgsMessageLog.logMessage("Downloading Whitebox Workflows library to the plugin directory.", level=Qgis.Info)

            # Based on the OS and arch, unzip the appropriate wheel
            platform_system = platform.system()
            if 'Linux' in platform_system:
                url = "https://www.whiteboxgeo.com/wbw_wheels/wbw_linux.whl"
                path = os.path.join(this_dir, 'wbw_linux.whl')
                (s, msg) = urllib.request.urlretrieve(url, path)
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    zip_ref.extractall(this_dir)
            
            elif 'Windows' in platform_system:
                url = "https://www.whiteboxgeo.com/wbw_wheels/wbw_win.whl"
                path = os.path.join(this_dir, 'wbw_win.whl')
                (s, msg) = urllib.request.urlretrieve(url, path)
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    zip_ref.extractall(this_dir)
            
            elif 'Darwin' in platform_system:
                # Intel or M-series?
                proc = platform.processor()
                if 'arm' in proc:
                    url = "https://www.whiteboxgeo.com/wbw_wheels/wbw_macosx_arm.whl"
                    path = os.path.join(this_dir, 'wbw_macosx_arm.whl')
                    (s, msg) = urllib.request.urlretrieve(url, path)
                    with zipfile.ZipFile(path, 'r') as zip_ref:
                        zip_ref.extractall(this_dir)
                        
                else:
                    url = "https://www.whiteboxgeo.com/wbw_wheels/wbw_macosx_intel.whl"
                    path = os.path.join(this_dir, 'wbw_macosx_intel.whl')
                    (s, msg) = urllib.request.urlretrieve(url, path)
                    with zipfile.ZipFile(path, 'r') as zip_ref:
                        zip_ref.extractall(this_dir)

        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """

        # self.addAlgorithm(Aspect())

        self.algs = []
        folder = self.descriptionsPath()
        # wbtdescriptions.createDescriptions()
        for descriptionFile in os.listdir(folder):
            if descriptionFile.endswith('txt'):
                try:
                    alg = WhiteboxWorkflowsAlgorithm(os.path.join(folder, descriptionFile))
                    if alg.name().strip() != '':
                        self.algs.append(alg)
                    else:
                        QgsMessageLog.logMessage(self.tr('Could not load Whitebox Workflows algorithm from file "{}".'.format(descriptionFile)),
                                                 self.tr('Processing'), Qgis.Critical)
                except Exception as e:
                    QgsMessageLog.logMessage(self.tr('Could not load WbW algorithm from file "{}".\n{}'.format(descriptionFile, str(e))),
                                             self.tr('Processing'), Qgis.Critical)

        for a in self.algs:
            self.addAlgorithm(a)

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'wbw'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Whitebox Workflows')

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        # return QgsProcessingProvider.icon(self)
        return QIcon(os.path.join(pluginPath, 'icons', 'WbW.svg'))

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return 'Whitebox Workflows (WbW)'
    
    def load(self):
        ProcessingConfig.settingIcons[self.name()] = self.icon()
        
        ProcessingConfig.addSetting(Setting(self.name(),
                                            self.FLOATING_LICENSE_ID,
                                            self.tr('Floating License ID (WbW-Pro only)'),
                                            self.wbtFloatingLicenseId(),
                                            valuetype=Setting.STRING))

        ProcessingConfig.addSetting(Setting(self.name(),
                                            self.WBW_COMPRESS_RASTERS,
                                            self.tr('Compress output rasters'),
                                            True))
        
        threads = QgsApplication.maxThreads()  # if user specified limit for rendering, lets keep that as default here, otherwise max
        # threads = cpu_count() if threads == -1 else threads  # if unset, maxThreads() returns -1
        ProcessingConfig.addSetting(Setting(self.name(),
                                            self.WBW_MAX_THREADS,
                                            ProcessingConfig.tr('Max Threads'), threads,
                                            valuetype=Setting.INT))
        
        ProcessingConfig.readSettings()
        self.refreshAlgorithms()
        return True

    def wbtFloatingLicenseId(self):
        floating_license_id = ProcessingConfig.getSetting(self.FLOATING_LICENSE_ID)
        return floating_license_id if floating_license_id is not None else ''

    def descriptionsPath(self):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), 'descriptions'))