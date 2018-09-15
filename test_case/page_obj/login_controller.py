from test_case.page_obj.base import InterfaceBase

class Login(InterfaceBase):
    '''
    登录相关接口
    '''

    def user_login(self, data):
        batch_process_url = self.base_url + "/check/login"
        response = self.post(batch_process_url, data=data)
        return response

    def user_logout(self):
        batch_process_url = self.base_url + "/logout"
        response = self.post(batch_process_url)
        return response
