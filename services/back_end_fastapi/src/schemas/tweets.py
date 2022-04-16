from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Tweets


TweetInSchema = pydantic_model_creator(
    Tweets, name="TweetIn", exclude=["author_id"], exclude_readonly=True)
TweetOutSchema = pydantic_model_creator(
    Tweets, name="Tweet", exclude=[
        "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateTweet(BaseModel):
    title: Optional[str]
    content: Optional[str]
    public: Optional[bool]
