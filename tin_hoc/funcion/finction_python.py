
import math

# # ax+b = c
# def ptb1(a,b,c):
#     if a == 0:
#         if b != c:
#             return False
#         if b == c:
#             return "luon dung"
#     else:
#         return (c-b)/a

# print("ax + b = c\n")
# a = int(input("nhap a = "))
# b = int(input("nhap b = "))
# c = int(input("nhap c = "))

# result = ptb1(a,b,c)

# print("nghiem cua phuog trinh la {}".format(round(result,2)))

# pi = 3.14
# def chuvi_dientich(r):
#     list1=[]
#     chuvi = 2*pi*r
#     dientich = pi * r*r
#     list1.append(chuvi)
#     list1.append(dientich)
#     return list1
# r = int(input("nhap ban kinh"))
# list1 = chuvi_dientich(r)
# print("chu vi cua hinh tron la {}".format(round(list1[0],2)))
# print("dien tich hinh tron la {}".format(round(list1[1],2)))


# # ax^2 + bx +c =0

# def giai_ptrinhbac2(a,b,c):
#     result = []
#     if a == 0:
#         if b == 0 and c != 0:
#             result.append("vo nghiem")
            
#         if b == 0 and c == 0:
#             result.append("vo so nghiem")
#     else:
#         detal = b*b - 4*c*a
#         if(detal < 0):
#             result.append("vo nghiem")
#         if(detal == 0):
#             x_kep = -b/2*a*c
#             result.append(x_kep)
#         if(detal > 0):
#             x_1 = (-b + math.sqrt(detal))/(2*a*c)
#             x_2 = (-b - math.sqrl(detal))/(2*a*c)
#             result.append(x_1)
#             result.append(x_2)
#     return result

# print("ax^2 +bx +c =0")
# a = float(input("nhap a = "))
# b = float(input("nhap b = "))
# c = float(input("nhap c = "))    

# result = giai_ptrinhbac2(a,b,c)
# if result[0] == "vo nghiem":
#     print("phuong trinh vo nghiem")
# elif result[0] == "vo so nghiem":
#     print("phuong trinh luon dung")
# else:
#     print("x1 = {},x2 = {}".format(result[0],result[1]))

so = int(input("nhap so co 2 chu so"))
list_so = ["khong","mot","hai","ba","bon","lam","sau","bay","tam","chin","muoi"]

while (so < 0) or (so > 99):
    print('nhap lai so')
    so = int(input("nhap so co 2 chu so"))

def tach(so):
    list = []
    chuc = so / 10
    donvi = so % 10
    list.append(chuc)
    list.append(donvi)
    return list

def check(so):
    list = tach(so)
    if list[0] == 0:
        print(list_so[list[1]])
    elif list[0] == 1 and list[1] == 0:
        print(list[10])
    elif list[0] != 0 and list[1] == 0:
        print(list_so[list[0]],end = " ")
        print(list_so[10])
    else:
        print(list_so[int(list[0])],end =" ")
        print(list_so[list[1]],end =" ")

check(so)

