from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class blog_details(BaseModel):
    blog_name : str
    blog_creator : str
    blog_id : int

app = FastAPI()

@app.get('/')
def index():
    return {'message' : 'heyy','date' : '20th Mar'}

### Static routes ###

@app.get('/about')
def about():
    return ({'name' :  'anil goyal','age':23})

#### passing query parameters ####

@app.get('/blog/fetch_blogs')
def fetch_blogs(limit : int, published : bool = True, sort: Optional[int] = None):
    if (published):
        return ({'data' : "Getting {} blogs from published".format(limit)})
    else:
        return ({'data' : "Getting {} blogs from unpublished".format(limit)})


### Dynamic routes ####

@app.get('/blog/{id}')
def id_info(id):
    return({"data" : id})

### type checking ####

@app.get('/blog/{id}/check')
def type_check(id : int):
    return({"data":id})

##### Post method examples with body parameter#####

@app.post('/blog/create_blog')
def create_blog(details : blog_details):
    return ('The blog has been created with name {} , id  {} and by {}'.format(details.blog_name,details.blog_id, details.blog_creator))


if __name__ == '__main__':
    uvicorn.run(app,host = "127.0.0.1", port = 9000)
