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
"""Search interface for queriables.

$Id$
"""
__docformat__ = "reStructuredText"

from zope.interface import implements
from zope.i18n import translate
from zope.schema import getFieldsInOrder
from zope.app.zapi import getName, getPath
from zope.app.pau.interfaces import IQuerySchemaSearch
from zope.app.form.utility import setUpWidgets, getWidgetsData
from zope.app.form.interfaces import IInputWidget
from zope.app.form.browser.interfaces import ISourceQueryView
from zope.app.i18n import ZopeMessageIDFactory as _

search_label = _('search-button', 'Search')

class QuerySchemaSearchView(object):
    implements(ISourceQueryView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self, name):
        schema = self.context.schema
        sourcename = getName(self.context)
        sourcepath = getPath(self.context)
        setUpWidgets(self, schema, IInputWidget, prefix=name+'.field')
        html = []
        
        # add sub title for source search field
        html.append('<h4 i18n:translate="">%s %s</h4>' % (sourcename, sourcepath))
        # start row for search fields
        html.append('<div class="row">')

        for field_name, field in getFieldsInOrder(schema):
            widget = getattr(self, field_name+'_widget')
            
            # for each field add lable...
            html.append('<div class="label">')
            html.append('<label for="%s" title="%s">'
                        % (widget.name, widget.hint))
            html.append(widget.label)
            html.append('</label>')
            html.append('</div>')
            
            # ...and field widget
            html.append('<div class="field">')
            html.append(widget())

            if widget.error():
                html.append('<div class="error">')
                html.append(widget.error())
                html.append('</div>')
            html.append('</div>')
        # end row
        html.append('</div>')

        # add search button for search fields
        html.append('<div class="row">')
        html.append('<div class="field">')
        html.append('<input type="submit" name="%s" value="%s" />'
                     % (name+'.search',
                        translate(search_label, context=self.request)))
        html.append('</div>')
        html.append('</div>')


        return '\n'.join(html)

    def results(self, name):
        if not (name+'.search' in self.request):
            return None
        schema = self.context.schema
        setUpWidgets(self, schema, IInputWidget, prefix=name+'.field')
        data = getWidgetsData(self, schema)
        return self.context.search(data)
