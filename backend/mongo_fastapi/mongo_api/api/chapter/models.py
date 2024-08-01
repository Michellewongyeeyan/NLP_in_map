from pydantic import BaseModel, Field


class Model(BaseModel):
    chapter: int = Field(...)
    location: str = Field(...)
    nominatim: list[float] = Field(...)
    lines: list[int] = Field(...)
    count: int = Field(...)
    text: list[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "chapter": 1,
                "location": "Athens",
                "nominatim": [39.2556311, -81.7715217],
                "lines": [15],
                "count": 1,
                "text": [
                    "—My name is absurd too: Malachi Mulligan, two dactyls. But it has a Hellenic ring, hasn’t it? Tripping and sunny like the buck himself. We must go to Athens. Will you come if I can get the aunt to fork out twenty quid?"
                ],
            },
        }

class ManyModel(BaseModel):
    data : list[Model] = Field(...)

class UpdateModel(BaseModel):
    chapter: int = Field(...)
    location: str = Field(...)
    nominatim: list[float] = Field(...)
    lines: list[int] = Field(...)
    count: int = Field(...)
    text: list[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "chapter": 2,
                "location": "Athens",
                "nominatim": [39.2556311, -81.7715217],
                "lines": [15],
                "count": 1,
                "text": [
                    "—My name is absurd too: Malachi Mulligan, two dactyls. But it has a Hellenic ring, hasn’t it? Tripping and sunny like the buck himself. We must go to Athens. Will you come if I can get the aunt to fork out twenty quid?"
                ],
            },
        }

# class Model(BaseModel):
#     model: str = Field(...)
#     api_url: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "model": "gemma:2b",
#                 "api_url": "http://127.0.0.1:11434/v1",
#             }
#         }

# class UpdateModel(BaseModel):
#     model: str = Field(...)
#     api_url: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "model": "gemma:2b",
#                 "api_url": "http://192.168.50.171:11434/v1",
#             }
#         }
