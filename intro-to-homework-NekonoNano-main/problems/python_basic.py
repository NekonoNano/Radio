# 本作业共包含 3 道题目，如果你不熟悉 Python 语法，自行查找资料进行学习，也欢迎同学分享自己觉得不错的教程


# 阶乘是一个非常常见的数学问题，它的定义是：n的阶乘等于1*2*3*...*n。例如，5的阶乘是1*2*3*4*5=120
# 请实现一个函数，输入一个整数n，返回n的阶乘
# 例如，输入5，返回120
# 提示：使用 for 循环实现
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result +=i
    return result


# 斐波那契数列是一个非常常见的数列，它的第一个和第二个数字都是1，之后的每个数字都是前两个数字之和。例如，斐波那契数列的前10个数字是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 请实现一个函数，输入一个整数n，返回斐波那契数列的第n个数字
# 例如，输入3，返回2；输入5，返回5
# 提示：使用递归实现
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)


# 计算两条直线的交点
# 一条平面上的直线可以用 ax + by = c 来表示，其中 a, b, c 是常数
# 请实现一个函数，输入分别是[a1, b1, c1] 和 [a2, b2, c2]，返回两条直线的交点[x, y]
# 如果两条直线平行或重合，返回 None
# 例如，输入[1, 1, 1] 和 [2, 2, 2]，返回 None；输入[1, 1, 1] 和 [0, 1, 0]，返回 [1, 0]
def intersection(line1, line2):
    a1,b1,c1 =line1
    a2,b2,c2 =line2
    d = a1*b2-a2*b1
    if d == 0:
        return None
    else:
        x = (c1*b2-c2*b1)/d
        y = (a1*c2-a2*c1)/d
        return [x,y]
        


if __name__ == "__main__":
    print(factorial(5))  # 120
    print(fibonacci(5))  # 5
    print(intersection([1, 1, 1], [2, 2, 2]))  # None
    print(intersection([1, 1, 1], [0, 1, 0]))  # [1.0, 0.0]
