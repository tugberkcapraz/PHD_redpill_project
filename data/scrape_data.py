import pandas as pd
import praw
from data.secret_keys import client_id, client_secret, user_agent

print ("Starting the script")
# put the credentials to environment!
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)
subreddit = reddit.subreddit("TheRedPill")
# OPT in to the quarantined subreddit scraping mode
subreddit.quaran.opt_in()
print("done")


posts = []
for post in subreddit.hot(limit=500):
    posts.append([post.title,
                  post.score,
                  post.id,
                  post.subreddit,
                  post.url,
                  post.num_comments,
                  post.selftext,
                  post.created])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# check all works by printing
print(posts)

# save the posts to csv file
posts.to_csv("redpill_sample_500.csv")


#%%

