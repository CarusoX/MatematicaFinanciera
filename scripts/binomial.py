def get_price_call_put(d, i, u, vu, vd):
    p = (1 + i - d) / (u - d)
    q = (u - (1 + i)) / (u - d)
    return 1 / (1 + i) * (vu * p + vd * q)
