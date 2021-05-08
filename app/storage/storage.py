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