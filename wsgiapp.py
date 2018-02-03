def app(environ, start_response):
    """A basic WSGI application
    Build your web framework from here!
    """

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world from a simple WSGI application!\n']
