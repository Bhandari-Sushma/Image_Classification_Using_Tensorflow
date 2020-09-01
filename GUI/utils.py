import tensorflow as tf
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image

from GUI.ClassificationApp import *

model = tf.keras.models.load_model('../saved_model/my_model')

# dictionary to label all the CIFAR-10 dataset classes.

classes = {
    0: 'aeroplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = model.predict([image])[0]
    sign = classes[np.argmax(pred)]
    print(sign)


def show_classify_button(file_path):
    classify_b = Button(win, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=10)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((win.winfo_width() / 2.25), (win.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print("Something went wrong!!")
