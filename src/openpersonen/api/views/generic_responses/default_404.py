def get_404_response(url):
    return {
        "type": "https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#/10.4.5 404 Not Found",
        "title": "Opgevraagde resource bestaat niet.",
        "status": 404,
        "detail": "The server has not found anything matching the Request-URI.",
        "instance": url,
        "code": "notFound",
    }
