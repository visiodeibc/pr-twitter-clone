from pydantic import BaseModel
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users


UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)
class UpdateUser(BaseModel):
    username: Optional[str]
    full_name: Optional[str]