import requests
from common.handle_config import confvalue


class RequestHandle:
    header = {
        "Content-Type": "application/json",
    }

    data = {
        "user": "message1204",
        "password": "o2D06r0NOP3Y",
        "expire_hours": 1
    }

    def tokenauth(self):
        token = requests.post(url=confvalue.readconf('api', 'weatherurl') + '/authorize/token',
                              headers=self.header,
                              json=self.data,
                              verify=False)
        return token


if __name__ == '__main__':
    requesttest = RequestHandle()
    print(requesttest.tokenauth().content)
