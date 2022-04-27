def my_counter1(l):
    for i,e in enumerate(l):
        print(i+1)
def my_counter2(l):
    i = 1
    while i <= len(l):
        print(i)
        i += 1
def my_counter3(l):
    i = 1
    while True:
        if i > len(l):
            break
        print(i)
        i += 1
if __name__ == '__main__':
    l = range(0,10)
    # my_counter1(l)
    # my_counter2(l)
    # my_counter3(l)

