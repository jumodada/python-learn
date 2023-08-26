# coding:utf-8

import xlsxwriter  # pip install xlsxwriter
import xlrd

# excel = xlsxwriter.Workbook('write.xlsx')
# book = excel.add_worksheet('study')
#
# title = ['姓名', '性别', '年龄', '成绩', '等级']
#
# for index, data in enumerate(title):
#     book.write(0, index, data)
# excel.close()

def read():
    result = []
    excel = xlrd.open_workbook('study.xlsx')
    book = excel.sheet_by_name('学生手册')
    for i in book.get_rows():
        content = []
        for j in i:
            content.append(j.value)
        result.append(content)
    return result


def write(content):
    excel = xlsxwriter.Workbook('write.xlsx')
    book = excel.add_worksheet('study')

    for index, data in enumerate(content):
        print(data)
        for sub_index, sub_data in enumerate(data):
            book.write(index, sub_index, sub_data)

    book1 = excel.add_worksheet('学生等级')
    data = [
        ['优秀', '良好', '中', '差'],
        [1100, 2000, 1000, 900]
    ]

    book1.write_column('A1', data[0])
    book1.write_column('B1', data[1])

    chart = excel.add_chart({'type': 'column'})
    chart.add_series({
        'categories': '=学生等级!$A1:$A4',
        'values': '=学生等级!$B1:$B4',
        'name': '成绩占比'
    })
    chart.set_title({'name': '成绩占比图表'})
    book1.insert_chart('A10', chart)

    excel.close()


if __name__ == '__main__':
    result = read()
    write(result)

