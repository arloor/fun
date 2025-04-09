# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义 x 范围
x = np.linspace(0.1, 128, 500)  # 避免 sqrt(0) 和 ln(0)

# 定义函数及其导数
functions = {
    r"$\sqrt{x}$": (np.sqrt(x), 0.5 / np.sqrt(x)),
    r"$\ln{x}$": (np.log(x), 1 / x),
    r"$\arctan{x}$": (np.arctan(x), 1 / (1 + x**2)),
    r"$-e^{-x}$": (-np.exp(-x), np.exp(-x)),
}

# 创建两个子图
plt.figure(figsize=(12, 5))

# 第一个子图：所有函数
plt.subplot(1, 2, 1)
for name, (y, _) in functions.items():
    plt.plot(x, y, label=name)
plt.title("所有函数")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# 第二个子图：所有导数
plt.subplot(1, 2, 2)
for name, (_, dy) in functions.items():
    plt.plot(x, dy, label=f"{name} 的导数")
plt.title("所有函数的导数")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
