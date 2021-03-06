# 如果a+b+c = 1000，并且a^2 + b^2 = c^2，求出所有的a,b,c可能的组合
# 第一次算法时间
# import time

# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))


# end_time = time.time()

# print("运行时间为：%f"%(end_time-start_time))

'''
a,b,c:0,500,500
a,b,c:200,375,425
a,b,c:375,200,425
a,b,c:500,0,500
运行时间为：193.888628
'''


# 为了让时间更短，提出第二种算法，双重循环
# import time 
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000-a-b
#         if a**2+b**2 == c**2:
#             print("a,b,c:%d,%d,%d"%(a,b,c)) 


# end_time = time.time()

# print("运行时间为：%f"%(end_time-start_time))

'''
a,b,c:0,500,500
a,b,c:200,375,425
a,b,c:375,200,425
a,b,c:500,0,500
运行时间为：1.816448
'''


# 思考：都可以从哪些角度去优化程序

'''
    1.什么是算法？
        算法是独立存在的一种解决问题的方法和思想
    2.算法的五大特性
        输入：算法具有0个或多个输入；
        输出：算法至少有1个或多个输出；
        有穷性：算法在有限的步骤之后会自动结束而不会无限循环，
        并且每一个步骤都可以在可接受的时间内完成；
        确定性：算法中的每一步都有确定的含义，不会出现二义性；
        可行性：算法的每一步都是可行的（每一步都能够执行有限的次数完成）
    3.算法效率衡量
        实现算法程序的执行的时间可以反应出来算法的效率
        单纯依靠运行时间来比较算法的优劣不一定是客观准确的（程序的运行离不开计算机环境，所以和硬件，操作系统有关）
    4.最终算法用什么衡量？
        时间复杂度
    5.表示法：大o记法
        假设计算机执行算法每个基本操作的时间是固定的一个时间单位，那么有多少个基本操作就代表会发费多少时间单位
        虽然对于不同的机器环境而言，确切的时间单位是不同的，但是对于算法进行多少个基本操作在规模数量级上是相同的
        因此，可以忽略机器环境的影响而客观的反应算法的时间效率
        对于算法的时间效率，用“大o记法”
        O(n^3)   100n^2    10000n^2
        O(n^2)
    6.时间复杂度分类
        最优时间复杂度：算法完成工作最少需要多少基本操作（过于理想化，没什么参考价值）
        最坏时间复杂度：算法完成工作最多需要多少基本操作（提供了一种保证，表明算法在此程度的基本操作中一定能完成工作）
        平均时间复杂度：算法完成工作平均需要多少基本操作（对算法整体一个全面的评价，但是这种衡量方式没有保证，）
        我们关注算法的最坏情况！！！ ———> 最坏时间复杂度
    7.时间复杂度的几条基本计算规则
        基本操作，也就是只有常数项，认为其时间复杂度为o（1）
        顺序结构，时间复杂度按加法进行计算
        循环结构，时间复杂度按乘法进行计算
        分支，取最大值、
        判断一个算法的效率时，只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
        没有特殊情况下，我们分析的都是最坏时间复杂度
    8.练习
        12                                     o(1)
        2n+3                                   o(n)
        3n^2 +2n + 1                           o(n^2)
        5log2n + 20                            o(logn)
        2n + 5nlog2n + 20                      o(nlogn)
        1000000n^2 + 2*n^3 +4                  o(n^3)
        2^n                                    o(2^n)

        0(1) < o(logn) o(n) < o(nlogn) < o(n^2) < o(n^3) < o(2^n) < o(n!) < o(n^n)
    9.练习：求n个正整数的和（高斯算法）
'''

# 作业：计算前1000个正整数的和
# import time


# def sum_of_n(n):
#     start_time = time.time()
#     the_sum = 0
#     for i in range(1,n+1):
#         the_sum = the_sum +1
#     end_time = time.time()
#     return the_sum,end_time-start_time

# print(sum_of_n(1000000))


# def sum_of_n_2(n):
    
#     return (n*(n+1))/2
# start = time.time()
# print(sum_of_n_2(1000000))
# end = time.time()
# print(end-start)

'''
    练习：求出列表中的最小值，
    要求:函数1：o(n^2)  两两比较
    函数2：o(n)         设置一个临时变量，更优化的算法就是把这个临时变量设置成列表中的第一个元素
'''
my_list = [3,4,5,6,8,100,22,12,500,12,2000]
def get_min(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] < my_list[j]:
                return
            return my_list[i]

print(get_min(my_list))

def get_min2():
    pass

