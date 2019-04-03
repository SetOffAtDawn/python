# 函数调用自己就是递归
def calc(n):
    print(n)
    return calc(n+1)
calc(1)
# 递归的特性：
#    必须有一个明确的结束条件
#    每次进入更深一层递归时，问题规模相比上次递归都应有所减少
#    递归效率不高，递归层次过多导致栈溢出

def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))

calc(10)
