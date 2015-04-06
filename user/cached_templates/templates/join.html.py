# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425629228.083738
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\user\\templates/join.html'
_template_uri = 'join.html'
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
        form = context.get('form', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
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
        form = context.get('form', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="top_banner">Get on your Colonial horse and ride along!</div>\r\n\r\n<form id="userjoinform" method="POST" action="/user/join/">\r\n\r\n\t<table id="join_form">\r\n\r\n\t\t')
        __M_writer(str(form))
        __M_writer('\r\n\r\n\t</table>\r\n\r\n<div class="text-center">\r\n\t<button type="submit" class="btn btn-primary">Join!</button>\r\n</div>\r\n\r\n</form>\r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "36": 7, "53": 9, "54": 17, "55": 17, "27": 0, "61": 55, "46": 9}, "filename": "C:\\Python34\\Scripts\\colonial\\user\\templates/join.html", "uri": "join.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
