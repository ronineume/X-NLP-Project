# SDSC3013 Project - CityUHK

We used Twitter API to scrawled 4799 tweets on the topic of US Election 2024 from X (Twitter)

# Description of dataset
Tweets{ \
edit_history_tweet_ids:	array | Unique identifiers indicating all versions of an edited Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edit, with the most recent version in the last position of the array. \
\
created_at:	date (ISO 8601) | Creation time of the Tweet. \
\
id:	string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. \
\
author_id: string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. \
\
text:	string | The content of the Tweet. \
\
retweet_count: integer | Number of times this Tweet has been Retweeted. \
\
reply_count: integer | Number of Replies of this Tweet. \
\
like_count:	integer | Number of Likes of this Tweet. \
\
quote_count:	integer | Number of times this Tweet has been Retweeted with a comment (also known as Quote). \
\
bookmark_count:	integer | Number of times this Tweet has been bookmarked. \
\
impression_count:	integer | Number of times this Tweet has been viewed. \
\
referenced_tweet_types: enum (retweeted, quoted, replied_to) | Indicates the type of relationship between this Tweet and the Tweet returned in the response: retweeted (this Tweet is a Retweet), quoted (a Retweet with comment, also known as Quoted Tweet), or replied_to (this Tweet is a reply). \
}

# References
https://github.com/nestauk/dap_medium_articles/tree/dev/twitter_api_tutorial \
[X API Usage](https://developer.x.com/en/docs/x-api/tweets/search/api-reference/get-tweets-search-recent)
