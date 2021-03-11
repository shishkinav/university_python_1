from pydantic import BaseModel, validator
import re


class SchemaWareHouse(BaseModel):
    name: str


class SchemaEquipment(BaseModel):
    maker: str
    model: str
    inv_number: str

    @validator('inv_number')
    def inventory_number(cls, value: str):
        if not re.match(r'\w{1}\d{2}.*', value):
            raise ValueError(f'Формат инвентарного номера {value} некорректен')
        return value.upper()
