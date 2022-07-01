from pytube import YouTube

def video_progress(stream,chunk,bytes_remaining):
	print("==================================")
	print("video downloading is in progress")
	#print(bytes_remaining / stream.filesize * 100)
	print(100 - (bytes_remaining / stream.filesize * 100))
	print("==================================")

def video_completed(stream,file_path):
	print("==================================")
	print("The video downloading is completed")
	print("==================================")

def download_video(video_url,video_path):

	utube_objet=YouTube(video_url,on_complete_callback=video_completed,on_progress_callback=video_progress)

	title=utube_objet.title
	author=utube_objet.author

	print("--------------------------------------------")
	print(f"The video '{title}' is uploaded by {author}")
	print("--------------------------------------------")

	print("Please enter 1 for highest resolution.")
	print("Please enter 2 for lowest resolution.")
	mode=int(input("Please enter your input:"))

	if mode==1:
		utube_objet.streams.get_highest_resolution().download(video_path)
	elif mode==2:
		utube_objet.streams.get_lowest_resolution().download(video_path)
	else:
		print("Bad input given.")	

def main():
	print("Welcome to the youtube video download program.")
	video_url=input("Please enter the Yooutube video url:")
	video_path=input("Please enter the path to store the video:")

	if video_url and video_path:
		download_video(video_url,video_path)

if __name__ == '__main__':
	main()