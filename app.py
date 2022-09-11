from flask import Flask, render_template, request

import numpy as np
from collections import Counter
import imghdr

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

TF_LITE_MODEL_FILE_NAME = "AnimalClassification.tflite"

interpreter = tf.lite.Interpreter(model_path = TF_LITE_MODEL_FILE_NAME)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.allocate_tensors()

class_indices = np.load('class_labels.npy', allow_pickle=True).item()


def predict_label(img_path):
	im = image.load_img(img_path, target_size=(240, 240))
	
	# For EfficientNet, rescaling is implemented in the model
	# Applying rescaling here yields wrong results
	#im = image.img_to_array(im)/255.0
	im = image.img_to_array(im)
	
	im = im.reshape(1,240,240,3)
	
	interpreter.set_tensor(input_details[0]['index'], im)
	interpreter.invoke()

	single_pred = interpreter.get_tensor(output_details[0]['index'])
	single_pred = np.squeeze(single_pred)
	
	results_dict = dict(zip(class_indices.keys(), single_pred))
	top3 = dict(Counter(results_dict).most_common(3))


	for key, value in top3.items():
		top3.update({key: str(round(value*100, 2))+'%'})

	#top3_str = ''
	#for key, value in top3.items():
	#	top3_str += key + ':' + value + '....'

	return top3


def img_validate(img):

	filename = img.filename
	file_ext = filename.split('.')[-1]
	print(imghdr.what(img), file_ext)
	error = None

	valid = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']
	vdio = ["webm", "mp2", "mpg", "mpeg", "mpe", "mpv", "ogg", "mp4", "m4p", "m4v", "mkv", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"]
	adio = ["mp3", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"]

	if not img:
		error = "Try again !! Please choose an image file before submitting"

	if imghdr.what(img) not in valid:
		error = "Try again !! Please select a valid image file"

	if file_ext in vdio:
		error = "Video format not supported. Please select a valid image file"

	if file_ext in adio:
		error = "Audio format not supported. Please select a valid image file"

	return error

# routes
@app.route("/", methods=["GET"])
def main():
	return render_template("index.html")
		   
		   
@app.route("/submit", methods=["POST"])
def get_output():
	img = request.files['my_image']
	
	error = img_validate(img)

	if error:
		return render_template("index.html", error = error)
	
	else:
		img_path = "static/" + img.filename
		img.save(img_path)
		
		top3 = predict_label(img_path)

		return render_template("index.html", prediction = top3, img_path = img_path)
		   
		   
if __name__ == '__main__':
	# app.debug = True
	app.run(debug = True)
	# app.run(host='0.0.0.0',debug=True)
	# app.run()
