##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Implementations of the session-based and cookie-based extractor and
    challenge plugins.

$Id$
"""

# BBB, entire module gone in 3.1
from persistent import Persistent
from zope.interface import Interface
from zope.app.container.contained import Contained

class SessionExtractor(Persistent, Contained):
    pass


class IFormChallengerLoginPageName(Interface):
    pass


class FormChallenger(Persistent, Contained):
    pass