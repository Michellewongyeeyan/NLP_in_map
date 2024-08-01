from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# 引入數據庫操作函數
from .database import (
    add_data,        # 新增
    delete_data,     # 刪除
    update_data,     # 更新
    get_datas,       # 獲取所有
    get_data,        # 獲取單個
)

# 引入數據模型
from .models import (
    Model,           # 模型
    UpdateModel,    # 更新模型
)

from api.utils.response import (
    ResponseModel,       # 响應模型
    ErrorResponseModel,  # 錯誤響應模型
)

# CRUD 增刪查改
# 新增
@router.post("/", response_description="創建")
async def add(model: Model = Body(...)):
    model = jsonable_encoder(model) # 將數據轉換為 JSON 可序列化的格式
    new_data = await add_data(model)
    if new_data:
        return ResponseModel(new_data, "Added Successfully.")
    return ErrorResponseModel("An error occurred", 404, "Already Exists")

# 刪除
@router.delete("/{id}", response_description="刪除")
async def delete(id: str):
    data = await delete_data(id)
    if data:
        return ResponseModel(
            f"Data with ID: {id} removed", "Deleted successfully"
        )
    return ErrorResponseModel(
        f"An error occurred", 404, "Data with id {id} doesn't exist"
    )

# 查看
## 全部
@router.get("/", response_description="取得所有")
async def gets():
    datas = await get_datas()
    return ResponseModel(datas, "Get all datas successfully")

# ## 單個
@router.get("/{id}", response_description="取得單個")
async def get(id: str):
    data = await get_data(id)
    if data:
        return ResponseModel(data, "Get data successfully")
    return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")    

# # 更新
@router.put("/{id}", response_description="更新")
async def update(id:str,req: UpdateModel = Body(...)):
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
