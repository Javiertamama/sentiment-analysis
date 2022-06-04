#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob

from flask import Flask

from flask import render_template, request 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # Use "@" as a decorator - Put the route into the function
def index():
    if request.method == "POST": # If method is "POST", it will send the text file from the frontend to the backend
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r)) # Use render_template to return the html page
    else:
        return(render_template("index.html", result="2"))

if __name__=="__main__":
    app.run() # Flask default port is 5000


# In[ ]:





# In[ ]:




