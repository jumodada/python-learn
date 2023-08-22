# 魔法读心术
A = [1, 9, 17, 25, 33, 41, 49, 57,
     3, 11, 19, 27, 35, 43, 51, 59,
     5, 13, 21, 29, 37, 45, 53, 61,
     7, 15, 23, 31, 39, 47, 55, 63]
B = [2, 10, 18, 26, 34, 42, 50, 58,
     3, 11, 19, 27, 35, 43, 51, 59,
     6, 14, 22, 30, 38, 46, 54, 62,
     7, 15, 23, 31, 39, 47, 55, 63]
C = [4, 12, 20, 28, 36, 44, 52, 60,
     5, 13, 21, 29, 37, 45, 53, 61,
     6, 14, 22, 30, 38, 46, 54, 62,
     7, 15, 23, 31, 39, 47, 55, 63]
D = [8, 12, 24, 28, 40, 44, 56, 60,
     9, 13, 25, 29, 41, 45, 57, 61,
     10, 14, 26, 30, 42, 46, 58, 62,
     11, 15, 27, 31, 43, 47, 59, 63]
E = [16, 20, 24, 28, 48, 52, 56, 60,
     17, 21, 25, 29, 49, 53, 57, 61,
     18, 22, 26, 30, 50, 54, 58, 62,
     19, 23, 27, 31, 51, 55, 59, 63]
F = [32, 36, 40, 44, 48, 52, 56, 60,
     33, 37, 41, 45, 49, 53, 57, 61,
     34, 38, 42, 46, 50, 54, 58, 62,
     35, 39, 43, 47, 51, 55, 59, 63]

# 返回时cards是一个字符串
cards = input("请告诉我你想的数字都位于哪些卡片上，多张卡片使用\",\"进行分隔哦，不要撒谎哦!!>>")
# split是分割字符串的一个操作方法, # 它的返回值就是一个list
# 记录用户输入的卡片
cards_number_list = []

card_list = cards.split(",")
for card in card_list:
    # upper()可以将所有字母变成大写字母
    # lower()可以将所有的字母变成小写字母
    upper_char = card.upper()
    if upper_char == "A":
        cards_number_list.append(A[0])
    elif upper_char == "B":
        cards_number_list.append(B[0])
    elif upper_char == "C":
        cards_number_list.append(C[0])
    elif upper_char == "D":
        cards_number_list.append(D[0])
    elif upper_char == "E":
        cards_number_list.append(E[0])
    elif upper_char == "F":
        cards_number_list.append(F[0])
    
# 计算所有数字的和
your_number = 0
for number in cards_number_list:
    your_number += number
print("你想的数字是{}".format(your_number))

