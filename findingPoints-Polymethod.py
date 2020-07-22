import math
import random

square = {
    "southwest": {
        "lng": 0,
        "lat": 0
        },
    "northeast": {
        "lng": 200,
        "lat": 200
        }
    }

print(square)


def gen_points(square, n = 5):
    y1 = square.get("southwest").get("lng")
    x1 = square.get("southwest").get("lat")
    y2 = square.get("northeast").get("lng")
    x2 = square.get("northeast").get("lat")
    
    sideLen = (y2-y1)
    radius = ((sideLen)/2) * .707107 #square root of 2 /2
    
    
    points = {
        
    }

    x0 = x1 + (sideLen/2)
    y0 = y1 + (sideLen/2)
    
    points[0] = { # center point
        "x": x0,
        "y": y0
        }

    numOuterPoints = 1
    theta = 0
    
    while numOuterPoints < n:
        theta = (2 * 3.14)/(n-1) * numOuterPoints 
        x = radius*math.cos(theta) + x0
        y = radius*math.sin(theta) + y0
        print("x: " + str(x))
        print("y: " + str(y))
        points[numOuterPoints] = {
            "x": x,
            "y": y
            }
        numOuterPoints = numOuterPoints + 1

        
    print(points)


gen_points(square)
