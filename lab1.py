# -*- coding: UTF-8 -*-
#coding=utf-8 #中文显示

import matplotlib.pyplot as plt #导入绘图库简写为plt
import numpy as np #导入数学函数库简写为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#产生0-3π的等差数组
y = np.sin(x) #计算x每个元素的正弦值

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #生成1*2个子图，当前激活第1个子图
plt.title(r'$f(x)=sin(x)$') #设置标题
plt.plot(x, y)#使用默认线条样式和颜色绘制x和y
#plt.show()

x1 = [t*0.375*np.pi for t in x] #函数下x1=x*0.375π
y1 = np.sin(x1)#计算x1每个元素的正弦值
plt.subplot(1,2,2)#生成1*2个子图，当前激活第2个子图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #设置标题
plt.plot(x, y1)#使用默认线条样式和颜色绘制x和y1
plt.show()#显示图像