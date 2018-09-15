# interface_test
framework of interface testing

interface_test
    --report
        --html(dir:存储html格式的测试报告)
    --test_case
        --models(dir:存储基本测试设置）
            --config(file:存储测试基本信息)
            --myunit(file:新建单元测试基础类)
        --page_obj(dir:存储接口设置)
            --base(file:新建接口基础类）
            --*_controller(file:接口实现类，继承于base)
        --*_sta(file:测试实现类，继承于myunit)
    --run_cicc_portal_test(file:测试执行文件，用于生成测试报告并发送相应邮件)
