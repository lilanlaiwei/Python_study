#!/usr/bin/python3

for num in range(5): #range:変数に｛(0～引数のstopの値)-1｝の範囲の整数を渡す。ここでstop=5
	print(num)


message = "Hello Python"
str_count = len(message) #len:文字数を求める関数、str_countには文字数(12)が代入される。

for index in range(str_count): #ループ変数indexには0～11が渡される。
	print(message[index])


names = ['加藤', '遠藤', '工藤', '工藤新一']
target = '工藤'

for name in names:
	if target in name:
		print(f'発見:{name}')
		break
else:
	print('見つかりませんでした')


for name in names:
	if target in name:
		print(f'発見:{name}')
		continue
	print('繰り返し処理を継続します')


even = [0, 2, 4, 6, 8, 10]
sum = 0

for n in even:
	print(n)

for n in even:
	sum += n
print(sum)


