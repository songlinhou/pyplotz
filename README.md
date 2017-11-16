# pyplotz 中文支持组件

 轻量级 matplotlib 中文支持组件。

A light weight wrapper for matplotlib users with Chinese characters supported.

-------

兼容 matplotlib 以及其依赖库（如: seaborn）

Completely compatible with matplotlib and 3rd-party libraries based on matplotlib (such as seaborn).

-------

无需配置，让中文显示原生兼容。

Without any configuration, you can use Chinese characters in matplotlib like it is natively supported.

-------

支持 matplotlib 混合编程, 完全相同的API设计。[查看示例](https://github.com/201528015329004/pyplotz/blob/master/examples/quick_start.ipynb)

Mixture of matplotlib and pyplotz is supported. Identical API with matplotlib. [Example](https://github.com/201528015329004/pyplotz/blob/master/examples/quick_start.ipynb)

```
from pyplotz.pyplotz import PyplotZ
import matplotlib.pyplot as plt
import numpy as np

pltz = PyplotZ() # create an instance
pltz.plot(np.linspace(-10,10),np.sin(np.linspace(-10,10)),'b', label='sin数据',alpha=0.7)
pltz.plot(np.linspace(-10,10),np.cos(np.linspace(-10,10)),'r', label='cos数据',alpha=0.7)
pltz.title("数据图")
pltz.xlabel("横坐标")
pltz.ylabel("纵坐标")
plt.grid() # you can use matplotlib API and pyplotz interchangeably.
pltz.legend() # use legend function from pltz to show Chinese properly

```


-------

请使用命令行安装：

Pleased install using command:

```pip install pyplotz```

