from pydantic import BaseModel, Field

# 模型
class Model(BaseModel):
    model: str = Field(...)
    api_url: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "model": "gemma:2b",
                "api_url": "http://127.0.0.1:11434/v1",
            }
        }
        
#  更新模型
class UpdateModel(BaseModel):
    model: str = Field(...)
    api_url: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "model": "gemma:2b",
                "api_url": "http://192.168.50.171:11434/v1",
            }
        }