# coding:utf-8

import pdfkit  # pip install pdfkit
# pdfkit.from_string pdfkit.from_url pdfkit.from_file  --> html

# pdfkit.from_url('https://www.imooc.com', 'test1.pdf')
html = """
<html>
<head>
<meta charset="utf-8" />
</head>
<body>
  <p>你好</p>
</body>
</html>
"""
pdfkit.from_string(html, 'test2.pdf')
