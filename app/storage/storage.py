from app.config import StorageConfig
import boto3

class StorageServices:

    session = boto3.session.Session()
    client = session.client('s3',
                            region_name=StorageConfig.AWS_REGION,
                            endpoint_url=StorageConfig.AWS_BUCKET_ENDPOINT,
                            aws_access_key_id=StorageConfig.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=StorageConfig.AWS_SECRET_ACCESS_KEY)


    def put_url(self, file_key)-> str:

        return self.client.generate_presigned_url(
                                    ClientMethod='put_object',
                                    Params={
                                        'Bucket': StorageConfig.AWS_BUCKET_NAME,
                                        'Key': f'{StorageConfig.AWS_PROJECT_NAME}/{file_key}'},
                                    ExpiresIn=300)       


    def get_url(self, file_key)-> str:

        return self.client.generate_presigned_url(
                                    ClientMethod='get_object',
                                    Params={
                                        'Bucket': StorageConfig.AWS_BUCKET_NAME,
                                        'Key': f'{StorageConfig.AWS_PROJECT_NAME}/{file_key}'},
                                    ExpiresIn=300)

    
    def delete_object(self, file_key)-> None:
        self.client.delete_object(Bucket = StorageConfig.AWS_BUCKET_NAME,
                                  Key=f'{StorageConfig.AWS_PROJECT_NAME}/{file_key}')

    
    def delete_objects(self, keys) -> None:
        self.client.delete_objects(Bucket = StorageConfig.AWS_BUCKET_NAME,
                                   Delete={'Objects': keys,
                                           'Quiet': True})


storage = StorageServices()

'''
from os import environ
import boto3

class Storage:
    project_name = 'swcannabis'
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url='https://nyc3.digitaloceanspaces.com',
                            aws_access_key_id=environ.get('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=environ.get('AWS_SECRET_ACCESS_KEY'))

    def put_url(self, file_key) -> str:

        return self.client.generate_presigned_url(ClientMethod='put_object',
                                                  Params={'Bucket': 'storage-fluxo',
                                                          'Key': f'{self.project_name}/{file_key}'},
                                                  ExpiresIn=300)

    def get_url(self, file_key):

        return self.client.generate_presigned_url(ClientMethod='get_object',
                                                  Params={'Bucket': 'storage-fluxo',
                                                          'Key': f'{self.project_name}/{file_key}'},
                                                  ExpiresIn=300)

    def delete_object(self, file_key):
        self.client.delete_object(Bucket='storage-fluxo',
                                  Key=f'{self.project_name}/{file_key}')


storage = Storage()
'''