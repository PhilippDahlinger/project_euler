import pickle

def permutations(symbols):
    if len(symbols) == 1:
        return [symbols]
    smaller = permutations(symbols[0:-1])
    s = symbols[-1]
    result = []
    for perm in smaller:
        for place in range(len(perm) + 1):
            new = perm.copy()
            new.insert(place, s)
            result.append(new)
    return result

if __name__ == "__main__":
    perms = permutations([0,1,2,3,4,5,6,7,8,9])
    pickle.dump(perms, open("perms.p", "wb"))
