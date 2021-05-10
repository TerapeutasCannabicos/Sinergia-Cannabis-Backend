from flask import Blueprint
from app.storage.controllers import MediaStorage

storage_api = Blueprint('storage_api', __name__)

storage_api.add_url_rule('/files/<file_format>',
                        view_func=MediaStorage.as_view('files'))