# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428377064.944805
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\home\\templates/tools.html'
_template_uri = 'tools.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'top_banner']


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
        def contents():
            return render_contents(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Tool Name</th>\r\n\t\t\t\t<th>Purpose</th>\r\n\t\t\t\t<th>Rights</th>\r\n\t\t\t\t<th>Run</th>\r\n\t\t\t</tr>\r\n\r\n\t\t\t<tr>\t\t\t\r\n\t\t\t\t<td>Overdue Items</td>\r\n\t\t\t\t<td>Return a list of overdue rentals</td>\r\n\t\t\t\t<td>Yes</td>\r\n\t\t\t\t<td><a class="btn btn-md btn-success" href="/home/overdue_items">Run</a></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\t\t\t\r\n\t\t\t\t<td>Tool 2</td>\r\n\t\t\t\t<td>Do something cool</td>\r\n\t\t\t\t<td>Yes</td>\r\n\t\t\t\t<td><a class="btn btn-md btn-success" href="/home/overdue_items">Run</a></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\t\t\t\r\n\t\t\t\t<td>Tool 3</td>\r\n\t\t\t\t<td>Do something similar to the others</td>\r\n\t\t\t\t<td>Yes</td>\r\n\t\t\t\t<td><a class="btn btn-md btn-success" href="/home/overdue_items">Run</a></td>\r\n\t\t\t</tr>\r\n\t\t</table>\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Tool Name</th>\r\n\t\t\t\t<th>Purpose</th>\r\n\t\t\t\t<th>Rights</th>\r\n\t\t\t</tr>\r\n\r\n\t\t\t<tr>\t\t\t\r\n\t\t\t\t<td>Overdue Items</td>\r\n\t\t\t\t<td>Return a list of overdue rentals</td>\r\n\t\t\t\t<td>No</td>\r\n\t\t\t</tr>\r\n\t\t</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Tools</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tools.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\home\\templates/tools.html", "source_encoding": "ascii", "line_map": {"59": 9, "37": 1, "63": 42, "42": 5, "75": 3, "81": 75, "52": 9, "27": 0, "60": 11, "61": 12, "62": 41, "69": 3}}
__M_END_METADATA
"""
