import time


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    time.sleep(0.25)
    return [b"Hello World"]
