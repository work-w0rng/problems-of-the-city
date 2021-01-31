from json import loads


def simple_middleware(get_response):
    def middleware(request):
        if 'api' != request.path.split('/')[1]:
            return get_response(request)
        print('--------------------')
        tmp = getattr(request, '_body', request.body)
        if tmp:
            tmp = loads(tmp)
        print(f'{request.method} запрос {request.path}:', tmp)
        response = get_response(request)
        print('---------')
        print('Ответ: ', response._container)
        print('--------------------')
        return response
    return middleware
