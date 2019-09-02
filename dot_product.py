def dpv(vec1, vec2)->float:
    """Dot product of two vectors"""
    product = 0.

    for idx, val in enumerate(vec1):
        product += val * vec2[idx]

    return product
