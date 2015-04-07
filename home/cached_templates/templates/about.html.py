# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428377078.5394
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\home\\templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'title', 'top_banner']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        def contents():
            return render_contents(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t   \t<div class="row">\r\n            <div class="col-xs-12">\r\n                \r\n             <img id="about_photo" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/sign.jpg" alt="The Signing" >\r\n\r\n    \t\t</div>\r\n        </div> \r\n\r\n\r\n        <div id="text">\r\n\t        <h3>The signing of the Constitution. September 17 1787</h3>\r\n\t        <p>\r\n\t        We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.\r\n\t        </p>\r\n\t    </div>\r\n\r\n\r\n\r\n\t\t<div class="row">\r\n\t\t   \t<div class="col-xs-12">\r\n\r\n             <img id="about_photo" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/washington.jpg" alt="The Signing" >\r\n                \r\n            </div>\r\n        </div> \r\n\r\n        <div id="text">\r\n\t        <h3>General Washington crosses the Delaware. December 26 1776</h3>\r\n\t        <p>\r\n\t        At about 11 p.m. on Christmas, Washingtons army commenced its crossing of the half-frozen river at three locations. The 2,400 soldiers led by Washington successfully braved the icy and freezing river and reached the New Jersey side of the Delaware just before dawn. The other two divisions, made up of some 3,000 men and crucial artillery, failed to reach the meeting point at the appointed time.\r\n\t        </p>\r\n\t    </div>\r\n\r\n\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<title>About Colonial</title>\r\n\t<meta name="Colonial Heritage Foundation Home Page" content="The Colonial Heritage Foundation promotes actively engaging the mind in history. Miss History class? We got you covered. We are sure to be able to answer any questions you have about colonial history. We will not just tell you, but we will show you!">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">About Us</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "about.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\home\\templates/about.html", "source_encoding": "ascii", "line_map": {"66": 14, "67": 19, "68": 19, "69": 37, "70": 37, "39": 1, "44": 6, "76": 3, "27": 0, "49": 10, "82": 3, "88": 8, "100": 94, "59": 14, "94": 8}}
__M_END_METADATA
"""
