
fastAPIのセットアップ
=====================

パッケージのインストール
------------------------

.. code-block:: shell

    python -m pip install fastapi

アプリサーバーのスクリプトの作成
--------------------------------

プロジェクトフォルダ内にmain.pyを作成する。

.. code-block:: python

    from fastapi import FastAPI

    app = FastAPI()


サーバーの起動
--------------

以下のコマンドを実行してサーバーを起動させる。

.. code-block:: 

    uvicorn main:app --reload

コマンドの実行後に以下のようなメッセージが表示される。

::

    INFO:     Will watch for changes in these directories: ['/Users/shun/Desktop/my-fastapi']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [17890] using StatReload
    INFO:     Started server process [17892]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.


.. note:: 

    起動コマンドの"main"はPythonのモジュール名(ファイル名)であり、
    "app"はモジュールスクリプト内で作成したFastAPIクラスの
    インスタンス変数名である。もし別名でモジュールやファイル名を
    作成した場合はそれに置き換える。
