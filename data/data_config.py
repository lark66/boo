class global_var :

    ID ='0'
    url ='1'
    uun ='2'
    method ='3'
    header ='4'
    case_depend ='5'
    data_depend='6'
    field_depend ='7'
    data ='8'
    expect ='9'
    result ='10'
def get_id():
    return global_var.Id

def get_url():
    return global_var.url
def get_run():
    return global_var.run
def get_method():
    return global_var.method
def get_header_value():
    header ={
        "header":"",
        'cookies':""
    }
    return global_var.header
def get_case_depend():
    return global_var.case_depend
def get_field_depend():
    return global_var.data_depend

def get_data():
    return global_var.data
def get_expect():
    return global_var.expect
def get_result():
    return global_var.result
