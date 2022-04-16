from dataclasses import field
from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Tweets(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    public = fields.BooleanField(default=False)
    author = fields.ForeignKeyField("models.Users", related_name="tweet")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"

class Likes(models.Model):
    id = fields.IntField(pk=True)
    valid = fields.BooleanField(default=True)
    liker = fields.ForeignKeyField("models.Users", related_name="like")
    tweet = fields.ForeignKeyField("models.Tweets", related_name="like")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    class Meta:
        unique_together=(("tweet", "liker"), )
        indexes=("tweet", "liker")