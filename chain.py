class Handler:
    """Abstract Handler"""
    def __init__(self, successor):
        self._sucessor = successor

    def handle(self, request):
        handled = self._handle(request)
        if not handled and self._sucessor:
            self._sucessor.handle(request)
    
    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass")

class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f"Request {request} handled in handler 1")
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print(f"End of chain, no handler for {request}")

class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
       
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


c = Client()
requests = [2, 5, 30]
c.delegate(requests)