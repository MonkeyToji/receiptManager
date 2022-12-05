def idConverter(idValue):
    points = idValue.split('--')
    output = points[1]
    return {"points": int(output)}
