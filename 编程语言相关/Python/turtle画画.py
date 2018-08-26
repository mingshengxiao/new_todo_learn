# -*- coding: utf-8 -*-

import turtle

def draw_square():
	# 添加一个窗口屏幕，画布
	window = turtle.Screen()
	# 设定画布的颜色为红色
	window.bgcolor('red')
	# 初始化对象
	brad = turtle.Turtle()

	# 改变形状
	brad.shape('turtle')
	# 改变颜色
	brad.color('yellow')
	# 改变速度
	brad.speed(2)

	temp = 10

	while temp <= 360:
		for i in range(1, 5):
			# 设定想要前进的距离
			brad.forward(100)
			# 向右方转90度
			brad.right(90)
		temp += 10
		brad.right(10)
	window.exitonclick()

draw_square()