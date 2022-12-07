from receiptToPoints import receiptConverter

receipt = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "Klarbrunn 12PK 12 FL OZ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
receiptTwo = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}


def test_receiptChecks():
    assert receiptConverter(receipt) == {'id': 'abctarget--25--2022-01-01xyz', 'points': 25}

def test_receiptChecksTwo():
    assert receiptConverter(receiptTwo) == {'id': 'abcm&mcornermarket--109--2022-03-20xyz', 'points': 109}
