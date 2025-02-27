import boto3
import requests

# Set variables
bucket_name = "ds2002-ghn9zh"  # Replace with your bucket name
file_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
file_name = "downloaded_cat.jpg"
expiration_time = 604800  # 7 days (in seconds)

# Download the file
print(f"Downloading file from {file_url}...")
response = requests.get(file_url)
with open(file_name, "wb") as file:
    file.write(response.content)
print(f"Saved as {file_name}")

# Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Upload file to S3
print("Uploading file to S3...")
s3.upload_file(file_name, bucket_name, file_name)
print(f"Uploaded {file_name} to s3://{bucket_name}/{file_name}")

# Generate presigned URL
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': file_name},
    ExpiresIn=expiration_time
)

print(f"Presigned URL (expires in 7 days): {presigned_url}")
