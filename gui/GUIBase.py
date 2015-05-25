# -*- coding: utf-8 -*-

"""
This file contains the QuDi GUI module base class.

QuDi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

QuDi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QuDi. If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2015 Jan M. Binder jan.binder@uni-ulm.de
"""

from core.Base import Base

class GUIBase(Base):
    """This is the GUI base class. It provides functions that every GUI module should have.
    """
    _modclass = 'GUIBase'
    _modtype = 'Gui'
    
    def __init__(self, manager, name, configuation = {}, callbacks = {}, **kwargs):
        Base.__init__(self, manager, name, configuation, callbacks, **kwargs)

    def show(self):
        self.logMsg('Every GUI module needs to reimplement the show() function!', msgType='error')

