consumer_key = 'your own'
consumer_secret = 'your own'
access_token = 'your own'
access_secret = 'your own'
bearer_token = 'your own'

import requests
import json
import time
import random
import os
import pandas as pd
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

rules = [
    {"value": '("Election2024" OR "USElection2024") -is:retweet lang:en', "tag": "Election2024"},
    {"value": '("Trump" OR "Trump2024") -is:retweet lang:en', "tag": "Trump2024"},
    {"value": '("Harris" OR "Kamala Harris") -is:retweet lang:en', "tag": "KamalaHarris"}
]

query_parameters = {
    "tweet.fields": "id,text,author_id,created_at,public_metrics,referenced_tweets",
    "user.fields": "id,name,username,created_at,description,location,verified,public_metrics",
    "expansions": "author_id",
    "max_results": 100,
}
def request_headers(bearer_token: str) -> dict:
    """
    Set up the request headers. 
    Returns a dictionary summarising the bearer token authentication details.
    """
    return {"Authorization": "Bearer {}".format(bearer_token)}
headers = request_headers(bearer_token)

def connect_to_endpoint(endpoint_url: str, headers: dict, parameters: dict) -> json:
    """
    Connects to the endpoint and requests data.
    Returns a json with Twitter data if a 200 status code is yielded.
    Programme stops if there is a problem with the request and sleeps
    if there is a temporary problem accessing the endpoint.
    """
    response = requests.request(
        "GET", url=endpoint_url, headers=headers, params=parameters
    )
    response_status_code = response.status_code
    if response_status_code != 200:
        if response_status_code >= 400 and response_status_code < 500:
            raise Exception(
                "Cannot get data, the program will stop!\nHTTP {}: {}".format(
                    response_status_code, response.text
                )
            )
        
        sleep_seconds = random.randint(5, 60)
        print(
            "Cannot get data, your program will sleep for {} seconds...\nHTTP {}: {}".format(
                sleep_seconds, response_status_code, response.text
            )
        )
        time.sleep(sleep_seconds)
        return connect_to_endpoint(endpoint_url, headers, parameters)
    return response.json()

def process_twitter_data(
    json_response: json,
    query_tag: str,
    tweets_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Adds new tweet/user information to the table of
    tweets/users and saves dataframes as pickle files,
    if data is avaiable.
    
    Returns the tweets and users updated dataframes.
"""
   
    if "data" in json_response.keys():
        #new = pd.DataFrame(json_response)
        new = pd.json_normalize(json_response)
        tweets_data = pd.concat([tweets_data, new])
        tweets_data.to_pickle("tweets_" + query_tag + ".pkl")

    return tweets_data

# Initialize two empty DataFrames to store tweet and user data
tweets_data = pd.DataFrame()

# Iterate over each rule, send requests, and retrieve tweet and user data
for i in range(len(rules)):
    query_parameters["query"] = rules[i]["value"]  # Set the query string for the current rule
    query_tag = rules[i]["tag"]  # Get the tag for the current rule for file naming

    # Connect to the Twitter API and get the JSON response
    json_response = connect_to_endpoint(endpoint_url, headers, query_parameters)
    
    # Process the JSON response and update the tweet data DataFrame
    tweets_data = process_twitter_data(
        json_response, query_tag, tweets_data
    )

    time.sleep(15)  # Pause for 15 seconds to comply with API rate limits

    # Check if there is a next page of data to retrieve
    while "next_token" in json_response["meta"]:
        query_parameters["next_token"] = json_response["meta"]["next_token"]  # Get the next page token

        # Connect to the Twitter API again to retrieve the next page of data
        json_response = connect_to_endpoint(endpoint_url, headers, query_parameters)
        
        # Process the JSON response and update the tweet and user data DataFrame
        tweets_data = process_twitter_data(
            json_response, query_tag, tweets_data
        )

        time.sleep(15)  # Pause for 15 seconds to comply with API rate limits

# Save tweet and user data as a JSON file
tweets_data.to_json("tweets_data.json", orient="records", lines=True, force_ascii=False)

print("Data has been successfully saved as a JSON file.")
