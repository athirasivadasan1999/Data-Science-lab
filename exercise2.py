#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
print(".......MATRIX 1.....")
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
R2 = int(input("Enter the number of rows:"))
C2 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
if(R1==C2):
    
    c=np.dot(matrix1,matrix2)  
    print("Dot product\n",c) 
else:
    print("dimensions are not equal")


# In[6]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
c=np.transpose(matrix1)
print("Transpose\n",c)


# In[8]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
c=np.trace(matrix1)
print("Trace\n",c)


# In[10]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
c=np.linalg.matrix_rank(matrix1)
print("Rank\n",c)


# In[16]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
if(R1==C1):
    c=np.linalg.det(matrix1)
    print("Determinant\n",c)
else:
    print("Determinant not found")


# In[ ]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
if(R1==C1):
    c=np.linalg.inv(matrix1)
    print("Inverse\n",c)
else:
    print("Inverse not found")


# In[20]:


import numpy as np
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R1, C1)
print(matrix1)
if(R1==C1):
    w, v = np.linalg.eig(matrix1)
    print("eigen value\n",w)
    print("eigen vector\n",v)
else:
    print("Inverse not found")


# In[ ]:




