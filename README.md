***
## PyFish
***
これはPythonで動作するwiiuのメモリ改造ライブラリです
## 使い方
```py
import PyFish
gecko=PyFish("192.168.3.5",	3771,1)
#             ipaddres		+    +-debugレベル1か0
#                wiiuの		+ポート
#							+設定しない場合7331を設定すること
gecko.poke("アドレス","値")		#固定コード
a=gecko.peek("アドレス")		#メモリの内容を取得
print(a)
```
pokeやpeekの最初に`pointer_`と入力しておくとポインターモードになり
引数が増えます
```py
pointer_poke("アドレス","あたい",オフセット,...)
pointer_peek("アドレス",オフセット,...)
```
**注意オフセットは整数型にしてください**