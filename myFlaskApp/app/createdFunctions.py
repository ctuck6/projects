from app import app
import string, random, os
from PIL import Image
from flask_login import current_user

def id_generator(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for i in range(size))

def savePicture(form_picture):
	random_hex = id_generator()
	fileName, fileExtension = os.path.splitext(form_picture.filename)

	if fileName == "default":
		pictureFilename = fileName + fileExtension
	else:
		pictureFilename = random_hex + fileExtension
	
	picturePath = os.path.join(app.root_path, 'static/profilePics', pictureFilename)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picturePath)

	if "default" not in current_user.image_file:
		oldPicture = os.path.join(app.root_path, "static/profilePics", current_user.image_file)
		os.remove(oldPicture)

	return pictureFilename
