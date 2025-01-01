#!/bin/bash

# スクリプトのディレクトリへ移動
# make からの呼び出しに対応するため
cd "$(dirname "$0")"

python3 gen_blog_front.py
python3 gen_booklist_front.py
