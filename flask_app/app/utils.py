import boto3, os


def get_key_from_s3_uri(s3_uri):
    if s3_uri.startswith('s3://'):
        s3_uri = s3_uri[len('s3://'):]
    parts = s3_uri.split('/', 1)
    return parts[1] if len(parts) > 1 else ''


def get_bucket_name_from_s3_uri(s3_uri):
    if s3_uri.startswith('s3://'):
        s3_uri = s3_uri[len('s3://'):]
    parts = s3_uri.split('/', 1)
    return parts[0]


def get_filename_with_extension_from_s3_uri(s3_uri):
    bucket_and_key = s3_uri.split("//")[-1].split("/", 1)
    if len(bucket_and_key) == 2:
        _, key = bucket_and_key
        filename_with_extension = os.path.basename(key)
        return filename_with_extension
    else:
        print("Invalid S3 URI format")
        return None


def download_image_from_s3(bucket_name, key, local_file_path):
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, key, local_file_path)
        print(f"Image downloaded successfully to {local_file_path}")
        return True
    except Exception as e:
        print(f"Error downloading image from S3: {e}")
        return False
