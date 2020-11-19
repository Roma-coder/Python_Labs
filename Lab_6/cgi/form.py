import cgi

form = cgi.FieldStorage()
num1 = int(form.getfirst('num1'))
num2 = int(form.getfirst('num2'))
num3 = int(form.getfirst('num3'))

e = false
result = max(num1, num2)/min(num1, num2)

if num1 + num2 > num3:
    if num1 + num3 > num2:
        if num2 + num3 > num1:
            e = 1

if e == 1:
    print('Content-type: text/html\n')
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Варіант 8</title>
            <link rel="stylesheet" href="./../bootstrap.min.css">
        </head>
        <body>""")

    print(f'<h1 align="center">Результат:  {e}</h1>')
    print('</body></html>')
