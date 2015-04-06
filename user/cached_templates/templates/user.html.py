# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427834424.221909
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\user\\templates/user.html'
_template_uri = 'user.html'
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
        addresses = context.get('addresses', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context)
        request = context.get('request', UNDEFINED)
        addresses = context.get('addresses', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' \r\n')
        if request.user.has_perm('home.manager'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Profile Picture</th>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\r\n')
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
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.email))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.phone))
                __M_writer('</td>\r\n')
                for address in addresses:
                    if user.address_id == address.id:
                        __M_writer('\t\t\t\t\t\t\t<td>')
                        __M_writer(str(address.address1))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(address.zip))
                        __M_writer('</td>\r\n')
                __M_writer('\t\t\t\t<td>\r\n\t\t\t\t<a href="/user/user.edit/')
                __M_writer(str(user.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/user/user.delete/')
                __M_writer(str(user.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/user/user.create/" class="btn btn-success">Add a Volunteer</a>\r\n\t\t</div>\r\n\r\n\r\n\r\n')
        elif request.user.has_perm('home.agent'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Profile Picture</th>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t\r\n\t\t\t<tr>\r\n')
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
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.email))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(user.phone))
                __M_writer('</td>\r\n')
                for address in addresses:
                    if user.address_id == address.id:
                        __M_writer('\t\t\t\t\t\t\t<td>')
                        __M_writer(str(address.address1))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(address.zip))
                        __M_writer('</td>\r\n')
                __M_writer('\t\t\t\t<td>\r\n\t\t\t\t<a href="/user/user.edit/')
                __M_writer(str(user.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\r\n\r\n')
        elif request.user.is_authenticated():
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Profile Picture</th>\r\n\t\t\t\t<th>Username</th>\r\n\t\t\t\t<th>First</th>\r\n\t\t\t\t<th>Last</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>City</th>\r\n\t\t\t\t<th>State</th>\r\n\t\t\t\t<th>Zip</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td><img class="profile_pic" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('user/media/profile_pic/pp_')
            __M_writer(str(users.id))
            __M_writer('.jpg" /></td>\r\n\t\t\t\t<td>')
            __M_writer(str(users.username))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(users.first_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(users.last_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(users.email))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(users.phone))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(addresses.address1))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(addresses.city))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(addresses.state))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(addresses.zip))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/user/user.editself/')
            __M_writer(str(users.id))
            __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n\t\t\t\r\n\t\t</table>\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<h1>Not Available</h1>\r\n\r\n')
        __M_writer('\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">User Accounts</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "user.html", "filename": "C:\\Python34\\Projects\\colonial\\user\\templates/user.html", "source_encoding": "ascii", "line_map": {"27": 0, "40": 1, "45": 5, "55": 10, "65": 10, "66": 11, "67": 12, "68": 28, "69": 29, "70": 29, "71": 29, "72": 29, "73": 29, "74": 30, "75": 30, "76": 31, "77": 31, "78": 32, "79": 32, "80": 33, "81": 33, "82": 34, "83": 34, "84": 35, "85": 36, "86": 37, "87": 37, "88": 37, "89": 38, "90": 38, "91": 41, "92": 42, "93": 42, "94": 43, "95": 43, "96": 47, "97": 55, "98": 56, "99": 72, "100": 73, "101": 73, "102": 73, "103": 73, "104": 73, "105": 74, "106": 74, "107": 75, "108": 75, "109": 76, "110": 76, "111": 77, "112": 77, "113": 78, "114": 78, "115": 79, "116": 80, "117": 81, "118": 81, "119": 81, "120": 82, "121": 82, "122": 85, "123": 86, "124": 86, "125": 90, "126": 94, "127": 95, "128": 111, "129": 111, "130": 111, "131": 111, "132": 112, "133": 112, "134": 113, "135": 113, "136": 114, "137": 114, "138": 115, "139": 115, "140": 116, "141": 116, "142": 117, "143": 117, "144": 118, "145": 118, "146": 119, "147": 119, "148": 120, "149": 120, "150": 122, "151": 122, "152": 128, "153": 129, "154": 133, "160": 3, "166": 3, "172": 166}}
__M_END_METADATA
"""
