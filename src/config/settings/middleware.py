def simple_middleware(get_response):
    def middleware(request):
        if 'api' != request.path.split('/')[1]:
            return get_response(request)
        print(f'{request.method} запрос {request.path}:', getattr(request, '_body', request.body))
        response = get_response(request)
        print('Ответ: ', response._container)
        return response
    return middleware
