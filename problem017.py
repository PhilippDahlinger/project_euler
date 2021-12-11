def unique(x):
    if x == 0:
        # usually not written out
        return 0
    if x == 1:
        return len("one")
    if x == 2:
        return len("two")
    if x == 3:
        return len("three")
    if x == 4:
        return len("four")
    if x == 5:
        return len("five")
    if x == 6:
        return len("six")
    if x == 7:
        return len("seven")
    if x == 8:
        return len("eight")
    if x == 9:
        return len("nine")
    if x == 10:
        return len("ten")
    if x == 11:
        return len("eleven")
    if x == 12:
        return len("twelve")
    if x == 13:
        return len("thirteen")
    if x == 14:
        return len("fourteen")
    if x == 15:
        return len("fifteen")
    if x == 16:
        return len("sixteen")
    if x == 17:
        return len("seventeen")
    if x == 18:
        return len("eighteen")
    if x == 19:
        return len("nineteen")

def tens(x):
    if x < 20:
        return unique(x)
    else:
        prefix = 0
        tens = int(str(x)[0])
        if tens == 2:
            prefix = len("twenty")
        elif tens == 3:
            prefix = len("thirty")
        elif tens == 4:
            prefix = len("forty")
        elif tens == 5:
            prefix = len("fifty")
        elif tens == 6:
            prefix = len("sixty")
        elif tens == 7:
            prefix = len("seventy")
        elif tens == 8:
            prefix = len("eighty")
        elif tens == 9:
            prefix = len("ninety")
        return prefix + unique(int(str(x)[1]))

def huns(x):
    if x < 100:
        return tens(x)
    else:
        huns = int(str(x)[0])
        prefix = unique(huns) + len("hundredand")
        print(x-huns*100)
        return prefix + tens(x - huns*100)

result = 0
for i in range(1,1000,):
    result += huns(i)
print(result+ 3 + len("thousand")-27)

