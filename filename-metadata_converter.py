import os
import piexif
from datetime import datetime
folder_path = input("Absolute path of image folder: ")

acceptable_file_extensions = [".jpg", ".jpeg", ".tif", ".tiff"]
unsupported_files = 0

for image in os.listdir(folder_path):
	img_name = os.path.splitext(image)[0]
	img_extension = os.path.splitext(image)[1]
	if img_extension not in acceptable_file_extensions:
		unsupported_files += 1
		continue
	img_path = os.path.join(folder_path, image)
	datetime_object = datetime.strptime(img_name, '%Y%m%d_%H%M%S')
	md_datetime = datetime_object.strftime("%Y:%m:%d %H:%M:%S")
	exif_dict = piexif.load(img_path)
	exif_dict['0th'][piexif.ImageIFD.DateTime] = md_datetime
	exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = md_datetime
	exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = md_datetime
	exif_dict['Exif'][41729] = b'1'
	exif_bytes = piexif.dump(exif_dict)
	piexif.insert(exif_bytes, img_path)

input(f"Done! {unsupported_files} file(s) remain unchanged (file extension not supported). Press enter to exit.")
