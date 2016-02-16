import flavio
from math import pi,log

"""Functions for imroved Isgur-Wise relations to obtain tensor
form factors from vector form factors in the heavy quark limit."""


def improved_isgur_wise(q2, ff, par, B, V, scale):
    mB = par['m_'+B]
    mV = par['m_'+V]
    mb = flavio.physics.running.running.get_mb(par, scale)
    alpha_s = flavio.physics.running.running.get_alpha(par, scale)['alpha_s']
    D0v = 0
    C0v = 0
    # eq. (3.8) of arXiv:1006.5013
    kappa = 1-2*alpha_s/(3*pi)*log(scale/mb)
    # eq. (3.6) of arXiv:1006.5013
    ff['T1'] = kappa*ff['V']
    ff['T2'] = kappa*ff['A1']
    # derived in analogy to arXiv:1006.5013 using hep-ph/0404250
    ff['T23'] = kappa*ff['A12'] * 2*mB**2/q2
    return ff