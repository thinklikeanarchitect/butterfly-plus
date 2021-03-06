# assign inputs
_value, _Cmu_, _kappa_, _E_ = IN
epsilonWallFunction = None

try:
    from butterfly.fields import EpsilonWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download butterfly from package manager.' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/ladybug-analysis-tools/butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    epsilonWallFunction = EpsilonWallFunction(_value, _Cmu_, _kappa_, _E_)


# assign outputs to OUT
OUT = (epsilonWallFunction,)