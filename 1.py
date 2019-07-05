import math


def temperature():
    # 华氏温度转换摄氏温度
    # F = 1.8C + 32
    f = float(input('请输入华氏温度:'))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))


def circle():
    # 输入圆半径计算周长面积
    radius = float(input('输入圆半径:'))
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    print("周长 = %.1f" % perimeter)
    print("面积 = %.1f" % area)


def leap_year():
    # 判断闰年
    year = int(input('年份:'))
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(is_leap)


if __name__ == '__main__':
    # circle()
    # temperature()
    leap_year()
