import requests


class RequestWebPage:
    """This class tends to study what we can do with classes and request library."""
    def __int__(self, url):
        self.url = url


def make_request() -> str:
    r = requests.get("https://dnsdumpster.com/")
    print(r.status_code)
    if r.status_code == 200:
        return r.text
    else:
        return False


print(make_request())
