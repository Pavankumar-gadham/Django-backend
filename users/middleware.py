class LogOriginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        origin = request.headers.get('Origin', 'No Origin Header')
        print(f"Incoming request Origin header: {origin}")
        response = self.get_response(request)
        return response
