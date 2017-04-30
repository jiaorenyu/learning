import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

current_palette = sns.color_palette()
#默认颜色
#sns.palplot(current_palette)
# 环形颜色
#sns.palplot(sns.color_palette("hls", 16)) 
#调整深度和饱和度
sns.palplot(sns.hls_palette(8, l=.3, s=.6))
plt.show()
