# ways to print unique chars in a string
nonuString = "AABCAAADA"

method1 = ''.join(set(nonuString))
print method1


def method2function ( nonuString ) :
    charlist = [0] * 256
    uniquechars = []

    #given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object
    for mychar in nonuString:
        if charlist[ord(mychar)] == 0:
            uniquechars.append(mychar)
        charlist[ord(mychar)] += 1
    return ''.join(uniquechars)

method2 = method2function(nonuString)
print method2