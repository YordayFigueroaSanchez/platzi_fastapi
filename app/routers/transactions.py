from models import Transaction
from fastapi import APIRouter

router = APIRouter()

@router.post("/transaction", tags=["transactions"])
async def create_transaction(transaction_data: Transaction):
    return transaction_data