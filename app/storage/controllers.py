import uuid
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.storage.storage import storage
from app.config import StorageConfig


class MediaStorage(MethodView):         #/files/put_url
    
    decorators = [jwt_required()]
    def get(self):

        file_format = request.args.get('file_format')

        if not file_format or file_format not in StorageConfig.AWS_ALLOWED_FORMATS:
            return {'error': 'File format must be one of: '+', '.join(StorageConfig.AWS_ALLOWED_FORMATS) + '.'}, 401

        file_name = f'{uuid.uuid4().hex}.{file_format}'

        url = storage.put_url(file_key=file_name)

        return {'file_url': url, 'file_name': file_name}, 200