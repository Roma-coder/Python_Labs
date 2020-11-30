# -*- coding: cp1251 -*-
import cgi

form = cgi.FieldStorage()


num1 = int(form.getfirst('num1'))
num2 = int(form.getfirst('num2'))
num3 = int(form.getfirst('num3'))


e = False

if num1 + num2 > num3:
    if num1 + num3 > num2:
        if num2 + num3 > num1:
            e = True

c = "Правильно" if e else "Неправильно"
print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Варіант 11</title>
        <link rel="stylesheet" href="./../bootstrap.min.css">
    </head>
    <body>""")

print(f'<h1 align="center">Результат:  {c}</h1>')
print('</body></html>')
