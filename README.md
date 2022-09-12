# Animal-Image-Classification-WebApp

----------
**1. Problem Definition**
-------------

A simple website where users can post an image of an animal and get the name as result. If the object is not an animal, provide a feedback as “not an animal”. Also, the WebApp should be deployed on a server so that it could be tested from anywhere.


----------
**2. Dataset Selection**
-------------

Imagenet dataset has 1000 classes and predominantly covers around 400 animal categories. However, this dataset fails to detect a human. Hence, just a pre-trained model using Imagenet is not sufficient and a model should be trained using custom dataset.

The dataset used here is [Animal Image Dataset (90 Different Animals)](https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals) from Kaggle.
This is a balanced dataset consisting of 5400 images in 90 different classes. This again does not include human images. [Human Detection Dataset](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset) from Kaggle helped to fill this gap. This dataset includes 559 human and 362 non-human images.

----------
**3. Model**
-------------

The comparison table at the [link](https://keras.io/api/applications/) provides various available Keras models with a good set of performance parameters - 
Top-1 Accuracy, Top-5 Accuracy,	Parameters,	Depth,	Time (ms) per inference step (CPU), Time (ms) per inference step (GPU), Size (MB). This helped to narrow down and identify the ones that could be suitable.

MobileNetV2, InceptionV3, EfficientB1, EfficientB4 were trained with the custom dataset. EfficientB1 was eventually found to be suitable for this problem.

----------
**4. WebApp**
-------------

The WebApp was developed using Flask framework. The user interface is kept simple so that the focus remains more on training the model and deployment.

![User Interface](https://user-images.githubusercontent.com/17127066/189523650-68fea882-4870-4d63-a800-82cc13f10751.jpg)

----------
**5. Model Evaluation**
-------------

![image](https://user-images.githubusercontent.com/17127066/189634119-dd50f870-b5d0-40cb-8fa3-66b175b98550.png)

![image(1)](https://user-images.githubusercontent.com/17127066/189634107-509cd0d6-22c2-4a8c-9e82-d4b48914a56e.png)


In the below image, it recognizes Former President Obama. There is also an eagle on the flag behind Obama. That is its second prediction.
![image(2)](https://user-images.githubusercontent.com/17127066/189634097-6141758c-60fa-4ba8-aecb-3df36f185c22.png)

Batman like images were not part of the training set and the model is confused.
Its third prediction is interesting - snake because of scales on the body.
![image(3)](https://user-images.githubusercontent.com/17127066/189634090-30210827-1a52-4358-81c7-f0f15d9fa76c.png)

I am sure cartoons were not part of the training set. But still it recognizes this as human.
![image(4)](https://user-images.githubusercontent.com/17127066/189634080-4e215816-b2f9-4cee-8f87-4ad7446d3592.png)

Model has not seen a baby with glasses, it gets confused.
![image(5)](https://user-images.githubusercontent.com/17127066/189634067-0c26b71a-98ab-4805-a0fa-2f307304dd00.png)

There were no images of humans with colors on their faces in the training set. 
![image(6)](https://user-images.githubusercontent.com/17127066/189634049-6edef97e-286d-48d5-a21a-2a17e405ac80.png)

![image(7)](https://user-images.githubusercontent.com/17127066/189634038-376d7e21-7cd7-40d5-a4db-dbc4c8960d97.png)

It predicts snakes because of snake-like marks on the pillars. The prediction should actually be  "not an animal".
The correction should be to include more such images and train the model saying, it is "not an animal".
![image(8)](https://user-images.githubusercontent.com/17127066/189634022-07b82bbd-5f6b-43f9-959a-4ef338eaf97d.png)

It recognizes shadow of the human. As a third prediction, it also feels, it is "not an animal".
![image(9)](https://user-images.githubusercontent.com/17127066/189634004-6c9e141a-87a2-4567-8ce2-169a19d247dd.png)



----------
**6. Deployment**
-------------

Here is a good reference [link](https://www.freecodecamp.org/news/deploy-your-machine-learning-models-for-free/) that discusses a list of options for someone looking out for Platform as a Service(PaaS). 'pythonanywhere' and 'Heroku' were found to be suitable and to be explored further.

pythonanywhere by Anaconda
- Deployment was fairly simple. However, once an image was selected for prediction, there was no response for a long time and eventually timed-out after 5 miutes. There were no errors in logs. From the [forums](https://www.pythonanywhere.com/forums/topic/31620/), found that webapp deployments with tensorflow has not been fairly successful.
- Tried to install tensorflow-cpu in a virtual environment. The file size is hardly 172 MB. Installation failed with the error that disk quota of 512 MB exceeded. The reason could be that the installation process consumed disk quota up to 512MB before it failed.
- Converted "model.h5" file to tensorflow lite format ("model.tflite"), the image predictions were successfully retrieved on the web page.
- Optimized/quantized also works as expcted without major surprises. 

----------
**7. Further Improvements**
-------------
- To train the model with new images to overcome some of the weird results as observed in "model Evaluation" section.
- To deploy in Heroku environment.