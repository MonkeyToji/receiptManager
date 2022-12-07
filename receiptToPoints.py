import math

def num_items_to_points(items):
    points = 0
    numberOfitems = len(items)
    if numberOfitems % 2 == 1:
        pairsOfitems = int((numberOfitems - 1) / 2)
        points += (pairsOfitems * 5)
    else:
        pairsOfitems = int((numberOfitems) / 2)
        points += (pairsOfitems * 5)
    return points

def receiptConverter(receipt):
    points = 0
    businessName = receipt['retailer']
    items = receipt['items']
    date = receipt['purchaseDate'].split("-")
    time = receipt['purchaseTime']
    total = receipt['total'].split(".")

# Handles converting name to point value
    for char in businessName:
        if char.isalnum():
            points += 1

# Handles converting total to point value
    if total[1] == '00':
        points += 50
        points += 25
    elif total[1] == '25':
        points += 25
    elif total[1] == '50':
        points += 25
    elif total[1] == '75':
        points += 25
    else:
        points += 0


# Handles converting Items to point values
    points += num_items_to_points(items)


# Handles converting item description to points
    for item in items:
        itemDescription = item['shortDescription']
        if len(itemDescription) % 3 == 0:
            itemCost = float(item['price'])
            points += math.ceil(itemCost * 00.2)


# Handle converting date to points
    militaryTime = int(time.replace(':',''))
    if militaryTime >= 1400 and militaryTime <= 1600:
        points += 10


# Handle date converting
    day = int(date[2])
    if day % 2 == 1:
        points += 6

# Handles making id
    dateMerge = '-'.join(date)
    businessNameMerge = businessName.replace(' ', '')

    return {'id': 'abc' + str(businessNameMerge).lower() + '--' + str(points) + '--' + str(dateMerge) + 'xyz', 'points': points}
