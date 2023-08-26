# coding:utf-8

import xlrd

excel = xlrd.open_workbook('study.xlsx')

book = excel.sheet_by_name('学生手册')
print(book)

book = excel.sheet_by_index(0)
print(book.name)

for i in excel.sheets():
    print(i.name)

print(book.nrows)
print(book.ncols)

for i in book.get_rows():
    content = []
    for j in i:
        content.append(j.value)
    print(content)


