import numpy as np

def build_spiral(size):
    s = np.zeros((size, size))
    last_dir = 3
    pos = (size-1)//2, (size-1)//2
    s[pos] = 1
    for n in range(2,size*size+1):
        new_dir = last_dir
        if last_dir == 3:
            # last up
            if s[pos[0], pos[1] + 1] == 0:
                # rotate
                new_dir = (last_dir + 1)%4
        elif last_dir == 0:
            #last right
            if s[pos[0]+1, pos[1]] == 0:
                new_dir = (last_dir + 1)%4
        elif last_dir == 1:
            # last down
            if s[pos[0], pos[1] -1] == 0:
                new_dir = (last_dir + 1)%4
        elif last_dir == 2:
            # last left
            if s[pos[0] -1, pos[1]] == 0:
                new_dir = (last_dir + 1)%4
        if new_dir == 0:
            # go right
            pos = (pos[0], pos[1] + 1)
        elif new_dir == 1:
            # go down
            pos = (pos[0] +1, pos[1])
        elif new_dir == 2:
            pos = (pos[0], pos[1] - 1)
        else:
            pos = (pos[0] -1, pos[1])
        s[pos] = n
        last_dir = new_dir
    return s

s = build_spiral(1001)
sumi = 0
for i in range(s.shape[0]):
    sumi += s[i,i]
    sumi += s[i, s.shape[0] -i-1]

sumi -= 1
print(sumi)
        

