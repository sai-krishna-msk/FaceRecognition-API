I have made an API out of a face recognition model, that I have built( you can check about that here [link to fc](https://github.com/sai-krishna-msk/FaceRecognition))

Solving a problem through ml or dl does not complete by building a good model( finding the solution to the problem is of no use if it can't serve the people who have the problem in the first place)
Scaling our model such that it reaches maximum number of people is an important part of solution to the problem, and by maximum number of people I mean multiple platforms such as (android , web etc..) and API are the best way to do it.

So, I have built a flask API out facial recognition model I have built , Which has the following features

1) Face authentication-: You can use the API For face authentication

2) Intruder alert -: You can get an alert,
- a) if there is anyone which your system does not recognize
- b) Anyone which it recognizes but he/she is not suppose be there
- c) You can also set time limits , one which person should be there at what time , if the person is found by your system other then the time allotted it will again send you a alert
*Alert in this case is through an email*

3) Every time a person is found by your system (may or may not be an intruder the data of when they are found, who are they will be logged in the database)

4) You can get a csv file of that logged information( for further analysis(IF you know what I mean :) )

5) and most importantly you can train new people dynamically

Note-:
You can send photos through android , through base64 encoding ( For which I have provided a main activity file )
You can send images through curl, ( for which scripts are provided)

Using the API-:
## Set up-:
### 1) download the repo
### 2) Install required dependencies
### 3) Downloading ngrok is recommended (it helps to use your api with https link (helps with a lot of things))
### 4) Fire up ngrok by entering the following ( make sure to navigate to where ngrok.exe shell is located before you enter the command)
```
ngrok.exe http 80
```
Now you would be getting a https link keep it noted

Now open the server folder and run
```
python app.py
```
on your command prompt (your API should be online) you can access you API at the link which you have copied when you ran ngrok server

### 2) Train some faces-:
- Before we can checkout the features of the API we need to train it with more than one member,
- I have written the code such that the server takes in only pickle files for training the faces, So for that purposes you can navigate to training folder there I have given you instruction (written code on how to create a dataset and convert it into a pickle file which you can upload )
- Now you need to upload that pickle file at the train end point(/train) for example
  https://50d66cff.ngrok.io -> this is your ngrok link then go to  https://50d66cff.ngrok.io/train and upload the file ( if everything is right then it should trine you model)

### 3) Using curl request's for testing
Replace the link with one you have copied earlier

- You can send the image to the server by, make sure there is an image named test.jpg in your current directory
```
curl -F "file=@test.jpg" https://a1ca3ed2.ngrok.io/ec/curl/test
```
where test.jpg would be the name of the file you are sending to the server for testing ( in return you would be getting the name, validity) we use this format for a reason

- You can view the logs by
```
curl   https://a1ca3ed2.ngrok.io/showLogs
```

- You can see weather the person is set as an intruder or not by
```
curl   https://a1ca3ed2.ngrok.io/checkPerson/<name>
```
name of the person in those angular brackets of whom you have trained

- You can make the Person intruder by
```
curl   https://a1ca3ed2.ngrok.io/makeIntruder/<name>
```

- You can reset a person by(from intruder to a valid person)
```
curl   https://a1ca3ed2.ngrok.io/resetPerson/<name>
```


- To get the entire logs in form of a csv file to your email
```
curl   https://a1ca3ed2.ngrok.io/resetPerson/csv
```

- If you wish to change the validation time of a person
```
curl   https://a1ca3ed2.ngrok.io/resetPerson/<time>
```
where time should be formatted as such
time -:
<name>,<initialHour>,<intialMinute>,<finalHour>,<finalMinute>

### Through android:
In android I have provided the code necessary for you to open the front cam, take a photo and send it to the server,
The only thing you need to do is changing the link of where it has to send, regarding which I have provided information in the respective repo (for executing through android )


### Accessing through Web:
- Don't forget to have an image named "test.jpg" in the folder while you are testing

Flask(Web/python):
Well there are a couple of options here you can be using flask as the backend in which case it does not make sense to send a  request to another API , because your model is written anyway in python you could instead plugin your model directly to your backend

But anyways, I have e given code which you could use in between you backend code to access the API

Node( Web/Node):
I have given code which you could plug in your backend code which will help you access the API


If you want to see an example of an API, using this template you can checkout my Face Recognition API for which I have used a similar template, you can test that put [here](https://github.com/sai-krishna-msk/FaceRecognition-API)



## Note-:
To enable email sending features you need to fill in your credentials , open app.py file
and from line 41 to 46 you need to fill in the information (required to send email), We are using smtp (which is not the bets way to send email , instead you could use Gmail API)
so, in most of the cases it wont work with your email(which you use on daily basis, so create a new Gmail account)

## Any Questions/issues/suggestions Please feel free to DM me [Twitter](https://twitter.com/sk_13579)
