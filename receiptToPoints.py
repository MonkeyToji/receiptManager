import math

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
    numberOfitems = len(items)
    if numberOfitems % 2 == 1:
        pairsOfitems = int((numberOfitems - 1) / 2)
        points += (pairsOfitems * 5)
    else:
        pairsOfitems = int((numberOfitems) / 2)
        points += (pairsOfitems * 5)


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


    return points





##################################################################################################
#example receipt
#
#
#
# receipt = {
#   "retailer": "Target",
#   "purchaseDate": "2022-01-01",
#   "purchaseTime": "13:01",
#   "items": [
#     {
#       "shortDescription": "Mountain Dew 12PK",
#       "price": "6.49"
#     },{
#       "shortDescription": "Emils Cheese Pizza",
#       "price": "12.25"
#     },{
#       "shortDescription": "Knorr Creamy Chicken",
#       "price": "1.26"
#     },{
#       "shortDescription": "Doritos Nacho Cheese",
#       "price": "3.35"
#     },{
#       "shortDescription": "Klarbrunn 12PK 12 FL OZ",
#       "price": "12.00"
#     }
#   ],
#   "total": "35.35"
# }
# #25

# receiptTwo = {
#   "retailer": "M&M Corner Market",
#   "purchaseDate": "2022-03-20",
#   "purchaseTime": "14:33",
#   "items": [
#     {
#       "shortDescription": "Gatorade",
#       "price": "2.25"
#     },{
#       "shortDescription": "Gatorade",
#       "price": "2.25"
#     },{
#       "shortDescription": "Gatorade",
#       "price": "2.25"
#     },{
#       "shortDescription": "Gatorade",
#       "price": "2.25"
#     }
#   ],
#   "total": "9.00"
# }
#109
##################################################################################################
# receiptConverter(receipt)
# receiptConverter(receiptTwo)
