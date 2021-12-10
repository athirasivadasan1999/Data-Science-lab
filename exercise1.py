#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original numbers")
print(x)
print(y)
print("comparison greater")
print(np.greater(x,y))
print("comparison greater or equal")
print(np.greater_equal(x,y))
print("comparison - less")
print(np.less(x,y))
print("Comparison less-equal")
print(np.less_equal(x,y))


# In[8]:


import numpy as np
array=np.arange(30,71,2)
print("Array of all integer from 30 to 70")
print(array)


# In[9]:


import numpy as np
array_2D=np.identity(3)
print("3*3 matrix:")
print(array_2D)


# In[15]:


x=np.arange(21)
print("original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15")
x[(x>=9)&(x<=15)]*=-1
print(x)


# In[16]:


x=np.diag([1,2,3,4,5])
print(x)


# In[17]:


import numpy as np
x = np.array([[0,1],[2,3]])
print("Original array:")
print(x)
print("Sum of all elements:")
print(np.sum(x))
print("Sum of each column:")
print(np.sum(x, axis=0))
print("Sum of each row:")
print(np.sum(x, axis=1))


# In[18]:


import numpy as np
import os
x = np.arange(12).reshape(4, 3)
print("Original array:")
print(x)
header = 'col1 col2 col3'
np.savetxt('temp.txt', x, fmt="%d", header=header) 
print("After loading, content of the text file:")
result = np.loadtxt('temp.txt')


# In[20]:


import numpy as np
nums1 = np.array([0.5, 1.5, 0.2])
nums2 = np.array([0.4999999999, 1.500000000, 0.2])
np.set_printoptions(precision=15)
print("Original arrays:")
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(nums1 == nums2)
nums1 = np.array([0.5, 1.5, 0.23])
nums2 = np.array([0.4999999999, 1.5000000001, 0.23])
print("\nOriginal arrays:")
np.set_printoptions(precision=15)
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(np.equal(nums1, nums2))


# In[21]:


import numpy as np 
nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last rows of the said array:")
new_nums = nums[::-1]
print(new_nums)


# In[22]:


import numpy as np 
nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])
print("Array1:") 
print(nums1)
print("Array2:") 
print(nums2)
print("\nMultiply said arrays of same size element-by-element:")
print(np.multiply(nums1, nums2))


# In[ ]:




