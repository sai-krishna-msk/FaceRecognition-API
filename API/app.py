from flask import Flask, request, Response , send_file
import jsonpickle
import numpy as np
import cv2
import os
import base64
from flask import jsonify
from flask import json
import datetime
import json


from mainDatabase import makingPersonValid as mp
from mainDatabase import gettingSpesefics as gs
from mainDatabase import settingTimeLimit as st
from mainDatabase import makingIntruder as mi
from mainDatabase import settingTimeLimit as stl



from model.mod import test
from flask import render_template
import bs4
from log import add
from log import writeAsCsv as wcsv
from log import selectAll as logsAll
from mainDatabase import addPerson as ap
from sending_mail import send_mail as sm
from sending_mail import send_text_mail as st
from flask_uploads import UploadSet, configure_uploads, ALL
from train import training
import pickle


app=Flask(__name__)
photos = UploadSet('photos', ALL)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/'
configure_uploads(app, photos)

sender_email="enter through which eail you want to send"
reciever_email = "enter to which user you want to send"
subject = "testing attachment"
messege ="This is an intruder alert"
sender_user_name ="enter you userame here"
sender_password = "enter you passowrd here"



@app.route("/ec/curl/test" , methods=["POST"])
def model():
    path = "curlImages/test.jpg"
    filestr = request.files['file'].read()
    npimg = np.fromstring(filestr, np.uint8)
    img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
    cv2.imwrite(path ,img )

    response =test(path)

    print(response)
    if(response==None):
        try:
            sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
        except:
            print("email courd not be sent")
        os.remove(path)
        return "Intruder"

    else:
        result = gs(response)
        validity = result[0][2]
        if(validity==0):
            add(response+","+"valid")
            os.remove(path)
            return response+","+"valid"
        else:
            try:
                sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
            except:
                print("Emial could not be sent")

            add(response+","+"invalid")
            os.remove(path)
            return response+","+"invalid"





@app.route('/ec/android/test', methods=['POST'])
def android_test():
    path = "androidImages/test.jpg"
    data =  request.stream.read()
    image = data
    image =  base64.b64decode(image)

    with open(path , 'wb') as f:
        f.write(image)
    response =test(path)

    print(response)
    if(response==None):
        try:

            sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
        except:
            print("Email could not be sent ")
        os.remove(path)
        return "Intruder"
    else:

        result = gs(response)

        validity = result[0][2]
        if(validity==0):
            add(response+","+"valid")
            os.remove(path)
            return response+","+"valid"
        else:
            try:
                sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )

            except:
                print("Email could not be sent")
            add(response+","+"invalid")
            os.remove(path)
            return response+","+"invalid"



@app.route('/ec/node/test' , methods =["POST"])
def node():
    path = 'nodeImages/images.jpg'
    data =  request.get_json()
    data = data['key']
    print(type(data))
    data = data.split(",")[1]
    data = bytes(data , 'utf-8')
    print(type(data))
    image =  base64.b64decode(data)
    with open(path , 'wb') as f:
        f.write(image)
    response =test(path)

    print(response)
    if(response==None):
        try:
            sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
        except:
            print("email courd not be sent")
        os.remove(path)
        return "Intruder"

    else:
        result = gs(response)
        validity = result[0][2]
        if(validity==0):
            add(response+","+"valid")
            os.remove(path)
            return response+","+"valid"
        else:
            try:
                sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
            except:
                print("Emial could not be sent")

            add(response+","+"invalid")
            os.remove(path)
            return response+","+"invalid"




@app.route('/ec/python/test' , methods =["POST"])
def python():
    response=""
    path = 'pythonImages/images.jpg'
    data =  request.stream.read()
    image =  base64.b64decode(data)
    with open(path , 'wb') as f:
        f.write(image)
    response =test(path)

    print(response)
    if(response==None):
        try:
            sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
        except:
            print("email courd not be sent")
        os.remove(path)
        return "Intruder"

    else:
        result = gs(response)
        validity = result[0][2]
        if(validity==0):
            add(response+","+"valid")
            os.remove(path)
            return response+","+"valid"
        else:
            try:
                sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )
            except:
                print("Emial could not be sent")

            add(response+","+"invalid")
            os.remove(path)
            return response+","+"invalid"




'''For making a person valid'''
@app.route("/resetPerson/<name>")
def reset(name):

    mp(name)
    return (name+" Person Sucessfuly made valid")



'''checking if the perosn is valid '''
@app.route("/checkPerson/<name>")
def checkPerson(name):
    result = gs(name)

    validity = result[0][2]
    if(validity==0):
        return "Yes the person is valid"
    else:
        return "The perosn is invalid"




'''Making a person Intruder '''
@app.route("/makeIntruder/<name>")
def makeintruder(name):


    mi(name)
    return ("Person Sucessfuly made Intruder !")




'''Returning the csv file '''
@app.route('/csv')
def getting():
    wcsv()
    try:
        sm(sender_email , reciever_email ,subject  ,messege , path , "smtp.gmail.com" ,587 , sender_user_name ,sender_password )

    except:
        print("Email could not be sent")


    return send_file('log.csv', attachment_filename='log.csv')


'''printing out all the logs '''
@app.route('/showLogs')
def showLogs():
    result = logsAll()
    return result



'''  train images '''
@app.route("/train" , methods=['GET' , 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:

        filename = photos.save(request.files['photo'])
        print("file has been saved")
        pickle_in = open("uploads/training_data.pickle","rb")
        data= pickle.load(pickle_in)
        print("Daya take")
        i=0
        for image , imgClass in data:

            if not os.path.exists("dataset/"+imgClass):

                os.makedirs("dataset/"+imgClass)
                ap(imgClass)

            path="dataset/"+str(imgClass)+"/"+str(i)+".jpg"
            print(path)
            cv2.imwrite(path , image)
            i=i+1
        training()
        cv2.destroyAllWindows()

    return render_template('upload.html')




'''  It changes the validation time of  person '''
@app.route("/changeTime/<details>" , methods=['GET'])
def changeTime(details):
    info  = details.split(",")
    print(info)
    name = info[0]
    initialHour = info[1]
    initialMinute = info[2]
    finalHour = info[3]
    finalMinute = info[4]
    print(name , initialHour , initialMinute , finalHour , finalMinute)


    #initialHour, intialMinute, finalHour, finalMinute, name = getTime(input)
    stl(initialHour, initialMinute , finalHour, finalMinute, name)


    return "sucessfuy changed the timmings of "+name+" to "+str(initialHour+" "+initialMinute+" "+finalHour+" "+finalMinute)




app.run(host='0.0.0.0', port=80 , debug=True)
#app.run(debug=True)
