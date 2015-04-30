import praw

r = praw.Reddit(user_agent= 'Automatic moderator comment distinguishing on threads with a  "Meta" flair by Julian Rose /u/naliuj2525')

r.login()
print('Logging in...')

mods = ['naliuj2525','fakeaccount']
cache = []

def run_bot():
    subreddit = r.get_subreddit('juliancss')
    submissions = subreddit.get_hot(limit=25)
    print('Loaded submissions...')
    for submission in submissions:
        if submission.link_flair_text == 'Meta':
            print('Submission found. ID:'+submission.id)
            post = r.get_submission(submission_id = submission.id)
            comments = post.comments
            for comment in comments:
                author = comment.author
                if author in mods and comment.id not in cache:
                    comment.delete()
                    print('Removed')
                    cache.append(comment.id)
                    
            
run_bot()
input()