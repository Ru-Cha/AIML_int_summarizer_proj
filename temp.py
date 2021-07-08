from flask import Flask, render_template, request
import numpy as np
import re
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize',methods=['POST'])
def summarize():
    return render_template('summarize.html')

@app.route('/results', methods=['POST'])
def results():
    lines = request.form["lines"]
    text = request.form["text"]
    url_ip = request.form["url"]
    
    if(url_ip):
        

        url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-url"
        
        payload = "url=" +url_ip+"&sentnum="+lines
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "b03ee82bbcmsh3579e3fca7285e5p1ce1a4jsnc7bb6182f40c",
            'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
            }
        
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response)
        
        op = json.loads(response.text)
        op_txt = op["sentences"]
        output = ""
        for i in op_txt:
            output = output + i
            
            
    elif(text):
        
        url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-text"
        
        payload = "text=" +text+ "&sentnum=" + lines
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "b03ee82bbcmsh3579e3fca7285e5p1ce1a4jsnc7bb6182f40c",
            'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
            }
        
        response = requests.request("POST", url, data=payload, headers=headers)
        op = json.loads(response.text)
        op_txt = op["sentences"]
        output = ""
        for i in op_txt:
            output = output + i
    
    return render_template('results.html',output=output)

if __name__ == "__main__":
    app.run()
    
    

output = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vel accumsan dolor. Cras at euismod velit. Nam vel luctus ante. Donec sagittis facilisis elit, non ultrices ex tempor sit amet. Morbi sollicitudin turpis in libero varius, eu ultricies felis lobortis. Vestibulum orci leo, aliquam varius ullamcorper a, fringilla non nunc. Donec non augue ut lacus ornare tincidunt. Pellentesque eu nisl ac tortor mattis auctor cursus non leo. Duis at pharetra ante. Phasellus eleifend ex non leo eleifend, a consequat libero porta. Pellentesque non libero neque. Quisque nec faucibus ligula. Aenean ornare tortor id eros interdum, ut semper nulla euismod. Pellentesque lobortis odio et ullamcorper efficitur. Aliquam ultrices tincidunt porta. Nunc interdum magna eget nibh consectetur euismod. Etiam eleifend volutpat metus sit amet eleifend. Aliquam elit nisi, lacinia id arcu sit amet, sodales laoreet risus. Etiam a malesuada libero. Nunc commodo elit vel lacinia ultricies. Nunc at turpis eu ipsum hendrerit pretium. Curabitur ex purus, efficitur nec leo ac, ultrices volutpat ex. Fusce eget viverra tellus. Integer hendrerit nulla eget tincidunt placerat. Aenean eu viverra mi. Donec ut sapien et sapien sodales tincidunt et eget augue. Morbi congue turpis sed elit porta molestie. Mauris semper consequat ligula, eget consectetur risus scelerisque vel. Aliquam condimentum tortor id tellus iaculis rutrum eget ac purus. Quisque faucibus lobortis erat, sollicitudin consectetur metus auctor quis. Nam accumsan ipsum eu rutrum vulputate. Phasellus mattis non metus vitae varius. Praesent augue orci, pharetra eu blandit vel, ullamcorper sed augue. Ut quis elit id eros fermentum facilisis ut quis mauris. Vivamus ullamcorper magna sit amet facilisis convallis. Curabitur at facilisis quam. Aliquam ac orci consectetur erat lacinia placerat. Praesent vitae consequat velit, et lobortis ante. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur sed volutpat nibh. Curabitur ipsum eros, auctor eu pharetra sed, bibendum eget odio. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lobortis lectus libero, dapibus mollis elit ultrices et. Maecenas ornare ex at nibh faucibus, vel dapibus elit aliquet."

def summary(text,lines):
    
    import requests
    
    url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-text"
    
    payload = "text=" +output+ "&sentnum=" + lines
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "b03ee82bbcmsh3579e3fca7285e5p1ce1a4jsnc7bb6182f40c",
        'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return(response.text)
