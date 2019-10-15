from util.operation_excel import  OperationExcel
import  data_config

class GetData:
    def __init__(self):
        self.opera_excel =OperationExcel
        #去过去excel行数 case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行

    def get_is_run(self,row):
        flag =None
        col =data_config.get_run()
        run_model= self.opera_excel.get_cell.value()
        if run_model =='yes'
            flag =True
        else:
            flag =False
        return  flag
    #是否hearder
    def is_header(self,row):
        col =data_config.get_header()
        header =self.opera_excel.get_cell_value(row,col)
        if header =='yes'
           return  data_config.get_header_value( )
        else:
            return None
    #获取请求方式
    def get_requesr_method(self):
        col =data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value()
        return  request_method
    #h获取url

    def get_request_url(self,row):
        col =data_config.get_url()
        url =self.opera_excel.get_cell_value(row,col)
        return  url
    #获取请求数据

    def get_request_data(self,row):
        col = data_config.get_data()
        data =self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data
    #通过获取关键子拿到data数据
    def get_data_for_json(self):
        opera_json = OperetionJson()
        opera_json.get_data(self.get_request_data(row))
        return  request_data
    #通过获取预期结果

    def get_expcet_data(self,row):
        col = data_config.get_expect()
        except=self.opera_excel.get_cell(row,col)
        if expect == '':
            return None

        return expect






