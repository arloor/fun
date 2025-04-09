import numpy as np
import matplotlib.pyplot as plt

# 定义 x 范围
x = np.linspace(0.1, 128, 500)  # 避免 sqrt(0) 和 ln(0)

# 定义函数及其导数
functions = {
    r"$\sqrt{x}$": (np.sqrt(x), 0.5 / np.sqrt(x)),
    r"$\ln{x}$": (np.log(x), 1 / x),
    r"$\arctan{x}$": (np.arctan(x), 1 / (1 + x**2)),
    r"$-e^{-x}$": (-np.exp(-x), np.exp(-x)),
}

# 绘图
for name, (y, dy) in functions.items():
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"{name}")
    plt.plot(x, dy, label=f"{name} 的导数", linestyle="--")
    plt.title(f"{name} 及其导数")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
