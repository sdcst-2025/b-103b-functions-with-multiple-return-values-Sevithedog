import math

"""
Find the distance between 2 points in 3d space using (x,y,z) cartesian coordinates as well as the coordinates of the midpoint.  This like the 2d x-y grid system, except there is a 3rd value, z which indicates coming out of the page.

To find the distance between 2 coordinates, we can use the distance formula:
d = sqrt( (x1-x2)^2 + (y1-y2)^2 )

To find the midpoint, of 2 coordinates in a 2d space, we find their average values:

(xm,ym) = (x1+x2)/2 , (y1+y2)/2

Write a function to determine the midpoint between 2 coordinates in 3d (x,y,z) space
"""

def midpoint(c1,c2):
    #c1 and c2 are tuples or lists in the format (x,y,z)
    #find the midpoint between the 2 coordinates
    x = -1
    y = -1
    z = -1
    return x,y,z

def distance (c1,c2):
    #c1 and c2 are lists or typles in the format (x,y,z)
    #find the distance between these 2 points
    d = 0
    return d


assert midpoint([3,4,5],[10,20,30]) == (6.5,12.0,17.5)
assert round( distance([3,4,5],[10,20,30]) , 3) == 30.496
a = (5,3,98)
b = (-43,101,12.3)
assert midpoint(a,b) == (-19,52,55.15)
assert round( distance(a,b) , 2) == 138.75