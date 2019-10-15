import  xlrd
data =xlrd.open_workbook('../.excel')
table  =data.sheets()[0]
print( table.nrows)
print(table.cess_value(2,3))

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name =file_name
            self.sheet_id =sheet_id
            self.data =self.get_data()
        else:
            self.file_name ='../'
            self.sheet_id =0
        self.data =self.get_data()


        self.file_name =file_name
        self.sheet_id =sheet_id
        self.data =self.get_data()

    def get_data(self,flie_name,sheet_id):
        data = xlrd.open_workbook(file_name)
        tables =data.sheets()[sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return table.nrows

    def get_cell_value(self):
        return self.data.cell_value(row,col)
    
if __name__ == '__main__':
    opers =OperationExcel()
    opers.get_data()
