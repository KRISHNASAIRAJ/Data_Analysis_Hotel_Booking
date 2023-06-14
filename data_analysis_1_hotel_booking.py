#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sb
warnings.filterwarnings('ignore')


# In[3]:


##Importing dataset


# In[4]:


df=pd.read_csv('hotel_booking.csv')


# In[5]:


#Exploring data analysis and cleaning


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[10]:


df.describe(include='object')


# In[11]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print("*"*50)


# In[12]:


df.isnull().sum()


# In[13]:


#df.drop(['company', 'agent'],axis=1,inplace=True)
df.dropna(inplace=True)


# In[14]:


df.isnull().sum()


# In[15]:


df.describe()


# In[16]:


df=df[df['adr']<5400]


# In[17]:


#Data Analysis and Visualization


# In[20]:


cancelled_percentage=df['is_canceled'].value_counts(normalize=True)
print(cancelled_percentage)


# In[26]:


#7% reservations are cancelled
plt.figure(figsize=(5,4))
plt.title("Reservation Status")
plt.bar(['Not Cancelled','Cancelled'],df['is_canceled'].value_counts(),edgecolor="k",width=0.5)
plt.show()


# In[31]:


plt.figure(figsize=(8,4))
ax1=sb.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation in different hotels",size=22)
plt.xlabel("Hotel")
plt.ylabel("Number of reservations")
plt.legend(['not canceled','canceled'])
plt.show()


# In[40]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[41]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[42]:


resort_hotel=resort_hotel.groupby("reservation_status_date")[['adr']].mean()
city_hotel=city_hotel.groupby("reservation_status_date")[['adr']].mean()


# In[45]:


plt.figure(figsize=(20,8))
plt.title("Average Daily Rate Comaprision of two hotels",fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label="Resort Hotel")
plt.plot(city_hotel.index,city_hotel['adr'],label="City Hotel")
plt.legend()
plt.show()


# In[53]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(8,4))
ax1=sb.countplot(x="month",hue='is_canceled',data=df,palette="bright")
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation Status Of Each Month")
plt.xlabel=("Month")
plt.ylabel=("No of Reservations")
plt.legend(['not canceled','canceled'])
plt.show()


# In[56]:


canceled_data=df[df["is_canceled"]==1]
top_2_country=canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title("Top 2 countries with reservation canceled")
plt.pie(top_2_country,autopct="%.2f",labels=top_2_country.index)
plt.show()


# In[61]:


market_segments=df['market_segment'].value_counts(normalize=True)
plt.figure(figsize=(8,8))
plt.title("Market Segment")
plt.pie(market_segments,autopct="%.2f",labels=market_segments.index)
plt.show()


# In[ ]:




