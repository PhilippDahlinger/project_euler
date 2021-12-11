def inc(p):
    pointer = len(p) - 2
    while pointer >= 0:
        if p[pointer+1] < p[pointer]:
            pointer -= 1
        else:
            break
    if pointer == -1:
        return
    #target = p[pointer]
    #print("Pointer: ", pointer)
    rest = p[pointer:]
    #print("Rest: ", rest)
    target = min([x  for x in rest if x > p[pointer]])
    #print("target: ", target)
    rest.remove(target)
    rest.sort()
    p[pointer] = target
    for i, v in enumerate(rest):
        p[pointer+1+i] = v


p = [0,1,2,3,4,5,6,7,8,9]
print(p)
for i in range(999999):
    inc(p)
    
result = ""
for x in p:
    result += str(x)
print(result)