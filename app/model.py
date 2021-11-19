from app.extensions import db
from flask import abort, make_response, jsonify
from sqlalchemy.exc import IntegrityError

class BaseModel(db.Model):

    __abstract__ = True

    @classmethod
    def create(cls, **data) -> object:
        return cls(**data)

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)

        try: 
            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors': str(err.orig)}), 400))
