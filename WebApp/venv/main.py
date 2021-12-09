from flask import Flask, render_template, request, redirect
import boto3
from werkzeug.datastructures import Headers
import re

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
Bucket = 'camerarecordings-utd1284'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['post'])
def insert():
    if request.method == 'POST':
        track = request.form['track']

        dynamoTable = dynamodb.Table('SmartTrack')

        dynamoTable.put_item(
            Item={
                'track':track
            }
        )
    return render_template('return.html')


#Return template that displays a successful insertion method 
@app.route('/return')
def Return():
    return render_template('return.html')

"""
--------------------------------------------------
"""
#This route renders a template that displays the recordings 
@app.route("/recordingbutton")
def recordings():
    keys = []
    client = boto3.client('s3')
    contents = client.list_objects_v2(Bucket=Bucket, Prefix='converted_videos/')
    for obj in contents['Contents']:
        keys.append(obj['Key'])
    return render_template('recordings.html',contents=keys)


#The <filename> is passing an arguement that is the name of the file
#Clicking on the file on the website will map files' name to our route endpoint hence '/recordings/<filename>'
@app.route('/stream/converted_videos/<filename>', methods=['GET'])
def SendFileToStream(filename):
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': Bucket, 'Key': 'converted_videos/' + filename},
        ExpiresIn=3600
    )
    if request.method == 'GET':
        return redirect(url, code=302)


if __name__ == '__main__':
    app.run(debug=True)