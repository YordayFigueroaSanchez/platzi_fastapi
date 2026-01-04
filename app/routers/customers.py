from fastapi import HTTPException, status, APIRouter
from models import CustomerBase, CustomerCreate, CustomerUpdate, Customer
from db import SessionDep
from sqlmodel import select

router = APIRouter()

@router.get("/customer", tags=["customers"])
async def get_customers(session: SessionDep):
    return session.exec(select(Customer)).all()

@router.post("/customer", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=["customers"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customer/{customer_id}", response_model=Customer, tags=["customers"])
async def get_customer_by_id(customer_id: int, session: SessionDep):
    # return session.exec(select(Customer).where(Customer.id == customer_id)).one_or_none()
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer_db

@router.patch("/customer/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=["customers"])
async def update_customer_by_id(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db

@router.delete("/customer/{customer_id}", tags=["customers"])
async def delete_customer_by_id(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    session.delete(customer_db)
    session.commit()
    return {"detail": "ok"}