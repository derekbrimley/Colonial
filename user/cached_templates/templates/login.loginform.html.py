# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428375526.757416
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/login.loginform.html'
_template_uri = 'login.loginform.html'
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
    return runtime._inherit_from(context, '/user/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n\t<div class="text-center">\r\n\t\t<img class="headertitle" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialheritage.png" alt="The Colonial Heritage Foundation">\r\n\t</div>\r\n\r\n\t\t<form id="loginform" method="POST" action="/user/login.loginform/">\r\n\t\t\t<table id="form">\r\n\t\t\t\t')
        __M_writer(str(form))
        __M_writer('\r\n\t\t\t</table>\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<button type="submit"  class="btn btn-success">Submit Login</button>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"65": 59, "59": 13, "36": 1, "37": 4, "55": 5, "56": 8, "57": 8, "58": 13, "27": 0, "47": 5}, "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/login.loginform.html", "uri": "login.loginform.html"}
__M_END_METADATA
"""
