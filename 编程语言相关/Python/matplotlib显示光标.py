# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor

# 设置图像风格
plt.style.use('fivethirtyeight')
# 生成数据
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

# 绘制图像
plt.plot(t, s)
plt.axis([0, 1, 1.1 * np.min(s), 2 * np.max(s)])
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')

# 获取当前axes对象
ax = plt.gca()
# 创建光标对象
cursor = Cursor(ax, useblit=True, color='r', linewidth=2)
plt.tight_layout()
plt.show()