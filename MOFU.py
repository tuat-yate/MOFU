import csv
import os
import xlrd
import warnings
import numpy as np

#SyntaxError



class _base():
    def __init__(self,fname=None):
        
        if not(fname==None):
            self._fname=fname
            #ファイルが存在しないときエラー
            if not(os.path.exists(self._fname)):
                raise FileNotFoundError(self._fname+' is not found.')
                #dirのときもエラー
                if(os.path.isfile(self._fname)):
                    raise FileNotFoundError(self._fname+' is directory, not file.')

            #file_typeを保存
            self._file_type=os.path.splitext(self._fname)[1].replace('.','')
            
            #使えるタイプじゃ無いときにエラー
            if(self._file_type.lower() not in ['csv','xlsx','xls']):
                raise SyntaxError('MOFU can use for csv, xlsx and xls file.')
        
        #引数無いときにエラー
        else:
            raise SyntaxError('MOFU require filename as argument like this,\nmf = MOFU(\'csvfile.csv\')')

    def __repr__(self):
        return '< class MOFU.base(=^・・^=) | type={} >'.format(self._file_type)
    
    @property
    def filename(self):
        return os.path.basename(self._fname)

class csvlib(_base):
    def __repr__(self):
        return '< class MOFU.csvlib(=^・・^=) | type={} >'.format(self._file_type)

    @property
    def read_data(self):
        with open(self._fname) as f:
            reader = csv.reader(f)
            return np.array([row for row in reader])

    @property
    def label_column(self):
        if(self.read_data.ndim==1):
            return self.read_data
        else:
            return self.read_data[0,:]

    @property
    def label_row(self):
        if(self.read_data.ndim==1):
            return self.read_data
        else:
            return self.read_data[:,0].T

    @property
    def dict_column(self):
        _tmp=dict()
        for i,label in enumerate(self.label_column):
            _tmp[label]=self.read_data[1:,i]
        return _tmp

    @property
    def dict_row(self):
        _tmp=dict()
        for i,label in enumerate(self.label_row):
            _tmp[label]=self.read_data[i,1:]
        return _tmp

class xlsxlib(_base):
    def __repr__(self):
        return '< class MOFU.xlsxlib(=^・・^=) | type={} >'.format(self._file_type)

    def read_data_by_sheet_name(self,sheet=None):
        _wb=xlrd.open_workbook(self._fname)
        #sheetの指定が無いときはwarnしつつ一番最初のシートを返す
        if(sheet==None):
            warnings.warn('You can access any sheet by using "sheet" argument. By default, this method access {} sheet'.format(_wb.sheet_names()[0]))
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
        _tmp_dict=dict()
        for i in self.sheet_names:
            _tmp_dict[i]=self.read_data_by_sheet_name(sheet=i)
        return _tmp_dict

def dict_row(ndarray):
    _tmp=dict()
    for i,label in enumerate(ndarray[:,0].T):
        _tmp[label]=ndarray[i,1:]
    return _tmp

def dict_column(ndarray):
    _tmp=dict()
    for i,label in enumerate(ndarray[0,:]):
        _tmp[label]=ndarray[1:,i]
    return _tmp
