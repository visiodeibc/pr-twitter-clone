-- upgrade --
CREATE TABLE IF NOT EXISTS "likes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "valid" BOOL NOT NULL  DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "tweet_id" INT NOT NULL REFERENCES "tweets" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "likes";
