from typing import List
import uuid
from fastapi import APIRouter, Depends
from fa_learn_group_app.dependencies import get_product_repo
from fa_learn_group_app.models.group import GroupIn, GroupOut
from fa_learn_group_app.repositories.group import BaseProductRepository



router = APIRouter()

@router.get("/Groups", response_model = List[GroupOut])
async def get_products(
        product_repo :BaseProductRepository = Depends(get_product_repo),
        limit :int = 100,
        skip :int = 0
    ):
    return product_repo.get_all(limit=limit,skip = skip)

@router.get("/Group", response_model = GroupOut)
async def get_product(
        id :uuid.UUID,
        product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.get_by_id((id))

@router.post("/Group", response_model = GroupOut)
async def create_product(
        product_in :GroupIn,
        product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.create(product_in)

@router.put("/Group", response_model=GroupOut | str)
async def update_product(
        id: uuid.UUID,
        product_in: GroupIn,
        product_repo: BaseProductRepository = Depends(get_product_repo),
        ):

    return product_repo.updateproduct(id, product_in)

@router.delete("/Group", response_model=str)
async def delete_product(
        id: uuid.UUID,
        product_repo: BaseProductRepository = Depends(get_product_repo),
        ):

    return product_repo.delete(id)



