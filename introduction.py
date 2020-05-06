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
        O(n^3)
        O(n^2)
'''

# 作业：计算前1000个正整数的和
import time
start_time = time.time()
a = 0
for i in range(1,10001):

    a += i
print("前10000个正整数的和%d"%a)
print(a)
end_time = time.time()

print("运行时间:%a"%(end_time-start_time))