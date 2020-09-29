# CSVLIB
# Requirement

```
xlrd
numpy
```
# APIs
## all
### property
#### **`MOFU.filename: str`**
```python
MOFU(anyfile).filename
```
`class`を呼び出す前の元のファイル名を表示します。フルパスではなく`basename`(ディレクトリ構造等を除いたファイル名)なので気をつけて下さい。

## csvlib
### property
#### **`read_data: ndarray`**
```python
MOFU.csvlib('*.csv').read_data
```
`(row,column)`の`ndarray`を返します。

#### **`label_column: list`**
```python
MOFU.csvlib('*.csv').label_column
```
| label1 | label2 | label3 |
|:------:|:------:|:------:|
| value1-1 | value2-1 | value3-1 |
| value1-2 | value2-2 | value3-2 |
| value1-3 | value2-3 | value3-3 |

このような構造を持つ`csv`ファイルに対して、
```
['label1' 'label2' 'label3']
```
のような`ndarray`を返します。

#### **`dict_column: dict`**
```python
MOFU.csvlib('*.csv').dict_column
```
| label1 | label2 | label3 |
|:------:|:------:|:------:|
| value1-1 | value2-1 | value3-1 |
| value1-2 | value2-2 | value3-2 |
| value1-3 | value2-3 | value3-3 |

このような構造を持つ`csv`ファイルに対して、`key`がラベル、`value`がその列の`ndarray`である`dict`を返します。

#### **`label_row: list`**
```python
MOFU.csvlib('*.csv').label_row
```
| label1 | value1-1 | value1-2 | value1-3 |
|:------:|:------:|:------:|:------:|
| label2 | value2-1 | value2-2 | value2-3 |
| label3 | value3-1 | value3-2 | value3-3 |

このような構造を持つ`csv`ファイルに対して、
```
['label1' 'label2' 'label3']
```
のような`ndarray`を返します。

#### **`dict_row: dict`**
```python
MOFU.csvlib('*.csv').dict_row
```
| label1 | value1-1 | value1-2 | value1-3 |
|:------:|:------:|:------:|:------:|
| label2 | value2-1 | value2-2 | value2-3 |
| label3 | value3-1 | value3-2 | value3-3 |

このような構造を持つ`csv`ファイルに対して、`key`がラベル、`value`がその列の`ndarray`である`dict`を返します。

### method

## xlsxlib
### property
#### **`fulldata: dict`**
`key`がシート名、`value`がそのシートの`ndarray`の`dict`を返します。
### method
#### **`read_data_by_sheet_name(sheet=None): ndarray`**
```Python
MOFU.xlsx('*.xlsx').read_data_by_sheet_name()
# or
MOFU.xlsx('*.xlsx').read_data_by_sheet_name(sheet='sheetname')
```
引数なしで呼び出すことで一番目(内部的には0番目)のシートを、シート名を`sheet=`で与えることで、任意のシートを呼び出すことができます。

## functions
#### **`dict_row(ndarray): dict`**
`ndarray`を与えることでA列が`key`のdictを生成します。`csv`ファイルと`xlsx`ファイルが同じもののとき、
```Python
MOFU.csvlib(csvname).dict_row
# と
MOFU.xlsxlib.dict_row(MOFU.xlsxlib(xlsxname).read_data_by_sheet_name())
```
は等価になります。

#### **`dict_column(ndarray): dict`**
`ndarray`を与えることで1行が`key`のdictを生成します。`csv`ファイルと`xlsx`ファイルが同じもののとき、
```Python
MOFU.csvlib(csvname).dict_column
# と
MOFU.xlsxlib.dict_column(MOFU.xlsxlib(xlsxname).read_data_by_sheet_name())
```
は等価になります。
