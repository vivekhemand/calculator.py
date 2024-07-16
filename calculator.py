from fastapi import FastAPI, HTTPException
import math

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}

@app.get("addition")
def addition(a:float,b:float):
    return{"result:",a+b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}

@app.get("/log")
def logarithm(x: float, base: float = 10):
    if x <= 0 or base <= 0 or base == 1:
        raise HTTPException(status_code=400, detail="Invalid input for logarithm")
    return {"result": math.log(x, base)}


