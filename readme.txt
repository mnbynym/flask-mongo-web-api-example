Flask-PyMongoのインストール
$ sudo pip3 install Flask-PyMongo

  Flask-PyMongo ドキュメント
  https://flask-pymongo.readthedocs.io/en/latest/

Flas-Corsのインストール
$ sudo pip install flask-cors

  Flask-Cors ドキュメント
  https://pypi.org/project/Flask-Cors/

Flaskはデフォルトで5000番ポートで起動するためサーバーのセキュリティ設定が必要

サーバーの実行方法
$ export FLASK_APP=api_server.py
$ flask run --debugger --reload --host=0.0.0.0
