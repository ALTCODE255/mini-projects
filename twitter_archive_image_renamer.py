from datetime import datetime
import os

directory = input("Absolute path of images: ")
dupe_count = 0

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
		os.rename(f"{directory}\\{current_file}", f"{directory}\\{new_name}")
	except FileExistsError:
		dupe_count += 1
		os.rename(f"{directory}\\{current_file}", f"{directory}\\(DUPLICATE {dupe_count}) - {new_name}")
	finally:
		if current_file == dir_list[-1]:
			break