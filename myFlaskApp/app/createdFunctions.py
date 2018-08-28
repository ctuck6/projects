import string

def id_generator(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for i in range(size))

def savePicture(form_picture):
	random_hex = id_generator()
	fileName, fileExtension = os.path.splitext(form_picture.filename)
	pictureFilename = random_hex + fileExtension
	picturePath = os.path.join(app.root_path, "static/profilePics", pictureFilename)
	outputSize = (125, 125)
	resizedImage = Image.open(form_picture)
	resizedImage.thumbnail(outputSize)
	resizedImage.save(picturePath)
	if current_user.image_file != 'default.jpg':
		oldPicture = os.path.join(app.root_path, "static/profilePics", current_user.image_file)
		os.remove(oldPicture)
	return pictureFilename