#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to work with rig pickers
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-pickersmanager'

# We skip the reloading of this module when launching the tool
no_reload = True


class PickersManagerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(PickersManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Pickers Manager',
            'id': 'artellapipe-tools-pickersmanager',
            'logo': 'pickersmanager_logo',
            'icon': 'picker',
            'tooltip': 'Tool to handle rig pickers',
            'tags': ['artella', 'manager', 'picker'],
            'sentry_id': '',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Pickers Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Pickers',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-pickersmanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Pickers',
                 'children': [{'id': 'artellapipe-tools-pickersmanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class PickersManagerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(PickersManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.pickersmanager.widgets import pickersmanagertool

        pickers_manager = pickersmanagertool.PickersManager(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [pickers_manager]
