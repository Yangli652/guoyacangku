# #l=["果芽","腾讯","老干妈","百度","阿里","唧唧哇哇","香蕉娱乐"]
# #if{"果芽"in l}:
# #print("合作方")
# #else:
# #print("非合作方")
# s=25
# if s<0:
#   print("请输入正确成绩")
# if s>0 and s<60:
#   print("不及格")
# if s>=60 and s<=70:
#   print("及格")
# if s>=71 and s<=80:
#   print("良好")
# if s>=81 and s<=100:
#   print("优秀")
# if s>100:
#   print("请输入正确成绩")
#
# s=90
# if(s>0 and s<60):
#     print("不及格")
# elif(s>=60 and s<=70):
#     print("及格")
# elif(s>=71 and s<=80):
#     print("良好")
# elif(s>=81 and s<=100):
#     print("优秀")
# else:
#     print("请输入正确的成绩")
#
# score_1=[9,10,11,21,31,41,51,59,60,61,69,71,79,81,99,91,100,99,]
# for s  in score_1:
#     if (s > 0 and s < 60):
#         print("不及格")
#     elif (s >= 60 and s <= 70):
#         print("及格")
#     elif (s >= 71 and s <= 80):
#         print("良好")
#     elif (s >= 81 and s <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
#
#     s=0
#     for i in range (100)
#         s=s+i
#     print(s)
# s=1
# for i in range(10,0,-1)
# s*=i
#      print(s)
# flag=True
# a=66
# while flag:
#     b=int(input("请输入数字"))
#     if b>a:
#         print("大了")
#     elif b<a:
#         print("小了")
#     else:
#         print("猜对了")
# #         flag=False
# for i in range (1,100):
#      if(i % 3 != 0):
#          continue
#      print(i)
#
 #定义一个取商和余数的方法
# def shangyushu(a,b):
#     print(a // b)
#     print(a % b)
# shangyushu(10,3)
# def shang_yu(a,b):
#     if(b== 0):
#         print("除数不能为0")
#     else:
#         print("商:",a // b ,",余数:",a % b)
# shang_yu(10,2)
# shang_yu(20,3)
# shang_yu(20,0)

# def sm(a,b=2):
#     return a+b
# print(sm(2,3))

# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#          self.res =self.a +self.b
#     def div(self):
#          self.res =self.a /self.b
#     def jian(self):
#         self.res = self.a - self.b
#     def get_result(self):
#          print(self.res)
# c= calc()
# c.input (10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
# c.jian()
# c.get_result()
#
# class calc():
#     res=None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#          self.res =self.a +self.b
#     def div(self):
#          self.res =self.a /self.b
#     def jian(self):
#         self.res = self.a - self.b
#     def get_result(self):
#          print(self.res)
# c= calc(29,30)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
# c.jian()
# c.get_result()

# for i in range(1,10):
#     # print("i每次遍历的值为:",i)
#     for j in range(1,i+1):
#         # print("j每次遍历的值为:",j)
#         print(j,"*",i,"=",i*j,end="\t") # \t 空格
#     print(end="\n")  # \n换行

for A in range (1,10):
    for B in range (1,A+1):
         print(B,"X",A,"=",A*B,end="\t")
    print()

#   l=[2,34,5,6,789,125,454,65,3,20]
#   length=len(l)
#    for i in range(length-1,0,-1):
#     for j in range (i):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
