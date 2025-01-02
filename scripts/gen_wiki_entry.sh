#!/bin/bash

# ファイル名を現在の日付から生成
wiki_path='./wiki/'
filename="$(date +'%Y-%m-%d')-wikiji.md"

# ファイルが既に存在するか確認
if [ -e "${wiki_path}${filename}" ]; then
    echo "ファイル '${wiki_path}${filename}' は既に存在しています。何もせずに終了します。"
    exit 0
fi

# ファイルに書き込むテキストを生成
content="---
title: \"\"
published: true
---
"

# ファイルにテキストを書き込み
touch ${wiki_path}${filename}
# pwd
echo -e "$content" >> "${wiki_path}${filename}"

# 結果を表示
echo "ファイル '${wiki_path}${filename}' が作成されました。"
