def show(n, v):
    if type(v) == type(999):
        print(f"{n:2} = {v}, type({n}) = {type(v)}, hex({n}) = {hex(v)}, bin({n}) = {bin(v)}")
    elif type(v) == type("string") and v[:2] == "0b":
        print(f"{n:2} = {v}, type({n}) = {type(v)}, int({n},base=2) = {int(v, base=2)}")
    elif type(v) == type("string") and v[:2] == "0x":
        print(f"{n:2} = {v}, type({n}) = {type(v)}, int({n},base=16) = {int(v, base=16)}")
    else:
        print(f"{n:2} = {v}, type({n}) = {type(v)}")


x = 0b1101
show('x', x)

xb = bin(x)
show('xb', xb)

xh = hex(x)
show('xh', xh)

y = x << 3
show('y', y)

yb = bin(y)
show('yb', yb)

a = x & 0b0111
show('a', a)
