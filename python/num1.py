import numpy as np

a=np.zeros(3)
a=np.ones([5,3])
#a=np.empty() bekar
a=np.linspace(2,11,5)
#a=np
list=[7,"s",88,-1]
a=np.array([list])
a.shape

np.random.seed(0)
a=np.random.rand(4)
a=np.random.randint(10,size=6)
a=a[0:2]




print (a)

