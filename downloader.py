from pytube import YouTube



def downloader(link):
	yt_obj = YouTube(link)
	video = yt_obj.streams.get_highest_resolution()
	video.download()

if __name__ == '__main__':
	link = 'https://www.youtube.com/watch?v=QU1pPzEGrqw'

	downloader(link)