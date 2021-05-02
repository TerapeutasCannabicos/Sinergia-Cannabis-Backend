from flask import abort, make_response, jsonify

class Filter:
    def getSchema(self, qs, schema_cls, rel=(), **kwargs) -> object:
        fields = qs.get("fields", None)
        embed = qs.get("embed", None)

        if not fields and not embed:
            return schema_cls(exclude=rel, **kwargs)
    
        params = fields.split(",") if fields else None
        relationships = embed.split(",") if embed else None

        if not fields:
            exclude = list(set(rel)-set(relationships))
            return schema_cls(exclude=exclude, **kwargs)

        if not embed:
            relationships = []

        only = params + relationships

        try:
            return schema_cls(only=only, **kwargs)
        except ValueError:
            abort(make_response(
                jsonify({'errors': 'invalid field or embed'}), 400))
                
filters = Filter()