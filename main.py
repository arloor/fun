# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义 x 范围
x = np.linspace(0.1, 128, 128)  # 避免 sqrt(0) 和 ln(0)

# 定义要标注的特殊x值
special_x = np.array([32, 64, 96, 128])

# 定义函数及其导数
functions = {
    # 函数 f(x) = x^a 的导数是 f'(x) = a * x^(a-1)
    r"${x}^{0.8}$": (np.power(x,0.8), 0.8 * np.power(x, -0.2)),
    r"${x}^{0.75}$": (np.power(x,0.75), 0.75 * np.power(x, -0.25)),
    r"${x}^{0.7}$": (np.power(x,0.7), 0.7 * np.power(x, -0.3)),
    r"${x}^{0.6}$": (np.power(x,0.6), 0.6 * np.power(x, -0.4)),
    r"${x}^{0.5}$": (np.power(x,0.5), 0.5 * np.power(x, -0.5)),
    r"$\ln{x}$": (np.log(x), 1 / x),
    r"$\arctan{x}$": (np.arctan(x), 1 / (1 + x**2)),
    r"$-e^{-x}$": (-np.exp(-x), np.exp(-x)),
}

# 创建两个子图
plt.figure(figsize=(12, 5))

# 第一个子图：所有函数
plt.subplot(1, 2, 1)
for name, (y, _) in functions.items():
    line, = plt.plot(x, y, label=name)
    # 在特殊点添加标注
    for x_val in special_x:
        idx = np.abs(x - x_val).argmin()
        y_val = y[idx]
        plt.plot(x_val, y_val, 'o', color=line.get_color())
        plt.annotate(f'({x_val:.0f}, {y_val:.2f})',
                    (x_val, y_val),
                    xytext=(5, 5),
                    textcoords='offset points')

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
