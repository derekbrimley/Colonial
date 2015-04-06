# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422762965.143603
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/volunteers.html'
_template_uri = 'volunteers.html'
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
        def contents():
            return render_contents(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        def contents():
            return render_contents(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<div class="clearfix"></div>\r\n\t<div class="text-right">\r\n\t\t<a href="/home/volunteers.create/" class="btn btn-success">Add a Volunteer</a>\r\n\t</div>\r\n\r\n\t<table id="volunteers_table" class="table table-striped table-bordered">\r\n\t\t\r\n\t\t<tr>\r\n\t\t\t<th>First</th>\r\n\t\t\t<th>Last</th>\r\n\t\t\t<th>Email</th>\r\n\t\t\t<th>Address</th>\r\n\t\t\t<th>Zip</th>\r\n\t\t\t<th>Volunteer</th>\r\n\t\t\t<th>Actions</th>\r\n\t\t</tr>\r\n\t\t<tr>\r\n')
        for user in users:
            __M_writer('\t\t\t<td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(user.address1))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(user.zip))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str(user.volunteer))
            __M_writer('</td>\r\n\t\t\t<td>\r\n\t\t\t<a href="/home/volunteers.edit/')
            __M_writer(str(user.id))
            __M_writer('">Edit</a> | \r\n\t\t\t<a href="/home/volunteers.delete/')
            __M_writer(str(user.id))
            __M_writer('">Delete</a>\r\n\t\t\t</td>\r\n\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "volunteers.html", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/volunteers.html", "source_encoding": "ascii", "line_map": {"64": 28, "65": 29, "66": 29, "67": 31, "68": 31, "69": 32, "70": 32, "71": 36, "77": 71, "27": 0, "35": 1, "45": 4, "52": 4, "53": 23, "54": 24, "55": 24, "56": 24, "57": 25, "58": 25, "59": 26, "60": 26, "61": 27, "62": 27, "63": 28}}
__M_END_METADATA
"""
