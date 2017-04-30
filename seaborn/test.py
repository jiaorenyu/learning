import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(sum(map(ord, "aesthetics")))

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


#sinplot()

sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data);

sns.set_style("ticks")
sinplot()
sns.despine()



with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()

plt.subplot(212)
sinplot(-1)
print(sns.axes_style())
plt.show()
