# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422766487.20313
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/volunteers.edit.html'
_template_uri = 'volunteers.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents']


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
        def contents():
            return render_contents(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
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
        def contents():
            return render_contents(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<form method="POST">\r\n<table>\r\n\r\n')
        __M_writer(str(form))
        __M_writer('\r\n\r\n</table>\r\n\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t<a href="/home/volunteers.delete/')
        __M_writer(str(user.id))
        __M_writer('/" class="btn btn-warning">Delete Account</a>\r\n</form>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/volunteers.edit.html", "line_map": {"64": 58, "36": 1, "54": 4, "55": 9, "56": 9, "57": 13, "58": 13, "27": 0, "46": 4}, "uri": "volunteers.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
