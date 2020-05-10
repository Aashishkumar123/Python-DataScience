#!/usr/bin/env python
# coding: utf-8

# # **-------------------------Manhatten Stock EXchange Data--------------------------------**
   ->> Importing All the Suitable  Liabraries :
# In[ ]:


import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sci


# In[ ]:


print("**---------------------Manhatten Stock Exchange Company-----------------------**")
rang=np.random.RandomState(42)
index=pd.date_range("20190101",periods=365)
data=pd.DataFrame({"Stock_IN":rang.randint(1,100,(365)),
                   "Stock_OUT":rang.randint(1,100,(365)),
                   "Total_Stock":data["Stock_IN"] + data["Stock_OUT"],
                   "Remainning_Stock":data["Stock_IN"]-data["Stock_OUT"],
                   "ProFit_%":data["Stock_IN"]/data["Stock_OUT"]*data["Total_Stock"]-data["Remainning_Stock"],
                   "Loss_%":data["ProFit_%"]-data["Total_Stock"]},index=index)
data.index.name="Dates"
data.head(20)


# In[ ]:


print("**------------------------------------Total_Stock data is less than 100--------------------------------**")
print(tabulate(data[data["Total_Stock"]<100].head(20),headers="keys",tablefmt="psql"))


# In[ ]:


print("**------------------------------Data of Profit is Less than or equal to 100------------------------------------**")
print(tabulate(data[data["ProFit_%"]<=100].head(20),
               headers="keys",tablefmt="psql"))


# In[ ]:


sns.set()
data.plot(label=data.columns)
plt.legend(ncol=2)
plt.title("Visualizing Of Manhatten Stock Exchange Company")
plt.show()


# In[ ]:


sns.set()
sns.pairplot(data)
plt.show()


# In[ ]:


sns.set()
sns.relplot(x="Stock_IN",y="Stock_OUT",hue="Total_Stock",data=data.query("Stock_OUT<=10"))
plt.show()

Data visualization of Profit_% :
# In[ ]:


pd.DataFrame(data["ProFit_%"]).head(10)


# In[ ]:


sns.set()
plt.grid(True,color='b',ls="--")
data["ProFit_%"].plot()
plt.legend()
plt.xticks(color="b")
plt.yticks(color="b")
plt.xlabel("Dates",color="b")
plt.ylabel("Profit_%",color="b")
plt.title("Profit_% of Manhatten Stock Exchange Data",color="b")
plt.show()

Data Visualization of Loss_% :
# In[ ]:


pd.DataFrame(data["Loss_%"]).head(10)


# In[ ]:


sns.set()
plt.grid(True,color="c",ls="--")
data["Loss_%"].plot(color="c")
plt.legend()
plt.xticks(color="c")
plt.yticks(color="c")
plt.xlabel("Dates",color="c")
plt.ylabel("Loss_%",color="c")
plt.title("Visualization of Loss_% of Manhatten Stock Exchange Data",color="c")
plt.show()

Stock_IN of Manhatten Stock Exchange Data :
# In[ ]:


pd.DataFrame(data["Stock_IN"]).sample(10)


# In[ ]:


plt.style.use("dark_background")
plt.grid(True,ls="--",color="w")
plt.plot(data["Stock_IN"],color="c",label="Stock_IN")
plt.legend()
plt.xlabel("Dates",color="w")
plt.ylabel("Stock_IN",color="w")
plt.xticks(color="w")
plt.yticks(color="w")
plt.title("Visualization of Stock_IN Data")
plt.show()

Stock_OUT of Manhatten Stock Exchange Data :
# In[ ]:


pd.DataFrame(data["Stock_OUT"]).sample(10)


# In[ ]:


plt.style.use("dark_background")
plt.grid(True,ls="--",color="w")
plt.plot(data["Stock_OUT"],color="c",label="Stock_IN")
plt.legend()
plt.xlabel("Dates",color="w")
plt.ylabel("Stock_IN",color="w")
plt.xticks(color="w")
plt.yticks(color="w")
plt.title("Visualization of Stock_OUT Data")
plt.show()

Data of Total_Stock & Remainning_Stock Data of Manhatten Stock Exchange :
# In[ ]:


pd.DataFrame(data["Total_Stock"].head(10))


# In[ ]:


pd.DataFrame(data["Remainning_Stock"].head(10))


# In[ ]:


plt.style.use("seaborn-whitegrid")
plt.grid(False)
data["Total_Stock"].plot(color="y")
data["Remainning_Stock"].plot(color="m")
plt.legend(loc="lower right")
plt.show()







