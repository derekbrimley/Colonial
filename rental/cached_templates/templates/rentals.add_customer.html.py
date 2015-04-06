# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427948200.836407
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add_customer.html'
_template_uri = 'rentals.add_customer.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Choose Customer</div>\r\n\t<div class="text-center"><h4>Next you will choose the products</h4></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>Profile Picture</th>\r\n\t\t\t<th>Username</th>\r\n\t\t\t<th>First</th>\r\n\t\t\t<th>Last</th>\r\n\t\t\t<th id="build_title">Select </th>\r\n\t\t</tr>\r\n\t\t<tr>\r\n')
        for user in users:
            __M_writer('\t\t\t\t<td><img class="profile_pic" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('user/media/profile_pic/pp_')
            __M_writer(str(user.id))
            __M_writer('.jpg" /></td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a class="btn btn-md btn-success" href="/rental/rentals.add_rentals/')
            __M_writer(str(user.id))
            __M_writer('">Build</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.add_customer.html", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add_customer.html", "source_encoding": "ascii", "line_map": {"66": 10, "74": 10, "75": 14, "76": 24, "77": 25, "78": 25, "79": 25, "80": 25, "81": 25, "82": 26, "83": 26, "84": 27, "85": 27, "86": 28, "87": 28, "88": 30, "89": 30, "90": 34, "27": 0, "96": 90, "38": 1, "43": 6, "48": 37, "54": 3, "60": 3}}
__M_END_METADATA
"""
