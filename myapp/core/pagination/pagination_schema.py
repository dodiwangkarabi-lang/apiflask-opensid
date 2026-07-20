from apiflask import Schema
from apiflask.fields import Integer
from marshmallow import validate

class BasePaginationSchema(Schema):
    count = Integer()
    page = Integer()
    per_page = Integer()
    pages = Integer()
    next = Integer(allow_none=True)
    previous = Integer(allow_none=True)


class PaginationQuerySchema(Schema):
    page = Integer(
        load_default=1,
        validate=validate.Range(min=1)
    )

    per_page = Integer(
        load_default=10,
        validate=validate.Range(min=1, max=100)
    )