import unittest
from unittest.mock import patch, MagicMock
from utils import get_key_from_s3_uri, get_bucket_name_from_s3_uri, download_image_from_s3, get_filename_with_extension_from_s3_uri

class TestUtils(unittest.TestCase):

    def test_get_key_from_s3_uri(self):
        s3_uri_with_key = 's3://bucket_name/path/to/image.jpg'
        expected_key = 'path/to/image.jpg'
        self.assertEqual(get_key_from_s3_uri(s3_uri_with_key), expected_key)

        s3_uri_without_key = 's3://bucket_name/'
        expected_key = ''
        self.assertEqual(get_key_from_s3_uri(s3_uri_without_key), expected_key)

        s3_uri_special_characters = 's3://bucket_name/path/to/image with spaces.jpg'
        expected_key = 'path/to/image with spaces.jpg'
        self.assertEqual(get_key_from_s3_uri(s3_uri_special_characters), expected_key)


    def test_get_bucket_name_from_s3_uri(self):
        s3_uri = 's3://bucket_name/path/to/image.jpg'
        expected_bucket_name = 'bucket_name'
        self.assertEqual(get_bucket_name_from_s3_uri(s3_uri), expected_bucket_name)

        s3_uri_no_bucket = 's3://'
        expected_bucket_name = ''
        self.assertEqual(get_bucket_name_from_s3_uri(s3_uri_no_bucket), expected_bucket_name)

        s3_uri_special_characters = 's3://bucket-name/path/to/image.jpg'
        expected_bucket_name = 'bucket-name'
        self.assertEqual(get_bucket_name_from_s3_uri(s3_uri_special_characters), expected_bucket_name)


    def test_get_filename_from_s3_uri(self):
        s3_valid_uri_with_filename_extension = "s3://my_bucket/path/to/file.txt"
        expected_filename = "file.txt"
        self.assertEqual(get_filename_with_extension_from_s3_uri(s3_valid_uri_with_filename_extension), expected_filename)

        s3_valid_uri_without_filename_extension = "s3://my_bucket/path/to/file"
        expected_filename = "file"
        self.assertEqual(get_filename_with_extension_from_s3_uri(s3_valid_uri_without_filename_extension), expected_filename)

        s3_invalid_uri = "invalid_uri_format"
        self.assertIsNone(get_filename_with_extension_from_s3_uri(s3_invalid_uri))


    @patch('utils.boto3.client')
    def test_download_image_success(self, mock_boto3_client):
        mock_s3_client = MagicMock()
        mock_boto3_client.return_value = mock_s3_client
        mock_s3_client.download_file.return_value = None
        bucket_name = 'test_bucket'
        key = 'path/to/image.jpg'
        local_file_path = '/tmp/local_image.jpg'
        self.assertTrue(download_image_from_s3(bucket_name, key, local_file_path))
        mock_s3_client.download_file.assert_called_once_with(bucket_name, key, local_file_path)


    @patch('utils.boto3.client')
    def test_download_image_failure(self, mock_boto3_client):
        mock_s3_client = MagicMock()
        mock_boto3_client.return_value = mock_s3_client
        mock_s3_client.download_file.side_effect = Exception('Download failed')
        bucket_name = 'test_bucket'
        key = 'path/to/image.jpg'
        local_file_path = '/tmp/local_image.jpg'
        self.assertFalse(download_image_from_s3(bucket_name, key, local_file_path))
        mock_s3_client.download_file.assert_called_once_with(bucket_name, key, local_file_path)

if __name__ == '__main__':
    unittest.main()
