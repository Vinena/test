'''
郑映慧 1619100019   2019/03/30
function:
    用户输入两个日期，用','分隔，（默认 日期2 >= 日期1），程序计算两日期之间的间隔并输出。
    若 日期1 >= 日期2 ， 则输出的两日期的间隔为负数。
'''

## 日期输入
date_one = input("请输入第一个日期（例：2019,03,29）:")
date_two = input("请输入第二个日期（例：2019,03,29）:")

## 数据读取
dlist_one=date_one.split(',')
dlist_two=date_two.split(',')
for i in range (3):
    dlist_one[i]=int(dlist_one[i])
    dlist_two[i]=int(dlist_two[i])

## 差值计算
def delta(j):
    return dlist_two[j]-dlist_one[j]
year_delta=delta(0)
month_delta=delta(1)
day_delta=delta(2)

# 判断因闰年而多了多少天
def RunNian(year_down,year_up):
    sum=0
    if year_down > year_up:
        year_down,year_up=year_up,year_down
        year_range = -1
    for nyear in range (year_down,year_up):
        if nyear%100 == 0:
            if nyear%400==0:
                sum+=1
        elif nyear%4 ==0:
            sum+=1
    if year_range == -1:
        return -sum
    else:
        return sum

# 判断因大月或二月而多了多少天
def DaYue (month_down,month_up):
    sum=0
    BigMonth=[1,3,5,7,8,10,12]
    for nmonth in range (month_down,month_up):
        if nmonth in BigMonth:
            sum+=1
        elif nmonth == 2:
            sum-=2 
    return sum

sum_delta = year_delta*365 + month_delta*30 + day_delta + RunNian(dlist_one[0],dlist_two[0]) +DaYue(dlist_one[1],dlist_two[1])

print(dlist_one[0],'年',dlist_one[1],'月',dlist_one[2],'日','与',end='')
print(dlist_two[0],'年',dlist_two[1],'月',dlist_two[2],'日','之间相隔：',end='')
print(sum_delta,'天')