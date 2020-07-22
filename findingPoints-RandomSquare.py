import math
import random

square = {
    "southwest": {
        "lng": 100,
        "lat": 200
        },
    "northeast": {
        "lng": 200,
        "lat": 300
        }
    }

print(square)


def gen_points(square, n = 4):
    y1 = square.get("southwest").get("lng")
    x1 = square.get("southwest").get("lat")
    y2 = square.get("northeast").get("lng")
    x2 = square.get("northeast").get("lat")
    nwX = x1
    nwY = y2
    
    sideLen = (y2-y1)
    area = sideLen ** 2

    x0 = x1
    y0 = y2
    print("x0: " + str(x0) + "   y0: " + str(y0))
    
    subSquares = {
        
    }

    numRows = math.ceil(math.sqrt(n))
    print("numRows: " + str(numRows))
    numSubSquares = (numRows ** 2)
    chosenSquares = random.sample(range(numSubSquares), n)
    for b in chosenSquares:
        row = math.floor(b/numRows)
        if(b >= numRows):
            col = b % numRows
        else:
            col = b
        subSquares[b] = {
            "row": row,
            "col": col
                         }
    
    for subSquare in subSquares.items():
        row = subSquare[1]['row']
        col = subSquare[1]['col']
        print(subSquare);
        print("row: " + str(row))
        print("col: " + str(col))
        rowOffset = sideLen/numRows * row
        colOffset = sideLen/numRows * col
        subSquares[subSquare[0]]["x1"] = x1 + colOffset
        subSquares[subSquare[0]]["y1"] = y1 + rowOffset
        subSquares[subSquare[0]]["x"] = x1 + colOffset + (sideLen/numRows)/2
        subSquares[subSquare[0]]["y"] = y1 + rowOffset + (sideLen/numRows)/2

    print(subSquares)


gen_points(square)
