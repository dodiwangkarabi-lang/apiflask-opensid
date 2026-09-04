# from typing import List

def paginated(arr: list, page, page_size) -> list:
    total = len(arr)
    total_pages = (total + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    
    hasil = {
        "data": arr[start:end],
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages
    }
    return hasil