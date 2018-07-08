
# coding: utf-8

# In[1]:


word=input("Input a reverse word:")
for char in range(len(word) -1,-1,-1):
  print(word[char], end="")
print("\n")

