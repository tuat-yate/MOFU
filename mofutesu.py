import MOFU
import csv
csvname='out.csv'
xlsxname='out.xlsx'
mf1=MOFU.csvlib(csvname)
mf2=MOFU.xlsxlib(xlsxname)
MOFU.save_as_csv(mf1.read_data,'file1.txt')
MOFU.save_as_csv(mf2.read_data[0],'file2.csv')