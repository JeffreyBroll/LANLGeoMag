'''Wrapper for DynamicMemory.h

Generated with:
/opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin/ctypesgen.py -l/usr/local/lib/libLanlGeoMag.dylib /usr/local/include/Lgm/DynamicMemory.h /usr/local/include/Lgm/Lgm_AE8_AP8.h /usr/local/include/Lgm/Lgm_CTrans.h /usr/local/include/Lgm/Lgm_DynamicMemory.h /usr/local/include/Lgm/Lgm_Eop.h /usr/local/include/Lgm/Lgm_FieldIntInfo.h /usr/local/include/Lgm/Lgm_FluxToPsd.h /usr/local/include/Lgm/Lgm_IGRF.h /usr/local/include/Lgm/Lgm_LeapSeconds.h /usr/local/include/Lgm/Lgm_LstarInfo.h /usr/local/include/Lgm/Lgm_MagEphemInfo.h /usr/local/include/Lgm/Lgm_MagModelInfo.h /usr/local/include/Lgm/Lgm_Octree.h /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h /usr/local/include/Lgm/Lgm_QuadPack.h /usr/local/include/Lgm/Lgm_Quat.h /usr/local/include/Lgm/Lgm_Sgp.h /usr/local/include/Lgm/Lgm_Vec.h /usr/local/include/Lgm/Lgm_WGS84.h /usr/local/include/Lgm/size.h -o Lgm_Wrap.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["/usr/local/lib/libLanlGeoMag.dylib"] = load_library("/usr/local/lib/libLanlGeoMag.dylib")

# 1 libraries
# End libraries

# No modules

__int64_t = c_longlong # /usr/include/i386/_types.h: 46

__darwin_off_t = __int64_t # /usr/include/sys/_types.h: 110

fpos_t = __darwin_off_t # /usr/include/stdio.h: 87

# /usr/include/stdio.h: 98
class struct___sbuf(Structure):
    pass

struct___sbuf.__slots__ = [
    '_base',
    '_size',
]
struct___sbuf._fields_ = [
    ('_base', POINTER(c_ubyte)),
    ('_size', c_int),
]

# /usr/include/stdio.h: 104
class struct___sFILEX(Structure):
    pass

# /usr/include/stdio.h: 163
class struct___sFILE(Structure):
    pass

struct___sFILE.__slots__ = [
    '_p',
    '_r',
    '_w',
    '_flags',
    '_file',
    '_bf',
    '_lbfsize',
    '_cookie',
    '_close',
    '_read',
    '_seek',
    '_write',
    '_ub',
    '_extra',
    '_ur',
    '_ubuf',
    '_nbuf',
    '_lb',
    '_blksize',
    '_offset',
]
struct___sFILE._fields_ = [
    ('_p', POINTER(c_ubyte)),
    ('_r', c_int),
    ('_w', c_int),
    ('_flags', c_short),
    ('_file', c_short),
    ('_bf', struct___sbuf),
    ('_lbfsize', c_int),
    ('_cookie', POINTER(None)),
    ('_close', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('_read', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_seek', CFUNCTYPE(UNCHECKED(fpos_t), POINTER(None), fpos_t, c_int)),
    ('_write', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_ub', struct___sbuf),
    ('_extra', POINTER(struct___sFILEX)),
    ('_ur', c_int),
    ('_ubuf', c_ubyte * 3),
    ('_nbuf', c_ubyte * 1),
    ('_lb', struct___sbuf),
    ('_blksize', c_int),
    ('_offset', fpos_t),
]

FILE = struct___sFILE # /usr/include/stdio.h: 163

# /usr/local/include/Lgm/Lgm_Vec.h: 7
class struct_Lgm_Vector(Structure):
    pass

struct_Lgm_Vector.__slots__ = [
    'x',
    'y',
    'z',
]
struct_Lgm_Vector._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
]

Lgm_Vector = struct_Lgm_Vector # /usr/local/include/Lgm/Lgm_Vec.h: 7

# /usr/local/include/Lgm/Lgm_Vec.h: 13
class struct_LgmPosition(Structure):
    pass

struct_LgmPosition.__slots__ = [
    'x',
    'y',
    'z',
]
struct_LgmPosition._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
]

LgmPosition = struct_LgmPosition # /usr/local/include/Lgm/Lgm_Vec.h: 13

# /usr/local/include/Lgm/Lgm_Vec.h: 15
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CreateVector'):
    Lgm_CreateVector = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CreateVector
    Lgm_CreateVector.argtypes = [c_double, c_double, c_double]
    Lgm_CreateVector.restype = POINTER(Lgm_Vector)

# /usr/local/include/Lgm/Lgm_Vec.h: 16
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CrossProduct'):
    Lgm_CrossProduct = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CrossProduct
    Lgm_CrossProduct.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_CrossProduct.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 17
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DotProduct'):
    Lgm_DotProduct = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DotProduct
    Lgm_DotProduct.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_DotProduct.restype = c_double

# /usr/local/include/Lgm/Lgm_Vec.h: 18
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_NormalizeVector'):
    Lgm_NormalizeVector = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_NormalizeVector
    Lgm_NormalizeVector.argtypes = [POINTER(Lgm_Vector)]
    Lgm_NormalizeVector.restype = c_double

# /usr/local/include/Lgm/Lgm_Vec.h: 19
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ScaleVector'):
    Lgm_ScaleVector = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ScaleVector
    Lgm_ScaleVector.argtypes = [POINTER(Lgm_Vector), c_double]
    Lgm_ScaleVector.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 20
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Magnitude'):
    Lgm_Magnitude = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Magnitude
    Lgm_Magnitude.argtypes = [POINTER(Lgm_Vector)]
    Lgm_Magnitude.restype = c_double

# /usr/local/include/Lgm/Lgm_Vec.h: 21
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ForceMagnitude'):
    Lgm_ForceMagnitude = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ForceMagnitude
    Lgm_ForceMagnitude.argtypes = [POINTER(Lgm_Vector), c_double]
    Lgm_ForceMagnitude.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 22
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MatTimesVec'):
    Lgm_MatTimesVec = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MatTimesVec
    Lgm_MatTimesVec.argtypes = [(c_double * 3) * 3, POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_MatTimesVec.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 23
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MatTimesMat'):
    Lgm_MatTimesMat = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MatTimesMat
    Lgm_MatTimesMat.argtypes = [(c_double * 3) * 3, (c_double * 3) * 3, (c_double * 3) * 3]
    Lgm_MatTimesMat.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 24
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_VecSub'):
    Lgm_VecSub = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_VecSub
    Lgm_VecSub.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_VecSub.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 25
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_VecAdd'):
    Lgm_VecAdd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_VecAdd
    Lgm_VecAdd.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_VecAdd.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 26
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_VecDiffMag'):
    Lgm_VecDiffMag = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_VecDiffMag
    Lgm_VecDiffMag.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_VecDiffMag.restype = c_double

# /usr/local/include/Lgm/Lgm_Vec.h: 27
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Transpose'):
    Lgm_Transpose = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Transpose
    Lgm_Transpose.argtypes = [(c_double * 3) * 3, (c_double * 3) * 3]
    Lgm_Transpose.restype = None

# /usr/local/include/Lgm/Lgm_Vec.h: 28
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_SphToCartCoords'):
    Lgm_SphToCartCoords = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_SphToCartCoords
    Lgm_SphToCartCoords.argtypes = [c_double, c_double, c_double, POINTER(Lgm_Vector)]
    Lgm_SphToCartCoords.restype = None

_qpInfo = c_int # /usr/local/include/Lgm/Lgm_QuadPack.h: 20

# /usr/local/include/Lgm/Lgm_QuadPack.h: 23
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'd1mach'):
    d1mach = _libs['/usr/local/lib/libLanlGeoMag.dylib'].d1mach
    d1mach.argtypes = [c_int]
    d1mach.restype = c_double

# /usr/local/include/Lgm/Lgm_QuadPack.h: 25
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqags'):
    dqags = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqags
    dqags.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double, POINTER(_qpInfo)), POINTER(_qpInfo), c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    dqags.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 29
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqagse'):
    dqagse = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqagse
    dqagse.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double, POINTER(_qpInfo)), POINTER(_qpInfo), c_double, c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int)]
    dqagse.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 35
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqagp'):
    dqagp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqagp
    dqagp.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double, POINTER(_qpInfo)), POINTER(_qpInfo), c_double, c_double, c_int, POINTER(c_double), c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    dqagp.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 40
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqagpe'):
    dqagpe = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqagpe
    dqagpe.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double, POINTER(_qpInfo)), POINTER(_qpInfo), c_double, c_double, c_int, POINTER(c_double), c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    dqagpe.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 47
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqk21'):
    dqk21 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqk21
    dqk21.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double, POINTER(_qpInfo)), POINTER(_qpInfo), c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    dqk21.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 50
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqelg'):
    dqelg = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqelg
    dqelg.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    dqelg.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 53
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'dqpsrt'):
    dqpsrt = _libs['/usr/local/lib/libLanlGeoMag.dylib'].dqpsrt
    dqpsrt.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int)]
    dqpsrt.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 434
class struct_Lgm_LeapSeconds(Structure):
    pass

struct_Lgm_LeapSeconds.__slots__ = [
    'nLeapSecondDates',
    'LeapSecondDates',
    'LeapSecondJDs',
    'LeapSeconds',
]
struct_Lgm_LeapSeconds._fields_ = [
    ('nLeapSecondDates', c_int),
    ('LeapSecondDates', POINTER(c_long)),
    ('LeapSecondJDs', POINTER(c_double)),
    ('LeapSeconds', POINTER(c_double)),
]

Lgm_LeapSeconds = struct_Lgm_LeapSeconds # /usr/local/include/Lgm/Lgm_CTrans.h: 434

# /usr/local/include/Lgm/Lgm_CTrans.h: 480
class struct_Lgm_DateTime(Structure):
    pass

struct_Lgm_DateTime.__slots__ = [
    'Date',
    'Year',
    'Month',
    'Day',
    'Doy',
    'Time',
    'Hour',
    'Minute',
    'Second',
    'Week',
    'wYear',
    'Dow',
    'DowStr',
    'fYear',
    'JD',
    'T',
    'DaySeconds',
    'TZD_sgn',
    'TZD_hh',
    'TZD_mm',
    'TimeSystem',
]
struct_Lgm_DateTime._fields_ = [
    ('Date', c_long),
    ('Year', c_int),
    ('Month', c_int),
    ('Day', c_int),
    ('Doy', c_int),
    ('Time', c_double),
    ('Hour', c_int),
    ('Minute', c_int),
    ('Second', c_double),
    ('Week', c_int),
    ('wYear', c_int),
    ('Dow', c_int),
    ('DowStr', c_char * 10),
    ('fYear', c_double),
    ('JD', c_double),
    ('T', c_double),
    ('DaySeconds', c_double),
    ('TZD_sgn', c_int),
    ('TZD_hh', c_int),
    ('TZD_mm', c_int),
    ('TimeSystem', c_int),
]

Lgm_DateTime = struct_Lgm_DateTime # /usr/local/include/Lgm/Lgm_CTrans.h: 480

# /usr/local/include/Lgm/Lgm_CTrans.h: 713
class struct_Lgm_CTrans(Structure):
    pass

struct_Lgm_CTrans.__slots__ = [
    'Verbose',
    'l',
    'UT1',
    'UTC',
    'DUT1',
    'LOD',
    'TAI',
    'GPS',
    'DAT',
    'TT',
    'TDB',
    'TCG',
    'gmst',
    'gast',
    'xp',
    'yp',
    'epsilon',
    'epsilon_true',
    'eccentricity',
    'lambda_sun',
    'earth_sun_dist',
    'RA_sun',
    'DEC_sun',
    'lambda_sun_ha',
    'r_sun_ha',
    'beta_sun_ha',
    'RA_sun_ha',
    'DEC_sun_ha',
    'Sun',
    'EcPole',
    'psi',
    'sin_psi',
    'cos_psi',
    'tan_psi',
    'RA_moon',
    'DEC_moon',
    'MoonPhase',
    'EarthMoonDistance',
    'M_cd',
    'M_cd_McIllwain',
    'CD_gcolat',
    'CD_glon',
    'ED_x0',
    'ED_y0',
    'ED_z0',
    'Zeta',
    'Theta',
    'Zee',
    'nNutationTerms',
    'dPsi',
    'dEps',
    'dPsiCosEps',
    'dPsiSinEps',
    'ddPsi',
    'ddEps',
    'EQ_Eq',
    'OmegaMoon',
    'dX',
    'dY',
    'Agei_to_mod',
    'Amod_to_gei',
    'Amod_to_tod',
    'Atod_to_mod',
    'Ateme_to_pef',
    'Apef_to_teme',
    'Apef_to_tod',
    'Atod_to_pef',
    'Awgs84_to_pef',
    'Apef_to_wgs84',
    'Agse_to_mod',
    'Amod_to_gse',
    'Asm_to_gsm',
    'Agsm_to_sm',
    'Agsm_to_mod',
    'Amod_to_gsm',
    'Agsm_to_gse',
    'Agse_to_gsm',
    'Awgs84_to_mod',
    'Amod_to_wgs84',
    'Awgs84_to_gei',
    'Agei_to_wgs84',
    'Agsm_to_wgs84',
    'Awgs84_to_gsm',
    'Awgs84_to_cdmag',
    'Acdmag_to_wgs84',
    'Lgm_IGRF_FirstCall',
    'Lgm_IGRF_OldYear',
    'Lgm_IGRF_g',
    'Lgm_IGRF_h',
    'Lgm_IGRF_R',
    'Lgm_IGRF_K',
    'Lgm_IGRF_S',
    'Lgm_IGRF_TwoNm1_Over_NmM',
    'Lgm_IGRF_NpMm1_Over_NmM',
    'Lgm_IGRF_SqrtNM1',
    'Lgm_IGRF_SqrtNM2',
]
struct_Lgm_CTrans._fields_ = [
    ('Verbose', c_int),
    ('l', Lgm_LeapSeconds),
    ('UT1', Lgm_DateTime),
    ('UTC', Lgm_DateTime),
    ('DUT1', c_double),
    ('LOD', c_double),
    ('TAI', Lgm_DateTime),
    ('GPS', Lgm_DateTime),
    ('DAT', c_double),
    ('TT', Lgm_DateTime),
    ('TDB', Lgm_DateTime),
    ('TCG', Lgm_DateTime),
    ('gmst', c_double),
    ('gast', c_double),
    ('xp', c_double),
    ('yp', c_double),
    ('epsilon', c_double),
    ('epsilon_true', c_double),
    ('eccentricity', c_double),
    ('lambda_sun', c_double),
    ('earth_sun_dist', c_double),
    ('RA_sun', c_double),
    ('DEC_sun', c_double),
    ('lambda_sun_ha', c_double),
    ('r_sun_ha', c_double),
    ('beta_sun_ha', c_double),
    ('RA_sun_ha', c_double),
    ('DEC_sun_ha', c_double),
    ('Sun', Lgm_Vector),
    ('EcPole', Lgm_Vector),
    ('psi', c_double),
    ('sin_psi', c_double),
    ('cos_psi', c_double),
    ('tan_psi', c_double),
    ('RA_moon', c_double),
    ('DEC_moon', c_double),
    ('MoonPhase', c_double),
    ('EarthMoonDistance', c_double),
    ('M_cd', c_double),
    ('M_cd_McIllwain', c_double),
    ('CD_gcolat', c_double),
    ('CD_glon', c_double),
    ('ED_x0', c_double),
    ('ED_y0', c_double),
    ('ED_z0', c_double),
    ('Zeta', c_double),
    ('Theta', c_double),
    ('Zee', c_double),
    ('nNutationTerms', c_int),
    ('dPsi', c_double),
    ('dEps', c_double),
    ('dPsiCosEps', c_double),
    ('dPsiSinEps', c_double),
    ('ddPsi', c_double),
    ('ddEps', c_double),
    ('EQ_Eq', c_double),
    ('OmegaMoon', c_double),
    ('dX', c_double),
    ('dY', c_double),
    ('Agei_to_mod', (c_double * 3) * 3),
    ('Amod_to_gei', (c_double * 3) * 3),
    ('Amod_to_tod', (c_double * 3) * 3),
    ('Atod_to_mod', (c_double * 3) * 3),
    ('Ateme_to_pef', (c_double * 3) * 3),
    ('Apef_to_teme', (c_double * 3) * 3),
    ('Apef_to_tod', (c_double * 3) * 3),
    ('Atod_to_pef', (c_double * 3) * 3),
    ('Awgs84_to_pef', (c_double * 3) * 3),
    ('Apef_to_wgs84', (c_double * 3) * 3),
    ('Agse_to_mod', (c_double * 3) * 3),
    ('Amod_to_gse', (c_double * 3) * 3),
    ('Asm_to_gsm', (c_double * 3) * 3),
    ('Agsm_to_sm', (c_double * 3) * 3),
    ('Agsm_to_mod', (c_double * 3) * 3),
    ('Amod_to_gsm', (c_double * 3) * 3),
    ('Agsm_to_gse', (c_double * 3) * 3),
    ('Agse_to_gsm', (c_double * 3) * 3),
    ('Awgs84_to_mod', (c_double * 3) * 3),
    ('Amod_to_wgs84', (c_double * 3) * 3),
    ('Awgs84_to_gei', (c_double * 3) * 3),
    ('Agei_to_wgs84', (c_double * 3) * 3),
    ('Agsm_to_wgs84', (c_double * 3) * 3),
    ('Awgs84_to_gsm', (c_double * 3) * 3),
    ('Awgs84_to_cdmag', (c_double * 3) * 3),
    ('Acdmag_to_wgs84', (c_double * 3) * 3),
    ('Lgm_IGRF_FirstCall', c_int),
    ('Lgm_IGRF_OldYear', c_double),
    ('Lgm_IGRF_g', (c_double * 13) * 13),
    ('Lgm_IGRF_h', (c_double * 13) * 13),
    ('Lgm_IGRF_R', (c_double * 13) * 13),
    ('Lgm_IGRF_K', (c_double * 13) * 13),
    ('Lgm_IGRF_S', (c_double * 13) * 13),
    ('Lgm_IGRF_TwoNm1_Over_NmM', (c_double * 13) * 13),
    ('Lgm_IGRF_NpMm1_Over_NmM', (c_double * 13) * 13),
    ('Lgm_IGRF_SqrtNM1', (c_double * 13) * 13),
    ('Lgm_IGRF_SqrtNM2', (c_double * 13) * 13),
]

Lgm_CTrans = struct_Lgm_CTrans # /usr/local/include/Lgm/Lgm_CTrans.h: 713

# /usr/local/include/Lgm/Lgm_CTrans.h: 716
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_free_ctrans'):
    Lgm_free_ctrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_free_ctrans
    Lgm_free_ctrans.argtypes = [POINTER(Lgm_CTrans)]
    Lgm_free_ctrans.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 717
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_init_ctrans'):
    Lgm_init_ctrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_init_ctrans
    Lgm_init_ctrans.argtypes = [c_int]
    Lgm_init_ctrans.restype = POINTER(Lgm_CTrans)

# /usr/local/include/Lgm/Lgm_CTrans.h: 718
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CopyCTrans'):
    Lgm_CopyCTrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CopyCTrans
    Lgm_CopyCTrans.argtypes = [POINTER(Lgm_CTrans)]
    Lgm_CopyCTrans.restype = POINTER(Lgm_CTrans)

# /usr/local/include/Lgm/Lgm_CTrans.h: 720
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Radec_to_Cart'):
    Lgm_Radec_to_Cart = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Radec_to_Cart
    Lgm_Radec_to_Cart.argtypes = [c_double, c_double, POINTER(Lgm_Vector)]
    Lgm_Radec_to_Cart.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 721
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_angle2pi'):
    Lgm_angle2pi = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_angle2pi
    Lgm_angle2pi.argtypes = [c_double]
    Lgm_angle2pi.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 722
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_angle360'):
    Lgm_angle360 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_angle360
    Lgm_angle360.argtypes = [c_double]
    Lgm_angle360.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 724
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_LeapYear'):
    Lgm_LeapYear = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_LeapYear
    Lgm_LeapYear.argtypes = [c_int]
    Lgm_LeapYear.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 726
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_JDN'):
    Lgm_JDN = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_JDN
    Lgm_JDN.argtypes = [c_int, c_int, c_int]
    Lgm_JDN.restype = c_long

# /usr/local/include/Lgm/Lgm_CTrans.h: 728
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_JD'):
    Lgm_JD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_JD
    Lgm_JD.argtypes = [c_int, c_int, c_int, c_double, c_int, POINTER(Lgm_CTrans)]
    Lgm_JD.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 729
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_JD_to_Date'):
    Lgm_JD_to_Date = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_JD_to_Date
    Lgm_JD_to_Date.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_JD_to_Date.restype = c_long

# /usr/local/include/Lgm/Lgm_CTrans.h: 730
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Date_to_JD'):
    Lgm_Date_to_JD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Date_to_JD
    Lgm_Date_to_JD.argtypes = [c_long, c_double, POINTER(Lgm_CTrans)]
    Lgm_Date_to_JD.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 731
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_jd_to_ymdh'):
    Lgm_jd_to_ymdh = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_jd_to_ymdh
    Lgm_jd_to_ymdh.argtypes = [c_double, POINTER(c_long), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_jd_to_ymdh.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 732
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DayOfYear'):
    Lgm_DayOfYear = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DayOfYear
    Lgm_DayOfYear.argtypes = [c_int, c_int, c_int, POINTER(Lgm_CTrans)]
    Lgm_DayOfYear.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 734
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MJD'):
    Lgm_MJD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MJD
    Lgm_MJD.argtypes = [c_int, c_int, c_int, c_double, c_int, POINTER(Lgm_CTrans)]
    Lgm_MJD.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 735
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MJD_to_Date'):
    Lgm_MJD_to_Date = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MJD_to_Date
    Lgm_MJD_to_Date.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_MJD_to_Date.restype = c_long

# /usr/local/include/Lgm/Lgm_CTrans.h: 736
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_mjd_to_ymdh'):
    Lgm_mjd_to_ymdh = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_mjd_to_ymdh
    Lgm_mjd_to_ymdh.argtypes = [c_double, POINTER(c_long), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_mjd_to_ymdh.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 738
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_hour24'):
    Lgm_hour24 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_hour24
    Lgm_hour24.argtypes = [c_double]
    Lgm_hour24.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 739
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_kepler'):
    Lgm_kepler = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_kepler
    Lgm_kepler.argtypes = [c_double, c_double]
    Lgm_kepler.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 740
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Coord_Transforms'):
    Lgm_Set_Coord_Transforms = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Coord_Transforms
    Lgm_Set_Coord_Transforms.argtypes = [c_long, c_double, POINTER(Lgm_CTrans)]
    Lgm_Set_Coord_Transforms.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 741
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Convert_Coords'):
    Lgm_Convert_Coords = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Convert_Coords
    Lgm_Convert_Coords.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_int, POINTER(Lgm_CTrans)]
    Lgm_Convert_Coords.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 742
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_IsValidDate'):
    Lgm_IsValidDate = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_IsValidDate
    Lgm_IsValidDate.argtypes = [c_long]
    Lgm_IsValidDate.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 743
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Doy'):
    Lgm_Doy = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Doy
    Lgm_Doy.argtypes = [c_long, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Lgm_Doy.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 744
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UT_to_hmsms'):
    Lgm_UT_to_hmsms = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UT_to_hmsms
    Lgm_UT_to_hmsms.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Lgm_UT_to_hmsms.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 745
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UT_to_HMS'):
    Lgm_UT_to_HMS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UT_to_HMS
    Lgm_UT_to_HMS.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Lgm_UT_to_HMS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 746
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UT_to_HMSd'):
    Lgm_UT_to_HMSd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UT_to_HMSd
    Lgm_UT_to_HMSd.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_UT_to_HMSd.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 747
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_D_to_DMS'):
    Lgm_D_to_DMS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_D_to_DMS
    Lgm_D_to_DMS.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Lgm_D_to_DMS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 748
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_D_to_DMSd'):
    Lgm_D_to_DMSd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_D_to_DMSd
    Lgm_D_to_DMSd.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    Lgm_D_to_DMSd.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 749
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_HMS'):
    Lgm_Print_HMS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_HMS
    Lgm_Print_HMS.argtypes = [c_double]
    Lgm_Print_HMS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 750
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_HMSd'):
    Lgm_Print_HMSd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_HMSd
    Lgm_Print_HMSd.argtypes = [c_double]
    Lgm_Print_HMSd.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 751
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_HMSdp'):
    Lgm_Print_HMSdp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_HMSdp
    Lgm_Print_HMSdp.argtypes = [c_double, c_int, c_int]
    Lgm_Print_HMSdp.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 752
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_DMS'):
    Lgm_Print_DMS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_DMS
    Lgm_Print_DMS.argtypes = [c_double]
    Lgm_Print_DMS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 753
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_DMSd'):
    Lgm_Print_DMSd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_DMSd
    Lgm_Print_DMSd.argtypes = [c_double]
    Lgm_Print_DMSd.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 754
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GetCurrentJD'):
    Lgm_GetCurrentJD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GetCurrentJD
    Lgm_GetCurrentJD.argtypes = [POINTER(Lgm_CTrans)]
    Lgm_GetCurrentJD.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 755
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GetCurrentMJD'):
    Lgm_GetCurrentMJD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GetCurrentMJD
    Lgm_GetCurrentMJD.argtypes = [POINTER(Lgm_CTrans)]
    Lgm_GetCurrentMJD.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 756
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_SunPosition'):
    Lgm_SunPosition = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_SunPosition
    Lgm_SunPosition.argtypes = [c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_SunPosition.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 757
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GLATLON_TO_CDMLATLONMLT'):
    Lgm_GLATLON_TO_CDMLATLONMLT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GLATLON_TO_CDMLATLONMLT
    Lgm_GLATLON_TO_CDMLATLONMLT.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(Lgm_CTrans)]
    Lgm_GLATLON_TO_CDMLATLONMLT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 758
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GLATLON_TO_EDMLATLONMLT'):
    Lgm_GLATLON_TO_EDMLATLONMLT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GLATLON_TO_EDMLATLONMLT
    Lgm_GLATLON_TO_EDMLATLONMLT.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(Lgm_CTrans)]
    Lgm_GLATLON_TO_EDMLATLONMLT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 759
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CDMAG_to_R_MLAT_MLON_MLT'):
    Lgm_CDMAG_to_R_MLAT_MLON_MLT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CDMAG_to_R_MLAT_MLON_MLT
    Lgm_CDMAG_to_R_MLAT_MLON_MLT.argtypes = [POINTER(Lgm_Vector), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(Lgm_CTrans)]
    Lgm_CDMAG_to_R_MLAT_MLON_MLT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 760
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_R_MLAT_MLT_to_CDMAG'):
    Lgm_R_MLAT_MLT_to_CDMAG = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_R_MLAT_MLT_to_CDMAG
    Lgm_R_MLAT_MLT_to_CDMAG.argtypes = [c_double, c_double, c_double, POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_R_MLAT_MLT_to_CDMAG.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 761
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_EDMAG_to_R_MLAT_MLON_MLT'):
    Lgm_EDMAG_to_R_MLAT_MLON_MLT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_EDMAG_to_R_MLAT_MLON_MLT
    Lgm_EDMAG_to_R_MLAT_MLON_MLT.argtypes = [POINTER(Lgm_Vector), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(Lgm_CTrans)]
    Lgm_EDMAG_to_R_MLAT_MLON_MLT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 762
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_R_MLAT_MLT_to_EDMAG'):
    Lgm_R_MLAT_MLT_to_EDMAG = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_R_MLAT_MLT_to_EDMAG
    Lgm_R_MLAT_MLT_to_EDMAG.argtypes = [c_double, c_double, c_double, POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_R_MLAT_MLT_to_EDMAG.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 763
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_WGS84_to_GEOD'):
    Lgm_WGS84_to_GEOD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_WGS84_to_GEOD
    Lgm_WGS84_to_GEOD.argtypes = [POINTER(Lgm_Vector), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_WGS84_to_GEOD.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 764
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_WGS84_to_GeodHeight'):
    Lgm_WGS84_to_GeodHeight = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_WGS84_to_GeodHeight
    Lgm_WGS84_to_GeodHeight.argtypes = [POINTER(Lgm_Vector), POINTER(c_double)]
    Lgm_WGS84_to_GeodHeight.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 765
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GEOD_to_WGS84'):
    Lgm_GEOD_to_WGS84 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GEOD_to_WGS84
    Lgm_GEOD_to_WGS84.argtypes = [c_double, c_double, c_double, POINTER(Lgm_Vector)]
    Lgm_GEOD_to_WGS84.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 766
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Nutation'):
    Lgm_Nutation = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Nutation
    Lgm_Nutation.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double)]
    Lgm_Nutation.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 767
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'IsoTimeStringToDateTime'):
    IsoTimeStringToDateTime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].IsoTimeStringToDateTime
    IsoTimeStringToDateTime.argtypes = [String, POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    IsoTimeStringToDateTime.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 768
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MonthStrToNum'):
    MonthStrToNum = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MonthStrToNum
    MonthStrToNum.argtypes = [String]
    MonthStrToNum.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 769
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_StrToLower'):
    Lgm_StrToLower = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_StrToLower
    Lgm_StrToLower.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Lgm_StrToLower.restype = ReturnString
    else:
        Lgm_StrToLower.restype = String
        Lgm_StrToLower.errcheck = ReturnString

# /usr/local/include/Lgm/Lgm_CTrans.h: 770
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_StrToUpper'):
    Lgm_StrToUpper = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_StrToUpper
    Lgm_StrToUpper.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Lgm_StrToUpper.restype = ReturnString
    else:
        Lgm_StrToUpper.restype = String
        Lgm_StrToUpper.errcheck = ReturnString

# /usr/local/include/Lgm/Lgm_CTrans.h: 775
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DateTime_Create'):
    Lgm_DateTime_Create = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DateTime_Create
    Lgm_DateTime_Create.argtypes = [c_int, c_int, c_int, c_double, c_int, POINTER(Lgm_CTrans)]
    Lgm_DateTime_Create.restype = POINTER(Lgm_DateTime)

# /usr/local/include/Lgm/Lgm_CTrans.h: 776
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Make_UTC'):
    Lgm_Make_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Make_UTC
    Lgm_Make_UTC.argtypes = [c_long, c_double, POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_Make_UTC.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 777
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_LoadLeapSeconds'):
    Lgm_LoadLeapSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_LoadLeapSeconds
    Lgm_LoadLeapSeconds.argtypes = [POINTER(Lgm_CTrans)]
    Lgm_LoadLeapSeconds.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 778
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GetLeapSeconds'):
    Lgm_GetLeapSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GetLeapSeconds
    Lgm_GetLeapSeconds.argtypes = [c_double, POINTER(Lgm_CTrans)]
    Lgm_GetLeapSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 779
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_IsLeapSecondDay'):
    Lgm_IsLeapSecondDay = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_IsLeapSecondDay
    Lgm_IsLeapSecondDay.argtypes = [c_long, POINTER(c_double), POINTER(Lgm_CTrans)]
    Lgm_IsLeapSecondDay.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 780
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TAI'):
    Lgm_UTC_to_TAI = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TAI
    Lgm_UTC_to_TAI.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_UTC_to_TAI.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 781
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TAI_to_UTC'):
    Lgm_TAI_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TAI_to_UTC
    Lgm_TAI_to_UTC.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TAI_to_UTC.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 782
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TT_to_TAI'):
    Lgm_TT_to_TAI = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TT_to_TAI
    Lgm_TT_to_TAI.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TT_to_TAI.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 783
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TAI_to_TT'):
    Lgm_TAI_to_TT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TAI_to_TT
    Lgm_TAI_to_TT.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TAI_to_TT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 784
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TT_to_TDB'):
    Lgm_TT_to_TDB = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TT_to_TDB
    Lgm_TT_to_TDB.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TT_to_TDB.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 785
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TDB_to_TT'):
    Lgm_TDB_to_TT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TDB_to_TT
    Lgm_TDB_to_TT.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TDB_to_TT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 786
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TT'):
    Lgm_UTC_to_TT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TT
    Lgm_UTC_to_TT.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_UTC_to_TT.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 787
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TT_to_UTC'):
    Lgm_TT_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TT_to_UTC
    Lgm_TT_to_UTC.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TT_to_UTC.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 788
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TAI_to_GPS'):
    Lgm_TAI_to_GPS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TAI_to_GPS
    Lgm_TAI_to_GPS.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TAI_to_GPS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 789
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GPS_to_TAI'):
    Lgm_GPS_to_TAI = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GPS_to_TAI
    Lgm_GPS_to_TAI.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_GPS_to_TAI.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 790
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_GPS'):
    Lgm_UTC_to_GPS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_GPS
    Lgm_UTC_to_GPS.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_UTC_to_GPS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 791
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GPS_to_UTC'):
    Lgm_GPS_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GPS_to_UTC
    Lgm_GPS_to_UTC.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_GPS_to_UTC.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 792
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_DateTime'):
    Lgm_Print_DateTime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_DateTime
    Lgm_Print_DateTime.argtypes = [Lgm_DateTime, c_int, c_int]
    Lgm_Print_DateTime.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 793
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DateTimeToString'):
    Lgm_DateTimeToString = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DateTimeToString
    Lgm_DateTimeToString.argtypes = [String, Lgm_DateTime, c_int, c_int]
    Lgm_DateTimeToString.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 794
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Print_SimpleTime'):
    Lgm_Print_SimpleTime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Print_SimpleTime
    Lgm_Print_SimpleTime.argtypes = [POINTER(Lgm_DateTime), c_int, String]
    Lgm_Print_SimpleTime.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 796
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DayOfWeek'):
    Lgm_DayOfWeek = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DayOfWeek
    Lgm_DayOfWeek.argtypes = [c_int, c_int, c_int, String]
    Lgm_DayOfWeek.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 797
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_JDNofWeek1'):
    Lgm_JDNofWeek1 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_JDNofWeek1
    Lgm_JDNofWeek1.argtypes = [c_int]
    Lgm_JDNofWeek1.restype = c_long

# /usr/local/include/Lgm/Lgm_CTrans.h: 798
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MaxWeekNumber'):
    Lgm_MaxWeekNumber = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MaxWeekNumber
    Lgm_MaxWeekNumber.argtypes = [c_int]
    Lgm_MaxWeekNumber.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 799
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ISO_WeekNumber'):
    Lgm_ISO_WeekNumber = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ISO_WeekNumber
    Lgm_ISO_WeekNumber.argtypes = [c_int, c_int, c_int, POINTER(c_int)]
    Lgm_ISO_WeekNumber.restype = c_int

# /usr/local/include/Lgm/Lgm_CTrans.h: 800
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ISO_YearWeekDow_to_Date'):
    Lgm_ISO_YearWeekDow_to_Date = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ISO_YearWeekDow_to_Date
    Lgm_ISO_YearWeekDow_to_Date.argtypes = [c_int, c_int, c_int, POINTER(c_long), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Lgm_ISO_YearWeekDow_to_Date.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 801
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_RemapTime'):
    Lgm_RemapTime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_RemapTime
    Lgm_RemapTime.argtypes = [c_double, c_double]
    Lgm_RemapTime.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 803
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GPS_to_GpsSeconds'):
    Lgm_GPS_to_GpsSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GPS_to_GpsSeconds
    Lgm_GPS_to_GpsSeconds.argtypes = [POINTER(Lgm_DateTime)]
    Lgm_GPS_to_GpsSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 804
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GpsSeconds_to_GPS'):
    Lgm_GpsSeconds_to_GPS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GpsSeconds_to_GPS
    Lgm_GpsSeconds_to_GPS.argtypes = [c_double, POINTER(Lgm_DateTime)]
    Lgm_GpsSeconds_to_GPS.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 805
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GpsSeconds_to_UTC'):
    Lgm_GpsSeconds_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GpsSeconds_to_UTC
    Lgm_GpsSeconds_to_UTC.argtypes = [c_double, POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_GpsSeconds_to_UTC.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 806
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_GpsSeconds'):
    Lgm_UTC_to_GpsSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_GpsSeconds
    Lgm_UTC_to_GpsSeconds.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_UTC_to_GpsSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 808
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TAI_to_TaiSeconds'):
    Lgm_TAI_to_TaiSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TAI_to_TaiSeconds
    Lgm_TAI_to_TaiSeconds.argtypes = [POINTER(Lgm_DateTime)]
    Lgm_TAI_to_TaiSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 809
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Lgm_TaiSeconds_to_GPS'):
        continue
    Lgm_TaiSeconds_to_GPS = _lib.Lgm_TaiSeconds_to_GPS
    Lgm_TaiSeconds_to_GPS.argtypes = [c_double, POINTER(Lgm_DateTime)]
    Lgm_TaiSeconds_to_GPS.restype = None
    break

# /usr/local/include/Lgm/Lgm_CTrans.h: 810
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TaiSeconds_to_UTC'):
    Lgm_TaiSeconds_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TaiSeconds_to_UTC
    Lgm_TaiSeconds_to_UTC.argtypes = [c_double, POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TaiSeconds_to_UTC.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 811
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TaiSeconds'):
    Lgm_UTC_to_TaiSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TaiSeconds
    Lgm_UTC_to_TaiSeconds.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_UTC_to_TaiSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 814
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'TAISecondsSinceJ2000'):
        continue
    TAISecondsSinceJ2000 = _lib.TAISecondsSinceJ2000
    TAISecondsSinceJ2000.argtypes = [c_double, POINTER(Lgm_CTrans)]
    TAISecondsSinceJ2000.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_CTrans.h: 815
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'UTCDaysSinceJ2000'):
        continue
    UTCDaysSinceJ2000 = _lib.UTCDaysSinceJ2000
    UTCDaysSinceJ2000.argtypes = [c_double, POINTER(Lgm_CTrans)]
    UTCDaysSinceJ2000.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_CTrans.h: 817
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TDBSecSinceJ2000'):
    Lgm_TDBSecSinceJ2000 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TDBSecSinceJ2000
    Lgm_TDBSecSinceJ2000.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_CTrans)]
    Lgm_TDBSecSinceJ2000.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 836
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_igrf_ctrans'):
    Lgm_B_igrf_ctrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_igrf_ctrans
    Lgm_B_igrf_ctrans.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_B_igrf_ctrans.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 837
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_cdip_ctrans'):
    Lgm_B_cdip_ctrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_cdip_ctrans
    Lgm_B_cdip_ctrans.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_B_cdip_ctrans.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 838
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_edip_ctrans'):
    Lgm_B_edip_ctrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_edip_ctrans
    Lgm_B_edip_ctrans.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_B_edip_ctrans.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 844
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Factorial'):
    Lgm_Factorial = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Factorial
    Lgm_Factorial.argtypes = [c_int]
    Lgm_Factorial.restype = c_double

# /usr/local/include/Lgm/Lgm_CTrans.h: 845
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitIGRF'):
    Lgm_InitIGRF = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitIGRF
    Lgm_InitIGRF.argtypes = [(c_double * 13) * 13, (c_double * 13) * 13, c_int, c_int, POINTER(Lgm_CTrans)]
    Lgm_InitIGRF.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 846
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitPnm'):
    Lgm_InitPnm = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitPnm
    Lgm_InitPnm.argtypes = [c_double, c_double, (c_double * 13) * 13, (c_double * 13) * 13, (c_double * 13) * 13, c_int, POINTER(Lgm_CTrans)]
    Lgm_InitPnm.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 847
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitTrigmp'):
    Lgm_InitTrigmp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitTrigmp
    Lgm_InitTrigmp.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), c_int]
    Lgm_InitTrigmp.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 848
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_PolFunInt'):
    Lgm_PolFunInt = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_PolFunInt
    Lgm_PolFunInt.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    Lgm_PolFunInt.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 849
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_RatFunInt'):
    Lgm_RatFunInt = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_RatFunInt
    Lgm_RatFunInt.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    Lgm_RatFunInt.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 850
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_IGRF'):
    Lgm_IGRF = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_IGRF
    Lgm_IGRF.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    Lgm_IGRF.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 851
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], '_Lgm_IGRF'):
    _Lgm_IGRF = _libs['/usr/local/lib/libLanlGeoMag.dylib']._Lgm_IGRF
    _Lgm_IGRF.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    _Lgm_IGRF.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 852
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], '_Lgm_IGRF2'):
    _Lgm_IGRF2 = _libs['/usr/local/lib/libLanlGeoMag.dylib']._Lgm_IGRF2
    _Lgm_IGRF2.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    _Lgm_IGRF2.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 853
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], '_Lgm_IGRF3'):
    _Lgm_IGRF3 = _libs['/usr/local/lib/libLanlGeoMag.dylib']._Lgm_IGRF3
    _Lgm_IGRF3.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    _Lgm_IGRF3.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 854
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], '_Lgm_IGRF4'):
    _Lgm_IGRF4 = _libs['/usr/local/lib/libLanlGeoMag.dylib']._Lgm_IGRF4
    _Lgm_IGRF4.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_CTrans)]
    _Lgm_IGRF4.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 856
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitdPnm'):
    Lgm_InitdPnm = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitdPnm
    Lgm_InitdPnm.argtypes = [(c_double * 13) * 13, (c_double * 13) * 13, c_int, POINTER(Lgm_CTrans)]
    Lgm_InitdPnm.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 857
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitSqrtFuncs'):
    Lgm_InitSqrtFuncs = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitSqrtFuncs
    Lgm_InitSqrtFuncs.argtypes = [(c_double * 13) * 13, (c_double * 13) * 13, c_int]
    Lgm_InitSqrtFuncs.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 858
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitK'):
    Lgm_InitK = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitK
    Lgm_InitK.argtypes = [(c_double * 13) * 13, c_int]
    Lgm_InitK.restype = None

# /usr/local/include/Lgm/Lgm_CTrans.h: 859
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitS'):
    Lgm_InitS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitS
    Lgm_InitS.argtypes = [(c_double * 13) * 13, c_int]
    Lgm_InitS.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 28
class struct__Lgm_OctreeData(Structure):
    pass

struct__Lgm_OctreeData.__slots__ = [
    'Position',
    'B',
    'Dist2',
]
struct__Lgm_OctreeData._fields_ = [
    ('Position', Lgm_Vector),
    ('B', Lgm_Vector),
    ('Dist2', c_double),
]

Lgm_OctreeData = struct__Lgm_OctreeData # /usr/local/include/Lgm/Lgm_Octree.h: 28

# /usr/local/include/Lgm/Lgm_Octree.h: 36
class struct__Lgm_OctreeCell(Structure):
    pass

struct__Lgm_OctreeCell.__slots__ = [
    'xLocationCode',
    'yLocationCode',
    'zLocationCode',
    'Level',
    'Center',
    'h',
    'Parent',
    'Octant',
    'nDataBelow',
    'nData',
    'Data',
]
struct__Lgm_OctreeCell._fields_ = [
    ('xLocationCode', c_uint),
    ('yLocationCode', c_uint),
    ('zLocationCode', c_uint),
    ('Level', c_uint),
    ('Center', Lgm_Vector),
    ('h', c_double),
    ('Parent', POINTER(struct__Lgm_OctreeCell)),
    ('Octant', POINTER(struct__Lgm_OctreeCell)),
    ('nDataBelow', c_ulong),
    ('nData', c_ulong),
    ('Data', POINTER(Lgm_OctreeData)),
]

Lgm_OctreeCell = struct__Lgm_OctreeCell # /usr/local/include/Lgm/Lgm_Octree.h: 56

# /usr/local/include/Lgm/Lgm_Octree.h: 59
class struct__pQueue(Structure):
    pass

struct__pQueue.__slots__ = [
    'Obj',
    'MinDist2',
    'IsPoint',
    'j',
    'Prev',
    'Next',
]
struct__pQueue._fields_ = [
    ('Obj', POINTER(Lgm_OctreeCell)),
    ('MinDist2', c_double),
    ('IsPoint', c_int),
    ('j', c_int),
    ('Prev', POINTER(struct__pQueue)),
    ('Next', POINTER(struct__pQueue)),
]

pQueue = struct__pQueue # /usr/local/include/Lgm/Lgm_Octree.h: 72

# /usr/local/include/Lgm/Lgm_Octree.h: 75
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Binary'):
    Binary = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Binary
    Binary.argtypes = [c_uint, String]
    Binary.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 76
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_OctreeFreeBranch'):
    Lgm_OctreeFreeBranch = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_OctreeFreeBranch
    Lgm_OctreeFreeBranch.argtypes = [POINTER(Lgm_OctreeCell)]
    Lgm_OctreeFreeBranch.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 77
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FreeOctree'):
    Lgm_FreeOctree = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FreeOctree
    Lgm_FreeOctree.argtypes = [POINTER(Lgm_OctreeCell)]
    Lgm_FreeOctree.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 78
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CreateOctreeRoot'):
    Lgm_CreateOctreeRoot = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CreateOctreeRoot
    Lgm_CreateOctreeRoot.argtypes = []
    Lgm_CreateOctreeRoot.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/Lgm/Lgm_Octree.h: 79
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_OctreeTraverseToLocCode'):
    Lgm_OctreeTraverseToLocCode = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_OctreeTraverseToLocCode
    Lgm_OctreeTraverseToLocCode.argtypes = [POINTER(Lgm_OctreeCell), c_uint, c_uint, c_uint, c_uint]
    Lgm_OctreeTraverseToLocCode.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/Lgm/Lgm_Octree.h: 80
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_LocateNearestCell'):
    Lgm_LocateNearestCell = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_LocateNearestCell
    Lgm_LocateNearestCell.argtypes = [POINTER(Lgm_OctreeCell), POINTER(Lgm_Vector)]
    Lgm_LocateNearestCell.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/Lgm/Lgm_Octree.h: 81
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MinDist'):
    MinDist = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MinDist
    MinDist.argtypes = [POINTER(Lgm_OctreeCell), POINTER(Lgm_Vector)]
    MinDist.restype = c_double

# /usr/local/include/Lgm/Lgm_Octree.h: 82
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'InsertCell'):
    InsertCell = _libs['/usr/local/lib/libLanlGeoMag.dylib'].InsertCell
    InsertCell.argtypes = [POINTER(Lgm_OctreeCell), POINTER(Lgm_Vector), POINTER(POINTER(pQueue)), c_double]
    InsertCell.restype = c_double

# /usr/local/include/Lgm/Lgm_Octree.h: 83
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'InsertPoint'):
    InsertPoint = _libs['/usr/local/lib/libLanlGeoMag.dylib'].InsertPoint
    InsertPoint.argtypes = [POINTER(Lgm_OctreeCell), c_int, POINTER(Lgm_Vector), POINTER(POINTER(pQueue))]
    InsertPoint.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 84
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'DescendTowardClosestLeaf'):
    DescendTowardClosestLeaf = _libs['/usr/local/lib/libLanlGeoMag.dylib'].DescendTowardClosestLeaf
    DescendTowardClosestLeaf.argtypes = [POINTER(Lgm_OctreeCell), POINTER(POINTER(pQueue)), POINTER(Lgm_Vector), c_double]
    DescendTowardClosestLeaf.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/Lgm/Lgm_Octree.h: 85
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'PopObj'):
    PopObj = _libs['/usr/local/lib/libLanlGeoMag.dylib'].PopObj
    PopObj.argtypes = [POINTER(POINTER(pQueue))]
    PopObj.restype = POINTER(pQueue)

# /usr/local/include/Lgm/Lgm_Octree.h: 86
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Octree_kNN'):
    Lgm_Octree_kNN = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Octree_kNN
    Lgm_Octree_kNN.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_OctreeCell), c_int, POINTER(c_int), c_double, POINTER(Lgm_OctreeData)]
    Lgm_Octree_kNN.restype = c_int

# /usr/local/include/Lgm/Lgm_Octree.h: 87
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'CreateNewOctants'):
    CreateNewOctants = _libs['/usr/local/lib/libLanlGeoMag.dylib'].CreateNewOctants
    CreateNewOctants.argtypes = [POINTER(Lgm_OctreeCell)]
    CreateNewOctants.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/Lgm/Lgm_Octree.h: 88
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'SubDivideVolume'):
    SubDivideVolume = _libs['/usr/local/lib/libLanlGeoMag.dylib'].SubDivideVolume
    SubDivideVolume.argtypes = [POINTER(Lgm_OctreeCell)]
    SubDivideVolume.restype = None

# /usr/local/include/Lgm/Lgm_Octree.h: 89
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitOctree'):
    Lgm_InitOctree = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitOctree
    Lgm_InitOctree.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_ulong, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_InitOctree.restype = POINTER(Lgm_OctreeCell)

# /usr/local/include/gsl/gsl_interp.h: 46
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'cache',
    'miss_count',
    'hit_count',
]
struct_anon_9._fields_ = [
    ('cache', c_size_t),
    ('miss_count', c_size_t),
    ('hit_count', c_size_t),
]

gsl_interp_accel = struct_anon_9 # /usr/local/include/gsl/gsl_interp.h: 46

# /usr/local/include/gsl/gsl_interp.h: 61
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'name',
    'min_size',
    'alloc',
    'init',
    'eval',
    'eval_deriv',
    'eval_deriv2',
    'eval_integ',
    'free',
]
struct_anon_10._fields_ = [
    ('name', String),
    ('min_size', c_uint),
    ('alloc', CFUNCTYPE(UNCHECKED(POINTER(None)), c_size_t)),
    ('init', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_double), POINTER(c_double), c_size_t)),
    ('eval', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_double), POINTER(c_double), c_size_t, c_double, POINTER(gsl_interp_accel), POINTER(c_double))),
    ('eval_deriv', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_double), POINTER(c_double), c_size_t, c_double, POINTER(gsl_interp_accel), POINTER(c_double))),
    ('eval_deriv2', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_double), POINTER(c_double), c_size_t, c_double, POINTER(gsl_interp_accel), POINTER(c_double))),
    ('eval_integ', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_double), POINTER(c_double), c_size_t, POINTER(gsl_interp_accel), c_double, c_double, POINTER(c_double))),
    ('free', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
]

gsl_interp_type = struct_anon_10 # /usr/local/include/gsl/gsl_interp.h: 61

# /usr/local/include/gsl/gsl_interp.h: 71
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'type',
    'xmin',
    'xmax',
    'size',
    'state',
]
struct_anon_11._fields_ = [
    ('type', POINTER(gsl_interp_type)),
    ('xmin', c_double),
    ('xmax', c_double),
    ('size', c_size_t),
    ('state', POINTER(None)),
]

gsl_interp = struct_anon_11 # /usr/local/include/gsl/gsl_interp.h: 71

# /usr/local/include/gsl/gsl_spline.h: 44
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'interp',
    'x',
    'y',
    'size',
]
struct_anon_12._fields_ = [
    ('interp', POINTER(gsl_interp)),
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
    ('size', c_size_t),
]

gsl_spline = struct_anon_12 # /usr/local/include/gsl/gsl_spline.h: 44

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 294
class struct_Lgm_MagModelInfo(Structure):
    pass

struct_Lgm_MagModelInfo.__slots__ = [
    'c',
    'nFunc',
    'Bfield',
    'SavePoints',
    'Hmax',
    'fp',
    'W',
    'G1',
    'G2',
    'Kp',
    'Dst',
    'P',
    'Bx',
    'By',
    'Bz',
    'T96MOD_V',
    'Trace_s',
    'B0',
    'B1',
    'B2',
    'InternalModel',
    'KineticEnergy',
    'Mass',
    'PitchAngle',
    'Pm_South',
    'Pm_North',
    'Bm',
    'Sm_South',
    'Sm_North',
    'Blocal',
    'FirstCall',
    's',
    'Px',
    'Py',
    'Pz',
    'Bvec',
    'Bmag',
    'BminusBcdip',
    'nPnts',
    'ds',
    'P_gsm',
    'S',
    'B',
    'Pmin',
    'Bvecmin',
    'Bmin',
    'Smin',
    'Spherical_Footprint_Pn',
    'Spherical_Footprint_Sn',
    'Spherical_Footprint_Bn',
    'Spherical_Footprint_Ps',
    'Spherical_Footprint_Ss',
    'Spherical_Footprint_Bs',
    'Ellipsoid_Footprint_Pn',
    'Ellipsoid_Footprint_Sn',
    'Ellipsoid_Footprint_Bn',
    'Ellipsoid_Footprint_Ps',
    'Ellipsoid_Footprint_Ss',
    'Ellipsoid_Footprint_Bs',
    'FieldLineType',
    'd2B_ds2',
    'Sb0',
    'imin1',
    'imin2',
    'acc',
    'accPx',
    'accPy',
    'accPz',
    'spline',
    'splinePx',
    'splinePy',
    'splinePz',
    'VerbosityLevel',
    'UseInterpRoutines',
    'Lgm_MagStep_eps_old',
    'Lgm_MagStep_FirstTimeThrough',
    'Lgm_MagStep_kmax',
    'Lgm_MagStep_kopt',
    'Lgm_MagStep_snew',
    'Lgm_MagStep_A',
    'Lgm_MagStep_alpha',
    'Lgm_MagStep_d',
    'Lgm_MagStep_x',
    'Lgm_I_integrand_FirstCall',
    'Lgm_I_integrand_JumpMethod',
    'Lgm_I_integrand_S',
    'Lgm_I_integrand_P',
    'Lgm_I_integrand_u_scale',
    'Lgm_n_I_integrand_Calls',
    'Lgm_I_Integrator',
    'Lgm_I_Integrator_epsrel',
    'Lgm_I_Integrator_epsabs',
    'Lgm_Sb_integrand_FirstCall',
    'Lgm_Sb_integrand_S',
    'Lgm_Sb_integrand_P',
    'Lgm_Sb_integrand_u_scale',
    'Lgm_n_Sb_integrand_Calls',
    'Lgm_Sb_Integrator',
    'Lgm_Sb_Integrator_epsrel',
    'Lgm_Sb_Integrator_epsabs',
    'Lgm_MagFlux_Integrator',
    'Lgm_MagFlux_Integrator_epsrel',
    'Lgm_MagFlux_Integrator_epsabs',
    'Lgm_LambdaIntegral_Integrator',
    'Lgm_LambdaIntegral_Integrator_epsrel',
    'Lgm_LambdaIntegral_Integrator_epsabs',
    'Lgm_FindBmRadius_Tol',
    'Lgm_FindShellLine_I_Tol',
    'Lgm_TraceToMirrorPoint_Tol',
    'OctreeRoot',
    'Octree_kNN_k',
    'Octree_kNN_InterpMethod',
    'Octree_kNN_MaxDist',
    'OctreeScaleMin',
    'OctreeScaleMax',
    'OctreeScaleDiff',
    'OpenLimit_xMin',
    'OpenLimit_xMax',
    'OpenLimit_yMin',
    'OpenLimit_yMax',
    'OpenLimit_zMin',
    'OpenLimit_zMax',
    'Lgm_LossConeHeight',
    'OP77_TILTL',
    'OP77_A',
    'OP77_B',
    'OP77_C',
    'OP77_D',
    'OP77_E',
    'OP77_F',
    'OP77_TT',
]
struct_Lgm_MagModelInfo._fields_ = [
    ('c', POINTER(Lgm_CTrans)),
    ('nFunc', c_long),
    ('Bfield', CFUNCTYPE(UNCHECKED(c_int), )),
    ('SavePoints', c_int),
    ('Hmax', c_double),
    ('fp', POINTER(FILE)),
    ('W', c_double * 6),
    ('G1', c_double),
    ('G2', c_double),
    ('Kp', c_int),
    ('Dst', c_double),
    ('P', c_double),
    ('Bx', c_double),
    ('By', c_double),
    ('Bz', c_double),
    ('T96MOD_V', c_double * 11),
    ('Trace_s', c_double),
    ('B0', c_double),
    ('B1', c_double),
    ('B2', c_double),
    ('InternalModel', c_int),
    ('KineticEnergy', c_double),
    ('Mass', c_double),
    ('PitchAngle', c_double),
    ('Pm_South', Lgm_Vector),
    ('Pm_North', Lgm_Vector),
    ('Bm', c_double),
    ('Sm_South', c_double),
    ('Sm_North', c_double),
    ('Blocal', c_double),
    ('FirstCall', c_int),
    ('s', c_double * 10000),
    ('Px', c_double * 10000),
    ('Py', c_double * 10000),
    ('Pz', c_double * 10000),
    ('Bvec', Lgm_Vector * 10000),
    ('Bmag', c_double * 10000),
    ('BminusBcdip', c_double * 10000),
    ('nPnts', c_int),
    ('ds', c_double),
    ('P_gsm', Lgm_Vector),
    ('S', c_double),
    ('B', c_double),
    ('Pmin', Lgm_Vector),
    ('Bvecmin', Lgm_Vector),
    ('Bmin', c_double),
    ('Smin', c_double),
    ('Spherical_Footprint_Pn', Lgm_Vector),
    ('Spherical_Footprint_Sn', c_double),
    ('Spherical_Footprint_Bn', c_double),
    ('Spherical_Footprint_Ps', Lgm_Vector),
    ('Spherical_Footprint_Ss', c_double),
    ('Spherical_Footprint_Bs', c_double),
    ('Ellipsoid_Footprint_Pn', Lgm_Vector),
    ('Ellipsoid_Footprint_Sn', c_double),
    ('Ellipsoid_Footprint_Bn', c_double),
    ('Ellipsoid_Footprint_Ps', Lgm_Vector),
    ('Ellipsoid_Footprint_Ss', c_double),
    ('Ellipsoid_Footprint_Bs', c_double),
    ('FieldLineType', c_int),
    ('d2B_ds2', c_double),
    ('Sb0', c_double),
    ('imin1', c_int),
    ('imin2', c_int),
    ('acc', POINTER(gsl_interp_accel)),
    ('accPx', POINTER(gsl_interp_accel)),
    ('accPy', POINTER(gsl_interp_accel)),
    ('accPz', POINTER(gsl_interp_accel)),
    ('spline', POINTER(gsl_spline)),
    ('splinePx', POINTER(gsl_spline)),
    ('splinePy', POINTER(gsl_spline)),
    ('splinePz', POINTER(gsl_spline)),
    ('VerbosityLevel', c_int),
    ('UseInterpRoutines', c_int),
    ('Lgm_MagStep_eps_old', c_double),
    ('Lgm_MagStep_FirstTimeThrough', c_int),
    ('Lgm_MagStep_kmax', c_int),
    ('Lgm_MagStep_kopt', c_int),
    ('Lgm_MagStep_snew', c_double),
    ('Lgm_MagStep_A', c_double * ((9 + 2) + 1)),
    ('Lgm_MagStep_alpha', (c_double * ((9 + 1) + 1)) * ((9 + 1) + 1)),
    ('Lgm_MagStep_d', (c_double * (9 + 2)) * (9 + 2)),
    ('Lgm_MagStep_x', c_double * (9 + 2)),
    ('Lgm_I_integrand_FirstCall', c_int),
    ('Lgm_I_integrand_JumpMethod', c_int),
    ('Lgm_I_integrand_S', c_double),
    ('Lgm_I_integrand_P', Lgm_Vector),
    ('Lgm_I_integrand_u_scale', Lgm_Vector),
    ('Lgm_n_I_integrand_Calls', c_int),
    ('Lgm_I_Integrator', c_int),
    ('Lgm_I_Integrator_epsrel', c_double),
    ('Lgm_I_Integrator_epsabs', c_double),
    ('Lgm_Sb_integrand_FirstCall', c_int),
    ('Lgm_Sb_integrand_S', c_double),
    ('Lgm_Sb_integrand_P', Lgm_Vector),
    ('Lgm_Sb_integrand_u_scale', Lgm_Vector),
    ('Lgm_n_Sb_integrand_Calls', c_int),
    ('Lgm_Sb_Integrator', c_int),
    ('Lgm_Sb_Integrator_epsrel', c_double),
    ('Lgm_Sb_Integrator_epsabs', c_double),
    ('Lgm_MagFlux_Integrator', c_int),
    ('Lgm_MagFlux_Integrator_epsrel', c_double),
    ('Lgm_MagFlux_Integrator_epsabs', c_double),
    ('Lgm_LambdaIntegral_Integrator', c_int),
    ('Lgm_LambdaIntegral_Integrator_epsrel', c_double),
    ('Lgm_LambdaIntegral_Integrator_epsabs', c_double),
    ('Lgm_FindBmRadius_Tol', c_double),
    ('Lgm_FindShellLine_I_Tol', c_double),
    ('Lgm_TraceToMirrorPoint_Tol', c_double),
    ('OctreeRoot', POINTER(Lgm_OctreeCell)),
    ('Octree_kNN_k', c_int),
    ('Octree_kNN_InterpMethod', c_int),
    ('Octree_kNN_MaxDist', c_double),
    ('OctreeScaleMin', c_double),
    ('OctreeScaleMax', c_double),
    ('OctreeScaleDiff', c_double),
    ('OpenLimit_xMin', c_double),
    ('OpenLimit_xMax', c_double),
    ('OpenLimit_yMin', c_double),
    ('OpenLimit_yMax', c_double),
    ('OpenLimit_zMin', c_double),
    ('OpenLimit_zMax', c_double),
    ('Lgm_LossConeHeight', c_double),
    ('OP77_TILTL', c_double),
    ('OP77_A', c_double * 65),
    ('OP77_B', c_double * 65),
    ('OP77_C', c_double * 45),
    ('OP77_D', c_double * 45),
    ('OP77_E', c_double * 65),
    ('OP77_F', c_double * 65),
    ('OP77_TT', c_double * 5),
]

Lgm_MagModelInfo = struct_Lgm_MagModelInfo # /usr/local/include/Lgm/Lgm_MagModelInfo.h: 294

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 297
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitMagInfo'):
    Lgm_InitMagInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitMagInfo
    Lgm_InitMagInfo.argtypes = []
    Lgm_InitMagInfo.restype = POINTER(Lgm_MagModelInfo)

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 298
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FreeMagInfo'):
    Lgm_FreeMagInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FreeMagInfo
    Lgm_FreeMagInfo.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_FreeMagInfo.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 299
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CopyMagInfo'):
    Lgm_CopyMagInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CopyMagInfo
    Lgm_CopyMagInfo.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_CopyMagInfo.restype = POINTER(Lgm_MagModelInfo)

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 301
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Trace'):
    Lgm_Trace = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Trace
    Lgm_Trace.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_Trace.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 302
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToMinBSurf'):
    Lgm_TraceToMinBSurf = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToMinBSurf
    Lgm_TraceToMinBSurf.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToMinBSurf.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 303
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToSMEquat'):
    Lgm_TraceToSMEquat = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToSMEquat
    Lgm_TraceToSMEquat.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToSMEquat.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 304
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToEarth'):
    Lgm_TraceToEarth = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToEarth
    Lgm_TraceToEarth.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToEarth.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 305
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToSphericalEarth'):
    Lgm_TraceToSphericalEarth = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToSphericalEarth
    Lgm_TraceToSphericalEarth.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToSphericalEarth.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 306
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceLine'):
    Lgm_TraceLine = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceLine
    Lgm_TraceLine.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, c_double, c_int, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceLine.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 307
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceLine2'):
    Lgm_TraceLine2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceLine2
    Lgm_TraceLine2.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_double, c_double, c_double, c_int, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceLine2.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 308
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'ReplaceFirstPoint'):
    ReplaceFirstPoint = _libs['/usr/local/lib/libLanlGeoMag.dylib'].ReplaceFirstPoint
    ReplaceFirstPoint.argtypes = [c_double, c_double, POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    ReplaceFirstPoint.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 309
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'AddNewPoint'):
    AddNewPoint = _libs['/usr/local/lib/libLanlGeoMag.dylib'].AddNewPoint
    AddNewPoint.argtypes = [c_double, c_double, POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    AddNewPoint.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 310
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'InitSpline'):
    InitSpline = _libs['/usr/local/lib/libLanlGeoMag.dylib'].InitSpline
    InitSpline.argtypes = [POINTER(Lgm_MagModelInfo)]
    InitSpline.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 311
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'FreeSpline'):
    FreeSpline = _libs['/usr/local/lib/libLanlGeoMag.dylib'].FreeSpline
    FreeSpline.argtypes = [POINTER(Lgm_MagModelInfo)]
    FreeSpline.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 312
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToMinRdotB'):
    Lgm_TraceToMinRdotB = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToMinRdotB
    Lgm_TraceToMinRdotB.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToMinRdotB.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 313
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Lgm_TraceIDL'):
        continue
    Lgm_TraceIDL = _lib.Lgm_TraceIDL
    Lgm_TraceIDL.argtypes = [c_int, POINTER(POINTER(None))]
    Lgm_TraceIDL.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 314
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TraceToMirrorPoint'):
    Lgm_TraceToMirrorPoint = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TraceToMirrorPoint
    Lgm_TraceToMirrorPoint.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(c_double), c_double, c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_TraceToMirrorPoint.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 319
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ModMid'):
    Lgm_ModMid = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ModMid
    Lgm_ModMid.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, c_int, c_double, CFUNCTYPE(UNCHECKED(c_int), POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)), POINTER(Lgm_MagModelInfo)]
    Lgm_ModMid.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 321
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_RatFunExt'):
    Lgm_RatFunExt = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_RatFunExt
    Lgm_RatFunExt.argtypes = [c_int, c_double, POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_RatFunExt.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 322
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MagStep'):
    Lgm_MagStep = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MagStep
    Lgm_MagStep.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), c_double, POINTER(c_double), POINTER(c_double), c_double, c_double, POINTER(c_double), POINTER(c_int), CFUNCTYPE(UNCHECKED(c_int), POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)), POINTER(Lgm_MagModelInfo)]
    Lgm_MagStep.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 332
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_igrf'):
    Lgm_B_igrf = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_igrf
    Lgm_B_igrf.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_igrf.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 333
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_cdip'):
    Lgm_B_cdip = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_cdip
    Lgm_B_cdip.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_cdip.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 334
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_edip'):
    Lgm_B_edip = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_edip
    Lgm_B_edip.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_edip.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 343
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_OP77'):
    Lgm_B_OP77 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_OP77
    Lgm_B_OP77.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_OP77.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 344
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'OlsenPfitzerStatic'):
    OlsenPfitzerStatic = _libs['/usr/local/lib/libLanlGeoMag.dylib'].OlsenPfitzerStatic
    OlsenPfitzerStatic.argtypes = [POINTER(c_double), POINTER(c_double), c_double, POINTER(Lgm_MagModelInfo)]
    OlsenPfitzerStatic.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 353
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B1_T87'):
    Lgm_B1_T87 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B1_T87
    Lgm_B1_T87.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B1_T87.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 354
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B2_T87'):
    Lgm_B2_T87 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B2_T87
    Lgm_B2_T87.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B2_T87.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 355
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B3_T87'):
    Lgm_B3_T87 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B3_T87
    Lgm_B3_T87.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B3_T87.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 356
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_T87'):
    Lgm_B_T87 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_T87
    Lgm_B_T87.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_T87.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 364
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_BM_T89'):
    Lgm_BM_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_BM_T89
    Lgm_BM_T89.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_BM_T89.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 365
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_BT_T89'):
    Lgm_BT_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_BT_T89
    Lgm_BT_T89.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_BT_T89.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 366
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_BRC_T89'):
    Lgm_BRC_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_BRC_T89
    Lgm_BRC_T89.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_BRC_T89.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 367
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_BC_T89'):
    Lgm_BC_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_BC_T89
    Lgm_BC_T89.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_BC_T89.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 368
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_T89'):
    Lgm_B_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_T89
    Lgm_B_T89.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_T89.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 376
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Lgm_B_T96MOD_MGH'):
        continue
    Lgm_B_T96MOD_MGH = _lib.Lgm_B_T96MOD_MGH
    Lgm_B_T96MOD_MGH.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_T96MOD_MGH.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 377
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lgm_field_t96mod_mgh_'):
        continue
    lgm_field_t96mod_mgh_ = _lib.lgm_field_t96mod_mgh_
    lgm_field_t96mod_mgh_.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    lgm_field_t96mod_mgh_.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 378
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lgm_field_t96mod_mgh__'):
        continue
    lgm_field_t96mod_mgh__ = _lib.lgm_field_t96mod_mgh__
    lgm_field_t96mod_mgh__.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    lgm_field_t96mod_mgh__.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 379
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lgm_field_t96mod_'):
        continue
    lgm_field_t96mod_ = _lib.lgm_field_t96mod_
    lgm_field_t96mod_.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    lgm_field_t96mod_.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 387
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_TS04'):
    Lgm_B_TS04 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_TS04
    Lgm_B_TS04.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_TS04.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 388
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ComputeW'):
    Lgm_ComputeW = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ComputeW
    Lgm_ComputeW.argtypes = [POINTER(c_double), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    Lgm_ComputeW.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 389
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Tsyg_TS04'):
    Tsyg_TS04 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Tsyg_TS04
    Tsyg_TS04.argtypes = [c_int, POINTER(c_double), c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Tsyg_TS04.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 390
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'TS04_EXTERN'):
    TS04_EXTERN = _libs['/usr/local/lib/libLanlGeoMag.dylib'].TS04_EXTERN
    TS04_EXTERN.argtypes = [c_int, c_int, c_int, c_int, POINTER(c_double), c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    TS04_EXTERN.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 405
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_T01S'):
    Lgm_B_T01S = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_T01S
    Lgm_B_T01S.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_T01S.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 406
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Tsyg_T01S'):
    Tsyg_T01S = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Tsyg_T01S
    Tsyg_T01S.argtypes = [c_int, POINTER(c_double), c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Tsyg_T01S.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 407
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'T01S_EXTALL'):
    T01S_EXTALL = _libs['/usr/local/lib/libLanlGeoMag.dylib'].T01S_EXTALL
    T01S_EXTALL.argtypes = [c_int, c_int, c_int, c_int, POINTER(c_double), c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    T01S_EXTALL.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 421
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_B_FromScatteredData'):
    Lgm_B_FromScatteredData = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_B_FromScatteredData
    Lgm_B_FromScatteredData.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_B_FromScatteredData.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 427
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_SimplifiedMead'):
    Lgm_SimplifiedMead = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_SimplifiedMead
    Lgm_SimplifiedMead.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_SimplifiedMead.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 433
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Iinv'):
    Iinv = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Iinv
    Iinv.argtypes = [POINTER(Lgm_MagModelInfo)]
    Iinv.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 434
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'I_integrand'):
    I_integrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].I_integrand
    I_integrand.argtypes = [c_double, POINTER(_qpInfo)]
    I_integrand.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 435
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Iinv_interped'):
    Iinv_interped = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Iinv_interped
    Iinv_interped.argtypes = [POINTER(Lgm_MagModelInfo)]
    Iinv_interped.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 436
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'I_integrand_interped'):
    I_integrand_interped = _libs['/usr/local/lib/libLanlGeoMag.dylib'].I_integrand_interped
    I_integrand_interped.argtypes = [c_double, POINTER(_qpInfo)]
    I_integrand_interped.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 437
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'SbIntegral'):
    SbIntegral = _libs['/usr/local/lib/libLanlGeoMag.dylib'].SbIntegral
    SbIntegral.argtypes = [POINTER(Lgm_MagModelInfo)]
    SbIntegral.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 438
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Sb_integrand'):
    Sb_integrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Sb_integrand
    Sb_integrand.argtypes = [c_double, POINTER(_qpInfo)]
    Sb_integrand.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 439
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'SbIntegral_interped'):
    SbIntegral_interped = _libs['/usr/local/lib/libLanlGeoMag.dylib'].SbIntegral_interped
    SbIntegral_interped.argtypes = [POINTER(Lgm_MagModelInfo)]
    SbIntegral_interped.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 440
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Sb_integrand_interped'):
    Sb_integrand_interped = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Sb_integrand_interped
    Sb_integrand_interped.argtypes = [c_double, POINTER(_qpInfo)]
    Sb_integrand_interped.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 441
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ratint'):
        continue
    ratint = _lib.ratint
    ratint.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    ratint.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 442
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'polint'):
        continue
    polint = _lib.polint
    polint.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    polint.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 443
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Interp'):
        continue
    Interp = _lib.Interp
    Interp.argtypes = [POINTER(c_double), POINTER(c_double), c_long, c_double, POINTER(c_double)]
    Interp.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 444
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Interp2'):
        continue
    Interp2 = _lib.Interp2
    Interp2.argtypes = [POINTER(c_double), POINTER(c_double), c_long, c_double, POINTER(c_double)]
    Interp2.restype = None
    break

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 445
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LFromIBmM_Hilton'):
    LFromIBmM_Hilton = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LFromIBmM_Hilton
    LFromIBmM_Hilton.argtypes = [c_double, c_double, c_double]
    LFromIBmM_Hilton.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 446
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'IFromLBmM_Hilton'):
    IFromLBmM_Hilton = _libs['/usr/local/lib/libLanlGeoMag.dylib'].IFromLBmM_Hilton
    IFromLBmM_Hilton.argtypes = [c_double, c_double, c_double]
    IFromLBmM_Hilton.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 447
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LFromIBmM_McIlwain'):
    LFromIBmM_McIlwain = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LFromIBmM_McIlwain
    LFromIBmM_McIlwain.argtypes = [c_double, c_double, c_double]
    LFromIBmM_McIlwain.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 448
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'IFromLBmM_McIlwain'):
    IFromLBmM_McIlwain = _libs['/usr/local/lib/libLanlGeoMag.dylib'].IFromLBmM_McIlwain
    IFromLBmM_McIlwain.argtypes = [c_double, c_double, c_double]
    IFromLBmM_McIlwain.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 450
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'BofS'):
    BofS = _libs['/usr/local/lib/libLanlGeoMag.dylib'].BofS
    BofS.argtypes = [c_double, POINTER(Lgm_MagModelInfo)]
    BofS.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 451
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'SofBm'):
    SofBm = _libs['/usr/local/lib/libLanlGeoMag.dylib'].SofBm
    SofBm.argtypes = [c_double, POINTER(c_double), POINTER(c_double), POINTER(Lgm_MagModelInfo)]
    SofBm.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 452
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_AlphaOfK'):
    Lgm_AlphaOfK = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_AlphaOfK
    Lgm_AlphaOfK.argtypes = [c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_AlphaOfK.restype = c_double

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 453
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Init_AlphaOfK'):
    Lgm_Init_AlphaOfK = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Init_AlphaOfK
    Lgm_Init_AlphaOfK.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_Init_AlphaOfK.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 454
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Grad_I'):
    Lgm_Grad_I = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Grad_I
    Lgm_Grad_I.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)]
    Lgm_Grad_I.restype = c_int

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 462
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MagModelInfo_Set_Psw'):
    Lgm_MagModelInfo_Set_Psw = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MagModelInfo_Set_Psw
    Lgm_MagModelInfo_Set_Psw.argtypes = [c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_MagModelInfo_Set_Psw.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 463
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MagModelInfo_Set_Kp'):
    Lgm_MagModelInfo_Set_Kp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MagModelInfo_Set_Kp
    Lgm_MagModelInfo_Set_Kp.argtypes = [c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_MagModelInfo_Set_Kp.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 464
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Octree_kNN_InterpMethod'):
    Lgm_Set_Octree_kNN_InterpMethod = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Octree_kNN_InterpMethod
    Lgm_Set_Octree_kNN_InterpMethod.argtypes = [POINTER(Lgm_MagModelInfo), c_int]
    Lgm_Set_Octree_kNN_InterpMethod.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 465
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Octree_kNN_k'):
    Lgm_Set_Octree_kNN_k = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Octree_kNN_k
    Lgm_Set_Octree_kNN_k.argtypes = [POINTER(Lgm_MagModelInfo), c_int]
    Lgm_Set_Octree_kNN_k.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 466
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Octree_kNN_MaxDist'):
    Lgm_Set_Octree_kNN_MaxDist = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Octree_kNN_MaxDist
    Lgm_Set_Octree_kNN_MaxDist.argtypes = [POINTER(Lgm_MagModelInfo), c_double]
    Lgm_Set_Octree_kNN_MaxDist.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 467
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Open_Limits'):
    Lgm_Set_Open_Limits = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Open_Limits
    Lgm_Set_Open_Limits.argtypes = [POINTER(Lgm_MagModelInfo), c_double, c_double, c_double, c_double, c_double, c_double]
    Lgm_Set_Open_Limits.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 468
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_LossConeHeight'):
    Lgm_Set_LossConeHeight = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_LossConeHeight
    Lgm_Set_LossConeHeight.argtypes = [POINTER(Lgm_MagModelInfo), c_double]
    Lgm_Set_LossConeHeight.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 472
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Lgm_B_igrf'):
    Lgm_Set_Lgm_B_igrf = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Lgm_B_igrf
    Lgm_Set_Lgm_B_igrf.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_Set_Lgm_B_igrf.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 474
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Lgm_B_T01S'):
    Lgm_Set_Lgm_B_T01S = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Lgm_B_T01S
    Lgm_Set_Lgm_B_T01S.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_Set_Lgm_B_T01S.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 476
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_gm_B_TS04'):
    Lgm_Set_gm_B_TS04 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_gm_B_TS04
    Lgm_Set_gm_B_TS04.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_Set_gm_B_TS04.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 478
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Lgm_B_T89'):
    Lgm_Set_Lgm_B_T89 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Lgm_B_T89
    Lgm_Set_Lgm_B_T89.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_Set_Lgm_B_T89.restype = None

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 480
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Set_Lgm_B_OP77'):
    Lgm_Set_Lgm_B_OP77 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Set_Lgm_B_OP77
    Lgm_Set_Lgm_B_OP77.argtypes = [POINTER(Lgm_MagModelInfo)]
    Lgm_Set_Lgm_B_OP77.restype = None

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 28
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'TRARA1'):
    TRARA1 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].TRARA1
    TRARA1.argtypes = [POINTER(c_int), POINTER(c_int), c_double, c_double, POINTER(c_double), POINTER(c_double), c_int]
    TRARA1.restype = None

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 29
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'TRARA2'):
    TRARA2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].TRARA2
    TRARA2.argtypes = [POINTER(c_int), c_int, c_int, c_double]
    TRARA2.restype = c_double

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 30
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_AE8_AP8_Flux'):
    Lgm_AE8_AP8_Flux = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_AE8_AP8_Flux
    Lgm_AE8_AP8_Flux.argtypes = [c_double, c_double, c_int, c_int, c_double, c_double]
    Lgm_AE8_AP8_Flux.restype = c_double

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 31
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_AE8_AP8_FluxFromPos'):
    Lgm_AE8_AP8_FluxFromPos = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_AE8_AP8_FluxFromPos
    Lgm_AE8_AP8_FluxFromPos.argtypes = [POINTER(Lgm_Vector), c_int, c_int, c_double, c_double, POINTER(Lgm_MagModelInfo)]
    Lgm_AE8_AP8_FluxFromPos.restype = c_double

# /usr/local/include/Lgm/Lgm_Eop.h: 26
class struct_Lgm_NgaEopp(Structure):
    pass

struct_Lgm_NgaEopp.__slots__ = [
    'ta',
    'A',
    'B',
    'C1',
    'C2',
    'D1',
    'D2',
    'P1',
    'P2',
    'E',
    'F',
    'G1',
    'G2',
    'H1',
    'H2',
    'Q1',
    'Q2',
    'tb',
    'I',
    'J',
    'K1',
    'K2',
    'K3',
    'K4',
    'L1',
    'L2',
    'L3',
    'L4',
    'R1',
    'R2',
    'R3',
    'R4',
    'dat',
    'EOPPWk',
    'teff',
]
struct_Lgm_NgaEopp._fields_ = [
    ('ta', c_double),
    ('A', c_double),
    ('B', c_double),
    ('C1', c_double),
    ('C2', c_double),
    ('D1', c_double),
    ('D2', c_double),
    ('P1', c_double),
    ('P2', c_double),
    ('E', c_double),
    ('F', c_double),
    ('G1', c_double),
    ('G2', c_double),
    ('H1', c_double),
    ('H2', c_double),
    ('Q1', c_double),
    ('Q2', c_double),
    ('tb', c_double),
    ('I', c_double),
    ('J', c_double),
    ('K1', c_double),
    ('K2', c_double),
    ('K3', c_double),
    ('K4', c_double),
    ('L1', c_double),
    ('L2', c_double),
    ('L3', c_double),
    ('L4', c_double),
    ('R1', c_double),
    ('R2', c_double),
    ('R3', c_double),
    ('R4', c_double),
    ('dat', c_int),
    ('EOPPWk', c_int),
    ('teff', c_int),
]

Lgm_NgaEopp = struct_Lgm_NgaEopp # /usr/local/include/Lgm/Lgm_Eop.h: 26

# /usr/local/include/Lgm/Lgm_Eop.h: 45
class struct_Lgm_Eop(Structure):
    pass

struct_Lgm_Eop.__slots__ = [
    'Size',
    'nEopVals',
    'Verbosity',
    'Date',
    'MJD',
    'xp',
    'yp',
    'DUT1',
    'LOD',
    'dPsi',
    'dEps',
    'dX',
    'dY',
    'DAT',
]
struct_Lgm_Eop._fields_ = [
    ('Size', c_long),
    ('nEopVals', c_long),
    ('Verbosity', c_int),
    ('Date', POINTER(c_long)),
    ('MJD', POINTER(c_double)),
    ('xp', POINTER(c_double)),
    ('yp', POINTER(c_double)),
    ('DUT1', POINTER(c_double)),
    ('LOD', POINTER(c_double)),
    ('dPsi', POINTER(c_double)),
    ('dEps', POINTER(c_double)),
    ('dX', POINTER(c_double)),
    ('dY', POINTER(c_double)),
    ('DAT', POINTER(c_double)),
]

Lgm_Eop = struct_Lgm_Eop # /usr/local/include/Lgm/Lgm_Eop.h: 45

# /usr/local/include/Lgm/Lgm_Eop.h: 63
class struct_Lgm_EopOne(Structure):
    pass

struct_Lgm_EopOne.__slots__ = [
    'Date',
    'JD',
    'MJD',
    'UTC',
    'xp',
    'yp',
    'DUT1',
    'LOD',
    'dPsi',
    'dEps',
    'dX',
    'dY',
    'DAT',
]
struct_Lgm_EopOne._fields_ = [
    ('Date', c_long),
    ('JD', c_double),
    ('MJD', c_double),
    ('UTC', c_double),
    ('xp', c_double),
    ('yp', c_double),
    ('DUT1', c_double),
    ('LOD', c_double),
    ('dPsi', c_double),
    ('dEps', c_double),
    ('dX', c_double),
    ('dY', c_double),
    ('DAT', c_double),
]

Lgm_EopOne = struct_Lgm_EopOne # /usr/local/include/Lgm/Lgm_Eop.h: 63

# /usr/local/include/Lgm/Lgm_Eop.h: 65
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_init_eop'):
    Lgm_init_eop = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_init_eop
    Lgm_init_eop.argtypes = [c_int]
    Lgm_init_eop.restype = POINTER(Lgm_Eop)

# /usr/local/include/Lgm/Lgm_Eop.h: 66
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_destroy_eop'):
    Lgm_destroy_eop = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_destroy_eop
    Lgm_destroy_eop.argtypes = [POINTER(Lgm_Eop)]
    Lgm_destroy_eop.restype = None

# /usr/local/include/Lgm/Lgm_Eop.h: 67
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_read_eop'):
    Lgm_read_eop = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_read_eop
    Lgm_read_eop.argtypes = [POINTER(Lgm_Eop)]
    Lgm_read_eop.restype = None

# /usr/local/include/Lgm/Lgm_Eop.h: 68
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_NgaEoppPred'):
    Lgm_NgaEoppPred = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_NgaEoppPred
    Lgm_NgaEoppPred.argtypes = [c_double, POINTER(Lgm_EopOne), POINTER(Lgm_NgaEopp)]
    Lgm_NgaEoppPred.restype = None

# /usr/local/include/Lgm/Lgm_Eop.h: 69
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_ReadNgaEopp'):
    Lgm_ReadNgaEopp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_ReadNgaEopp
    Lgm_ReadNgaEopp.argtypes = [POINTER(Lgm_NgaEopp), c_int]
    Lgm_ReadNgaEopp.restype = c_int

# /usr/local/include/Lgm/Lgm_Eop.h: 70
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_get_eop_at_JD'):
    Lgm_get_eop_at_JD = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_get_eop_at_JD
    Lgm_get_eop_at_JD.argtypes = [c_double, POINTER(Lgm_EopOne), POINTER(Lgm_Eop)]
    Lgm_get_eop_at_JD.restype = None

# /usr/local/include/Lgm/Lgm_Eop.h: 71
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_set_eop'):
    Lgm_set_eop = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_set_eop
    Lgm_set_eop.argtypes = [POINTER(Lgm_EopOne), POINTER(Lgm_CTrans)]
    Lgm_set_eop.restype = None

# /usr/local/include/Lgm/Lgm_Eop.h: 72
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_unset_eop'):
    Lgm_unset_eop = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_unset_eop
    Lgm_unset_eop.argtypes = [POINTER(Lgm_EopOne), POINTER(Lgm_CTrans)]
    Lgm_unset_eop.restype = None

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 48
class struct_Lgm_FieldIntInfo(Structure):
    pass

struct_Lgm_FieldIntInfo.__slots__ = [
    'KineticEnergy',
    'Mass',
    'PitchAngle',
    'Pm_South',
    'Pm_North',
    'Bm',
    'Sm_South',
    'Sm_North',
    'FirstCall',
    'n_I_integrand_Calls',
    'n_Sb_integrand_Calls',
    'epsabs',
    'epsrel',
    's',
    'P',
    'Bvec',
    'Bmag',
    'nPnts',
    'VerbosityLevel',
]
struct_Lgm_FieldIntInfo._fields_ = [
    ('KineticEnergy', c_double),
    ('Mass', c_double),
    ('PitchAngle', c_double),
    ('Pm_South', Lgm_Vector),
    ('Pm_North', Lgm_Vector),
    ('Bm', c_double),
    ('Sm_South', c_double),
    ('Sm_North', c_double),
    ('FirstCall', c_int),
    ('n_I_integrand_Calls', c_int),
    ('n_Sb_integrand_Calls', c_int),
    ('epsabs', c_double),
    ('epsrel', c_double),
    ('s', c_double * 1000),
    ('P', Lgm_Vector * 1000),
    ('Bvec', Lgm_Vector * 1000),
    ('Bmag', c_double * 1000),
    ('nPnts', c_int),
    ('VerbosityLevel', c_int),
]

Lgm_FieldIntInfo = struct_Lgm_FieldIntInfo # /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 48

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 53
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'I_integrand'):
    I_integrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].I_integrand
    I_integrand.argtypes = [c_double, POINTER(_qpInfo)]
    I_integrand.restype = c_double

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 55
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Sb_integrand'):
    Sb_integrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Sb_integrand
    Sb_integrand.argtypes = [c_double, POINTER(_qpInfo)]
    Sb_integrand.restype = c_double

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 56
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ratint'):
        continue
    ratint = _lib.ratint
    ratint.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    ratint.restype = None
    break

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 57
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'polint'):
        continue
    polint = _lib.polint
    polint.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double), POINTER(c_double)]
    polint.restype = None
    break

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 58
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Interp'):
        continue
    Interp = _lib.Interp
    Interp.argtypes = [POINTER(c_double), POINTER(c_double), c_long, c_double, POINTER(c_double)]
    Interp.restype = None
    break

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 59
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Interp2'):
        continue
    Interp2 = _lib.Interp2
    Interp2.argtypes = [POINTER(c_double), POINTER(c_double), c_long, c_double, POINTER(c_double)]
    Interp2.restype = None
    break

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 60
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LFromIBmM_Hilton'):
    LFromIBmM_Hilton = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LFromIBmM_Hilton
    LFromIBmM_Hilton.argtypes = [c_double, c_double, c_double]
    LFromIBmM_Hilton.restype = c_double

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 61
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'IFromLBmM_Hilton'):
    IFromLBmM_Hilton = _libs['/usr/local/lib/libLanlGeoMag.dylib'].IFromLBmM_Hilton
    IFromLBmM_Hilton.argtypes = [c_double, c_double, c_double]
    IFromLBmM_Hilton.restype = c_double

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 62
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LFromIBmM_McIlwain'):
    LFromIBmM_McIlwain = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LFromIBmM_McIlwain
    LFromIBmM_McIlwain.argtypes = [c_double, c_double, c_double]
    LFromIBmM_McIlwain.restype = c_double

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 63
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'IFromLBmM_McIlwain'):
    IFromLBmM_McIlwain = _libs['/usr/local/lib/libLanlGeoMag.dylib'].IFromLBmM_McIlwain
    IFromLBmM_McIlwain.argtypes = [c_double, c_double, c_double]
    IFromLBmM_McIlwain.restype = c_double

byte = c_ubyte # /usr/local/include/Lgm/Lgm_FluxToPsd.h: 56

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 120
class struct_Lgm_FluxToPsd(Structure):
    pass

struct_Lgm_FluxToPsd.__slots__ = [
    'nE',
    'E',
    'nA',
    'A',
    'FLUX_EA',
    'PSD_EA',
    'DateTime',
    'Position',
    'AofK',
    'EofMu',
    'B',
    'nMu',
    'Mu',
    'nK',
    'K',
    'PSD_MK',
    'DumpDiagnostics',
    'Alloced',
]
struct_Lgm_FluxToPsd._fields_ = [
    ('nE', c_int),
    ('E', POINTER(c_double)),
    ('nA', c_int),
    ('A', POINTER(c_double)),
    ('FLUX_EA', POINTER(POINTER(c_double))),
    ('PSD_EA', POINTER(POINTER(c_double))),
    ('DateTime', Lgm_DateTime),
    ('Position', Lgm_Vector),
    ('AofK', POINTER(c_double)),
    ('EofMu', POINTER(POINTER(c_double))),
    ('B', c_double),
    ('nMu', c_int),
    ('Mu', POINTER(c_double)),
    ('nK', c_int),
    ('K', POINTER(c_double)),
    ('PSD_MK', POINTER(POINTER(c_double))),
    ('DumpDiagnostics', c_int),
    ('Alloced', c_int),
]

Lgm_FluxToPsd = struct_Lgm_FluxToPsd # /usr/local/include/Lgm/Lgm_FluxToPsd.h: 120

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 124
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CreateFluxToPsd'):
    Lgm_CreateFluxToPsd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CreateFluxToPsd
    Lgm_CreateFluxToPsd.argtypes = [c_int]
    Lgm_CreateFluxToPsd.restype = POINTER(Lgm_FluxToPsd)

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 125
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FreeFluxToPsd'):
    Lgm_FreeFluxToPsd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FreeFluxToPsd
    Lgm_FreeFluxToPsd.argtypes = [POINTER(Lgm_FluxToPsd)]
    Lgm_FreeFluxToPsd.restype = None

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 126
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FluxToPsd_SetFlux'):
    Lgm_FluxToPsd_SetFlux = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FluxToPsd_SetFlux
    Lgm_FluxToPsd_SetFlux.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int, POINTER(c_double), c_int, POINTER(Lgm_FluxToPsd)]
    Lgm_FluxToPsd_SetFlux.restype = None

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 127
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FluxToPsd_SetDateTimeAndPos'):
    Lgm_FluxToPsd_SetDateTimeAndPos = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FluxToPsd_SetDateTimeAndPos
    Lgm_FluxToPsd_SetDateTimeAndPos.argtypes = [POINTER(Lgm_DateTime), POINTER(Lgm_Vector), POINTER(Lgm_FluxToPsd)]
    Lgm_FluxToPsd_SetDateTimeAndPos.restype = None

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 128
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FluxPsd_GetPsdAtConstMusAndKs'):
    Lgm_FluxPsd_GetPsdAtConstMusAndKs = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FluxPsd_GetPsdAtConstMusAndKs
    Lgm_FluxPsd_GetPsdAtConstMusAndKs.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int, POINTER(c_double), c_int, POINTER(Lgm_FluxToPsd)]
    Lgm_FluxPsd_GetPsdAtConstMusAndKs.restype = None

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 135
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'DumpGif'):
    DumpGif = _libs['/usr/local/lib/libLanlGeoMag.dylib'].DumpGif
    DumpGif.argtypes = [String, c_int, c_int, POINTER(POINTER(c_double))]
    DumpGif.restype = None

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 136
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Energy_to_Mu'):
    Lgm_Energy_to_Mu = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Energy_to_Mu
    Lgm_Energy_to_Mu.argtypes = [c_double, c_double, c_double]
    Lgm_Energy_to_Mu.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 137
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Mu_to_Energy'):
    Lgm_Mu_to_Energy = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Mu_to_Energy
    Lgm_Mu_to_Energy.argtypes = [c_double, c_double, c_double]
    Lgm_Mu_to_Energy.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 138
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_p2c2'):
    Lgm_p2c2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_p2c2
    Lgm_p2c2.argtypes = [c_double, c_double]
    Lgm_p2c2.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 139
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_v2overc2'):
    Lgm_v2overc2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_v2overc2
    Lgm_v2overc2.argtypes = [c_double, c_double]
    Lgm_v2overc2.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 140
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_gamma'):
    Lgm_gamma = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_gamma
    Lgm_gamma.argtypes = [c_double, c_double]
    Lgm_gamma.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 141
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_PsdToDiffFlux'):
    Lgm_PsdToDiffFlux = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_PsdToDiffFlux
    Lgm_PsdToDiffFlux.argtypes = [c_double, c_double]
    Lgm_PsdToDiffFlux.restype = c_double

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 142
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DiffFluxToPsd'):
    Lgm_DiffFluxToPsd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DiffFluxToPsd
    Lgm_DiffFluxToPsd.argtypes = [c_double, c_double]
    Lgm_DiffFluxToPsd.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 44
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_LoadLeapSeconds'):
    Lgm_LoadLeapSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_LoadLeapSeconds
    Lgm_LoadLeapSeconds.argtypes = [POINTER(Lgm_LeapSeconds)]
    Lgm_LoadLeapSeconds.restype = c_int

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 45
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_GetLeapSeconds'):
    Lgm_GetLeapSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_GetLeapSeconds
    Lgm_GetLeapSeconds.argtypes = [c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_GetLeapSeconds.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 46
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_IsLeapSecondDay'):
    Lgm_IsLeapSecondDay = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_IsLeapSecondDay
    Lgm_IsLeapSecondDay.argtypes = [c_long, POINTER(Lgm_LeapSeconds)]
    Lgm_IsLeapSecondDay.restype = c_int

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 47
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TAI'):
    Lgm_UTC_to_TAI = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TAI
    Lgm_UTC_to_TAI.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_UTC_to_TAI.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 48
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TAI_to_UTC'):
    Lgm_TAI_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TAI_to_UTC
    Lgm_TAI_to_UTC.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_TAI_to_UTC.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 49
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TT'):
    Lgm_UTC_to_TT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TT
    Lgm_UTC_to_TT.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_UTC_to_TT.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 50
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TT_to_UTC'):
    Lgm_TT_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TT_to_UTC
    Lgm_TT_to_UTC.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_TT_to_UTC.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 51
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TT_to_TDB'):
    Lgm_TT_to_TDB = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TT_to_TDB
    Lgm_TT_to_TDB.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_TT_to_TDB.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 52
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TDB_to_TT'):
    Lgm_TDB_to_TT = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TDB_to_TT
    Lgm_TDB_to_TT.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_TDB_to_TT.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 53
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_UTC_to_TDB'):
    Lgm_UTC_to_TDB = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_UTC_to_TDB
    Lgm_UTC_to_TDB.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_UTC_to_TDB.restype = c_double

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 54
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_TDB_to_UTC'):
    Lgm_TDB_to_UTC = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_TDB_to_UTC
    Lgm_TDB_to_UTC.argtypes = [c_double, c_double, POINTER(Lgm_LeapSeconds)]
    Lgm_TDB_to_UTC.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 114
class struct_Lgm_LstarInfo(Structure):
    pass

struct_Lgm_LstarInfo.__slots__ = [
    'KineticEnergy',
    'Mass',
    'PitchAngle',
    'LSimpleMax',
    'mInfo',
    'FindShellPmin',
    'ComputeVgc',
    'SaveShellLines',
    'nFieldPnts',
    's_gsm',
    'Bmag',
    'x_gsm',
    'y_gsm',
    'z_gsm',
    'nPnts',
    'MLT',
    'mlat',
    'Spherical_Footprint_Pn',
    'Spherical_Footprint_Sn',
    'Spherical_Footprint_Bn',
    'Spherical_Footprint_Ps',
    'Spherical_Footprint_Ss',
    'Spherical_Footprint_Bs',
    'Ellipsoid_Footprint_Pn',
    'Ellipsoid_Footprint_Sn',
    'Ellipsoid_Footprint_Bn',
    'Ellipsoid_Footprint_Ps',
    'Ellipsoid_Footprint_Ss',
    'Ellipsoid_Footprint_Bs',
    'Mirror_Pn',
    'Mirror_Sn',
    'Mirror_Ps',
    'Mirror_Ss',
    'PhiVal',
    'AngularVelocity',
    'I',
    'Bmin',
    'Pmin',
    'GradI',
    'Vgc',
    'nSplnPnts',
    'xa',
    'ya',
    'y2',
    'Phi',
    'acc',
    'pspline',
    'VerbosityLevel',
    'PreStr',
    'PostStr',
    'LS',
    'LS_dip_approx',
    'LS_McIlwain_M',
    'm',
    'xma',
    'yma',
    'ym2',
    'nParticles',
    'Particles',
]
struct_Lgm_LstarInfo._fields_ = [
    ('KineticEnergy', c_double),
    ('Mass', c_double),
    ('PitchAngle', c_double),
    ('LSimpleMax', c_double),
    ('mInfo', POINTER(Lgm_MagModelInfo)),
    ('FindShellPmin', c_int),
    ('ComputeVgc', c_int),
    ('SaveShellLines', c_int),
    ('nFieldPnts', c_int * 100),
    ('s_gsm', (c_double * 1000) * 100),
    ('Bmag', (c_double * 1000) * 100),
    ('x_gsm', (c_double * 1000) * 100),
    ('y_gsm', (c_double * 1000) * 100),
    ('z_gsm', (c_double * 1000) * 100),
    ('nPnts', c_int),
    ('MLT', c_double * 100),
    ('mlat', c_double * 100),
    ('Spherical_Footprint_Pn', Lgm_Vector * 100),
    ('Spherical_Footprint_Sn', c_double * 100),
    ('Spherical_Footprint_Bn', c_double * 100),
    ('Spherical_Footprint_Ps', Lgm_Vector * 100),
    ('Spherical_Footprint_Ss', c_double * 100),
    ('Spherical_Footprint_Bs', c_double * 100),
    ('Ellipsoid_Footprint_Pn', Lgm_Vector * 100),
    ('Ellipsoid_Footprint_Sn', c_double * 100),
    ('Ellipsoid_Footprint_Bn', c_double * 100),
    ('Ellipsoid_Footprint_Ps', Lgm_Vector * 100),
    ('Ellipsoid_Footprint_Ss', c_double * 100),
    ('Ellipsoid_Footprint_Bs', c_double * 100),
    ('Mirror_Pn', Lgm_Vector * 100),
    ('Mirror_Sn', c_double * 100),
    ('Mirror_Ps', Lgm_Vector * 100),
    ('Mirror_Ss', c_double * 100),
    ('PhiVal', c_double * 100),
    ('AngularVelocity', c_double * 100),
    ('I', c_double * 100),
    ('Bmin', Lgm_Vector * 100),
    ('Pmin', Lgm_Vector * 100),
    ('GradI', Lgm_Vector * 100),
    ('Vgc', Lgm_Vector * 100),
    ('nSplnPnts', c_int),
    ('xa', c_double * 500),
    ('ya', c_double * 500),
    ('y2', c_double * 500),
    ('Phi', c_double),
    ('acc', POINTER(gsl_interp_accel)),
    ('pspline', POINTER(gsl_interp)),
    ('VerbosityLevel', c_int),
    ('PreStr', c_char * 64),
    ('PostStr', c_char * 64),
    ('LS', c_double),
    ('LS_dip_approx', c_double),
    ('LS_McIlwain_M', c_double),
    ('m', c_int),
    ('xma', c_double * 500),
    ('yma', c_double * 500),
    ('ym2', c_double * 500),
    ('nParticles', c_int),
    ('Particles', Lgm_Vector * 5000),
]

Lgm_LstarInfo = struct_Lgm_LstarInfo # /usr/local/include/Lgm/Lgm_LstarInfo.h: 114

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 117
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'SetLstarTolerances'):
    SetLstarTolerances = _libs['/usr/local/lib/libLanlGeoMag.dylib'].SetLstarTolerances
    SetLstarTolerances.argtypes = [c_int, POINTER(Lgm_LstarInfo)]
    SetLstarTolerances.restype = None

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 118
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'InitLstarInfo'):
    InitLstarInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].InitLstarInfo
    InitLstarInfo.argtypes = [c_int]
    InitLstarInfo.restype = POINTER(Lgm_LstarInfo)

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 119
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'FreeLstarInfo'):
    FreeLstarInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].FreeLstarInfo
    FreeLstarInfo.argtypes = [POINTER(Lgm_LstarInfo)]
    FreeLstarInfo.restype = None

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 120
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_CopyLstarInfo'):
    Lgm_CopyLstarInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_CopyLstarInfo
    Lgm_CopyLstarInfo.argtypes = [POINTER(Lgm_LstarInfo)]
    Lgm_CopyLstarInfo.restype = POINTER(Lgm_LstarInfo)

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 122
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Grad_I'):
        continue
    Grad_I = _lib.Grad_I
    Grad_I.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_LstarInfo)]
    Grad_I.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 123
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ComputeVcg'):
        continue
    ComputeVcg = _lib.ComputeVcg
    ComputeVcg.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_LstarInfo)]
    ComputeVcg.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 124
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'FindBmRadius'):
    FindBmRadius = _libs['/usr/local/lib/libLanlGeoMag.dylib'].FindBmRadius
    FindBmRadius.argtypes = [c_double, c_double, c_double, POINTER(c_double), c_double, POINTER(Lgm_LstarInfo)]
    FindBmRadius.restype = c_int

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 125
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'FindShellLine'):
    FindShellLine = _libs['/usr/local/lib/libLanlGeoMag.dylib'].FindShellLine
    FindShellLine.argtypes = [c_double, POINTER(c_double), c_double, c_double, POINTER(c_double), POINTER(c_double), c_double, c_double, POINTER(Lgm_LstarInfo)]
    FindShellLine.restype = c_int

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'spline'):
        continue
    spline = _lib.spline
    spline.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, c_double, POINTER(c_double)]
    spline.restype = None
    break

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'splint'):
        continue
    splint = _lib.splint
    splint.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_double, POINTER(c_double)]
    splint.restype = None
    break

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 128
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'quicksort'):
    quicksort = _libs['/usr/local/lib/libLanlGeoMag.dylib'].quicksort
    quicksort.argtypes = [c_ulong, POINTER(c_double)]
    quicksort.restype = None

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 129
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'quicksort2'):
    quicksort2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].quicksort2
    quicksort2.argtypes = [c_ulong, POINTER(c_double), POINTER(c_double)]
    quicksort2.restype = None

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 130
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_info'):
        continue
    init_info = _lib.init_info
    init_info.argtypes = []
    init_info.restype = POINTER(Lgm_MagModelInfo)
    break

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 131
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'NewTimeLstarInfo'):
    NewTimeLstarInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].NewTimeLstarInfo
    NewTimeLstarInfo.argtypes = [c_long, c_double, c_double, CFUNCTYPE(UNCHECKED(c_int), POINTER(Lgm_Vector), POINTER(Lgm_Vector), POINTER(Lgm_MagModelInfo)), POINTER(Lgm_LstarInfo)]
    NewTimeLstarInfo.restype = None

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 132
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lstar'):
    Lstar = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lstar
    Lstar.argtypes = [POINTER(Lgm_Vector), POINTER(Lgm_LstarInfo)]
    Lstar.restype = c_int

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 133
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MagFlux'):
    MagFlux = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MagFlux
    MagFlux.argtypes = [POINTER(Lgm_LstarInfo)]
    MagFlux.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 134
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MagFlux2'):
    MagFlux2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MagFlux2
    MagFlux2.argtypes = [POINTER(Lgm_LstarInfo)]
    MagFlux2.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 135
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MagFluxIntegrand'):
    MagFluxIntegrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MagFluxIntegrand
    MagFluxIntegrand.argtypes = [c_double, POINTER(_qpInfo)]
    MagFluxIntegrand.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 136
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'MagFluxIntegrand2'):
    MagFluxIntegrand2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].MagFluxIntegrand2
    MagFluxIntegrand2.argtypes = [c_double, POINTER(_qpInfo)]
    MagFluxIntegrand2.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 137
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LambdaIntegrand'):
    LambdaIntegrand = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LambdaIntegrand
    LambdaIntegrand.argtypes = [c_double, POINTER(_qpInfo)]
    LambdaIntegrand.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 138
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LambdaIntegral'):
    LambdaIntegral = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LambdaIntegral
    LambdaIntegral.argtypes = [POINTER(Lgm_LstarInfo)]
    LambdaIntegral.restype = c_double

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 139
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'AngVelInv'):
        continue
    AngVelInv = _lib.AngVelInv
    AngVelInv.argtypes = [c_double]
    AngVelInv.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 142
class struct_Lgm_MagEphemInfo(Structure):
    pass

struct_Lgm_MagEphemInfo.__slots__ = [
    'LstarInfo',
    'LstarQuality',
    'SaveShellLines',
    'Date',
    'UTC',
    'Lat',
    'Lon',
    'Rad',
    'P',
    'S',
    'B',
    'Pmin',
    'Bmin',
    'Smin',
    'Spherical_Footprint_Pn',
    'Spherical_Footprint_Sn',
    'Spherical_Footprint_Bn',
    'Spherical_Footprint_Ps',
    'Spherical_Footprint_Ss',
    'Spherical_Footprint_Bs',
    'Ellipsoid_Footprint_Pn',
    'Ellipsoid_Footprint_Sn',
    'Ellipsoid_Footprint_Bn',
    'Ellipsoid_Footprint_Ps',
    'Ellipsoid_Footprint_Ss',
    'Ellipsoid_Footprint_Bs',
    'FieldLineType',
    'UseInterpRoutines',
    'ComputeVgc',
    'nAlpha',
    'Alpha',
    'Pmn_gsm',
    'Pms_gsm',
    'Bm',
    'I',
    'Sb',
    'Tb',
    'K',
    'nShellPoints',
    'ShellSphericalFootprint_Pn',
    'ShellSphericalFootprint_Sn',
    'ShellSphericalFootprint_Bn',
    'ShellSphericalFootprint_Ps',
    'ShellSphericalFootprint_Ss',
    'ShellSphericalFootprint_Bs',
    'ShellEllipsoidFootprint_Ps',
    'ShellEllipsoidFootprint_Ss',
    'ShellEllipsoidFootprint_Bs',
    'ShellEllipsoidFootprint_Pn',
    'ShellEllipsoidFootprint_Sn',
    'ShellEllipsoidFootprint_Bn',
    'ShellMirror_Pn',
    'ShellMirror_Sn',
    'ShellMirror_Ps',
    'ShellMirror_Ss',
    'Shell_Bmin',
    'Shell_Pmin',
    'Shell_GradI',
    'Shell_Vgc',
    'ShellI',
    'nFieldPnts',
    's_gsm',
    'Bmag',
    'x_gsm',
    'y_gsm',
    'z_gsm',
    'Mcurr',
    'Mref',
    'Mused',
    'LHilton',
    'LMcIlwain',
    'Lstar',
]
struct_Lgm_MagEphemInfo._fields_ = [
    ('LstarInfo', POINTER(Lgm_LstarInfo)),
    ('LstarQuality', c_int),
    ('SaveShellLines', c_int),
    ('Date', c_long),
    ('UTC', c_double),
    ('Lat', c_double),
    ('Lon', c_double),
    ('Rad', c_double),
    ('P', Lgm_Vector),
    ('S', c_double),
    ('B', c_double),
    ('Pmin', Lgm_Vector),
    ('Bmin', c_double),
    ('Smin', c_double),
    ('Spherical_Footprint_Pn', Lgm_Vector),
    ('Spherical_Footprint_Sn', c_double),
    ('Spherical_Footprint_Bn', c_double),
    ('Spherical_Footprint_Ps', Lgm_Vector),
    ('Spherical_Footprint_Ss', c_double),
    ('Spherical_Footprint_Bs', c_double),
    ('Ellipsoid_Footprint_Pn', Lgm_Vector),
    ('Ellipsoid_Footprint_Sn', c_double),
    ('Ellipsoid_Footprint_Bn', c_double),
    ('Ellipsoid_Footprint_Ps', Lgm_Vector),
    ('Ellipsoid_Footprint_Ss', c_double),
    ('Ellipsoid_Footprint_Bs', c_double),
    ('FieldLineType', c_int),
    ('UseInterpRoutines', c_int),
    ('ComputeVgc', c_int),
    ('nAlpha', c_int),
    ('Alpha', POINTER(c_double)),
    ('Pmn_gsm', POINTER(Lgm_Vector)),
    ('Pms_gsm', POINTER(Lgm_Vector)),
    ('Bm', POINTER(c_double)),
    ('I', POINTER(c_double)),
    ('Sb', POINTER(c_double)),
    ('Tb', POINTER(c_double)),
    ('K', POINTER(c_double)),
    ('nShellPoints', POINTER(c_int)),
    ('ShellSphericalFootprint_Pn', POINTER(POINTER(Lgm_Vector))),
    ('ShellSphericalFootprint_Sn', POINTER(POINTER(c_double))),
    ('ShellSphericalFootprint_Bn', POINTER(POINTER(c_double))),
    ('ShellSphericalFootprint_Ps', POINTER(POINTER(Lgm_Vector))),
    ('ShellSphericalFootprint_Ss', POINTER(POINTER(c_double))),
    ('ShellSphericalFootprint_Bs', POINTER(POINTER(c_double))),
    ('ShellEllipsoidFootprint_Ps', POINTER(POINTER(Lgm_Vector))),
    ('ShellEllipsoidFootprint_Ss', POINTER(POINTER(c_double))),
    ('ShellEllipsoidFootprint_Bs', POINTER(POINTER(c_double))),
    ('ShellEllipsoidFootprint_Pn', POINTER(POINTER(Lgm_Vector))),
    ('ShellEllipsoidFootprint_Sn', POINTER(POINTER(c_double))),
    ('ShellEllipsoidFootprint_Bn', POINTER(POINTER(c_double))),
    ('ShellMirror_Pn', POINTER(POINTER(Lgm_Vector))),
    ('ShellMirror_Sn', POINTER(POINTER(c_double))),
    ('ShellMirror_Ps', POINTER(POINTER(Lgm_Vector))),
    ('ShellMirror_Ss', POINTER(POINTER(c_double))),
    ('Shell_Bmin', POINTER(POINTER(Lgm_Vector))),
    ('Shell_Pmin', POINTER(POINTER(Lgm_Vector))),
    ('Shell_GradI', POINTER(POINTER(Lgm_Vector))),
    ('Shell_Vgc', POINTER(POINTER(Lgm_Vector))),
    ('ShellI', POINTER(POINTER(c_double))),
    ('nFieldPnts', POINTER(POINTER(c_int))),
    ('s_gsm', POINTER(POINTER(POINTER(c_double)))),
    ('Bmag', POINTER(POINTER(POINTER(c_double)))),
    ('x_gsm', POINTER(POINTER(POINTER(c_double)))),
    ('y_gsm', POINTER(POINTER(POINTER(c_double)))),
    ('z_gsm', POINTER(POINTER(POINTER(c_double)))),
    ('Mcurr', c_double),
    ('Mref', c_double),
    ('Mused', c_double),
    ('LHilton', POINTER(c_double)),
    ('LMcIlwain', POINTER(c_double)),
    ('Lstar', POINTER(c_double)),
]

Lgm_MagEphemInfo = struct_Lgm_MagEphemInfo # /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 142

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 148
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'j_to_fp_1'):
        continue
    j_to_fp_1 = _lib.j_to_fp_1
    j_to_fp_1.argtypes = [c_double, c_double]
    j_to_fp_1.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 149
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'j_to_fp_2'):
        continue
    j_to_fp_2 = _lib.j_to_fp_2
    j_to_fp_2.argtypes = [c_double, c_double, c_double]
    j_to_fp_2.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 150
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Ek_to_mu_1'):
        continue
    Ek_to_mu_1 = _lib.Ek_to_mu_1
    Ek_to_mu_1.argtypes = [c_double, c_double, c_double]
    Ek_to_mu_1.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 151
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Ek_to_mu_2'):
        continue
    Ek_to_mu_2 = _lib.Ek_to_mu_2
    Ek_to_mu_2.argtypes = [c_double, c_double, c_double, c_double]
    Ek_to_mu_2.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 152
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Ek_to_v'):
        continue
    Ek_to_v = _lib.Ek_to_v
    Ek_to_v.argtypes = [c_double, c_int]
    Ek_to_v.restype = c_double
    break

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 155
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_InitMagEphemInfo'):
    Lgm_InitMagEphemInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_InitMagEphemInfo
    Lgm_InitMagEphemInfo.argtypes = [c_int, c_int]
    Lgm_InitMagEphemInfo.restype = POINTER(Lgm_MagEphemInfo)

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 156
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_FreeMagEphemInfo'):
    Lgm_FreeMagEphemInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_FreeMagEphemInfo
    Lgm_FreeMagEphemInfo.argtypes = [POINTER(Lgm_MagEphemInfo)]
    Lgm_FreeMagEphemInfo.restype = None

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 158
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'ReadMagEphemInfoStruct'):
    ReadMagEphemInfoStruct = _libs['/usr/local/lib/libLanlGeoMag.dylib'].ReadMagEphemInfoStruct
    ReadMagEphemInfoStruct.argtypes = [String, POINTER(c_int), POINTER(Lgm_MagEphemInfo)]
    ReadMagEphemInfoStruct.restype = None

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 159
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'WriteMagEphemInfoStruct'):
    WriteMagEphemInfoStruct = _libs['/usr/local/lib/libLanlGeoMag.dylib'].WriteMagEphemInfoStruct
    WriteMagEphemInfoStruct.argtypes = [String, c_int, POINTER(Lgm_MagEphemInfo)]
    WriteMagEphemInfoStruct.restype = None

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 128
class struct_Lgm_PhaseSpaceDensity(Structure):
    pass

struct_Lgm_PhaseSpaceDensity.__slots__ = [
    'nE1',
    'E1',
    'nA1',
    'A1',
    'PSD_EA1',
    'FLUX_EA1',
    'nE2',
    'E2',
    'nA2',
    'A2',
    'PSD_EA2',
    'nM1',
    'M1',
    'nK1',
    'K1',
    'PSD_MK1',
    'nM2',
    'M2',
    'nK2',
    'K2',
    'PSD_MK2',
    'DumpDiagnostics',
]
struct_Lgm_PhaseSpaceDensity._fields_ = [
    ('nE1', c_int),
    ('E1', POINTER(c_double)),
    ('nA1', c_int),
    ('A1', POINTER(c_double)),
    ('PSD_EA1', POINTER(POINTER(c_double))),
    ('FLUX_EA1', POINTER(POINTER(c_double))),
    ('nE2', c_int),
    ('E2', POINTER(c_double)),
    ('nA2', c_int),
    ('A2', POINTER(c_double)),
    ('PSD_EA2', POINTER(POINTER(c_double))),
    ('nM1', c_int),
    ('M1', POINTER(c_double)),
    ('nK1', c_int),
    ('K1', POINTER(c_double)),
    ('PSD_MK1', POINTER(POINTER(c_double))),
    ('nM2', c_int),
    ('M2', POINTER(c_double)),
    ('nK2', c_int),
    ('K2', POINTER(c_double)),
    ('PSD_MK2', POINTER(POINTER(c_double))),
    ('DumpDiagnostics', c_int),
]

Lgm_PhaseSpaceDensity = struct_Lgm_PhaseSpaceDensity # /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 128

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 132
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Lgm_InitPhaseSpaceDensity'):
        continue
    Lgm_InitPhaseSpaceDensity = _lib.Lgm_InitPhaseSpaceDensity
    Lgm_InitPhaseSpaceDensity.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int]
    Lgm_InitPhaseSpaceDensity.restype = POINTER(Lgm_PhaseSpaceDensity)
    break

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 133
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'Lgm_FreePhaseSpaceDensity'):
        continue
    Lgm_FreePhaseSpaceDensity = _lib.Lgm_FreePhaseSpaceDensity
    Lgm_FreePhaseSpaceDensity.argtypes = [POINTER(Lgm_PhaseSpaceDensity)]
    Lgm_FreePhaseSpaceDensity.restype = None
    break

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 134
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'UpSizeImage'):
    UpSizeImage = _libs['/usr/local/lib/libLanlGeoMag.dylib'].UpSizeImage
    UpSizeImage.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    UpSizeImage.restype = None

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 135
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'DumpGif'):
    DumpGif = _libs['/usr/local/lib/libLanlGeoMag.dylib'].DumpGif
    DumpGif.argtypes = [String, c_int, c_int, POINTER(POINTER(c_double))]
    DumpGif.restype = None

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 142
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Energy_to_Mu'):
    Lgm_Energy_to_Mu = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Energy_to_Mu
    Lgm_Energy_to_Mu.argtypes = [c_double, c_double, c_double]
    Lgm_Energy_to_Mu.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 143
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Mu_to_Energy'):
    Lgm_Mu_to_Energy = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Mu_to_Energy
    Lgm_Mu_to_Energy.argtypes = [c_double, c_double, c_double]
    Lgm_Mu_to_Energy.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 144
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_p2c2'):
    Lgm_p2c2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_p2c2
    Lgm_p2c2.argtypes = [c_double, c_double]
    Lgm_p2c2.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 145
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_v2overc2'):
    Lgm_v2overc2 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_v2overc2
    Lgm_v2overc2.argtypes = [c_double, c_double]
    Lgm_v2overc2.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 146
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_gamma'):
    Lgm_gamma = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_gamma
    Lgm_gamma.argtypes = [c_double, c_double]
    Lgm_gamma.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 147
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_PsdToDiffFlux'):
    Lgm_PsdToDiffFlux = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_PsdToDiffFlux
    Lgm_PsdToDiffFlux.argtypes = [c_double, c_double]
    Lgm_PsdToDiffFlux.restype = c_double

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 148
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_DiffFluxToPsd'):
    Lgm_DiffFluxToPsd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_DiffFluxToPsd
    Lgm_DiffFluxToPsd.argtypes = [c_double, c_double]
    Lgm_DiffFluxToPsd.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 13
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_NormalizeQuat'):
    Lgm_NormalizeQuat = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_NormalizeQuat
    Lgm_NormalizeQuat.argtypes = [POINTER(c_double)]
    Lgm_NormalizeQuat.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 14
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MatrixTrace'):
    Lgm_MatrixTrace = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MatrixTrace
    Lgm_MatrixTrace.argtypes = [(c_double * 3) * 3]
    Lgm_MatrixTrace.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 15
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_MatrixToQuat'):
    Lgm_MatrixToQuat = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_MatrixToQuat
    Lgm_MatrixToQuat.argtypes = [(c_double * 3) * 3, POINTER(c_double)]
    Lgm_MatrixToQuat.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 16
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_Quat_To_Matrix'):
    Lgm_Quat_To_Matrix = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_Quat_To_Matrix
    Lgm_Quat_To_Matrix.argtypes = [c_double * 4, (c_double * 3) * 3]
    Lgm_Quat_To_Matrix.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 17
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatToAxisAngle'):
    Lgm_QuatToAxisAngle = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatToAxisAngle
    Lgm_QuatToAxisAngle.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(Lgm_Vector)]
    Lgm_QuatToAxisAngle.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 18
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_AxisAngleToQuat'):
    Lgm_AxisAngleToQuat = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_AxisAngleToQuat
    Lgm_AxisAngleToQuat.argtypes = [POINTER(Lgm_Vector), c_double, POINTER(c_double)]
    Lgm_AxisAngleToQuat.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 19
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatRotateVector'):
    Lgm_QuatRotateVector = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatRotateVector
    Lgm_QuatRotateVector.argtypes = [POINTER(c_double), POINTER(Lgm_Vector), POINTER(Lgm_Vector)]
    Lgm_QuatRotateVector.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 20
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatMagnitude'):
    Lgm_QuatMagnitude = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatMagnitude
    Lgm_QuatMagnitude.argtypes = [POINTER(c_double)]
    Lgm_QuatMagnitude.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 21
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecLength'):
    Lgm_QuatVecLength = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecLength
    Lgm_QuatVecLength.argtypes = [POINTER(c_double)]
    Lgm_QuatVecLength.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 22
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecDot'):
    Lgm_QuatVecDot = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecDot
    Lgm_QuatVecDot.argtypes = [POINTER(c_double), POINTER(c_double)]
    Lgm_QuatVecDot.restype = c_double

# /usr/local/include/Lgm/Lgm_Quat.h: 23
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecZero'):
    Lgm_QuatVecZero = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecZero
    Lgm_QuatVecZero.argtypes = [POINTER(c_double)]
    Lgm_QuatVecZero.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 24
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecSet'):
    Lgm_QuatVecSet = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecSet
    Lgm_QuatVecSet.argtypes = [POINTER(c_double), c_double, c_double, c_double]
    Lgm_QuatVecSet.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 25
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecAdd'):
    Lgm_QuatVecAdd = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecAdd
    Lgm_QuatVecAdd.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_QuatVecAdd.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 26
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecSub'):
    Lgm_QuatVecSub = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecSub
    Lgm_QuatVecSub.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_QuatVecSub.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 27
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecCopy'):
    Lgm_QuatVecCopy = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecCopy
    Lgm_QuatVecCopy.argtypes = [POINTER(c_double), POINTER(c_double)]
    Lgm_QuatVecCopy.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 28
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecScale'):
    Lgm_QuatVecScale = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecScale
    Lgm_QuatVecScale.argtypes = [POINTER(c_double), c_double]
    Lgm_QuatVecScale.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 29
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecNormalize'):
    Lgm_QuatVecNormalize = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecNormalize
    Lgm_QuatVecNormalize.argtypes = [POINTER(c_double)]
    Lgm_QuatVecNormalize.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 30
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatVecCross'):
    Lgm_QuatVecCross = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatVecCross
    Lgm_QuatVecCross.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Lgm_QuatVecCross.restype = None

# /usr/local/include/Lgm/Lgm_Quat.h: 31
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_QuatCombineQuats'):
    Lgm_QuatCombineQuats = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_QuatCombineQuats
    Lgm_QuatCombineQuats.argtypes = [c_double * 4, c_double * 4, c_double * 4]
    Lgm_QuatCombineQuats.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 99
class struct__SgpTLE(Structure):
    pass

struct__SgpTLE.__slots__ = [
    'Line0',
    'Line1',
    'Line2',
    'Name',
    'IdNumber',
    'ElsetClass',
    'IntDesig',
    'ElementSetEpoch',
    'dMMdT1',
    'dMMdT2',
    'BstarDrag',
    'ElementSetType',
    'ElementSetNum',
    'Line1CheckSum',
    'Inclination',
    'RAofAscNode',
    'Eccentricity',
    'ArgOfPerigee',
    'MeanAnomaly',
    'MeanMotion',
    'RevNumAtEpoch',
    'Line2CheckSum',
    'Date',
    'UT',
    'Year',
    'Month',
    'Day',
    'Doy',
    'Dow',
    'JD',
    'Period',
    'IntDesig2',
    'ObjectType',
    'EpochStr',
    'YYYYDDDdFRAC',
]
struct__SgpTLE._fields_ = [
    ('Line0', c_char * 80),
    ('Line1', c_char * 80),
    ('Line2', c_char * 80),
    ('Name', c_char * 80),
    ('IdNumber', c_int),
    ('ElsetClass', c_char),
    ('IntDesig', c_char * 20),
    ('ElementSetEpoch', c_double),
    ('dMMdT1', c_double),
    ('dMMdT2', c_double),
    ('BstarDrag', c_double),
    ('ElementSetType', c_int),
    ('ElementSetNum', c_int),
    ('Line1CheckSum', c_int),
    ('Inclination', c_double),
    ('RAofAscNode', c_double),
    ('Eccentricity', c_double),
    ('ArgOfPerigee', c_double),
    ('MeanAnomaly', c_double),
    ('MeanMotion', c_double),
    ('RevNumAtEpoch', c_int),
    ('Line2CheckSum', c_int),
    ('Date', c_long),
    ('UT', c_double),
    ('Year', c_int),
    ('Month', c_int),
    ('Day', c_int),
    ('Doy', c_int),
    ('Dow', c_char * 5),
    ('JD', c_double),
    ('Period', c_double),
    ('IntDesig2', c_char * 20),
    ('ObjectType', c_char * 20),
    ('EpochStr', c_char * 20),
    ('YYYYDDDdFRAC', c_double),
]

_SgpTLE = struct__SgpTLE # /usr/local/include/Lgm/Lgm_Sgp.h: 99

# /usr/local/include/Lgm/Lgm_Sgp.h: 158
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'IFLAG',
    'XMO',
    'XNODEO',
    'OMEGAO',
    'EO',
    'XINCL',
    'XNO',
    'XNDT2O',
    'XNDD6O',
    'BSTAR',
    'XDOT',
    'YDOT',
    'ZDOT',
    'EPOCH',
    'DS50',
    'argpdot',
    'argpo',
    'atime',
    'aycof',
    'bstar',
    'cc1',
    'cc4',
    'cc5',
    'con41',
    'd2',
    'd2201',
    'd2211',
    'd3',
    'd3210',
    'd3222',
    'd4',
    'd4410',
    'd4422',
    'd5220',
    'd5232',
    'd5421',
    'd5433',
    'dedt',
    'del1',
    'del2',
    'del3',
    'delmo',
    'didt',
    'dmdt',
    'dnodt',
    'domdt',
    'e3',
    'ecco',
    'ee2',
    'error',
    'eta',
    'gsto',
    'inclo',
    'mdot',
    'mo',
    'no',
    'nodecf',
    'nodedot',
    'nodeo',
    'omgcof',
    'peo',
    'pgho',
    'pho',
    'pinco',
    'plo',
    'se2',
    'se3',
    'sgh2',
    'sgh3',
    'sgh4',
    'sh2',
    'sh3',
    'si2',
    'si3',
    'sinmao',
    'sl2',
    'sl3',
    'sl4',
    't',
    't2cof',
    't3cof',
    't4cof',
    't5cof',
    'x1mth2',
    'x7thm1',
    'xfact',
    'xgh2',
    'xgh3',
    'xgh4',
    'xh2',
    'xh3',
    'xi2',
    'xi3',
    'xl2',
    'xl3',
    'xl4',
    'xlamo',
    'xlcof',
    'xli',
    'xmcof',
    'xni',
    'zmol',
    'zmos',
    'GravConst',
    'irez',
    'init',
    'method',
    'isimp',
    'X',
    'Y',
    'Z',
    'VX',
    'VY',
    'VZ',
]
struct_anon_14._fields_ = [
    ('IFLAG', c_int),
    ('XMO', c_double),
    ('XNODEO', c_double),
    ('OMEGAO', c_double),
    ('EO', c_double),
    ('XINCL', c_double),
    ('XNO', c_double),
    ('XNDT2O', c_double),
    ('XNDD6O', c_double),
    ('BSTAR', c_double),
    ('XDOT', c_double),
    ('YDOT', c_double),
    ('ZDOT', c_double),
    ('EPOCH', c_double),
    ('DS50', c_double),
    ('argpdot', c_double),
    ('argpo', c_double),
    ('atime', c_double),
    ('aycof', c_double),
    ('bstar', c_double),
    ('cc1', c_double),
    ('cc4', c_double),
    ('cc5', c_double),
    ('con41', c_double),
    ('d2', c_double),
    ('d2201', c_double),
    ('d2211', c_double),
    ('d3', c_double),
    ('d3210', c_double),
    ('d3222', c_double),
    ('d4', c_double),
    ('d4410', c_double),
    ('d4422', c_double),
    ('d5220', c_double),
    ('d5232', c_double),
    ('d5421', c_double),
    ('d5433', c_double),
    ('dedt', c_double),
    ('del1', c_double),
    ('del2', c_double),
    ('del3', c_double),
    ('delmo', c_double),
    ('didt', c_double),
    ('dmdt', c_double),
    ('dnodt', c_double),
    ('domdt', c_double),
    ('e3', c_double),
    ('ecco', c_double),
    ('ee2', c_double),
    ('error', c_double),
    ('eta', c_double),
    ('gsto', c_double),
    ('inclo', c_double),
    ('mdot', c_double),
    ('mo', c_double),
    ('no', c_double),
    ('nodecf', c_double),
    ('nodedot', c_double),
    ('nodeo', c_double),
    ('omgcof', c_double),
    ('peo', c_double),
    ('pgho', c_double),
    ('pho', c_double),
    ('pinco', c_double),
    ('plo', c_double),
    ('se2', c_double),
    ('se3', c_double),
    ('sgh2', c_double),
    ('sgh3', c_double),
    ('sgh4', c_double),
    ('sh2', c_double),
    ('sh3', c_double),
    ('si2', c_double),
    ('si3', c_double),
    ('sinmao', c_double),
    ('sl2', c_double),
    ('sl3', c_double),
    ('sl4', c_double),
    ('t', c_double),
    ('t2cof', c_double),
    ('t3cof', c_double),
    ('t4cof', c_double),
    ('t5cof', c_double),
    ('x1mth2', c_double),
    ('x7thm1', c_double),
    ('xfact', c_double),
    ('xgh2', c_double),
    ('xgh3', c_double),
    ('xgh4', c_double),
    ('xh2', c_double),
    ('xh3', c_double),
    ('xi2', c_double),
    ('xi3', c_double),
    ('xl2', c_double),
    ('xl3', c_double),
    ('xl4', c_double),
    ('xlamo', c_double),
    ('xlcof', c_double),
    ('xli', c_double),
    ('xmcof', c_double),
    ('xni', c_double),
    ('zmol', c_double),
    ('zmos', c_double),
    ('GravConst', c_int),
    ('irez', c_int),
    ('init', c_char),
    ('method', c_char),
    ('isimp', c_char),
    ('X', c_double),
    ('Y', c_double),
    ('Z', c_double),
    ('VX', c_double),
    ('VY', c_double),
    ('VZ', c_double),
]

_SgpInfo = struct_anon_14 # /usr/local/include/Lgm/Lgm_Sgp.h: 158

# /usr/local/include/Lgm/Lgm_Sgp.h: 209
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_TleChecksum'):
    LgmSgp_TleChecksum = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_TleChecksum
    LgmSgp_TleChecksum.argtypes = [String]
    LgmSgp_TleChecksum.restype = c_int

# /usr/local/include/Lgm/Lgm_Sgp.h: 210
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'Lgm_SgpDecodeTle'):
    Lgm_SgpDecodeTle = _libs['/usr/local/lib/libLanlGeoMag.dylib'].Lgm_SgpDecodeTle
    Lgm_SgpDecodeTle.argtypes = [String, String, String, POINTER(_SgpTLE), c_int]
    Lgm_SgpDecodeTle.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 211
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_ReadTlesFromFile'):
    LgmSgp_ReadTlesFromFile = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_ReadTlesFromFile
    LgmSgp_ReadTlesFromFile.argtypes = [String, POINTER(c_int), POINTER(_SgpTLE), c_int]
    LgmSgp_ReadTlesFromFile.restype = c_int

# /usr/local/include/Lgm/Lgm_Sgp.h: 212
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_ReadTlesFromStrings'):
    LgmSgp_ReadTlesFromStrings = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_ReadTlesFromStrings
    LgmSgp_ReadTlesFromStrings.argtypes = [String, String, String, POINTER(c_int), POINTER(_SgpTLE), c_int]
    LgmSgp_ReadTlesFromStrings.restype = c_int

# /usr/local/include/Lgm/Lgm_Sgp.h: 219
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_InitElements'):
        continue
    LgmSgp_InitElements = _lib.LgmSgp_InitElements
    LgmSgp_InitElements.argtypes = [POINTER(_SgpInfo), POINTER(_SgpTLE)]
    LgmSgp_InitElements.restype = None
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 220
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_SGP_STR3'):
        continue
    LgmSgp_SGP_STR3 = _lib.LgmSgp_SGP_STR3
    LgmSgp_SGP_STR3.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SGP_STR3.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 221
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_SGP4_STR3'):
        continue
    LgmSgp_SGP4_STR3 = _lib.LgmSgp_SGP4_STR3
    LgmSgp_SGP4_STR3.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SGP4_STR3.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 222
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_SDP4_STR3'):
        continue
    LgmSgp_SDP4_STR3 = _lib.LgmSgp_SDP4_STR3
    LgmSgp_SDP4_STR3.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SDP4_STR3.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 223
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_SGP8_STR3'):
        continue
    LgmSgp_SGP8_STR3 = _lib.LgmSgp_SGP8_STR3
    LgmSgp_SGP8_STR3.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SGP8_STR3.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 224
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'LgmSgp_SDP8_STR3'):
        continue
    LgmSgp_SDP8_STR3 = _lib.LgmSgp_SDP8_STR3
    LgmSgp_SDP8_STR3.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SDP8_STR3.restype = c_int
    break

# /usr/local/include/Lgm/Lgm_Sgp.h: 229
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_SGP4'):
    LgmSgp_SGP4 = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_SGP4
    LgmSgp_SGP4.argtypes = [c_double, POINTER(_SgpInfo)]
    LgmSgp_SGP4.restype = c_int

# /usr/local/include/Lgm/Lgm_Sgp.h: 231
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_SGP4_Init'):
    LgmSgp_SGP4_Init = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_SGP4_Init
    LgmSgp_SGP4_Init.argtypes = [POINTER(_SgpInfo), POINTER(_SgpTLE)]
    LgmSgp_SGP4_Init.restype = c_int

# /usr/local/include/Lgm/Lgm_Sgp.h: 233
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_GetGravConst'):
    LgmSgp_GetGravConst = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_GetGravConst
    LgmSgp_GetGravConst.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    LgmSgp_GetGravConst.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 236
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_dpper'):
    LgmSgp_dpper = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_dpper
    LgmSgp_dpper.argtypes = [c_double, c_char, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(_SgpInfo)]
    LgmSgp_dpper.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 239
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_dspace'):
    LgmSgp_dspace = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_dspace
    LgmSgp_dspace.argtypes = [c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(_SgpInfo)]
    LgmSgp_dspace.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 242
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_initl'):
    LgmSgp_initl = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_initl
    LgmSgp_initl.argtypes = [c_int, c_int, c_double, c_double, c_double, POINTER(c_double), String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    LgmSgp_initl.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 247
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_dscom'):
    LgmSgp_dscom = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_dscom
    LgmSgp_dscom.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    LgmSgp_dscom.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 265
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_dsinit'):
    LgmSgp_dsinit = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_dsinit
    LgmSgp_dsinit.argtypes = [c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    LgmSgp_dsinit.restype = None

# /usr/local/include/Lgm/Lgm_Sgp.h: 278
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'LgmSgp_gstime'):
    LgmSgp_gstime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].LgmSgp_gstime
    LgmSgp_gstime.argtypes = [c_double]
    LgmSgp_gstime.restype = c_double

# /usr/local/include/Lgm/size.h: 26
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_t_size'):
    size_t_size = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_t_size
    size_t_size.argtypes = []
    size_t_size.restype = c_int

# /usr/local/include/Lgm/size.h: 27
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_MagModelInfo'):
    size_MagModelInfo = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_MagModelInfo
    size_MagModelInfo.argtypes = []
    size_MagModelInfo.restype = c_int

# /usr/local/include/Lgm/size.h: 28
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_CTrans'):
    size_CTrans = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_CTrans
    size_CTrans.argtypes = []
    size_CTrans.restype = c_int

# /usr/local/include/Lgm/size.h: 29
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_Vector'):
    size_Vector = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_Vector
    size_Vector.argtypes = []
    size_Vector.restype = c_int

# /usr/local/include/Lgm/size.h: 30
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_DateTime'):
    size_DateTime = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_DateTime
    size_DateTime.argtypes = []
    size_DateTime.restype = c_int

# /usr/local/include/Lgm/size.h: 31
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_gsl_interp_accel'):
    size_gsl_interp_accel = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_gsl_interp_accel
    size_gsl_interp_accel.argtypes = []
    size_gsl_interp_accel.restype = c_int

# /usr/local/include/Lgm/size.h: 32
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_gsl_interp_type'):
    size_gsl_interp_type = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_gsl_interp_type
    size_gsl_interp_type.argtypes = []
    size_gsl_interp_type.restype = c_int

# /usr/local/include/Lgm/size.h: 33
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_gsl_interp'):
    size_gsl_interp = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_gsl_interp
    size_gsl_interp.argtypes = []
    size_gsl_interp.restype = c_int

# /usr/local/include/Lgm/size.h: 34
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_gsl_spline'):
    size_gsl_spline = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_gsl_spline
    size_gsl_spline.argtypes = []
    size_gsl_spline.restype = c_int

# /usr/local/include/Lgm/size.h: 35
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_Lgm_OctreeData'):
    size_Lgm_OctreeData = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_Lgm_OctreeData
    size_Lgm_OctreeData.argtypes = []
    size_Lgm_OctreeData.restype = c_int

# /usr/local/include/Lgm/size.h: 36
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_Lgm_OctreeCell'):
    size_Lgm_OctreeCell = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_Lgm_OctreeCell
    size_Lgm_OctreeCell.argtypes = []
    size_Lgm_OctreeCell.restype = c_int

# /usr/local/include/Lgm/size.h: 37
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_pQueue'):
    size_pQueue = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_pQueue
    size_pQueue.argtypes = []
    size_pQueue.restype = c_int

# /usr/local/include/Lgm/size.h: 38
if hasattr(_libs['/usr/local/lib/libLanlGeoMag.dylib'], 'size_Lgm_LeapSeconds'):
    size_Lgm_LeapSeconds = _libs['/usr/local/lib/libLanlGeoMag.dylib'].size_Lgm_LeapSeconds
    size_Lgm_LeapSeconds.argtypes = []
    size_Lgm_LeapSeconds.restype = c_int

# /usr/local/include/Lgm/Lgm_QuadPack.h: 2
try:
    LGM_QUADPACK_H = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_QuadPack.h: 13
try:
    TRUE = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_QuadPack.h: 14
try:
    FALSE = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_QuadPack.h: 15
def dmax1(a, b):
    return (a > b) and a or b

# /usr/local/include/Lgm/Lgm_QuadPack.h: 16
def dmin1(a, b):
    return (a < b) and a or b

# /usr/local/include/Lgm/Lgm_CTrans.h: 4
def STRINGIFY(x):
    return x

# /usr/local/include/Lgm/Lgm_CTrans.h: 5
def EXPAND(x):
    return (STRINGIFY (x))

# /usr/local/include/Lgm/Lgm_WGS84.h: 5
try:
    WGS84_A = 6378.1369999999997
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 6
try:
    WGS84_B = 6356.7523142
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 7
try:
    WGS84_F = 0.0033528106718309896
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 8
try:
    WGS84_FINV = 298.25722293286969
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 10
try:
    WGS84_E2 = 0.0066943799901399998
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 11
try:
    WGS84_E = 0.081819190928906244
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 12
try:
    WGS84_EP2 = 0.0067394967565869027
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 13
try:
    WGS84_EP = 0.082094438036853665
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 14
try:
    WGS84_A2 = 40680631.590768993
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 15
try:
    WGS84_B2 = 40408299.984087057
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 16
try:
    WGS84_A2mB2 = 272331.60668193549
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 17
try:
    WGS84_E4 = 4.4814723641447188e-05
except:
    pass

# /usr/local/include/Lgm/Lgm_WGS84.h: 18
try:
    WGS84_1mE2 = 0.99330561999573896
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 15
try:
    DegPerRad = 57.295779513082323
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 16
try:
    RadPerDeg = 0.017453292519943295
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 17
try:
    RadPerArcSec = 4.8481368110953598e-06
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 18
try:
    M_SQRTPI = 1.7724538509055161
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 19
try:
    M_SQRTPI_2 = 0.88622692545275805
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 20
try:
    M_1_SQRTPI = 0.56418958354775628
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 21
try:
    M_2PI = 6.2831853071795862
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 22
try:
    M_OneThird = 0.33333333333333331
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 24
try:
    FALSE = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 25
try:
    TRUE = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 29
try:
    Re = 6378.1369999999997
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 32
try:
    AU = 149597870.0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 35
try:
    LGM_GOLD = 1.6180339887498949
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 36
try:
    LGM_1O_GOLD = 0.6180339887498949
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 37
try:
    LGM_1M_1O_GOLD = 0.38196601125010515
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 39
try:
    LGM_ERROR = (-1)
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 40
try:
    LGM_FILL_VALUE = (-9.9999999999999996e+30)
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 42
try:
    LGM_JD_J2000 = 2451545.0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 43
try:
    LGM_JD_GPS0 = 2444245.0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 44
try:
    LGM_JD_TAI0 = 2436205.0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 51
try:
    LGM_TIME_SYS_UTC = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 52
try:
    LGM_TIME_SYS_TAI = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 53
try:
    LGM_TIME_SYS_GPS = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 54
try:
    LGM_TIME_SYS_TT = 3
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 55
try:
    LGM_TIME_SYS_TDB = 4
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 56
try:
    LGM_TIME_SYS_UT1 = 5
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 69
try:
    EME2000_COORDS = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 70
try:
    ICRF2000_COORDS = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 71
try:
    GEI2000_COORDS = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 80
try:
    MOD_COORDS = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 92
try:
    TOD_COORDS = 3
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 102
try:
    TEME_COORDS = 4
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 119
try:
    PEF_COORDS = 5
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 136
try:
    WGS84_COORDS = 6
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 137
try:
    IRTF_COORDS = 6
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 138
try:
    GEO_COORDS = 6
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 164
try:
    GSE_COORDS = 7
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 166
try:
    GSM_COORDS = 8
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 168
try:
    SM_COORDS = 9
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 170
try:
    EDMAG_COORDS = 10
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 172
try:
    CDMAG_COORDS = 11
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 183
try:
    EME2000_TO_EME2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 184
try:
    EME2000_TO_ICRF2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 185
try:
    EME2000_TO_GEI2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 186
try:
    EME2000_TO_MOD = 102
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 187
try:
    EME2000_TO_TOD = 103
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 188
try:
    EME2000_TO_TEME = 104
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 189
try:
    EME2000_TO_PEF = 105
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 190
try:
    EME2000_TO_WGS84 = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 191
try:
    EME2000_TO_ITRF = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 192
try:
    EME2000_TO_GEO = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 193
try:
    EME2000_TO_GSE = 107
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 194
try:
    EME2000_TO_GSM = 108
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 195
try:
    EME2000_TO_SM = 109
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 196
try:
    EME2000_TO_EDMAG = 110
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 197
try:
    EME2000_TO_CDMAG = 111
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 199
try:
    ICRF2000_TO_EME2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 200
try:
    ICRF2000_TO_ICRF2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 201
try:
    ICRF2000_TO_GEI2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 202
try:
    ICRF2000_TO_MOD = 102
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 203
try:
    ICRF2000_TO_TOD = 103
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 204
try:
    ICRF2000_TO_TEME = 104
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 205
try:
    ICRF2000_TO_PEF = 105
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 206
try:
    ICRF2000_TO_WGS84 = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 207
try:
    ICRF2000_TO_ITRF = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 208
try:
    ICRF2000_TO_GEO = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 209
try:
    ICRF2000_TO_GSE = 107
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 210
try:
    ICRF2000_TO_GSM = 108
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 211
try:
    ICRF2000_TO_SM = 109
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 212
try:
    ICRF2000_TO_EDMAG = 110
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 213
try:
    ICRF2000_TO_CDMAG = 111
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 215
try:
    GEI2000_TO_EME2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 216
try:
    GEI2000_TO_ICRF2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 217
try:
    GEI2000_TO_GEI2000 = 101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 218
try:
    GEI2000_TO_MOD = 102
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 219
try:
    GEI2000_TO_TOD = 103
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 220
try:
    GEI2000_TO_TEME = 104
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 221
try:
    GEI2000_TO_PEF = 105
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 222
try:
    GEI2000_TO_WGS84 = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 223
try:
    GEI2000_TO_ITRF = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 224
try:
    GEI2000_TO_GEO = 106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 225
try:
    GEI2000_TO_GSE = 107
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 226
try:
    GEI2000_TO_GSM = 108
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 227
try:
    GEI2000_TO_SM = 109
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 228
try:
    GEI2000_TO_EDMAG = 110
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 229
try:
    GEI2000_TO_CDMAG = 111
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 231
try:
    MOD_TO_EME2000 = 201
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 232
try:
    MOD_TO_ICRF2000 = 201
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 233
try:
    MOD_TO_GEI2000 = 201
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 234
try:
    MOD_TO_MOD = 202
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 235
try:
    MOD_TO_TOD = 203
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 236
try:
    MOD_TO_TEME = 204
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 237
try:
    MOD_TO_PEF = 205
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 238
try:
    MOD_TO_WGS84 = 206
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 239
try:
    MOD_TO_ITRF = 206
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 240
try:
    MOD_TO_GEO = 206
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 241
try:
    MOD_TO_GSE = 207
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 242
try:
    MOD_TO_GSM = 208
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 243
try:
    MOD_TO_SM = 209
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 244
try:
    MOD_TO_EDMAG = 210
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 245
try:
    MOD_TO_CDMAG = 211
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 247
try:
    TOD_TO_EME2000 = 301
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 248
try:
    TOD_TO_ICRF2000 = 301
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 249
try:
    TOD_TO_GEI2000 = 301
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 250
try:
    TOD_TO_MOD = 302
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 251
try:
    TOD_TO_TOD = 303
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 252
try:
    TOD_TO_TEME = 304
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 253
try:
    TOD_TO_PEF = 305
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 254
try:
    TOD_TO_WGS84 = 306
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 255
try:
    TOD_TO_ITRF = 306
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 256
try:
    TOD_TO_GEO = 306
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 257
try:
    TOD_TO_GSE = 307
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 258
try:
    TOD_TO_GSM = 308
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 259
try:
    TOD_TO_SM = 309
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 260
try:
    TOD_TO_EDMAG = 310
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 261
try:
    TOD_TO_CDMAG = 311
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 263
try:
    TEME_TO_EME2000 = 401
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 264
try:
    TEME_TO_ICRF2000 = 401
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 265
try:
    TEME_TO_GEI2000 = 401
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 266
try:
    TEME_TO_MOD = 402
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 267
try:
    TEME_TO_TOD = 403
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 268
try:
    TEME_TO_TEME = 404
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 269
try:
    TEME_TO_PEF = 405
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 270
try:
    TEME_TO_WGS84 = 406
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 271
try:
    TEME_TO_ITRF = 406
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 272
try:
    TEME_TO_GEO = 406
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 273
try:
    TEME_TO_GSE = 407
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 274
try:
    TEME_TO_GSM = 408
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 275
try:
    TEME_TO_SM = 409
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 276
try:
    TEME_TO_EDMAG = 410
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 277
try:
    TEME_TO_CDMAG = 411
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 279
try:
    PEF_TO_EME2000 = 501
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 280
try:
    PEF_TO_ICRF2000 = 501
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 281
try:
    PEF_TO_GEI2000 = 501
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 282
try:
    PEF_TO_MOD = 502
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 283
try:
    PEF_TO_TOD = 503
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 284
try:
    PEF_TO_TEME = 504
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 285
try:
    PEF_TO_PEF = 505
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 286
try:
    PEF_TO_WGS84 = 506
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 287
try:
    PEF_TO_ITRF = 506
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 288
try:
    PEF_TO_GEO = 506
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 289
try:
    PEF_TO_GSE = 507
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 290
try:
    PEF_TO_GSM = 508
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 291
try:
    PEF_TO_SM = 509
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 292
try:
    PEF_TO_EDMAG = 510
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 293
try:
    PEF_TO_CDMAG = 511
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 295
try:
    WGS84_TO_EME2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 296
try:
    WGS84_TO_ICRF2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 297
try:
    WGS84_TO_GEI2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 298
try:
    WGS84_TO_MOD = 602
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 299
try:
    WGS84_TO_TOD = 603
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 300
try:
    WGS84_TO_TEME = 604
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 301
try:
    WGS84_TO_PEF = 605
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 302
try:
    WGS84_TO_WGS84 = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 303
try:
    WGS84_TO_ITRF = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 304
try:
    WGS84_TO_GEO = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 305
try:
    WGS84_TO_GSE = 607
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 306
try:
    WGS84_TO_GSM = 608
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 307
try:
    WGS84_TO_SM = 609
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 308
try:
    WGS84_TO_EDMAG = 610
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 309
try:
    WGS84_TO_CDMAG = 611
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 311
try:
    ITRF_TO_EME2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 312
try:
    ITRF_TO_ICRF2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 313
try:
    ITRF_TO_GEI2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 314
try:
    ITRF_TO_MOD = 602
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 315
try:
    ITRF_TO_TOD = 603
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 316
try:
    ITRF_TO_TEME = 604
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 317
try:
    ITRF_TO_PEF = 605
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 318
try:
    ITRF_TO_WGS84 = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 319
try:
    ITRF_TO_ITRF = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 320
try:
    ITRF_TO_GEO = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 321
try:
    ITRF_TO_GSE = 607
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 322
try:
    ITRF_TO_GSM = 608
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 323
try:
    ITRF_TO_SM = 609
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 324
try:
    ITRF_TO_EDMAG = 610
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 325
try:
    ITRF_TO_CDMAG = 611
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 327
try:
    GEO_TO_EME2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 328
try:
    GEO_TO_ICRF2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 329
try:
    GEO_TO_GEI2000 = 601
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 330
try:
    GEO_TO_MOD = 602
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 331
try:
    GEO_TO_TOD = 603
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 332
try:
    GEO_TO_TEME = 604
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 333
try:
    GEO_TO_PEF = 605
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 334
try:
    GEO_TO_WGS84 = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 335
try:
    GEO_TO_ITRF = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 336
try:
    GEO_TO_GEO = 606
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 337
try:
    GEO_TO_GSE = 607
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 338
try:
    GEO_TO_GSM = 608
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 339
try:
    GEO_TO_SM = 609
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 340
try:
    GEO_TO_EDMAG = 610
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 341
try:
    GEO_TO_CDMAG = 611
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 343
try:
    GSE_TO_EME2000 = 701
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 344
try:
    GSE_TO_ICRF2000 = 701
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 345
try:
    GSE_TO_GEI2000 = 701
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 346
try:
    GSE_TO_MOD = 702
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 347
try:
    GSE_TO_TOD = 703
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 348
try:
    GSE_TO_TEME = 704
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 349
try:
    GSE_TO_PEF = 705
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 350
try:
    GSE_TO_WGS84 = 706
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 351
try:
    GSE_TO_ITRF = 706
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 352
try:
    GSE_TO_GEO = 706
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 353
try:
    GSE_TO_GSE = 707
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 354
try:
    GSE_TO_GSM = 708
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 355
try:
    GSE_TO_SM = 709
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 356
try:
    GSE_TO_EDMAG = 710
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 357
try:
    GSE_TO_CDMAG = 711
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 359
try:
    GSM_TO_EME2000 = 801
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 360
try:
    GSM_TO_ICRF2000 = 801
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 361
try:
    GSM_TO_GEI2000 = 801
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 362
try:
    GSM_TO_MOD = 802
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 363
try:
    GSM_TO_TOD = 803
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 364
try:
    GSM_TO_TEME = 804
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 365
try:
    GSM_TO_PEF = 805
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 366
try:
    GSM_TO_WGS84 = 806
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 367
try:
    GSM_TO_ITRF = 806
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 368
try:
    GSM_TO_GEO = 806
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 369
try:
    GSM_TO_GSE = 807
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 370
try:
    GSM_TO_GSM = 808
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 371
try:
    GSM_TO_SM = 809
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 372
try:
    GSM_TO_EDMAG = 810
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 373
try:
    GSM_TO_CDMAG = 811
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 375
try:
    SM_TO_EME2000 = 901
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 376
try:
    SM_TO_ICRF2000 = 901
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 377
try:
    SM_TO_GEI2000 = 901
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 378
try:
    SM_TO_MOD = 902
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 379
try:
    SM_TO_TOD = 903
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 380
try:
    SM_TO_TEME = 904
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 381
try:
    SM_TO_PEF = 905
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 382
try:
    SM_TO_WGS84 = 906
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 383
try:
    SM_TO_ITRF = 906
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 384
try:
    SM_TO_GEO = 906
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 385
try:
    SM_TO_GSE = 907
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 386
try:
    SM_TO_GSM = 908
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 387
try:
    SM_TO_SM = 909
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 388
try:
    SM_TO_EDMAG = 910
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 389
try:
    SM_TO_CDMAG = 911
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 391
try:
    EDMAG_TO_EME2000 = 1001
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 392
try:
    EDMAG_TO_ICRF2000 = 1001
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 393
try:
    EDMAG_TO_GEI2000 = 1001
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 394
try:
    EDMAG_TO_MOD = 1002
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 395
try:
    EDMAG_TO_TOD = 1003
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 396
try:
    EDMAG_TO_TEME = 1004
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 397
try:
    EDMAG_TO_PEF = 1005
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 398
try:
    EDMAG_TO_WGS84 = 1006
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 399
try:
    EDMAG_TO_ITRF = 1006
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 400
try:
    EDMAG_TO_GEO = 1006
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 401
try:
    EDMAG_TO_GSE = 1007
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 402
try:
    EDMAG_TO_GSM = 1008
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 403
try:
    EDMAG_TO_SM = 1009
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 404
try:
    EDMAG_TO_EDMAG = 1010
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 405
try:
    EDMAG_TO_CDMAG = 1011
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 407
try:
    CDMAG_TO_EME2000 = 1101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 408
try:
    CDMAG_TO_ICRF2000 = 1101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 409
try:
    CDMAG_TO_GEI2000 = 1101
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 410
try:
    CDMAG_TO_MOD = 1102
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 411
try:
    CDMAG_TO_TOD = 1103
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 412
try:
    CDMAG_TO_TEME = 1104
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 413
try:
    CDMAG_TO_PEF = 1105
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 414
try:
    CDMAG_TO_WGS84 = 1106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 415
try:
    CDMAG_TO_ITRF = 1106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 416
try:
    CDMAG_TO_GEO = 1106
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 417
try:
    CDMAG_TO_GSE = 1107
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 418
try:
    CDMAG_TO_GSM = 1108
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 419
try:
    CDMAG_TO_SM = 1109
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 420
try:
    CDMAG_TO_EDMAG = 1110
except:
    pass

# /usr/local/include/Lgm/Lgm_CTrans.h: 421
try:
    CDMAG_TO_CDMAG = 1111
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 6
try:
    OCTREE_MAX_LEVELS = 16
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 7
try:
    OCTREE_ROOT_LEVEL = 15
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 8
try:
    OCTREE_MAX_VAL = 32768.0
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 9
try:
    OCTREE_MAX_DATA_PER_OCTANT = 10
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 11
try:
    TRUE = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 12
try:
    FALSE = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 15
try:
    OCTREE_KNN_SUCCESS = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 16
try:
    OCTREE_KNN_TOO_FEW_NNS = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 17
try:
    OCTREE_KNN_NOT_ENOUGH_DATA = (-1)
except:
    pass

# /usr/local/include/Lgm/Lgm_Octree.h: 19
try:
    OCTREE_IS_NULL = (-2)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 11
try:
    LGM_ELECTRON_MASS = 9.1093818800000006e-31
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 12
try:
    LGM_AMU = 1.6605379999999998e-27
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 13
try:
    LGM_PROTON_MASS = (1.0079400000000001 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 14
try:
    LGM_OXYGEN_MASS = (15.9994 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 15
try:
    RE = 6378135.0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 16
try:
    LGM_CC = 299792458.0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 17
try:
    LGM_EE = 1.6022000000000001e-19
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 31
try:
    LGM_OPEN_IMF = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 32
try:
    LGM_CLOSED = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 33
try:
    LGM_OPEN_N_LOBE = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 34
try:
    LGM_OPEN_S_LOBE = 3
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 35
try:
    LGM_INSIDE_EARTH = (-1)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 36
try:
    LGM_TARGET_HEIGHT_UNREACHABLE = (-2)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 39
try:
    LGM_MAGSTEP_KMAX = 9
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 40
try:
    LGM_MAGSTEP_IMAX = (LGM_MAGSTEP_KMAX + 1)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 41
try:
    LGM_MAGSTEP_JMAX = (LGM_MAGSTEP_KMAX + 2)
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 42
try:
    LGM_MAGSTEP_REDMAX = 1.0000000000000001e-05
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 43
try:
    LGM_MAGSTEP_REDMIN = 0.69999999999999996
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 44
try:
    LGM_MAGSTEP_SCLMAX = 0.10000000000000001
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 45
try:
    LGM_MAGSTEP_SAFE1 = 0.25
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 46
try:
    LGM_MAGSTEP_SAFE2 = 0.69999999999999996
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 48
try:
    DQAGS = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 49
try:
    DQAGP = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 50
try:
    DQK21 = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 59
try:
    LINEAR = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 60
try:
    LINEAR_DFI = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 61
try:
    QUADRATIC = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 62
try:
    QUADRATIC_DFI = 3
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 63
try:
    NEWTON_INTERP = 4
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 65
try:
    LGM_CDIP = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 66
try:
    LGM_EDIP = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 67
try:
    LGM_IGRF = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 69
try:
    LGM_MAX_INTERP_PNTS = 10000
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 71
try:
    LGM_RELATIVE_JUMP_METHOD = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_MagModelInfo.h: 72
try:
    LGM_ABSOLUTE_JUMP_METHOD = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 19
try:
    LGM_AP8MAX = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 20
try:
    LGM_AP8MIN = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 21
try:
    LGM_AE8MAX = 7
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 22
try:
    LGM_AE8MIN = 8
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 23
try:
    LGM_INTEGRAL_FLUX = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_AE8_AP8.h: 24
try:
    LGM_DIFFERENTIAL_FLUX = 2
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 6
try:
    ELECTRON_MASS = 9.1093818800000006e-31
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 7
try:
    AMU = 1.6605379999999998e-27
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 8
try:
    PROTON_MASS = (1.0079400000000001 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 9
try:
    OXYGEN_MASS = (15.9994 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 10
try:
    RE = 6378135.0
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 11
try:
    CC = 299792458.0
except:
    pass

# /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 12
try:
    EE = 1.6022000000000001e-19
except:
    pass

# /usr/local/include/Lgm/Lgm_FluxToPsd.h: 54
try:
    LGM_Ee0 = 0.51099890999999997
except:
    pass

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 4
def STRINGIFY(x):
    return x

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 5
def EXPAND(x):
    return (STRINGIFY (x))

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 13
try:
    FALSE = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_LeapSeconds.h: 14
try:
    TRUE = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 10
try:
    ELECTRON_MASS = 9.1093818800000006e-31
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 11
try:
    AMU = 1.6605379999999998e-27
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 12
try:
    PROTON_MASS = (1.0079400000000001 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 13
try:
    OXYGEN_MASS = (15.9994 * AMU)
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 14
try:
    RE = 6378135.0
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 15
try:
    CC = 299792458.0
except:
    pass

# /usr/local/include/Lgm/Lgm_LstarInfo.h: 16
try:
    EE = 1.6022000000000001e-19
except:
    pass

# /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 14
try:
    MAX_PITCH_ANGLES = 90
except:
    pass

# /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 52
try:
    LGM_Ee0 = 0.51099890999999997
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 172
try:
    SGP_CK2 = 0.000541308
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 173
try:
    SGP_CK4 = 6.2098875000000002e-07
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 174
try:
    SGP_E6A = 9.9999999999999995e-07
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 175
try:
    SGP_QOMS2T = 1.88027916e-09
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 176
try:
    SGP_S = 1.0122292799999999
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 177
try:
    SGP_TOTHRD = 0.66666667000000002
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 178
try:
    SGP_XJ3 = (-2.53881e-06)
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 179
try:
    SGP_XKE = 0.0743669161
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 180
try:
    SGP_XKMPER = 6378.1350000000002
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 181
try:
    SGP_XMNPDA = 1440.0
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 182
try:
    SGP_AE = 1.0
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 183
try:
    SGP_DE2RA = 0.017453292499999998
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 184
try:
    SGP_PI = 3.1415926500000002
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 185
try:
    SGP_PIO2 = 1.5707963300000001
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 186
try:
    SGP_TWOPI = 6.2831853000000004
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 187
try:
    SGP_X3PIO2 = 4.7123889800000001
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 192
try:
    SGP_wgs72old = 0
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 193
try:
    SGP_wgs72 = 1
except:
    pass

# /usr/local/include/Lgm/Lgm_Sgp.h: 194
try:
    SGP_wgs84 = 2
except:
    pass

Lgm_Vector = struct_Lgm_Vector # /usr/local/include/Lgm/Lgm_Vec.h: 7

LgmPosition = struct_LgmPosition # /usr/local/include/Lgm/Lgm_Vec.h: 13

Lgm_LeapSeconds = struct_Lgm_LeapSeconds # /usr/local/include/Lgm/Lgm_CTrans.h: 434

Lgm_DateTime = struct_Lgm_DateTime # /usr/local/include/Lgm/Lgm_CTrans.h: 480

Lgm_CTrans = struct_Lgm_CTrans # /usr/local/include/Lgm/Lgm_CTrans.h: 713

_Lgm_OctreeData = struct__Lgm_OctreeData # /usr/local/include/Lgm/Lgm_Octree.h: 28

_Lgm_OctreeCell = struct__Lgm_OctreeCell # /usr/local/include/Lgm/Lgm_Octree.h: 36

_pQueue = struct__pQueue # /usr/local/include/Lgm/Lgm_Octree.h: 59

Lgm_MagModelInfo = struct_Lgm_MagModelInfo # /usr/local/include/Lgm/Lgm_MagModelInfo.h: 294

Lgm_NgaEopp = struct_Lgm_NgaEopp # /usr/local/include/Lgm/Lgm_Eop.h: 26

Lgm_Eop = struct_Lgm_Eop # /usr/local/include/Lgm/Lgm_Eop.h: 45

Lgm_EopOne = struct_Lgm_EopOne # /usr/local/include/Lgm/Lgm_Eop.h: 63

Lgm_FieldIntInfo = struct_Lgm_FieldIntInfo # /usr/local/include/Lgm/Lgm_FieldIntInfo.h: 48

Lgm_FluxToPsd = struct_Lgm_FluxToPsd # /usr/local/include/Lgm/Lgm_FluxToPsd.h: 120

Lgm_LstarInfo = struct_Lgm_LstarInfo # /usr/local/include/Lgm/Lgm_LstarInfo.h: 114

Lgm_MagEphemInfo = struct_Lgm_MagEphemInfo # /usr/local/include/Lgm/Lgm_MagEphemInfo.h: 142

Lgm_PhaseSpaceDensity = struct_Lgm_PhaseSpaceDensity # /usr/local/include/Lgm/Lgm_PhaseSpaceDensity.h: 128

_SgpTLE = struct__SgpTLE # /usr/local/include/Lgm/Lgm_Sgp.h: 99

# No inserted files

