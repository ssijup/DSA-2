def hhash(key) :
    balue = 0
    length = 3
    for i in key :
        balue = (balue + ord(i)) %  length
    return balue

siju = "sijusssscdacddaczdcsdcwfgbfg"
print(hhash(siju))