# DataBase
import os
import motor.motor_asyncio
from bson.objectid import ObjectId

# 連接 Mongo
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["ME_CONFIG_MONGODB_URL"])
database = client.ansc
data_collection = database.get_collection("app")

## 洗格式
def helper(_dict: dict) -> dict:
    _dict["id"]  = str(_dict["_id"])
    del _dict["_id"]
    return _dict

# CRUD 增刪查改
# 新增
async def add_data(new_data: dict | list) -> dict | list:
    if isinstance(new_data, dict):
        # 插入单个数据
        data = await data_collection.insert_one(new_data)
        new_data = await data_collection.find_one({"_id": data.inserted_id})
        return helper(new_data)
    elif isinstance(new_data, list):
        # 批量插入多个数据
        datas = await data_collection.insert_many(new_data)
        new_data = [ helper(data) for data in new_data]
        return new_data
    
# async def add_data(new_data: dict|list) -> dict:
#     # 加入
#     data = await data_collection.insert_one(new_data)
#     new_data = await data_collection.find_one({"_id": data.inserted_id})
#     return helper(new_data)

# 刪除
async def delete_data(id: str):
    if len(id) == 24:
        data = await data_collection.find_one({"_id": ObjectId(id)})
        if data:
            await data_collection.delete_one({"_id": ObjectId(id)})
            return True
    return False

# 查看
## 全部
async def get_datas() -> list:
    datas = []
    async for data in data_collection.find():
        datas.append(helper(data))
    return datas

## 單個
async def get_data(id: str):
    if len(id) == 24:
        try:
            data = await data_collection.find_one({"_id": ObjectId(id)})
            if data:
                return helper(data)
        except:
            return False
    return False

# 更新
async def update_data(id: str, new_data: dict):
    # Return false if an empty request body is sent.
    if len(id) == 24:
        try:
            data = await data_collection.find_one({"_id": ObjectId(id)})
            print(data)
            if data:
                updated_data = await data_collection.update_one(
                    {"_id": ObjectId(id)}, {"$set": new_data}
                )
                if updated_data:
                    return True
        except:
            return False
    return False