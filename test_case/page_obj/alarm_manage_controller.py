from test_case.page_obj.base import InterfaceBase

class AlarmManage(InterfaceBase):
    '''
    报警相关接口
    '''

    # 保存处理后的报警信息并进行校验，单个及批量都是此接口
    def batch_process(self, data):
        batch_process_url = self.base_url + "/alarm/batchProcess"
        response = self.post(batch_process_url, data=data)
        return response