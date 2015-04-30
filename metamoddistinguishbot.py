import praw
import time

r = praw.Reddit(user_agent= 'Automatic moderator comment distinguishing on threads with a  "Meta" flair by Julian Rose /u/naliuj2525')

r.login()
print('Logging in...')

cache = []

def run_bot():
    subreddit = r.get_subreddit('juliancss')
    mods = r.get_moderators('juliancss')
    submissions = subreddit.get_hot(limit=25)
    for submission in submissions:
        if submission.link_flair_text == 'Meta':
            comments = praw.helpers.flatten_tree(submission.comments)
            for comment in comments:
                author = comment.author
                if author in mods and comment.id not in cache:
                    comment.distinguish()
                    cache.append(comment.id)
                    print('Distinguished '+comment.id)

while True:
    run_bot()
    time.sleep(10)