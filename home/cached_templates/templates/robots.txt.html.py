# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428088836.883846
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\home\\templates/robots.txt.html'
_template_uri = 'robots.txt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('User-agent: *<br>\r\nDisallow: /account/media/<br>\r\nDisallow: /base_app/media/<br>\r\nDisallow: /catalog/media/<br>\r\nDisallow: /homepage/media/<br>\r\nDisallow: /account/__pycache__<br>\r\nDisallow: /base_app/__pycache__<br>\r\nDisallow: /catalog/__pycache__<br>\r\nDisallow: /homepage/__pycache__<br>\r\nDisallow: /account/cached_templates<br>\r\nDisallow: /base_app/cached_templates<br>\r\nDisallow: /catalog/cached_templates<br>\r\nDisallow: /homepage/cached_templates<br>\r\nDisallow: /.gitattributes<br>\r\nDisallow: /.gitignore<br>\r\nDisallow: /init_db<br>\r\nDisallow: /manage')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\home\\templates/robots.txt.html", "source_encoding": "ascii", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "robots.txt.html"}
__M_END_METADATA
"""
