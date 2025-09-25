# 100 review of functions

## Objectives
* to review and remember
  1. when to use functions


Functions are really intended to be small blocks of code.  One very overlooked value of functions is to make small decisions and return True or False values to help make your conditional statements much easier to read.

We can use complex conditional statements using multiple *and* and *or* connectors, but we could also make them available in a function that returns a boolean value.

Consider the sample1.py program.

At other times, we might want to create a function that returns multiple return values!  Maybe you need an x-y coordinate, or even an x-y-z coordinate!

Open up sample2.py and see how it looks!

Assignment 1:
Create a function that takes 2 parameters that are integers.  The function will return both the greatest common factor as well as the lowest common multiple.  You will likely need some other functions to help you accomplish this task.
Some ideas (you don't have to use them):
* a function that takes 1 parameter that is an integer.  The function will return a list of the factors for that number
* a function that takes 2 lists and determines the largest number that is common to both sets

Some sample code is provided.

Assignment 2:
Find the distance between 2 points in 3d space using (x,y,z) cartesian coordinates as well as the coordinates of the midpoint.  This like the 2d x-y grid system, except there is a 3rd value, z which indicates coming out of the page.

To find the distance between 2 coordinates, we can use the distance formula:
d = sqrt( (x1-x2)^2 + (y1-y2)^2 )

To find the midpoint, of 2 coordinates in a 2d space, we find their average values:

(xm,ym) = (x1+x2)/2 , (y1+y2)/2

Write a function to determine the midpoint between 2 coordinates in 3d (x,y,z) space
