import MOFU
csvname='out.csv'
xlsxname='out.xlsx'
print(MOFU.csvlib(csvname).dict_column)
print(MOFU.dict_column(MOFU.xlsxlib(xlsxname).read_data_by_sheet_name()))