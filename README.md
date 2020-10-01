# CSVLIB
# Requirement

```
xlrd
numpy
```
# APIs overview
# APIs detail
## all
### property
#### **`MOFU.filename: str`**
```python
MOFU(anyfile).filename
```
`class`を呼び出す前の元のファイル名を表示します。フルパスではなく`basename`(ディレクトリ構造等を除いたファイル名)なので気をつけて下さい。

## csvlib
### property
#### **`read_data: list`**
```python
MOFU.csvlib('*.csv').read_data
```
`(row,column)`の`list`を返します。

### method

## xlsxlib
### property
#### **`MOFU.xlsxlib.read_data: list`**
`(sheet,row,column)`の`list`を返します。
#### **`MOFU.xlsxlib.label: list`**
シート名の`list`を返します。
### method
#### **`read_data_by_sheet_name(sheet=None): ndarray`**
```Python
MOFU.xlsx('*.xlsx').read_data_by_sheet_name()
# or
MOFU.xlsx('*.xlsx').read_data_by_sheet_name(sheet='sheetname')
```
引数なしで呼び出すことで一番目(内部的には0番目)のシートを、シート名を`sheet=`で与えることで、任意のシートを呼び出すことができます。