from pytube import YouTube

url = input("Enter your url -> ")
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title + "\n")

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url + "\n")

print("********************Download video*************************")
#get all the stream resolution for the
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#or
# my_video = my_video.streams.first()

#Download video
my_video.download()