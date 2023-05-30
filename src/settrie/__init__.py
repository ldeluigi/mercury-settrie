# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _py_settrie
else:
    import _py_settrie

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def new_settrie():
    return _py_settrie.new_settrie()

def destroy_settrie(st_id):
    return _py_settrie.destroy_settrie(st_id)

def insert(st_id, set, str_id):
    return _py_settrie.insert(st_id, set, str_id)

def find(st_id, set):
    return _py_settrie.find(st_id, set)

def supersets(st_id, set):
    return _py_settrie.supersets(st_id, set)

def subsets(st_id, set):
    return _py_settrie.subsets(st_id, set)

def iterator_size(iter_id):
    return _py_settrie.iterator_size(iter_id)

def iterator_next(iter_id):
    return _py_settrie.iterator_next(iter_id)

def destroy_iterator(iter_id):
    return _py_settrie.destroy_iterator(iter_id)

def save_as_binary_image(st_id):
    return _py_settrie.save_as_binary_image(st_id)

def push_binary_image_block(st_id, p_block):
    return _py_settrie.push_binary_image_block(st_id, p_block)

def binary_image_size(image_id):
    return _py_settrie.binary_image_size(image_id)

def binary_image_next(image_id):
    return _py_settrie.binary_image_next(image_id)

def destroy_binary_image(image_id):
    return _py_settrie.destroy_binary_image(image_id)


# The source version file is <proj>/src/version.py, anything else is auto generated.
__version__ = '1.4.2'

from settrie.SetTrie import SetTrie
from settrie.SetTrie import Result
