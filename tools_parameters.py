import numpy

def drill_feed(diameter, vc = 35):
    '''Parametr dla wierteł HSS, zwraca posuw mm/min'''
    d = diameter
    fz = 0
    # rotation for minute
    n = (1000.0 * vc) / (float(d) * 3.14)
    # feed mm/min
    if diameter * 10 in numpy.arange(0, 51, 1):
        fz = 0.1
    elif diameter * 10 in numpy.arange(51, 76, 1):
        fz = 0.12
    elif diameter * 10 in numpy.arange(76, 100, 1):
        fz = 0.15
    else:
        fz = 0.20
    f = fz * int(n)
    return int(f)


def drill_spin(diameter, vc = 35):
    '''Parametr dla wierteł HSS, zwraca obroty na minute'''
    d = diameter

    # rotation for minute
    n = (1000.0 * vc) / (float(d) * 3.14)
    return int(n)


def cutter_feed(diameter, vc = 400):
    '''Parametr dla frezów, zwraca posuw mm/min '''
    d = diameter
    fz = d * 0.005

    # revolution for minute
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    # feed milimeter for minute
    f = fz * n
    return int(f)

def cutter_feed_hundred(diameter, vc = 400):
    '''Parametr dla frezów, zwraca posuw mm/100 obrotów '''
    d = diameter
    fz = 0.02

    # revolution for minute
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    # feed milimeter for minute
    f = fz * n/60
    return float(f)

def cutter_spin(diameter, vc = 400):
    '''Parametr dla frezów, zwraca obroty'''
    d = diameter
    fz = 0.02

    # revolutions for minute
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    return int(n)

