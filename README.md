# リポジトリをクローンする
クローンしたい場所で以下を実行<br>
実行した直下にリポジトリ名と同じ名前のディレクトリができます。（今回は`chatbot`ディレクトリができます）
```
git clone {repository_url}
```

# 仮想環境の立ち上げ
#### 例
```
source {仮想環境名}/bin/activate
```
```
source line/bin/activate
```
以下が先頭についていればOKです
```
(line) 
```

# 依存環境のインストール
仮想環境が立ち上がっている状態で、以下のコマンドを実行すると一括で依存関係をインストールできます。<br>
```
pip install -r requirements.txt
```
できなければ以下を実行（複数のPythonが入っているとき等）
```
pip3 install -r requirements.text
```
インストールできているかは以下のコマンドで確認できます。
```
pip install
 or
pip3 install
```

# 環境変数を設定する
`.env`の`ACCESS_TOKEN`と`CHANNEL_SECRET`を設定する
```
ACCESS_TOKEN={ここに設定}
CHANNEL_SECRET={ここに設定}
```

# 仮想環境を終了する
以下を実行する
```
deactivate
```

# 参考
LineBot公式GitHub<br>
https://github.com/line/line-bot-sdk-python

# TODO
venvで作成されたファイルを共有しない様にする
