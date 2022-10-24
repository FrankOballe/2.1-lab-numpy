#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[4]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))


# In[5]:


#4. Print a.
print(a)


# In[21]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))


# In[22]:


print (b)
type(b)


# In[23]:


#7. Do a and b have the same size? How do you prove that in Python code?

a.size == b.size


# In[9]:


#8. Are you able to add a and b? Why or why not?


# No because they do notr have the same form


# In[24]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
# 5*2*3
c = b.transpose(1,2,0)

print (c)


# In[25]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add (a, c)


# In[26]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a, d)

# The difference is that the eequivalent values of each array have been added


# In[27]:


#12. Multiply a and c. Assign the result to e.

e = a*c

print(e)


# In[28]:


#13. Does e equal to a? Why or why not?

e == a


# In[29]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()


# In[30]:


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

print(f)


# In[18]:


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


# In[35]:


for a in range (d.shape[0]):
    for b in range (d.shape[1]):
        for c in range (d.shape[2]):
            if d[a,b,c] > d_min and d[a,b,c] < d_mean:
                f[a,b,c] = 25
            elif d[a,b,c] > d_mean < d_max:
                f[a,b,c] = 75
            elif d[a,b,c] == d_mean:
                f[a,b,c] = 50
            elif d[a,b,c] == d_min:
                f[a,b,c] = 0
            elif d[a,b,c] == d_max:
                f[a,b,c] = 100
print(f)


# In[36]:


#18. Bonus question
f = f.astype(str)

for a in range (d.shape[0]):
    for b in range (d.shape[1]):
        for c in range (d.shape[2]):
            if d[a,b,c] > d_min and d[a,b,c] < d_mean:
                f[a,b,c] = "A"
            elif d[a,b,c] > d_mean < d_max:
                f[a,b,c] = "B"
            elif d[a,b,c] == d_mean:
                f[a,b,c] = "C"
            elif d[a,b,c] == d_min:
                f[a,b,c] = "D"
            elif d[a,b,c] == d_max:
                f[a,b,c] = "E"


# In[37]:


print(f)


# In[ ]:




