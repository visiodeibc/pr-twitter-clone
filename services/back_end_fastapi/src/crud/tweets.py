from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Tweets
from src.schemas.tweets import TweetOutSchema
from src.schemas.token import Status

async def get_all_tweets():
    return await TweetOutSchema.from_queryset(Tweets.filter(public=True))

async def get_tweets(current_user):
    return await TweetOutSchema.from_queryset(Tweets.filter(author=current_user.id))


async def get_tweet(tweet_id) -> TweetOutSchema:
    return await TweetOutSchema.from_queryset_single(Tweets.get(id=tweet_id))


async def create_tweet(tweet, current_user) -> TweetOutSchema:
    tweet_dict = tweet.dict(exclude_unset=True)
    tweet_dict["author_id"] = current_user.id
    tweet_obj = await Tweets.create(**tweet_dict)
    return await TweetOutSchema.from_tortoise_orm(tweet_obj)


async def update_tweet(tweet_id, tweet, current_user) -> TweetOutSchema:
    try:
        db_tweet = await TweetOutSchema.from_queryset_single(Tweets.get(id=tweet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Tweet {tweet_id} not found")

    if db_tweet.author.id == current_user.id:
        await Tweets.filter(id=tweet_id).update(**tweet.dict(exclude_unset=True))
        return await TweetOutSchema.from_queryset_single(Tweets.get(id=tweet_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_tweet(tweet_id, current_user) -> Status:
    try:
        db_tweet = await TweetOutSchema.from_queryset_single(Tweets.get(id=tweet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Tweet {tweet_id} not found")

    if db_tweet.author.id == current_user.id:
        deleted_count = await Tweets.filter(id=tweet_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Tweet {tweet_id} not found")
        return Status(message=f"Deleted note {tweet_id}") 

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")