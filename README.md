# SNET 

##SNETは仮想マシンを起動できるソフトウェアです。
以下のファイルで構成されています。
------
Cprofile.exe：プロファイルの作成ソフトウェア
SNET.jar ：起動用プログラム
resources：ソフトウェアに必要なリソース格納フォルダ
bin/VM manager.exe：ソフトウェア本体

使用方法 

Cprofile.exeを使用して仮想マシンプロファイルを作成します
SNET.jarをダブルクリックで起動(VM manager.exe単体では動作しません)
リソースの読み込みが完了するとSNET.jarはbinフォルダ内の「VM manager.exe」
を起動します。

VM manager.exeの起動ボタンを押すとプロファイル選択画面になるので
プロファイルを選択すると仮想化ソフトウェアで
エラーにならない限り仮想マシンが起動します。

SNET.jarはresourcesフォルダとbinフォルダ内のVM managerを読み込む必要
があるため二つのフォルダはSNET.jarと同じ階層に配置する必要があります。

(このソフトウェアが現在対応している仮想化ソフトウェアは
VirtualBoxのみです)
