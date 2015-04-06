# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425569535.974946
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial/home/templates/base_ajax.htm'
_template_uri = '/home/templates/base_ajax.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('  \r\n\r\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Sub-templates should place their ajax content here.\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"33": 7, "34": 10, "35": 10, "48": 13, "40": 15, "41": 18, "42": 18, "60": 54, "16": 6, "18": 0, "54": 13, "27": 4, "28": 6, "29": 7}, "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial/home/templates/base_ajax.htm", "uri": "/home/templates/base_ajax.htm"}
__M_END_METADATA
"""
