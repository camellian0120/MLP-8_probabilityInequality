# Markov.py
# 参考 : https://collatz.hatenablog.com/entry/2021/04/11/151935
# 　　   https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def
# 　　   https://note.nkmk.me/python-numpy-zeros-ones-full/#numpyfull
import numpy as np
from scipy.stats import norm #normは正規分布
import matplotlib.pyplot as plt

X = np.arange(0, 100, 0.1)

#pdfは確率密度関数
#平均:60, 標準偏差:10
Y = norm.pdf(X, 50, 10)
A = np.full(shape=1000,fill_value=60)

#グラフの表示
plt.axhline(0,  color='k')
plt.axvline(0,  color='k')
plt.axvline(60, color='C1', label="a")
# plt.axhline((50/60),  color='g', label="E[x]/a")
plt.plot(X, Y, label="norm")
plt.fill_between(X, Y, where=(X >= A), alpha=0.3, color='C1')
# plt.fill_between(X, Y, where=(X <= A), alpha=0.3, color='C1')
plt.legend()
plt.savefig("norm.png")
