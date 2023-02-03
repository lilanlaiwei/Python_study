#!/usr/bin/python3

age = input("年齢は：")
height = input("身長は：")

int_age = int(age)
int_height = int(height)

if (10 <= int_age) and (int_age <= 80):
	if (120 <= int_height) and (int_height <= 190):
		print("お乗りいただけます。")
elif(80 < int_age) or (190 < int_height):
	print("残念ですが…")
else:
        print("またお越しください。")
