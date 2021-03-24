#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pickle
from flask import Flask,render_template,request


# In[16]:


machinemodel=pickle.load(open('mymodelsave.pkl','rb'))


# In[18]:


app=Flask(__name__)
@app.route("/")
def nitin():
    return render_template('pro.html')
@app.route("/detail",methods=['GET','POST'])
def dkjsdjkkjds():
    if(request.method=='POST'):
        exp=float(request.form['a'])
        ans=machinemodel.predict([[exp]])
        return render_template('pro.html',salary=ans)
if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:




