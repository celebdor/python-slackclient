import requests


class SlackRequest(object):
    def __init__(self):
        pass

    def do(self, token, request="?", post_data={}, domain="slack.com"):
        post_data["token"] = token
        url = 'https://{}/api/{}'.format(domain, request)
        request = requests.post(url, data=post_data)
        return request
