# SDSC3013 Project - CityUHK

We used Twitter API to scrawled 4799 tweets on the topic of US Election 2024 from X (Twitter)

# Description of dataset (After Data Clean)
| Field                     | Type                    | Description                                                                                                                             |
|---------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `edited`                  | integer                   | 0: No edits ; 1: Tweet is edited |
| `tweets_created_at`       | Y-m-d H:M:S (UTC)        | Creation time of the Tweet.                                                                                                            |
| `tweet_id`                      | integer                 | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `author_id`              | integer                  | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `text`                    | string                  | The content of the Tweet.                                                                                                              |
| `retweet_count`          | integer                 | Number of times this Tweet has been Retweeted.                                                                                         |
| `reply_count`            | integer                 | Number of Replies of this Tweet.                                                                                                        |
| `tweet_like_count`             | integer                 | Number of Likes of this Tweet.                                                                                                          |
| `quote_count`            | integer                 | Number of times this Tweet has been Retweeted with a comment (also known as Quote).                                                    |
| `bookmark_count`         | integer                 | Number of times this Tweet has been bookmarked.                                                                                         |
| `impression_count`       | integer                 | Number of times this Tweet has been viewed.                                                                                            |
| `referenced_tweet_types` | integer                    | Indicates the type of relationship between this Tweet and the Tweet returned in the response: retweeted, quoted, or replied_to. 0: Original 1: replied_to 2: quoted 3: 'quoted', 'replied_to'       |

# References
[twitter_api_tutorial](https://github.com/nestauk/dap_medium_articles/tree/dev/twitter_api_tutorial) \
[X API Usage](https://developer.x.com/en/docs/x-api/tweets/search/api-reference/get-tweets-search-recent) \
[徒手搓LLM）逐行代码从0构造一个LLM——LlaMa篇](https://zhuanlan.zhihu.com/p/1674261485) \
[llama3 model.py](https://github.com/meta-llama/llama3/blob/main/llama/model.py)
