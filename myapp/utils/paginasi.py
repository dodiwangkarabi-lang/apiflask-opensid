class Pagination:
    def paginate(self, queryset, page: int, page_size: int):
        offset = (page - 1) * page_size

        total = queryset.count()
        items = queryset[offset:offset + page_size]

        return {
            "count": total,
            "page": page,
            "page_size": page_size,
            "results": items,
        }