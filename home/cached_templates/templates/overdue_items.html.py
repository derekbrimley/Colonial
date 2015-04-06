# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428137050.306407
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\home\\templates/overdue_items.html'
_template_uri = 'overdue_items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top_banner', 'contents']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/home/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        def contents():
            return render_contents(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Overdue Items</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t<div class="text-center">\r\n\t\t\t\t<button class="btn overdue btn-success btn-md" id="30" role="button"><h2>30</h2></button>\r\n\t\t\t\t<button class="btn overdue btn-success btn-md" id="60" role="button"><h2>60</h2></button>\r\n\t\t\t\t<button class="btn overdue btn-success btn-md" id="90" role="button"><h2>90</h2></button>\r\n\t\t\t\t<button class="btn overdue btn-primary btn-md" id="email" role="button"><h2>Email</h2></button>\r\n\t\t</div>\r\n\r\n\t\t<br>\r\n\r\n\t\t<div class="overdue_report">\r\n\r\n\r\n\t\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "overdue_items.html", "filename": "C:\\Python34\\Projects\\colonial\\home\\templates/overdue_items.html", "line_map": {"75": 69, "51": 3, "36": 1, "69": 9, "57": 3, "41": 5, "27": 0, "63": 9}}
__M_END_METADATA
"""
