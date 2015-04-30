import praw

r = praw.Reddit(user_agent= 'Automatic moderator comment distinguishing on threads with a  "Meta" flair by Julian Rose /u/naliuj2525')

r.login()
print('Logging in...')

cache = []

def run_bot():
    subreddit = r.get_subreddit('juliancss')
    mods = r.get_moderators('juliancss')
    submissions = subreddit.get_hot(limit=25)
    print('Loaded submissions...')
    for submission in submissions:
        if submission.link_flair_text == 'Meta':
            print('Submission found. ID:'+submission.id)
            comments = praw.helpers.flatten_tree(submission.comments)
            for comment in comments:
                author = comment.author
                print(author)
                if author in mods:
                    comment.distinguish()
                                       
run_bot()
input = input()