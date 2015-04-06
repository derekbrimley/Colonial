# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423297147.50028
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/thankyou.html'
_template_uri = 'thankyou.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
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
        __M_writer('\r\n\t<div class="top_banner">Thank You!</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t   \t<div class="row">\r\n            <div class="col-xs-12">\r\n                \r\n             <img id="about_photo" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/joinordie.jpg" alt="Thank You" >\r\n\r\n    \t\t</div>\r\n        </div> \r\n\r\n\r\n        <div id="text">\r\n\t        <h3>Join or Die (attributed to Benjamin Franklin)</h3>\r\n\t        <p>\r\n\t        This cartoon originally appeared during the French and Indian War. It was recycled to stimulate the American Colonies to unite against the British Rule. We are grateful you have joined us! Together we will preserve our nations Divine History.\r\n\t        </p>\r\n\t    </div>\r\n\t    <div id="form_buttons">\r\n\t    \t<a href="/home/index/" class="btn btn-info">Home</a>\r\n\t    </div>\r\n\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/thankyou.html", "source_encoding": "ascii", "uri": "thankyou.html", "line_map": {"64": 9, "52": 3, "37": 1, "71": 9, "72": 14, "73": 14, "58": 3, "27": 0, "42": 5, "79": 73}}
__M_END_METADATA
"""
