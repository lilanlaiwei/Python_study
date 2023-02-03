#!/usr/bin/python3

import math #mathモジュールを使用
print(math.sqrt(2.0))


import calendar
calendar.prmonth(2023,2) #2023年2月のカレンダーを表示


s = '''\n組み込み関数
\tモジュールをインポートせずに使える使用頻度の高い関数'''
print(s)


print(abs(-123)) #絶対値　-123は引数

minus_value = 100 * -1
print(abs(minus_value))


print(round(1.12, 1)) #round(数値, 有効桁数)
print(round(1.36, 1)) #四捨五入


print(min(10, 20, 5, 30)) #最小値を戻り値として返す。
print(max(10, 20, 5, 30)) #最大値を戻り値として返す。


height = 176
print("推しの身長は"+ str(height) +"cmです。") #数値を文字列に変換


name = input('input your name: ') #入力されたものを受け取り、変数に代入
message  = 'Hello ' + name + ' !'
print(message)


s = '''
 関数定義
 '''
print(s)


def helloworld():
    name = input('input your name: ')
    message = 'Hello' + name + '!'
    print(message)

helloworld()
