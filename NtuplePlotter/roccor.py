# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_roccor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_roccor')
    _roccor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_roccor', [dirname(__file__)])
        except ImportError:
            import _roccor
            return _roccor
        try:
            _mod = imp.load_module('_roccor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _roccor = swig_import_helper()
    del swig_import_helper
else:
    import _roccor
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _roccor.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _roccor.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _roccor.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _roccor.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _roccor.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _roccor.SwigPyIterator_equal(self, x)

    def copy(self):
        return _roccor.SwigPyIterator_copy(self)

    def next(self):
        return _roccor.SwigPyIterator_next(self)

    def __next__(self):
        return _roccor.SwigPyIterator___next__(self)

    def previous(self):
        return _roccor.SwigPyIterator_previous(self)

    def advance(self, n):
        return _roccor.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _roccor.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _roccor.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _roccor.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _roccor.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _roccor.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _roccor.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _roccor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class CrystalBall(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CrystalBall, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CrystalBall, name)
    __repr__ = _swig_repr
    pi = _roccor.CrystalBall_pi
    SPiO2 = _roccor.CrystalBall_SPiO2
    S2 = _roccor.CrystalBall_S2
    __swig_setmethods__["m"] = _roccor.CrystalBall_m_set
    __swig_getmethods__["m"] = _roccor.CrystalBall_m_get
    if _newclass:
        m = _swig_property(_roccor.CrystalBall_m_get, _roccor.CrystalBall_m_set)
    __swig_setmethods__["s"] = _roccor.CrystalBall_s_set
    __swig_getmethods__["s"] = _roccor.CrystalBall_s_get
    if _newclass:
        s = _swig_property(_roccor.CrystalBall_s_get, _roccor.CrystalBall_s_set)
    __swig_setmethods__["a"] = _roccor.CrystalBall_a_set
    __swig_getmethods__["a"] = _roccor.CrystalBall_a_get
    if _newclass:
        a = _swig_property(_roccor.CrystalBall_a_get, _roccor.CrystalBall_a_set)
    __swig_setmethods__["n"] = _roccor.CrystalBall_n_set
    __swig_getmethods__["n"] = _roccor.CrystalBall_n_get
    if _newclass:
        n = _swig_property(_roccor.CrystalBall_n_get, _roccor.CrystalBall_n_set)
    __swig_setmethods__["B"] = _roccor.CrystalBall_B_set
    __swig_getmethods__["B"] = _roccor.CrystalBall_B_get
    if _newclass:
        B = _swig_property(_roccor.CrystalBall_B_get, _roccor.CrystalBall_B_set)
    __swig_setmethods__["C"] = _roccor.CrystalBall_C_set
    __swig_getmethods__["C"] = _roccor.CrystalBall_C_get
    if _newclass:
        C = _swig_property(_roccor.CrystalBall_C_get, _roccor.CrystalBall_C_set)
    __swig_setmethods__["D"] = _roccor.CrystalBall_D_set
    __swig_getmethods__["D"] = _roccor.CrystalBall_D_get
    if _newclass:
        D = _swig_property(_roccor.CrystalBall_D_get, _roccor.CrystalBall_D_set)
    __swig_setmethods__["N"] = _roccor.CrystalBall_N_set
    __swig_getmethods__["N"] = _roccor.CrystalBall_N_get
    if _newclass:
        N = _swig_property(_roccor.CrystalBall_N_get, _roccor.CrystalBall_N_set)
    __swig_setmethods__["NA"] = _roccor.CrystalBall_NA_set
    __swig_getmethods__["NA"] = _roccor.CrystalBall_NA_get
    if _newclass:
        NA = _swig_property(_roccor.CrystalBall_NA_get, _roccor.CrystalBall_NA_set)
    __swig_setmethods__["Ns"] = _roccor.CrystalBall_Ns_set
    __swig_getmethods__["Ns"] = _roccor.CrystalBall_Ns_get
    if _newclass:
        Ns = _swig_property(_roccor.CrystalBall_Ns_get, _roccor.CrystalBall_Ns_set)
    __swig_setmethods__["NC"] = _roccor.CrystalBall_NC_set
    __swig_getmethods__["NC"] = _roccor.CrystalBall_NC_get
    if _newclass:
        NC = _swig_property(_roccor.CrystalBall_NC_get, _roccor.CrystalBall_NC_set)
    __swig_setmethods__["F"] = _roccor.CrystalBall_F_set
    __swig_getmethods__["F"] = _roccor.CrystalBall_F_get
    if _newclass:
        F = _swig_property(_roccor.CrystalBall_F_get, _roccor.CrystalBall_F_set)
    __swig_setmethods__["G"] = _roccor.CrystalBall_G_set
    __swig_getmethods__["G"] = _roccor.CrystalBall_G_get
    if _newclass:
        G = _swig_property(_roccor.CrystalBall_G_get, _roccor.CrystalBall_G_set)
    __swig_setmethods__["k"] = _roccor.CrystalBall_k_set
    __swig_getmethods__["k"] = _roccor.CrystalBall_k_get
    if _newclass:
        k = _swig_property(_roccor.CrystalBall_k_get, _roccor.CrystalBall_k_set)
    __swig_setmethods__["cdfMa"] = _roccor.CrystalBall_cdfMa_set
    __swig_getmethods__["cdfMa"] = _roccor.CrystalBall_cdfMa_get
    if _newclass:
        cdfMa = _swig_property(_roccor.CrystalBall_cdfMa_get, _roccor.CrystalBall_cdfMa_set)
    __swig_setmethods__["cdfPa"] = _roccor.CrystalBall_cdfPa_set
    __swig_getmethods__["cdfPa"] = _roccor.CrystalBall_cdfPa_get
    if _newclass:
        cdfPa = _swig_property(_roccor.CrystalBall_cdfPa_get, _roccor.CrystalBall_cdfPa_set)

    def __init__(self, *args):
        this = _roccor.new_CrystalBall(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def init(self, m_, s_, a_, n_):
        return _roccor.CrystalBall_init(self, m_, s_, a_, n_)

    def pdf(self, *args):
        return _roccor.CrystalBall_pdf(self, *args)

    def cdf(self, x):
        return _roccor.CrystalBall_cdf(self, x)

    def invcdf(self, u):
        return _roccor.CrystalBall_invcdf(self, u)
    __swig_destroy__ = _roccor.delete_CrystalBall
    __del__ = lambda self: None
CrystalBall_swigregister = _roccor.CrystalBall_swigregister
CrystalBall_swigregister(CrystalBall)

class RocRes(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RocRes, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RocRes, name)
    __repr__ = _swig_repr
    NMAXETA = _roccor.RocRes_NMAXETA
    NMAXTRK = _roccor.RocRes_NMAXTRK
    MC = _roccor.RocRes_MC
    Data = _roccor.RocRes_Data
    Extra = _roccor.RocRes_Extra
    __swig_setmethods__["cb"] = _roccor.RocRes_cb_set
    __swig_getmethods__["cb"] = _roccor.RocRes_cb_get
    if _newclass:
        cb = _swig_property(_roccor.RocRes_cb_get, _roccor.RocRes_cb_set)

    def __init__(self):
        this = _roccor.new_RocRes()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getEtaBin(self, feta):
        return _roccor.RocRes_getEtaBin(self, feta)

    def getNBinDT(self, v, H):
        return _roccor.RocRes_getNBinDT(self, v, H)

    def getNBinMC(self, v, H):
        return _roccor.RocRes_getNBinMC(self, v, H)

    def getUrnd(self, H, F, v):
        return _roccor.RocRes_getUrnd(self, H, F, v)

    def dumpParams(self):
        return _roccor.RocRes_dumpParams(self)

    def init(self, filename):
        return _roccor.RocRes_init(self, filename)

    def reset(self):
        return _roccor.RocRes_reset(self)
    __swig_destroy__ = _roccor.delete_RocRes
    __del__ = lambda self: None

    def Sigma(self, pt, H, F):
        return _roccor.RocRes_Sigma(self, pt, H, F)

    def kSpread(self, gpt, rpt, eta, nlayers, w):
        return _roccor.RocRes_kSpread(self, gpt, rpt, eta, nlayers, w)

    def kSmear(self, *args):
        return _roccor.RocRes_kSmear(self, *args)

    def kExtra(self, pt, eta, nlayers, u, w):
        return _roccor.RocRes_kExtra(self, pt, eta, nlayers, u, w)

    def getkDat(self, H):
        return _roccor.RocRes_getkDat(self, H)

    def getkRes(self, H):
        return _roccor.RocRes_getkRes(self, H)
RocRes_swigregister = _roccor.RocRes_swigregister
RocRes_swigregister(RocRes)

class RocOne(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RocOne, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RocOne, name)
    __repr__ = _swig_repr
    NMAXETA = _roccor.RocOne_NMAXETA
    NMAXPHI = _roccor.RocOne_NMAXPHI
    MC = _roccor.RocOne_MC
    DT = _roccor.RocOne_DT
    __swig_destroy__ = _roccor.delete_RocOne
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _roccor.new_RocOne(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def checkSYS(self, iSYS, iMEM, kSYS=0, kMEM=0):
        return _roccor.RocOne_checkSYS(self, iSYS, iMEM, kSYS, kMEM)

    def checkTIGHT(self, iTYPE, iSYS, iMEM, kTYPE=0, kSYS=0, kMEM=0):
        return _roccor.RocOne_checkTIGHT(self, iTYPE, iSYS, iMEM, kTYPE, kSYS, kMEM)

    def reset(self):
        return _roccor.RocOne_reset(self)

    def init(self, filename, iTYPE=0, iSYS=0, iMEM=0):
        return _roccor.RocOne_init(self, filename, iTYPE, iSYS, iMEM)

    def kScaleDT(self, Q, pt, eta, phi):
        return _roccor.RocOne_kScaleDT(self, Q, pt, eta, phi)

    def kScaleMC(self, Q, pt, eta, phi, kSMR=1):
        return _roccor.RocOne_kScaleMC(self, Q, pt, eta, phi, kSMR)

    def kScaleAndSmearMC(self, Q, pt, eta, phi, n, u, w):
        return _roccor.RocOne_kScaleAndSmearMC(self, Q, pt, eta, phi, n, u, w)

    def kScaleFromGenMC(self, Q, pt, eta, phi, n, gt, w):
        return _roccor.RocOne_kScaleFromGenMC(self, Q, pt, eta, phi, n, gt, w)

    def kGenSmear(self, *args):
        return _roccor.RocOne_kGenSmear(self, *args)

    def getM(self, T, H, F):
        return _roccor.RocOne_getM(self, T, H, F)

    def getA(self, T, H, F):
        return _roccor.RocOne_getA(self, T, H, F)

    def getK(self, T, H):
        return _roccor.RocOne_getK(self, T, H)

    def getR(self):
        return _roccor.RocOne_getR(self)
RocOne_swigregister = _roccor.RocOne_swigregister
RocOne_swigregister(RocOne)

class RoccoR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RoccoR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RoccoR, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _roccor.new_RoccoR(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _roccor.delete_RoccoR
    __del__ = lambda self: None

    def init(self, dirname):
        return _roccor.RoccoR_init(self, dirname)

    def kGenSmear(self, *args):
        return _roccor.RoccoR_kGenSmear(self, *args)

    def kScaleDT(self, Q, pt, eta, phi, s=0, m=0):
        return _roccor.RoccoR_kScaleDT(self, Q, pt, eta, phi, s, m)

    def kScaleAndSmearMC(self, Q, pt, eta, phi, n, u, w, s=0, m=0):
        return _roccor.RoccoR_kScaleAndSmearMC(self, Q, pt, eta, phi, n, u, w, s, m)

    def kScaleFromGenMC(self, Q, pt, eta, phi, n, gt, w, s=0, m=0):
        return _roccor.RoccoR_kScaleFromGenMC(self, Q, pt, eta, phi, n, gt, w, s, m)

    def getM(self, T, H, F, E=0, m=0):
        return _roccor.RoccoR_getM(self, T, H, F, E, m)

    def getA(self, T, H, F, E=0, m=0):
        return _roccor.RoccoR_getA(self, T, H, F, E, m)

    def getK(self, T, H, E=0, m=0):
        return _roccor.RoccoR_getK(self, T, H, E, m)

    def Nset(self):
        return _roccor.RoccoR_Nset(self)

    def Nmem(self, s=0):
        return _roccor.RoccoR_Nmem(self, s)
RoccoR_swigregister = _roccor.RoccoR_swigregister
RoccoR_swigregister(RoccoR)

# This file is compatible with both classic and new-style classes.


