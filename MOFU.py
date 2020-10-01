import csv
import os
import xlrd
import warnings
import numpy as np


class _base():
    @property
    def filename(self):
        return os.path.basename(self._fname)

class csvlib(_base):
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
            if not(self._file_type.lower() == 'csv'):
                raise SyntaxError('MOFU can use for csv file.')
        #引数無いときにエラー
        else:
            raise SyntaxError('MOFU require filename as argument like this,\nmf = MOFU(\'csvfile.csv\')')

    def __repr__(self):
        return '< class MOFU.csvlib(=^・・^=) | type={} >'.format(self._file_type)

    @property
    def read_data(self):
        with open(self._fname) as f:
            reader = csv.reader(f)
            return [row for row in reader]

class xlsxlib(_base):
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
            if not(self._file_type.lower() == 'xlsx' or self._file_type.lower() == 'xls'):
                raise SyntaxError('MOFU can use for xlsx or xls file.')
        #引数無いときにエラー
        else:
            raise SyntaxError('MOFU require filename as argument like this,\nmf = MOFU(\'xlsxfile.xlsx\')')

    def __repr__(self):
        return '< class MOFU.xlsxlib(=^・・^=) | type={} >'.format(self._file_type)

    def read_data_by_sheet_name(self,sheet=None):
        #sheetの指定が無いときはwarnしつつ一番最初のシートを返す
        _wb=xlrd.open_workbook(self._fname)
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
            return [_sheet.row_values(row) for row in range(_sheet.nrows)]

    @property
    def read_data(self):
        _wb=xlrd.open_workbook(self._fname)
        _tmp=list()
        for i in _wb.sheet_names():
            _sheet=_wb.sheet_by_name(i)
            _tmp.append([_sheet.row_values(row) for row in range(_sheet.nrows)])
        return _tmp

    @property
    def label(self):
        _wb=xlrd.open_workbook(self._fname)
        return _wb.sheet_names()
