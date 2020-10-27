from django.http import JsonResponse
from django.views.defaults import page_not_found

from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


def handler404(request, exception):
    if request.path.startswith("/api"):
        return JsonResponse(
            {
                "type": "https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#/10.4.5 404 Not Found",
                "title": "Opgevraagde resource bestaat niet.",
                "status": 404,
                "detail": "The server has not found anything matching the Request-URI.",
                "instance": request.build_absolute_uri(),
                "code": "notFound",
            },
            status=HTTP_404_NOT_FOUND,
        )
    else:
        return page_not_found(request, exception)


def handler500(request):
    return JsonResponse(
        {
            "type": "https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1",
            "title": "Interne server fout.",
            "status": 500,
            "detail": "The server encountered an unexpected condition which prevented it from fulfilling the request.",
            "instance": request.build_absolute_uri(),
            "code": "serverError",
        },
        status=HTTP_500_INTERNAL_SERVER_ERROR,
    )
