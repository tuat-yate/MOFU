# CSVLIB
# Requirement

```
xlrd
numpy
```
# APIs overview
# APIs detail
## csvlib
### property
### **`MOFU.csvlib.read_data: list`**
```python
MOFU.csvlib('*.csv').read_data
```
`(row,column)`の`list`を返します。

### method
### **`MOFU.csvlib.save(path): None`**
```Python
MOFU.xlsxlib('*.xlsx').save('*.csv',sheet=1)
```
第一引数で与えたpathで保存します。

## xlsxlib
### property
### **`MOFU.xlsxlib.read_data: list`**
`(sheet,row,column)`の`list`を返します。
### **`MOFU.xlsxlib.label: list`**
シート名の`list`を返します。

### method
### **`MOFU.xlsxlib.read_data_by_sheet_name(sheet=None): ndarray`**
```Python
MOFU.xlsx('*.xlsx').read_data_by_sheet_name()
# or
MOFU.xlsx('*.xlsx').read_data_by_sheet_name('sheetname')
```
引数なしで呼び出すことで一番目(内部的には0番目)のシートを、シート名を`sheet=`で与えることで、任意のシートを呼び出すことができます。

### **`MOFU.xlsxlib.save(path,sheet=0): None`**
```Python
MOFU.xlsxlib('*.xlsx').save('*.csv',sheet=1)
```
第一引数で与えたpathで保存します。`sheet=`を指定しない場合は最初のシートを保存します。
## function

### **`MOFU.save_as_csv(array,path): None`**
```python
MOFU.save_as_csv(array,'*.csv')
```
第一引数で与えたarrayを第二引数で与えたpathで保存します。