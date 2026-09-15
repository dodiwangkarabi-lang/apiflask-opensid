from apiflask import Schema, fields

class ErrorResponseSchema(Schema):
    message = fields.String(required=True)
    is_success = fields.Boolean(required=True)
    errors = fields.Dict(
        keys=fields.String(),
        values=fields.List(fields.String()),
        required=False,
    )
    
class SuccessResponseSchema(Schema):
    message = fields.String(required=True)
    is_success = fields.Boolean(required=True)
    data = fields.Raw(required=False, allow_none=True)