import instaloader

test = instaloader.Instaloader()

account = input("Enter account username ->")

test.download_profile(account, profile_pic_only=True)