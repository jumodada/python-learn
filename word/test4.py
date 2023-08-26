# coding:utf-8

import pdfkit  # pkhtmltopdf 
from pydocx import PyDocX  # pip install pydocx

html = PyDocX.to_html('简历1.docx')
f = open('html1.html', 'w')
f.write(html)
f.close()

#pdfkit.from_file('html1.html', 'test3.pdf')
pdfkit.from_string(html, 'test4.pdf')
