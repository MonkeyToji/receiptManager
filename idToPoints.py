def idConverter(idValue):
    points = idValue["id"].split('--')
    output = points[1]
    return {"points": output}
