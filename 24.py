

# 交换a与b
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

# +:0, -:1, *:2, /:3
# in:two number
# out:a tuple with result and its operator
def f(a,b):
    # 让a>=b
    if(a<b):
        a,b=swap(a,b)
    res=[]
    res.append((a*b,'*'))
    res.append((a+b,'+'))
    res.append((a-b,'-'))
    if(b!=0):
        res.append((a/b,'/'))
        res.append((b/a,'/'))
    else:
        res.append((0,'/'))
    return res

# a:list,element is number
# temp:list,the solution,len=N+1
# N:dimension of initial problem
# n:len (a)
def cal(a,n,temp,N):
    if(n<=2):
        res=f(a[0],a[1])
        for i in res:
            # 例(c,'+') i[0]对应c,i[1]对应'+'
            temp[N+1-n]=(a[0],i[1],a[1],'=',24)
            if(abs(i[0]-24)<=1E-7):
                temp[0]=True
                # 输出求解过程
                print(temp[1:])
                break
        return
    else:
        for i in range(0,n):
            # 若前面得到了结果则退出分支
            # 若注释if，则即使得到结果也会计算其他求解24点的方案
            if(temp[0]==True):
                break
            for j in range(i+1,n):
                res=f(a[i],a[j])
                for k in res:
                    temp[N+1-n]=(a[i],k[1],a[j],k[0])
                    # 下一步要求解的新数组 
                    new_a=[]
                    for m in range(0,n):
                        if(m!=i and m!=j):
                            new_a.append(a[m])
                    new_a.append(k[0])
                    # print (new_a,n,temp [0])
                    # input ()
                    cal(new_a,n-1,temp,N)

# 测试用例
N=4 # 初始问题大小为4个数算24点问题
temp=[False]*(N+1) # temp用来存储当前求解过程，temp [0]用来判断是否已经得到结果，初始为False，temp [1:]用来存储当前求解过程，初始为空

# 例子：输入4个数为3,8,8,9，输出结果为[(9.0, '-', 8.0), ('*', 8.0), ('*', 3.0), '=', 24]
cal([3,8,8,9],N,temp,N)
