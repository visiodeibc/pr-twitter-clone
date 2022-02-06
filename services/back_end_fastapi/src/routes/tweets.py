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

@router.get(
    "/all_tweets",
    response_model=List[TweetOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_tweets():
    return await crud.get_all_tweets()

@router.get(
    "/tweets",
    response_model=List[TweetOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_tweets(current_user: UserOutSchema = Depends(get_current_user)):
    return await crud.get_tweets(current_user)


@router.get(
    "/tweet/{tweet_id}",
    response_model=TweetOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_tweet(tweet_id: int) -> TweetOutSchema:
    try:
        return await crud.get_tweet(tweet_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Tweet does not exist",
        )


@router.post(
    "/tweets", response_model=TweetOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_tweet(
    tweet: TweetInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> TweetOutSchema:
    return await crud.create_tweet(tweet, current_user)


@router.patch(
    "/tweet/{tweet_id}",
    dependencies=[Depends(get_current_user)],
    response_model=TweetOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_tweet(
    tweet_id: int,
    tweet: UpdateTweet,
    current_user: UserOutSchema = Depends(get_current_user),
) -> TweetOutSchema:
    return await crud.update_tweet(tweet_id, tweet, current_user)


@router.delete(
    "/tweet/{tweet_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_tweet(
    tweet_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_tweet(tweet_id, current_user)
