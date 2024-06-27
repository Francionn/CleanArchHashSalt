
class HttpResponse:
    def __init__(self, status_code, body) -> None:
        self.headers = status_code
        self.body = body
