import keras ,cv2
v = cv2.VideoCapture(0)
m = keras.model.load_model('pra_suk.h5')
ret , fram = v.read()
print(m.predict(fram.reshape(1,224,224,3)))
v.release()