# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425714213.527899
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\user\\templates/passwordchanged.html'
_template_uri = 'passwordchanged.html'
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
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context)
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


"""
__M_BEGIN_METADATA
{"uri": "passwordchanged.html", "filename": "C:\\Python34\\Scripts\\colonial\\user\\templates/passwordchanged.html", "source_encoding": "ascii", "line_map": {"64": 9, "37": 1, "71": 9, "72": 10, "73": 11, "74": 16, "75": 17, "76": 23, "82": 76, "52": 3, "58": 3, "27": 0, "42": 6}}
__M_END_METADATA
"""
