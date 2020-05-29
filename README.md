# Contents

- **Introduction**

- **Features**

- **Using the code**

# Introduction



Building a Machine Learning or Deep Learning Model in and on itself does not serve a purpose unless a system serves the model(pun intended)

Making the model accessible a key component of problem as the following is the project fulfilling it  



# Features

I wrapped the facial Recognition model trained into a Web API using Flask, If you want to see/use only the Face Recognition part you can find it [Here](https://github.com/sai-krishna-msk/FaceRecognition)

equipped with the following features 

1) Face authentication-: You can use the API For face authentication

2) Intruder alert -: You can get an alert,

- a) if there is anyone which your system does not recognize
- b) Anyone which it recognizes but he/she is not suppose be there
- c) You can also set time limits , one which person should be there at what time , if the person is found by your system other then the time allotted it will again send you a alert
  *Alert in this case is through an email*

3) Every time a person is found by the system (may or may not be an intruder the data of when they are found, who are they will be logged in the database)

4) You can get a csv file of that logged information( for further analysis(IF you know what I mean :) )

5) Most importantly you can train new people online without taking down the system

**Images can be sent through Android making use of base64 encoding ( For which I have provided a main activity file )
You can send images through curl, ( for which scripts are provided)**



# Using the Code

1) **Download the repo**

2) **Install required dependencies**

```bash
pip install -r requirements.txt
```

3) **Downloading ngrok is recommended (it gives you a temporary access to your service with a https)**

4) **Fire up ngrok by entering the following ( make sure to navigate to where ngrok.exe shell is located before you enter the command)**

```bash
ngrok.exe http 80
```

- You can notice a https url note it down

5) Open the server folder and run

```bash
python app.py
```

on your command prompt (your API should be online) you can access you API at the link which has been noted above

###  Training Faces

- Before we go through other features of the API we need to train it with more than one individual

- System Accepts training images in pickled format for which you have to navigate to [training directory](https://github.com/sai-krishna-msk/FaceRecognition-API/tree/master/training), necessary information to create dataset has been provided in that directory 

- Now you need to upload that pickle file at the train end point(/train) for example
  https://50d66cff.ngrok.io -> this is your ngrok link then go to  https://50d66cff.ngrok.io/train and upload the file ( if everything is right then it should train your model)

### Using curl request's for testing

You can send the image to the server by doing following(make sure there is an image named test.jpg in your current working directory )

```
curl -F "file=@test.jpg" https://a1ca3ed2.ngrok.io/ec/curl/test
```

where test.jpg would be the name of the image being sent to the server for testing (in return you would be getting the name, validity)

- Logs can be accessed using the following url

```bash
curl   https://a1ca3ed2.ngrok.io/showLogs
```

- To verify weather the person is set as an intruder or not can be done using 

```bash
curl   https://a1ca3ed2.ngrok.io/checkPerson/<name>
```

- To make an individual as intruder 

```bash
curl   https://a1ca3ed2.ngrok.io/makeIntruder/<name>
```

- To set a person who is an intruder to authorized individual

```bash
curl   https://a1ca3ed2.ngrok.io/resetPerson/<name>
```

- To get the entire logs in form of a csv file to your email

```bash
curl   https://a1ca3ed2.ngrok.io/resetPerson/csv
```

- If you wish to change time [training](https://github.com/sai-krishna-msk/FaceRecognition-API/tree/master/training) between which an individual should be considered authorized  

```bash
curl   https://a1ca3ed2.ngrok.io/resetPerson/<time>
```

where time should be formatted as such
time -:
<name>,<initialHour>,<intialMinute>,<finalHour>,<finalMinute>

## Making use of API through Android devices

In [android](https://github.com/sai-krishna-msk/FaceRecognition-API/tree/master/android) directory necessary code is provided for you to open the front camera, take a photo and send it to the server,
The only thing you need to do is changing the link of where it has to send, regarding which I have provided information in the respective repo (for executing through android )

## Accessing through Web:

- While testing this feature make sure you have file named test.jpg in the current directory

### Flask(Web/python)

To make use of this API in your own Flask app, Navigate to [Flask Directory](https://github.com/sai-krishna-msk/FaceRecognition-API/tree/master/Web/Flask) where necessary instructions have been provided 

### Node( Web/Node)

To make use of this api in your node applications navigate to [Node Directory](https://github.com/sai-krishna-msk/FaceRecognition-API/tree/master/Web/Node) where necessary instructions are provided 

## Note

To enable sending an email you need to fill in your credentials, open *app.py* file
and from line 41 to 46 you need to fill in the information (required to send email), We are using smtp (which is not a standard way automate the process of sending a mail, instead you could use Gmail API)
so, in most of the cases it wont work with your current email(If it is then your account not so secure) So create a new Gmail account if you feel it's worth it :)
