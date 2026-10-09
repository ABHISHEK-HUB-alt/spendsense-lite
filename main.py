from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

expenses = [
    {"id": 1, "title": "Internet Bill", "amount": 1500, "category": "Utilities"},
    {"id": 2, "title": "Lunch", "amount": 250, "category": "Food"}
]

class Expense(BaseModel):
    title: str
    amount: float
    category: str

@app.get("/expenses")
def get_expenses():
    return expenses

@app.post("/expenses")
def create_expense(expense: Expense):
    new_id = len(expenses) + 1
    new_expense = {
        "id": new_id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category
    }
    expenses.append(new_expense)
    return {"message": "Expense added successfully!", "data": new_expense}
