from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my calculator"}

@app.get("/calculator")
async def calculate(x: float, y: float, operation: str):
    if operation == "addition":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiplication":
        result = x * y
    elif operation == "division":
        result = x / y
    elif operation == "logarithm":
        result = math.log(x, y)  # Calculate logarithm base y of x
    else:
         return {"error": "Invalid operation. Allowed operations: add, subtract, multiply, divide, logarithm"}

    return {"result": result}