s = {}

def get_s(rest, allowed):
    try:
        return s[rest, allowed]
    except KeyError:
        if rest == 0:
            s[rest, allowed] = 1
            return 1
        result = 0
        for i,coin in enumerate(allowed):
            if coin > rest:
                continue
            new_rest = rest - coin
            new_allowed = allowed[i:]
            result += get_s(new_rest, new_allowed)
        s[rest, allowed] = result
        return result

start_allowed = (200, 100, 50, 20, 10, 5,2,1)
print(get_s(200, start_allowed))
