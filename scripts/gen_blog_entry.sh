#!/bin/bash

# ファイル名を現在の日付から生成
posts_path='./_posts/'
filename="$(date +'%Y-%m-%d')-today.md"

# ファイルが既に存在するか確認
if [ -e "${posts_path}${filename}" ]; then
    echo "ファイル '${posts_path}${filename}' は既に存在しています。何もせずに終了します。"
    exit 0
fi

# ファイルに書き込むテキストを生成
content="---
title: \"\"
date:  $(date +'%Y-%m-%d %H:00:00 %z')
published: false
---
"

# ファイルにテキストを書き込み
touch ${posts_path}${filename}
# pwd
echo -e "$content" >> "${posts_path}${filename}"

# 結果を表示
echo "ファイル '${posts_path}${filename}' が作成されました。"
