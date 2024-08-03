from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# 引入數據庫操作函數
from .database import (
    add_data,  # 新增
    delete_data,  # 刪除
    update_data,  # 更新
    get_datas,  # 獲取所有
    get_data,  # 獲取單個
    get_data_by_chapter,
)

# 引入數據模型
from .models import (
    Model,  # 模型
    ManyModel,
    UpdateModel,  # 更新模型
)

from api.utils.response import (
    ResponseModel,  # 响應模型
    ErrorResponseModel,  # 錯誤響應模型
)


# CRUD
@router.post("/", response_description="add data")
async def add(model: Model = Body(...)):
    model = jsonable_encoder(model)
    new_data = await add_data(model)
    if new_data:
        return ResponseModel(new_data, "Added Successfully.")
    return ErrorResponseModel("An error occurred", 404, "Already Exists")


@router.post("/many", response_description="add many data")
async def add_many(model: ManyModel = Body(...)):
    model = jsonable_encoder(model.data)
    new_data = await add_data(model)
    if new_data:
        return ResponseModel(new_data, "Added Successfully.")
    return ErrorResponseModel("An error occurred", 404, "Already Exists")


@router.delete("/{id}", response_description="delect data")
async def delete(id: str):
    data = await delete_data(id)
    if data:
        return ResponseModel(f"Data with ID: {id} removed", "Deleted successfully")
    return ErrorResponseModel(
        f"An error occurred", 404, "Data with id {id} doesn't exist"
    )


@router.get("/", response_description="gets data")
async def gets():
    datas = await get_datas()
    return ResponseModel(datas, "Get all datas successfully")


@router.get("/{id}", response_description="get data")
async def get(id: str):
    data = await get_data(id)
    if data:
        return ResponseModel(data, "Get data successfully")
    return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")


@router.get("/data/{num}", response_description="get data by chapter")
async def get_chapter(num: int):
    data = await get_data_by_chapter(num)
    if data:
        return ResponseModel(data, "Get chapter {num} data successfully")
    return ErrorResponseModel("An error occurred.", 404, "chapter data doesn't exist.")


@router.put("/{id}", response_description="update data")
async def update(id: str, req: UpdateModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_data = await update_data(id, req)
    if updated_data:
        return ResponseModel(
            "Data with ID: {} name update is successful".format(id),
            "Data name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the data.",
    )
