# 标准库

#包（库）：和windows中的文件夹概念一样，包含多级子包，每个包可以有n个模块。

#Python的标准库：是随着python安装的时候默认自带的库

#Python的第三方库：是第三方提供的，需要下载安装
'''
1.import + 包名.模块名
2.import + 包名.模块名 + as + 变量名
3.from + 包名 + import + 模块
'''
import Math.sorting
d = Math.sorting.sort([13,56,35,5723,23])
print(d)

import Math.sorting as math
d = math.sort([13,56,35,5723,23])
print(d)

from Math import sorting
d = sorting.sort([13,56,35,5723,23])
print(d)

import Math.Computer as mc
d = mc.Computers("HUAWEI",2000,"black",14)
print(d)
