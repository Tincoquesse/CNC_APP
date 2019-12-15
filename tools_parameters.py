def drill_feed(diameter, vc = 35):
    '''Parametr dla wierteł HSS, zwraca posuw mm/min'''
    d = diameter
    fz = 0.1
    # rotation for minute
    n = (1000.0 * vc) / (float(d) * 3.14)
    # feed mm/min
    if diameter in range(0,5):
        fz = 0.1
    elif diameter in range(4,9):
        fz = 0.18
    else:
        fz = 0.22
    f = fz * n
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
    fz = 0.02

    # revolution for minute
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    # feed milimeter for minute
    f = fz * n
    return int(f)


def cutter_spin(diameter, vc = 400):
    '''Parametr dla frezów, zwraca obroty'''
    d = diameter
    fz = 0.02

    # revolutions for minute
    n = (1000.0 * vc)/(float(d) * 3.14)
    if n > 22000:
        n = 22000
    return int(n)
