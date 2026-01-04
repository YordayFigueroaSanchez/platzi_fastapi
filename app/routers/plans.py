from fastapi import APIRouter
from models import PlanCreate, Plan
from db import SessionDep
from sqlmodel import select
from fastapi import status

router = APIRouter()

@router.post("/plan", tags=["plans"], status_code=status.HTTP_201_CREATED)
async def create_plan(plan_data: PlanCreate, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db

@router.get("/plan", tags=["plans"])
async def get_plans(session: SessionDep):
    query = select(Plan)
    plans = session.exec(query).all()
    return plans