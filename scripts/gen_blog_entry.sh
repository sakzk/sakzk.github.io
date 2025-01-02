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
title: \"$(date +'%Y年%m月%d日')の日記 365日中$(date +%-j)日目\"
date:  $(date +'%Y-%m-%d %H:00:00 %z')
published: false
---

## チェックリスト
- [ ] ジョギング: 2キロ以上
- [ ] 筋トレ: 5分以上
- [ ] 水シャワー: 1分以上
- [ ] アニメを1話見る or 感想記事を書く
- [ ] 18:30以降食べない

## 2025年にやりたい171+αのことの進捗
- [ ] leetcode 1問以上
- 
- 

## それ以外でやったこと
- 
- 
- 

## 本日の評価

"

# ファイルにテキストを書き込み
touch ${posts_path}${filename}
# pwd
echo -e "$content" >> "${posts_path}${filename}"

# 結果を表示
echo "ファイル '${posts_path}${filename}' が作成されました。"
