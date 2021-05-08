import uuid
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.storage import storage

class MediaStorage(MethodView):    
    decorators = [jwt_required]

    def get(self, file_format):
        file_name = f'{uuid.uuid4().hex}.{file_format}'
        url = storage.put_url(file_key=file_name)
        return {'media_url': url, 'file_name': file_name}, 200