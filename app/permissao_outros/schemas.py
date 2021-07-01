from app.extensions import ma 

class PermissaoSchema(ma.SQLAlchemySchema):
    
    id = ma.Integer(dump_only=True)

    outros = ma.Nested('OutrosSchema', many=True, dump_only=True)