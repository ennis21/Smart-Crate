import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import boto3 
from botocore.exceptions import NoCredentialsError


#Client creating a session to use AWS S3 functionalities


#Create a boto3 Resource
s3 = boto3.resource('s3')



#Function that uploads the file to the s3 bucket
def upload_to_aws(local_file, bucket):
    
    #Create the s3 client
    s3 = boto3.client('s3')


    #Go through and upload all the files in the directory with exception handling
    
    if not file.startswith('~'):
            try:
                
                 s3.upload_file(os.path.join(local_file, file), bucket, file)
                 print("Upload Successful")
                 return True
            except FileNotFoundError:
                print("The file was not found")
                return False
            except NoCredentialsError:
                print("Credentials not available")
                return False



#Main function
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


    '''
    Path points to the directory we want to watch  
    Function below handles the camera file path being updated
    Define the path for the recordings 
    '''
    path = "C:/Users/Ennis/Desktop/Fall 2021 Classes/Senior Design Project 2/Smart-Crate/Video Recordings"
    bucket = 'camerarecordings-utd1284'
    

    #Initialize the event handler 
    event_handler = LoggingEventHandler()

    #Initialize the observer 
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)


    #Start observing the given directory for changes
    observer.start()
    try:
        while True:
            '''
            Call function to upload theh files to s3 bucket
            Bucket Name: Name of the s3 bucket is camerarecordings-utd1284
            local_file: The path for the files we want to upload 
            s3_file_name: the name of our file when its sent to the bucket
            '''
            '''INFINITE LOOP'''
            '''USE THE CAMERA TRIGGER TO UPLOAD TO THE S3 BUCKET'''
            
            for file in os.listdir(path):
                 uploaded = upload_to_aws(path, bucket)
            
            #Set up the sleep time when not observing the folder 
            time.sleep(5)
    finally:
        observer.stop()
        observer.join()





    




