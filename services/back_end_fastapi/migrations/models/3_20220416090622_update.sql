-- upgrade --
ALTER TABLE "likes" ADD "liker_id" INT NOT NULL;
CREATE UNIQUE INDEX "uid_likes_tweet_i_b4b0c8" ON "likes" ("tweet_id", "liker_id");
ALTER TABLE "likes" ADD CONSTRAINT "fk_likes_users_f49ee11f" FOREIGN KEY ("liker_id") REFERENCES "users" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "likes" DROP CONSTRAINT "fk_likes_users_f49ee11f";
DROP INDEX "uid_likes_tweet_i_b4b0c8";
ALTER TABLE "likes" DROP COLUMN "liker_id";
