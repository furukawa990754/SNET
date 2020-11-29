# SNET 

## 使用方法 

*SNET.jarの起動にはJava JREが必要です。

Cprofile.exeを使用して仮想マシンプロファイルを作成します。
SNET.jarをダブルクリックで起動するか下の起動方法を参照してください
リソースの読み込みが完了するとSNET.jarはbinフォルダ内の「VM manager.exe」
を起動します。

以下　VM manager.exeでの操作

起動ボタンを押すとプロファイル選択画面になるので
プロファイルを選択した後仮想化ソフトウェアで
エラーにならない限り仮想マシンが起動します。
SNET.jarはresourcesフォルダとbinフォルダ内のVM managerを読み込む必要があるため二つのフォルダはSNET.jarと同じ階層に配置する必要があります。

(このソフトウェアは起動処理にVirtualBoxのVBoxmanageコマンドを使用しますのでVBoxmanageコマンドにパスを通す必要があります)

------
### 起動方法(SNET.jar)

もしダブルクリックで起動できない環境の場合、以下のコマンドで起動ができます。

バージョン表示とともに処理が終了次第「VM manager.exe」に処理が移ります。

(このコマンドで起動する場合プロンプトのカレントディレクトリはSNET.jarが格納されているフォルダにする必要があります。)

java -jar SNET.jar


