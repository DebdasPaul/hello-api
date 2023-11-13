from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(param):
     """A simple function that return "Hello {param}!
     
    Parameters
        ----------
    param : string|float|integer     
    
    """
    
    if len(param)==0:       
        return ("No parameter value is specified!")
    else:
        return {f"Hello {param}!"}
