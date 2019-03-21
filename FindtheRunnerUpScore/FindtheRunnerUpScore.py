if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split()) #what are the differences betwen a map and a list? 
    #map is a function that returns a list of the result after applying the given functio to each iterable... in this case casting as an int
    arrmax = max(arr)
    runnerup = None
    for x in arr:
        if x < arrmax:
            if (runnerup == None):
                runnerup = x
            elif x > runnerup:
                runnerup = x
    print runnerup
