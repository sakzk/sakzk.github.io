#!/bin/bash

# ファイル名を現在の日付から生成
filename=$(date +'_posts/%Y-%m-%d-%foo').md

# ファイルが既に存在するか確認
if [ -e "$filename" ]; then
    echo "ファイル '$filename' は既に存在しています。何もせずに終了します。"
    exit 0
fi

# ファイルに書き込むテキストを生成
content="---
layout: post
title:  \"foo\"
date:   $(date +'%Y-%m-%d %H:00:00 %z')
---

#"

# ファイルにテキストを書き込み
echo -e "$content" >> "$filename"

# 結果を表示
echo "ファイル '$filename' が作成されました。"
