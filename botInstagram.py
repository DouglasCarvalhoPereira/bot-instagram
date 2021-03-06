from instaloader import Instaloader, Profile

login_name = 'insta_botbr'

target_profile = 'dani_personal_fit'
# OR
#import sys
#target_profile = sys.argv[1] # pass in target profile as argument

loader = Instaloader()

# login
try:
    loader.load_session_from_file(login_name)
except FileNotFoundError:
    loader.context.log("Session file does not exist yet - Logging in.")
if not loader.context.is_logged_in:
    loader.interactive_login(login_name)
    loader.save_session_to_file()

profile = Profile.from_username(loader.context, target_profile)
followers = profile.get_followers()

loader.context.log()
loader.context.log('Profile {} has {} followers:'.format(profile.username, profile.followers))
loader.context.log()

for follower in followers:
    loader.context.log(follower.username, flush=True)