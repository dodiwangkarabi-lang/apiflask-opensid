# from math import ceil
# from sqlalchemy import func, select

# def paginate(query, stmt, page=1, per_page=10):
#     total = query.session.scalar(
#         select(func.count()).select_from(stmt.subquery())
#     )

#     items = query.session.scalars(
#         stmt.offset((page - 1) * per_page)
#             .limit(per_page)
#     ).all()

#     return {
#         "count": total,
#         "page": page,
#         "per_page": per_page,
#         "pages": ceil(total / per_page),
#         "results": items,
#     }
    
    
"""
Usage:

stmt = select(User).order_by(User.id)

return paginate(
    db.session,
    stmt,
    page=query["page"],
    per_page=query["per_page"],
)
"""