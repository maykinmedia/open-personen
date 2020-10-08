from vng_api_common.routers import APIRootView as _APIRootView


class APIRootView(_APIRootView):
    action = "list"
    basename = "ingeschrevenpersonen"
