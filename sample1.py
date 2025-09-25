def isGood(a,b,c,d,e):
    if a <= 3:
        return False
    if b <= 0:
        return False
    if not c in ["dog","cat"]:
        return False
    if d%2 != 0:
        return False
    if not e:
        return False
    return True


# print this statement if:
# a is >3 and b is positive and c is either dog or cat and d is an even number and e is True
# what would this have to look like if you made it a single if statement?  

if isGood(4,1,"dog",2,True):
    print("all the values are good!")