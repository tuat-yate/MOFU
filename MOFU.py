import csv
import os
import xlrd
import warnings
import numpy as np

class read():
    def __init__(self,filename=None):
        if not(filename==None):
            self._filename=filename
            if not(os.path.exists(self._filename)):
                raise FileNotFoundError(self._filename+' is not found.')
            self._file_type=os.path.splitext(self._filename)[1].replace('.','')
            if not(self._file_type=='csv' or self._file_type=='xlsx' or self._file_type=='xlx'):
                raise ValueError('MOFU can use for csv, xlsx and xls.')
        #引数無いとき
        else:
            raise ValueError('MOFU require filename as argument like this,\nmf = MOFU(\'csvfile.csv\')')
    
    def __repr__(self):
        return '<class MOFU.read(=^・・^=) | {} has {} sheets>'.format(os.path.basename(self._filename),len(self.sheet_names))

    @property    
    def sheet_names(self):
        if(self._file_type=='csv'):
            return ['main']
        else:
            return xlrd.open_workbook(self._filename).sheet_names()

    def data(self,sheet=None):
        #for csv file
        if(self._file_type=='csv'):
            with open(self._filename) as f:
                reader = csv.reader(f)
                return np.array([row for row in reader])

        #xlsx or xls
        if(self._file_type=='xlsx' or self._file_type=='xls'):
            _wb=xlrd.open_workbook(self._filename)
            #sheetの指定が無いときはwarnしつつ一番最初のシートを返す
            if(sheet==None):
                warnings.warn('')
                _sheet=_wb.sheet_by_name(_wb.sheet_names()[0])
                return np.array([_sheet.row_values(row) for row in range(_sheet.nrows)])
            #指定があるけどそれがsheet名として存在しないとき
            elif (sheet not in _wb.sheet_names()):
                raise ValueError('Not found {} sheet in {}'.format(sheet,self._filename))
            #大丈夫そうなとき
            else:
                _sheet=_wb.sheet_by_name(sheet)
                return np.array([_sheet.row_values(row) for row in range(_sheet.nrows)])

    @property
    def fulldata(self):
        if(self._file_type=='csv'):
            return {'main':self.data()}
        else:
            _tmp_dict=dict()
            for i in self.sheet_names:
                _tmp_dict[i]=self.data(sheet=i)
            return _tmp_dict