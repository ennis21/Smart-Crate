from __future__ import print_function
import de2120_barcode_scanner
import time
import sys
import boto3
from botocore.exceptions import ClientError
import json
from boto3.dynamodb.conditions import Key
from pprint import pprint
from sendemail import *

def run_example():
    print("\nSparkFun DE2120 Barcode Scanner Breakout Example 1")
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()

    if my_scanner.begin() == False:
        print("\nThe Barcode Scanner module isn't connected correctly to the system. Please check wiring", \
            file=sys.stderr)
        return
    print("\nScanner ready!")

    scan_buffer = ""
    
    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            print("\nCode found: " + str(scan_buffer))
            trackingnumber = str(scan_buffer)  

            
                 #Convert buffer value to a string 
            trackinginfo = get_tracking(trackingnumber)            #Validate if the tracking number is found in dynamodb

            scan_buffer = ""                        #Empty the string and scan again 
        #time.sleep(0.02)

def get_tracking(trackingnumber):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SmartTrack')
    
    '''For the AWS SNS function to notify the user a package is being delivered'''
    topic_arn='arn:aws:sns:us-west-1:862742272774:Delivery-Alert'
    door_open = 1
        
        #Option 1
        

    print("This is the tracking number " + trackingnumber)
    response = table.scan()
    print(response)

    Items = response['Items']


    for item in Items: 
        print(item['track'])
        print(trackingnumber)
        track = item['track']

        trackingnumber =int(trackingnumber)
        track=int(track)

        if trackingnumber == track:
            print("Correct, notifying user of package being delivered")
            publishmessage(topic_arn, door_open)
            
        else:
            print("Wrong")
    
if __name__ == '__main__':
    try:
        run_example()
    except(KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
