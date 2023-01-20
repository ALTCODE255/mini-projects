from datetime import datetime
import os

directory = input("Absolute path of images: ")

def get_tweet_timestamp(tid_string):
	twitter_id = int(tid_string[:19])
	date_binary = str(bin(twitter_id)[2:40])
	unix_time_seconds = (int(date_binary, 2) + 1288834974657) / 1000
	timestamp_object = datetime.fromtimestamp(unix_time_seconds)
	filename = str(timestamp_object.strftime("%Y%m%d_%H%M%S")) + os.path.splitext(tid_string)[1]
	return(filename)

dir_list = os.listdir(directory)

for current_file in dir_list:
	new_name = get_tweet_timestamp(current_file)
	try:
		os.rename(directory + "\\" + current_file, directory + "\\" + new_name)
	except FileExistsError:
		pass
	finally:
		if current_file == dir_list[-1]:
			break