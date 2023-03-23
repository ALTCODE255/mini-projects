from datetime import datetime, timedelta
import os
import shutil
import sys


def getTweetTimestamp(tweet_id: int) -> datetime:
	date_binary = str(bin(tweet_id)[2:40])
	unix_time_seconds = (int(date_binary, 2) + 1288834974657) / 1000
	timestamp_object = datetime.fromtimestamp(unix_time_seconds)
	return timestamp_object


def renameToNewDirectory(in_folder: str, out_folder: str):
	dupe_count = 0
	success_count = 0
	file_list = os.listdir(in_folder)
	for file in file_list:
		if file[:19].isdigit():
			file_ext = os.path.splitext(file)[1]
			twitter_id = int(file[:19])
			new_filename = getTweetTimestamp(twitter_id).strftime("%Y%m%d_%H%M%S")
			if os.path.exists(f"{out_folder}\\{new_filename + file_ext}"):
				dupe_count = 0
				hasDuplicates = True
				while hasDuplicates:
					dupe_count += 1
					new_filename = (
						getTweetTimestamp(twitter_id) + timedelta(seconds=dupe_count)
					).strftime("%Y%m%d_%H%M%S")
					hasDuplicates = os.path.exists(
						f"{out_folder}\\{new_filename + file_ext}"
					)
				dupe_count = 0
			shutil.copy(
				f"{in_folder}\\{file}", f"{out_folder}\\{new_filename + file_ext}"
			)
			success_count += 1
	print(
		f"---\nDone! {success_count} file(s) successfully copied and renamed. Check folder '{out_folder}' for renamed files."
	)
	input("Press enter to exit.")


if __name__ == "__main__":
	input_directory = input("Path of archive media folder: ")
	output_directory = input("Path of folder to output renamed files to: ")
	if not os.path.exists(input_directory) or not os.path.exists(output_directory):
		print(
			"One or more specified directories do not exist! Please try again.",
			file=sys.stderr,
		)
		input("Press enter to exit.")
	else:
		renameToNewDirectory(input_directory, output_directory)
