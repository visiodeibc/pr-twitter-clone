-- upgrade --
ALTER TABLE "tweets" RENAME COLUMN "private" TO "public";
-- downgrade --
ALTER TABLE "tweets" RENAME COLUMN "public" TO "private";
