# coding:utf-8

students = {'dewei': '到', 'xx': '在', 'xiaoyun': '在呢', 'xiaogao': '在'}

# print('xiaogao 在吗')
# xiaogao = students.popitem()
# print('{} 喊 {}'.format(xiaogao[0], xiaogao[1]))
# print('xiaoyun 在吗')
# xiaoyun = students.popitem()
# print('{} 喊 {}'.format(xiaoyun[0], xiaoyun[1]))
# print('xx 在吗')
# xx = students.popitem()
# print('{} 喊 {}'.format(xx[0], xx[1]))
# print('dewei在吗')
# dewei = students.popitem()
# print('{} 喊 {}'.format(dewei[0], dewei[1]))
# print(students)
# students.popitem()

print(students.items())

for key, val in students.items() :
    print(key, val)