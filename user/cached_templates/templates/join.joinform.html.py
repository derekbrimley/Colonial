# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425632881.382107
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\user\\templates/join.joinform.html'
_template_uri = 'join.joinform.html'
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
        def contents():
            return render_contents(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        __M_writer('\r\n\r\n')
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n\t<div class="text-center">\r\n\t\t<img class="headertitle" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialheritage.png" alt="The Colonial Heritage Foundation">\r\n\t</div>\r\n\r\n\t<div class="top_banner">Get on your Colonial horse and ride along!</div>\r\n\r\n\t\t<form id="joinform" method="POST" action="/user/join.joinform/">\r\n\r\n\t\t\t<table id="join_form">\r\n\r\n\t\t\t\t')
        __M_writer(str(form))
        __M_writer('\r\n\t\t\t\t<span class="is_username_message"></span>\r\n\r\n\t\t\t</table>\r\n\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Join!</button>\r\n\t\t\t</div>\r\n\r\n\t\t</form>\r\n\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Scripts\\colonial\\user\\templates/join.joinform.html", "uri": "join.joinform.html", "line_map": {"65": 59, "59": 21, "36": 1, "37": 7, "55": 9, "56": 12, "57": 12, "58": 21, "27": 0, "47": 9}, "source_encoding": "ascii"}
__M_END_METADATA
"""
