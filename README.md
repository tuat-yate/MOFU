# CSVLIB
## 要件

```
xlrd
numpy
```

## APIs
### property
#### `MOFU.read.sheet_names: list`
ファイル内のすべてのシート名を`list`で返します。与えたファイルが`csv`のときは`['main']`を返します。
#### `MOFU.read.fulldata: dict`
ファイル内のすべてのシートを`dict`を返します。フォーマットは`{(sheet_name):(sheetのndarray),...}`です。与えたファイルが`csv`のときは`{'main':(csvのndarray)}`を返します。`csv`ファイルを扱う場合、`MOFU.read.fulldata['main']`と後述の`MOOFU.read.data()`は等価になります。
### method
#### `MOFU.read.__init__`  
#### `MOFU.read.__repr__`  
猫とファイルが持っているシートの数を表示します。
#### `MOFU.read.data(sheet=None):  ndarray`  
`csv`の場合は引数`sheet`の値に関わらず`csv`のデータを`ndarray`で返します。それ以外のファイルの場合は、引数がないときファイルの最初のシート、引数`sheet`が与えられている場合はその名前のシートの`ndarray`を返します。引数`sheet`に与えた値に一致するシートがない場合はエラーになります。