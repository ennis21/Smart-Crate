from __future__ import print_function
import de2120_barcode_scanner
import time
import sys
import boto3
from botocore.exceptions import ClientError
import json
from boto3.dynamodb.conditions import Key
from pprint import pprint

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
    
            '''
            if trackinginfo:
                print("Get traccking works")
                pprint(trackinginfo, sort_dicts=False)
                '''

            scan_buffer = ""                        #Empty the string and scan again 
        #time.sleep(0.02)

    


def get_tracking(trackingnumber):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SmartTrack')
        
        #Option 1
        

    print("This is the tracking number " + trackingnumber)
    #response = table.get_item(Key={'track': trackingnumber})
    #response = table.query(KeyConditionExpression=Key('track').eq('trackingnumber'))
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
            print("Correct")
        else:
            print("Wrong")


        '''
    for item in Items:
        if trackingnumber == Items:
            print("correct")
        print("wrong")
        '''




    '''
    ####Tracking Validation needs adjusting####
    if trackingnumber in response:
        print("Tracking Number Found") 
    else:  
        print("Tracking Number Not Found")
    '''

    '''
    #Option2
    response = dynamodb.query(
        KeyConditionExpression=Key('track').eq(trackingnumber)
    )

    items = response['Items']

    for item in items:
        print(item)

    '''

    
    

    
if __name__ == '__main__':
    try:
        run_example()
    except(KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)