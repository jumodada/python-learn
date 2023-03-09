# coding:utf-8

user = {'username': 'dewei', 'age': 33}
xx = {'username': 'pot', 'age': 10, 'top': 175, 'sex': '男'}
user.update(xx)
print(user)

value = user.setdefault('username', 'xiaoyun')
value = user.setdefault('birthday', '2020-1-1')
print(user, value)


# user['top'] = 174
#
# print(user)
# user['username'] = 'pot'
# print(user)
# user['top'] = 175
# user['age'] = 10
# print(user)
