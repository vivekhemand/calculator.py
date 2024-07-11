from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}

@app.get("/calculator")
async def calculate(x: float, y: float, operation: str):
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        result = x / y
    elif operation == "logarithm":
        result = math.log(x, y)  # Calculate logarithm base y of x
    else:
         return {"error": "Invalid operation. Allowed operations: add, subtract, multiply, divide, logarithm"}

    return {"result": result}