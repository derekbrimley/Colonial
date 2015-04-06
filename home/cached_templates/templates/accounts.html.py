# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425203294.626264
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/accounts.html'
_template_uri = 'accounts.html'
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
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
        if request.user.has_perm('home.manager'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for user in user:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(user.username))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.first_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.last_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.email))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.username))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.username))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/accounts.edit/')
                __M_writer(str(user.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/accounts.delete/')
                __M_writer(str(user.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/accounts.create/" class="btn btn-success">Add a Volunteer</a>\r\n\t\t</div>\r\n\r\n\r\n')
        elif request.user.has_perm('home.agent'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for user in users:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(user.username))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.first_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.last_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.email))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.address))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.zip))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/accounts.edit/')
                __M_writer(str(user.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.username))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.first_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.last_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.email))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.address))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(request.user.zip))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/accounts.edit/')
            __M_writer(str(request.user.id))
            __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n\t\t</table>\r\n\r\n')
        __M_writer('\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Accounts</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "accounts.html", "line_map": {"130": 3, "136": 130, "27": 0, "38": 1, "43": 5, "53": 9, "61": 9, "62": 11, "63": 12, "64": 25, "65": 26, "66": 26, "67": 26, "68": 27, "69": 27, "70": 28, "71": 28, "72": 29, "73": 29, "74": 30, "75": 30, "76": 31, "77": 31, "78": 33, "79": 33, "80": 34, "81": 34, "82": 38, "83": 45, "84": 46, "85": 59, "86": 60, "87": 60, "88": 60, "89": 61, "90": 61, "91": 62, "92": 62, "93": 63, "94": 63, "95": 64, "96": 64, "97": 65, "98": 65, "99": 67, "100": 67, "101": 71, "102": 74, "103": 75, "104": 88, "105": 88, "106": 89, "107": 89, "108": 90, "109": 90, "110": 91, "111": 91, "112": 92, "113": 92, "114": 93, "115": 93, "116": 95, "117": 95, "118": 101, "124": 3}, "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/accounts.html"}
__M_END_METADATA
"""
