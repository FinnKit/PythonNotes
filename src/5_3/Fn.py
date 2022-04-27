def my_fn(n):
    l = []
    for i in range(0, n):
        if i == 0:
            l.append(0)
        elif i == 1:
            l.append(1)
        else:
            l.append(l[i-1] + l[i-2])
    return l

if __name__ == '__main__':
    l = my_fn(10)
    print(l)