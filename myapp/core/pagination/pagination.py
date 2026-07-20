from apiflask import Schema
from typing import Any

def paginate(query, schema: Schema, params: dict) -> dict[str, Any]:
    """Paginate a SQLAlchemy query and serialize the results.

    This helper executes pagination on the given SQLAlchemy query using the
    provided pagination parameters, then serializes the paginated items with
    the given APIFlask/Marshmallow schema.

    Args:
        query: A SQLAlchemy query object that supports the ``paginate()`` method.
        schema: A schema instance used to serialize the paginated items.
            For example: ``UserSchema(many=True)``.
        params: A dictionary containing pagination parameters. Expected keys:

            - ``page`` (int): The page number (starting from 1).
            - ``per_page`` (int): Number of items per page.

    Returns:
        dict: A dictionary containing pagination metadata and serialized data
        with the following structure::

            {
                "count": 100,
                "page": 1,
                "per_page": 10,
                "pages": 10,
                "next": 2,
                "previous": None,
                "results": [...]
            }
            
    Example:
        Basic usage::

            @bp.get("/users")
            @bp.input(PaginationQuerySchema, location="query")
            def list_users(query):
                return paginate(
                    query=User.query.order_by(User.id),
                    schema=UserSchema(many=True),
                    params=query,
                )

        With filtering::

            @bp.get("/users")
            @bp.input(PaginationQuerySchema, location="query")
            def list_active_users(query):
                return paginate(
                    query=User.query.filter(User.is_active == True),
                    schema=UserSchema(many=True),
                    params=query,
                )
    """
    pagination = query.paginate(
        page=params["page"],
        per_page=params["per_page"],
        error_out=False,
    )

    return {
        "count": pagination.total,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "pages": pagination.pages,
        "next": pagination.next_num if pagination.has_next else None,
        "previous": pagination.prev_num if pagination.has_prev else None,
        "results": schema.dump(pagination.items),
    }