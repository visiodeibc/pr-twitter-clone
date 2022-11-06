from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.tweets as crud
from src.auth.jwthandler import get_current_user
from src.schemas.tweets import TweetOutSchema, TweetInSchema, UpdateTweet
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()
@router.post(
    "/like", dependencies=[Depends(get_current_user)]
)
async def create_like(
    tweet_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.create_like(tweet_id, current_user)


# @router.get(
#     "/likes",
#     response_model=List[TweetOutSchema],
#     # dependencies=[Depends(get_current_user)],
# )
# async def get_tweets():
#     return await crud.get_all_tweets()


# @router.patch(
#     "/tweet/{tweet_id}",
#     dependencies=[Depends(get_current_user)],
#     response_model=TweetOutSchema,
#     responses={404: {"model": HTTPNotFoundError}},
# )
# async def update_tweet(
#     tweet_id: int,
#     tweet: UpdateTweet,
#     current_user: UserOutSchema = Depends(get_current_user),
# ) -> TweetOutSchema:
#     return await crud.update_tweet(tweet_id, tweet, current_user)
