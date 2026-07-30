# def filter_hasil(data: list, **kwargs) -> list:
#     result = [
#         d
#         for d in data
#         if all(d.get(k) == v for k, v in kwargs.items())
#     ]
#     return result

def filter_hasil(data: list, **kwargs) -> list:
    return [
        d
        for d in data
        if all(
            d.get("document", {}).get(k) == v
            for k, v in kwargs.items()
        )
    ]