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


class PickersManager(artellapipe.ToolWidget, object):
    def __init__(self, project, config, settings, parent):
        super(PickersManager, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(PickersManager, self).ui()
