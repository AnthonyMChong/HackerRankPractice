def splitN ( source , n ):
    retList = []
    segCout = len(source) / n
    sourcelist = list(source)
    for segin in range (0 , n):
        seg = []
        for x in range(0,segCout):
            if x + (segin*n) < len(source):
                seg.append(sourcelist[x + (segin*n)])
        retList.append(''.join(seg))
    return retList

if __name__ == '__main__':
    nonuString = "AABCAAADA"
    print splitN (nonuString , 3)