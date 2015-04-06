# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427871474.380668
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\user\\templates/user.edit.html'
_template_uri = 'user.edit.html'
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
        form = context.get('form', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        users = context.get('users', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('\r\n\t<div class="top_banner">Edit User Account</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context)
        user = context.get('user', UNDEFINED)
        users = context.get('users', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('home.manager'):
            __M_writer('\t\t<div class="text-center">\r\n\t\t\t<img class="profile_pic" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('user/media/profile_pic/pp_')
            __M_writer(str(request.urlparams[0]))
            __M_writer('.jpg" />\r\n\t\t</div>\r\n\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str(form))
            __M_writer('\r\n\t\t\t\t<span class="is_username_message"></span>\r\n\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t<a href="/user/user.delete/')
            __M_writer(str(users.id))
            __M_writer('/" class="btn btn-warning">Delete Account</a>\r\n\t\t\t\t<a href="/user/user.changepassword/')
            __M_writer(str(users.id))
            __M_writer('/" class="btn btn-info">Change Password</a>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        else:
            __M_writer('\t\t<div class="text-center">\r\n\t\t\t<img class="profile_pic" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('user/media/profile_pic/pp_')
            __M_writer(str(request.urlparams[0]))
            __M_writer('.jpg" />\r\n\t\t</div>\r\n\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str(form))
            __M_writer('\r\n\t\t\t\t<span id="is_username_message"></span>\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t<a href="/user/user.changepassword/')
            __M_writer(str(user.id))
            __M_writer('/" class="btn btn-info">Change Password</a>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\user\\templates/user.edit.html", "line_map": {"68": 8, "79": 8, "80": 9, "81": 10, "82": 11, "83": 11, "84": 11, "85": 11, "86": 18, "87": 18, "88": 25, "89": 25, "90": 26, "91": 26, "92": 30, "93": 31, "94": 32, "95": 32, "96": 32, "97": 32, "98": 39, "27": 0, "100": 45, "101": 45, "102": 50, "41": 1, "108": 102, "46": 5, "99": 39, "56": 3, "62": 3}, "uri": "user.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
