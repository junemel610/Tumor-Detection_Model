import streamlit as st
import tensorflow as tf
from keras.models import load_model
import numpy as np
from PIL import Image, ImageOps

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('TumorDetection.h5')
  return model
model=load_model()
st.write("""
# Tumor Detection System"""
)
file=st.file_uploader("Choose a photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(128,128)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Glioma','Meningioma',
                 'No Tumor','Pituitary']
    string="PREDICTION : "+class_names[np.argmax(prediction)]
    st.success(string)