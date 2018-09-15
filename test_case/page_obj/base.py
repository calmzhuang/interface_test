import requests
from test_case.models.config import ua

class InterfaceBase(object):
    '''
    接口基础类，用于所有接口的继承
    '''
    def __init__(self, user_agent=ua.chrome):
        self.base_url = "http://47.97.73.74:8181"
        self.headers = {"User-Agent": user_agent}
        self.r_session = requests.session()

    # 定义get接口请求
    def get(self, url, params):
        response = self.r_session.get(url=url, params=params, headers=self.headers)
        return response

    # 定义post接口请求
    def post(self, url, data=None):
        response = self.r_session.post(url=url, data=data, headers=self.headers)
        return response

    # 定义head接口请求
    def head(self, url, params):
        response = self.r_session.head(url=url, params=params, headers=self.headers)
        return response

    # 定义put接口请求
    def put(self, url, params):
        response = self.r_session.put(url=url, params=params, headers=self.headers)
        return response

    # 定义delete接口请求
    def delete(self, url, params):
        response = self.r_session.delete(url=url, params=params, headers=self.headers)
        return response

    # 定义options接口请求
    def options(self, url, params):
        response = self.r_session.options(url=url, params=params, headers=self.headers)
        return response

    # 定义patch接口请求
    def patch(self, url, params):
        response = self.r_session.patch(url=url, params=params, headers=self.headers)
        return response