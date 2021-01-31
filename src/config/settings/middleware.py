def simple_middleware(get_response):
    def middleware(request):
        print(f'Запрос {request.path}:', getattr(request, '_body', request.body))
        response = get_response(request)
        print('Ответ: ', response._container)
        return response
    return middleware
