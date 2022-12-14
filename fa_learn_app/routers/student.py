from typing import List
import uuid
from fastapi import APIRouter, Depends
from fa_learn_app.dependencies import get_product_repo
from fa_learn_app.models.student import StudentIn, StudentOut
from fa_learn_app.repositories.student import BaseProductRepository



router = APIRouter()

@router.get("/students", response_model = List[StudentOut])
async def get_products(
        product_repo :BaseProductRepository = Depends(get_product_repo),
        limit :int = 100,
        skip :int = 0
    ):
    return product_repo.get_all(limit=limit, skip=skip)

@router.get("/student", response_model = StudentOut)
async def get_product(
        id :uuid.UUID,
        product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.get_by_id((id))

@router.post("/student", response_model = StudentOut)
async def create_product(
        product_in :StudentIn,
        product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.create(product_in)

@router.put("/student", response_model=StudentOut | str)
async def update_product(
        id: uuid.UUID,
        product_in: StudentIn,
        product_repo: BaseProductRepository = Depends(get_product_repo),
        ):

    return product_repo.updateproduct(id, product_in)

@router.delete("/student", response_model=str)
async def delete_product(
        id: uuid.UUID,
        product_repo: BaseProductRepository = Depends(get_product_repo),
        ):

    return product_repo.delete(id)



