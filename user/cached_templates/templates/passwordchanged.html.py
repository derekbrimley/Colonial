# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428376781.931238
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/passwordchanged.html'
_template_uri = 'passwordchanged.html'
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
        

        __M_writer('\r\n\r\n\r\n')
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
        __M_writer('\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t<div>\r\n\t\t\t<a href="/home/index/" class="btn btn-info">Home</a>\r\n\t\t\t<a href="/user/user/" class="btn btn-info">Account/Login</a>\r\n\t\t\t<button class="show_login_dialog btn btn-primary">Sign In</button>\r\n\t\t</div>\r\n')
        else:
            __M_writer('\t\t<div>\r\n\t\t\t<a href="/home/index/" class="btn btn-info">Home</a>\r\n\t\t\t<button class="show_login_dialog btn btn-primary">Sign In</button>\r\n\t\t</div>\r\n\t\t\r\n')
        __M_writer('\t\t\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Password Successfully Changed </div>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "passwordchanged.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/passwordchanged.html", "source_encoding": "ascii", "line_map": {"64": 23, "59": 9, "37": 1, "70": 3, "42": 6, "76": 3, "82": 76, "52": 9, "27": 0, "60": 10, "61": 11, "62": 16, "63": 17}}
__M_END_METADATA
"""
