import boto3

#file_name is a parameter that holds the name of the file we want to download 
def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"converted_videos/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output




def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)

    return contents

