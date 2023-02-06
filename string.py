#!/usr/bin/python3

print('Hello World')
print("Hello World")

print("Let's start leaning Python.")
print('Let\'s start leaning Python.')

text = "123"
print(int(text) + 456)  #int()で文字列を数値化

text = "123.4"
print(float(text)) #文字列をfloat型に変換

num = 123
num1 = 123.456
print(str(num))
print(str(num1))

sample_str = 'abc def GHI JKL'
print (sample_str.replace('abc','xyz'))
print (sample_str.swapcase()) #大文字を小文字に、小文字を大文字に
print (sample_str.title()) #単語の先頭だけ大文字に
print (sample_str.lower()) #すべて小文字に
print (sample_str.upper()) #すべて大文字に

x = 1
y = 2
result = '{} + {} = {}'.format(x, y, x+y)
print(result)
