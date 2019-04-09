def merge_the_tools(string, k):
    # your code goes here
    print string


if __name__ == '__main__':
    #k is a factor of n
    # string s of length n
    #split s into n/k subsegmens where ti consists of k characters in s
    #then use ti to create string ui such that
    #ui character in ui occurs only once
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    