from tkinter import *
import tensorflow as tf
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
<<<<<<< HEAD

=======
>>>>>>> 289e990... V1.0
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

<<<<<<< HEAD
# initialise GUI

win = Tk()
win.geometry('800x800')
win.title('Image Classification CIFAR10')
win.configure()
win.iconbitmap('photos/photoIcon.ico')
label = Label(win, foreground='blue', font=('times new roman', 20, 'bold', 'italic'))
sign_image = Label(win)


=======

# initialise GUI

win = Tk()
win.geometry('800x600')
win.title('Image Classification CIFAR10')
win.configure(background='#CDCDCD')
win.iconbitmap('photos/photoIcon.ico')
label = Label(win, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(win)




>>>>>>> 289e990... V1.0
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
<<<<<<< HEAD
    try:
        pred = model.predict([image])[0]
        sign = classes[np.argmax(pred)]
        print(sign)
        label.configure(text=sign)
    except:
        error = "something went wrong!! May be wrong image format."
        label.config(text=error)


def show_classify_button(file_path):
    classify_b = Button(win, text="Classify the Image", command=lambda: classify(file_path), padx=10, pady=10)
    classify_b.configure(font=('arial', 10, 'italic', 'bold'))
=======
    pred = model.predict([image])[0]
    sign = classes[np.argmax(pred)]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(win, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=10)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
>>>>>>> 289e990... V1.0
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
<<<<<<< HEAD
        Exception("While Uploading the image..something went wrong!!")


heading = Label(win, text="Image Classification CIFAR10", pady=20, font=('arial', 20, 'bold'))
heading.configure()
heading.pack(side=TOP)

upload = Button(win, text="Upload an image", command=upload_image, padx=10, pady=10)
upload.configure(font=('arial', 10, 'italic', 'bold'))
upload.pack(side=TOP, pady=50)
sign_image.pack(side=TOP, expand=True)
label.pack(side=TOP, expand=True)

win.mainloop()

=======
        print("Something went wrong!!")





upload = Button(win, text="Upload an image", command=upload_image, padx=10, pady=10)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)

sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(win, text="Image Classification CIFAR10", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()


win.mainloop()
>>>>>>> 289e990... V1.0
