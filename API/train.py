
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os




def training():
	print("[INFO] loading face detector...")
	protoPath = os.path.sep.join("face_detection_model/deploy.prototxt")
	modelPath = os.path.sep.join("face_detection_model/res10_300x300_ssd_iter_140000.caffemodel")
	detector = cv2.dnn.readNetFromCaffe("face_detection_model/deploy.prototxt" , "face_detection_model/res10_300x300_ssd_iter_140000.caffemodel")

	print("[INFO] loading face recognizer...")
	embedder = cv2.dnn.readNetFromTorch("face_detection_model/openface_nn4.small2.v1.t7")

	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images("dataset"))

	# initialize our lists of extracted facial embeddings and
	# corresponding people names
	knownEmbeddings = []
	knownNames = []

	# initialize the total number of faces processed
	total = 0

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		name = imagePath.split(os.path.sep)[-2]

		# load the image, resize it to have a width of 600 pixels (while
		# maintaining the aspect ratio), and then grab the image
		# dimensions
		image = cv2.imread(imagePath)
		if(image is None):
			break
		image = imutils.resize(image, width=600)
		(h, w) = image.shape[:2]

		# construct a blob from the image
		imageBlob = cv2.dnn.blobFromImage(
			cv2.resize(image, (300, 300)), 1.0, (300, 300),
			(104.0, 177.0, 123.0), swapRB=False, crop=False)

		# apply OpenCV's deep learning-based face detector to localize
		# faces in the input image
		detector.setInput(imageBlob)
		detections = detector.forward()

		# ensure at least one face was found
		if len(detections) > 0:

			i = np.argmax(detections[0, 0, :, 2])
			confidence = detections[0, 0, i, 2]


			if confidence > 0.95:
				# compute the (x, y)-coordinates of the bounding box for
				# the face
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# extract the face ROI and grab the ROI dimensions
				face = image[startY:endY, startX:endX]
				cv2.imshow("faces" , face)
				if(cv2.waitKey(1) and 0xFF==27):
					break
				(fH, fW) = face.shape[:2]

				# ensure the face width and height are sufficiently large
				if fW < 20 or fH < 20:
					continue

				# construct a blob for the face ROI, then pass the blob
				# through our face embedding model to obtain the 128-d
				# quantification of the face
				faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
					(96, 96), (0, 0, 0), swapRB=True, crop=False)
				embedder.setInput(faceBlob)
				vec = embedder.forward()

				# add the name of the person + corresponding face
				# embedding to their respective lists
				knownNames.append(name)
				knownEmbeddings.append(vec.flatten())
				total += 1

	print("[INFO] serializing {} encodings...".format(total))
	data = {"embeddings": knownEmbeddings, "names": knownNames}

	with open("output/embeddings.pickle", 'wb') as pickle_file:
	    pickle.dump(data, pickle_file)




	from sklearn.preprocessing import LabelEncoder
	from sklearn.svm import SVC
	import argparse


	print("starting training Process")
	data = pickle.loads(open("output/embeddings.pickle", "rb").read())

	le = LabelEncoder()
	labels = le.fit_transform(data["names"])

	print("[INFO] training model...")
	recognizer = SVC(C=1.0, kernel="linear", probability=True)
	recognizer.fit(data["embeddings"], labels)

	print("Svm trained")

	f = open("output/recognizer.pickle", "wb")
	f.write(pickle.dumps(recognizer))
	f.close()

	f = open("output/le.pickle", "wb")
	f.write(pickle.dumps(le))
	f.close()
