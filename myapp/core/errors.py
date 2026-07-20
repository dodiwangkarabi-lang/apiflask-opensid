def register_error_handlers(app):

    @app.error_processor
    def handle_error(error):
        data = error.detail or {}

        # Hilangkan level json/query/form/files
        if isinstance(data, dict) and len(data) == 1:
            key = next(iter(data))
            if key in ("json", "query", "form", "files"):
                data = data[key]

        return {
            "message": error.message,
            "errors": data
        }, error.status_code