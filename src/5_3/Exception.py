class ParamsError(Exception):
    pass
def add(arg1, arg2):
    try:
        # return int(arg1) + int(arg2)
        return arg1 + arg2
    except ValueError:
        raise ParamsError("传入的参数错误")
    except TypeError:
        raise ParamsError("数据类型错误")
    finally:
        print("function add end")
if __name__ == '__main__':
    #print(add(1, 'a1'))
    print(add(1, '2'))