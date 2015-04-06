# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423607352.889414
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/accounts.edit.html'
_template_uri = 'accounts.edit.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n<form method="POST">\r\n\r\n\t<table id="form">\r\n\r\n\t\t')
        __M_writer(str(form))
        __M_writer('\r\n\r\n\t</table>\r\n\t<div id="form_buttons">\r\n\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t<a href="/home/accounts.delete/')
        __M_writer(str(user.id))
        __M_writer('/" class="btn btn-warning">Delete Account</a>\r\n\t</div>\r\n</form>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Edit Accounts</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "accounts.edit.html", "line_map": {"64": 21, "65": 21, "38": 1, "71": 3, "43": 5, "77": 3, "83": 77, "53": 8, "27": 0, "61": 8, "62": 16, "63": 16}, "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/accounts.edit.html"}
__M_END_METADATA
"""
