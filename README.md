# Animal-Image-Classification-WebApp

----------
**1. Problem Definition**
-------------

A simple website where users can post an image of an animal and get the name as result. If the object is not an animal, provide a feedback as “not an animal”. Also, the WebApp should be deployed on a server so that it could be tested from anywhere.


----------
**2. Dataset Selection**
-------------

Imagenet dataset has 1000 classes and predominantly covers around 400 animal categories. However, this dataset fails to detect a human. Hence, just a pre-trained model using Imagenet is not sufficient and a model should be trained using a custom dataset.

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
**5. Deployment**
-------------

Here is a good reference [link](https://www.freecodecamp.org/news/deploy-your-machine-learning-models-for-free/) that discusses a list of options for someone looking out for Platform as a Service(PaaS). 'pythonanywhere' and 'Heroku' were found to be suitable and to be explored further.

pythonanywhere by Anaconda
- Deployment was fairly simple. However, once an image was selected for prediction, there was no response for a long time and eventually timed-out after 5 miutes. There were no errors in logs. From the [forums](https://www.pythonanywhere.com/forums/topic/31620/), found that webapp deployments with tensorflow has not been fairly successful.
- Tried to install tensorflow-cpu in a virtual environment. The file size is hardly 172 MB. Installation failed with the error that disk quota of 512 MB exceeded. The reason could be that the installation process consumed disk quota up to 512MB before it failed.
- Converted "model.h5" file to tensorflow lite format ("model.tflite"), the image predictions were successfully retrieved on the web page.
----------
**5. Further Improvements**
-------------
- To try out the performance and response of the webapp with a quantized model.
- To deploy in Heroku environment.