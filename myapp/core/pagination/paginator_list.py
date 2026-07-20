from math import ceil
from urllib.parse import urlencode


def paginate(
    *,
    items: list,
    page: int,
    per_page: int,
    base_url: str,
    query_params: dict | None = None,
):
    total = len(items)

    start = (page - 1) * per_page
    end = start + per_page

    results = items[start:end]

    total_pages = ceil(total / per_page) if total > 0 else 1

    query_params = query_params.copy() if query_params else {}

    def build_url(page_number: int):
        params = {
            **query_params,
            "page": page_number,
            "limit": per_page,
        }
        return f"{base_url}?{urlencode(params)}"

    next_url = (
        build_url(page + 1)
        if page < total_pages
        else None
    )

    previous_url = (
        build_url(page - 1)
        if page > 1
        else None
    )

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": results,
    }
    
    """
    penggunaan:
    
    pagination = paginator.paginate(
        items=hasil_pencarian,
        page=1,
        per_page=10,
        base_url="https://api.example.com/api/surat",
        query_params={
            "search": "surat",
            "ordering": "-tanggal",
        },
    )
    """

    # def paginate(self, items, page, per_page):
    #     total = len(items)

    #     start = (page - 1) * per_page
    #     end = start + per_page

    #     return {
    #         "count": total,
    #         "page": page,
    #         "pages": ceil(total / per_page),
    #         "items": items[start:end],
    #         "has_next": end < total,
    #         "has_prev": page > 1,
    #     }

"""
hasil = mesin_pencarian.search(keyword)

pagination = paginator.paginate(
    hasil,
    page=params.page,
    per_page=params.limit,
)
"""