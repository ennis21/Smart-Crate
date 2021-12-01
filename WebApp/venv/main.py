import boto3
from flask import Flask, render_template, request, send_file

from s3functions import download_file, list_files

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
    contents = list_files(Bucket)
    return render_template('recordings.html',contents=contents)


#The <filename> is passing an arguement that is the name of the file
#Clicking on the file on the website will map files' name to our route endpoint hence '/recordings/<filename>'
@app.route('/stream/converted_videos/<filename>', methods=['GET'])
def stream(filename):
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': Bucket, 'Key': 'converted_videos/' + filename},
        ExpiresIn=3600
    )
    if request.method == 'GET':
        return url


# @app.route('/video_feed')
# def video_feed():
#     return Response(,
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
    


if __name__ == '__main__':
    app.run(debug=True)
