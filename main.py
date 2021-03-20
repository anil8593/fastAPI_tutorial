from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message' : 'heyy','date' : '20th Mar'}

@app.get('/about')
def about():
    return ({'name':'Anil Kumar Goyal','age': 23})