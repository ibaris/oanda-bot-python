# -*- coding: utf-8 -*-
"""
HEADER
======
*Created on 22.03.2021 by bari_is*

*For COPYING and LICENSE details, please refer to the LICENSE file*

"""

__all__ = ["Pairs"]

__AUD__ = ["AUD_CAD",
           "AUD_CHF",
           "AUD_JPY",
           "AUD_NZD",
           "AUD_USD"]

__CAD__ = ["CAD_CHF",
           "CAD_JPY"]

__EUR__ = ["EUR_AUD",
           "EUR_CAD",
           "EUR_CHF",
           "EUR_GBP",
           "EUR_JPY",
           "EUR_NZD",
           "EUR_USD"]

__GBP__ = ["GBP_AUD",
           "GBP_CAD",
           "GBP_CHF",
           "GBP_JPY",
           "GBP_NZD",
           "GBP_USD"]

__NZD__ = ["NZD_CAD",
           "NZD_CHF",
           "NZD_JPY",
           "NZD_USD"]

__USD__ = ["USD_CAD",
           "USD_CHF",
           "USD_JPY"]

__MAJOR__ = ["AUD_CAD",
             "AUD_CHF",
             "AUD_JPY",
             "AUD_NZD",
             "AUD_USD",

             "CAD_CHF",
             "CAD_JPY",

             "CHF_JPY",

             "EUR_AUD",
             "EUR_CAD",
             "EUR_CHF",
             "EUR_GBP",
             "EUR_JPY",
             "EUR_NZD",
             "EUR_USD",

             "GBP_AUD",
             "GBP_CAD",
             "GBP_CHF",
             "GBP_JPY",
             "GBP_NZD",
             "GBP_USD",

             "NZD_CAD",
             "NZD_CHF",
             "NZD_JPY",
             "NZD_USD",

             "USD_CAD",
             "USD_CHF",
             "USD_JPY"]


class Pairs(dict):
    """ Represents the optimization result.
    Attributes
    ----------
    major : list
        Returns the major currency pairs.

    Notes
    -----
    There may be additional attributes not listed above depending of the
    specific solver. Since this class is essentially a subclass of dict
    with attribute accessors, one can see which attributes are available
    using the `keys()` method.
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __repr__(self):
        if self.keys():
            m = max(map(len, list(self.keys()))) + 1
            return '\n'.join([k.rjust(m) + ': ' + repr(v)
                              for k, v in sorted(self.items())])
        else:
            return self.__class__.__name__ + "()"

    def __dir__(self):
        return list(self.keys())


Pairs = Pairs(major=__MAJOR__, aud=__AUD__, cad=__CAD__, eur=__EUR__, gbp=__GBP__, nzd=__NZD__, usd=__USD__)
