from app.extensions import ma


class LoginSchema(ma.Schema):

    email = ma.Email(required=True)
    password = ma.String(load_only=True, required=True)