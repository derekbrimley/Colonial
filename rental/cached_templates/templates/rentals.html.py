# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428378399.468747
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\Colonial\\rental\\templates/rentals.html'
_template_uri = 'rentals.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
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


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Rental Home</div>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('\t<div="row">\r\n\r\n\t \t<div class="col-md-6 item_container text-center">\r\n\t  \t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('rental/media/icons/view.jpg" />\r\n\t\t\t<div class="text-center">                                                                                           \r\n\t\t\t\t<a href="/rental/rentals.view/" class="btn btn-success btn-lg" role="button"><h2>View Rentals</h2></a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t                                                       \r\n\r\n')
            __M_writer('\r\n\r\n\t  \t<div class="col-md-6 item_container text-center">\r\n\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('rental/media/icons/add.jpg" />\r\n\t  \t\t<div class="text-center">\r\n\t  \t\t\t<a href="/rental/rentals.add_customer/" class="btn btn-success btn-lg" role="button"><h2>Build Rental</h2></a>\r\n\t\t\t</div>\r\n\t  \t</div>\r\n\r\n\t</div>\r\n\r\n')
        else:
            __M_writer('\r\n\t<h1 class="text-center">Down for maintenance</h1>\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.html", "filename": "C:\\Python34\\Projects\\Colonial\\rental\\templates/rentals.html", "source_encoding": "ascii", "line_map": {"65": 10, "27": 0, "38": 1, "81": 39, "73": 10, "74": 11, "75": 12, "76": 15, "77": 15, "78": 28, "79": 31, "80": 31, "43": 6, "82": 40, "83": 44, "53": 3, "89": 83, "59": 3}}
__M_END_METADATA
"""
