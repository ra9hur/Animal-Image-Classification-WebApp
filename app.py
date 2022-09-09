from flask import Flask, render_template, request

import numpy as np
from collections import Counter
import imghdr

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

#dic = {0: 'Cat', 1: 'Dog'}

model = load_model('AnimalClassification.h5')
class_indices = np.load('class_labels.npy', allow_pickle=True).item()

#model.make_predict_function()

def predict_label(img_path):
	im = image.load_img(img_path, target_size=(240, 240))
	
	# For EfficientNet, rescaling is implemented in the model
	# Applying rescaling here yields wrong results
	#im = image.img_to_array(im)/255.0
	im = image.img_to_array(im)
	
	im = im.reshape(1,240,240,3)
	
	#p = model.predict_classes(i)
	single_pred = np.squeeze(model.predict(im))
	
	results_dict = dict(zip(class_indices.keys(), single_pred))
	top3 = dict(Counter(results_dict).most_common(3))


	for key, value in top3.items():
		top3.update({key: str(round(value*100, 2))+'%'})

	#top3_str = ''
	#for key, value in top3.items():
	#	top3_str += key + ':' + value + '....'

	return top3

# routes
@app.route("/", methods=["GET"])
def main():
	return render_template("index.html")
		   
		   
@app.route("/submit", methods=["POST"])
def get_output():
	img = request.files['my_image']
	
	if not img:
		error = "Try again !! Please choose an image file before submitting"
		return render_template("index.html", error = error)

	valid = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'jpg', 'bmp', 'png', 'webp', 'exr']
	print(imghdr.what(img))
	if imghdr.what(img) not in valid:
		error = "Try again !! Please select a valid image file"
		return render_template("index.html", error = error)

	img_path = "static/" + img.filename
	img.save(img_path)
	
	top3 = predict_label(img_path)
		
	return render_template("index.html", prediction = top3, img_path = img_path)
		   
		   
if __name__ == '__main__':
	# app.debug = True
	# app.run(debug = True)
	app.run()
