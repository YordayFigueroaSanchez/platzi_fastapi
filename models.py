from sqlmodel.main import Relationship
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

# CustomerPlan
class CustomerPlan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    plan_id: int = Field(foreign_key="plan.id")

# Plan
class PlanBase(SQLModel):
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)
class PlanCreate(PlanBase):
    pass
class PlanUpdate(PlanBase):
    pass
class Plan(PlanBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)
    

# Customer
class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list["Plan"] = Relationship(back_populates="customers", link_model=CustomerPlan)

# Transaction
class TransactionBase(SQLModel):
    amount: int
    description: str

class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")
    
class TransactionUpdate(TransactionBase):
    pass

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: "Customer" = Relationship(back_populates="transactions")

# Invoice
class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def amount_total(self):
        return sum(transaction.amount for transaction in self.transactions)