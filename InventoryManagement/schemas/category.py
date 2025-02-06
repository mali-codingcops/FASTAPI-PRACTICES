from pydantic import BaseModel, field_validator

class CategoryBase(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str):
        if not name:
            raise ValueError("Category Name Shouldn't be Empty")
        return name


class CategoryCreated(CategoryBase):
    pass

class Category(CategoryBase):
    id : int