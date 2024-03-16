import requests


class RequestWebPage:
    """This class tends to study what we can do with classes and request library."""

    def __init__(self, url):
        self.url = url

    def make_request(self) -> str:
        r = requests.get(self.url)
        print(r.status_code)
        if r.status_code == 200:
            return r.text[:500]
        else:
            return False


reqDnsDumpster = RequestWebPage("https://dnsdumpster.com/")
print(reqDnsDumpster.make_request())
