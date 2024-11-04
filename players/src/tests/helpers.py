from typing import Optional


class TestRequest:
    def __init__(self, path: str, body: Optional[str], method: str):
        self.path = path
        self.body = body
        self.method = method
