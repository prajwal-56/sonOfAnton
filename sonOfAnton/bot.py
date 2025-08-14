import praw
import random

reddit = praw.Reddit(
    client_id="sTHuuziE0_nM8kPtxVwCyg",
    client_secret="U53bWbVsxOnzf4WnzoSxzHamEsES4w",
    user_agent="winterJerry",
    username="Electronic_Nebula911",
    password="wubbaLubbaDubDub"
)

print("Logged in as:", reddit.user.me())

# ------------------------------------------



subs = ["test", "learnpython", "Coconaad" , "SipsTea" , "interestingasfuck"]
comments = [
    "Hey , This is a test for a comment. Did it work ?" , 
    "Came here to say the same thing." ,
    "This. Absolutely this.", 
    "Reddit never disappoints.",
    "Well, that escalated quickly.",
    "Classic Reddit moment.",
    "I didn't expect to read this today, but here we are.",
    "Just when I thought I’d seen it all."
]

titles = [
    "Hey This is a test post and I vibecoded most of the script. lol", 
    "This is my first test post" 
]

bodies = [
     "Hello Reddit! This post was made by a bot I vibeCoded.",
    "Automating Reddit posts is easier than I thought! I vibeCoded this bot btw",
    "PRAW is fun to work with. I vibeCoded this bot btw"
]


# # stores a random subreddit to post the comment on

# # subReddit = random.choice(subs)
# subreddit_name = "test"
# comment = random.choice(comments)

# subreddit = reddit.subreddit(subreddit_name) # 
# post = random.choice(list(subreddit.hot(limit=10)))
# post.reply(comment)

# print("Success Bithc !!!")
# print(f"commented \"{comment}\" on {subreddit} ")

#____________________________________________________

subreddit_name = "test"
title = random.choice(titles)
body = random.choice(bodies)

# Submit the post
reddit.subreddit(subreddit_name).submit(title=title, selftext=body)

print(f"Posted to r/{subreddit_name}: {title}")
