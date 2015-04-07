# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428376764.691663
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/changepassword.html'
_template_uri = 'changepassword.html'
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
        users = context.get('users', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
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
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('\r\n\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str(form))
            __M_writer('\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<a href="/user/user/" class="btn btn-info">Back</a>\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str(form))
            __M_writer('\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<a href="/user/user/')
            __M_writer(str(user.id))
            __M_writer('/" class="btn btn-info">Back</a>\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Change Password</div>\r\n\t<h1>')
        __M_writer(str( users.username ))
        __M_writer('</h1>\r\n\t<h3>')
        __M_writer(str( users.security_question ))
        __M_writer('</h3>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "changepassword.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\user\\templates/changepassword.html", "source_encoding": "ascii", "line_map": {"65": 12, "66": 13, "67": 14, "68": 20, "69": 20, "70": 30, "71": 31, "72": 36, "73": 36, "74": 40, "75": 40, "76": 47, "82": 5, "99": 93, "89": 5, "90": 7, "91": 7, "92": 8, "93": 8, "27": 0, "40": 1, "41": 4, "46": 9, "56": 12}}
__M_END_METADATA
"""
