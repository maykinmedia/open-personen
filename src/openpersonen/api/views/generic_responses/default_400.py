def get_expand_400_response(url, query_param):
    return {
        "type": "https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1",
        "title": "Minstens één param is niet geldig.",
        "status": 400,
        "detail": "The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modification.",
        "instance": url,
        "code": "ongeldigParam",
        "invalidParams": [
            {
                "type": "ongeldigParam",
                "name": query_param,
                "code": "ongeldigParam",
                "reason": "Param is niet geldig.",
            }
        ],
    }
