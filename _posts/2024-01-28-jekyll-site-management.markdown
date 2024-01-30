---
layout: post
title:  "jekyllの使い方で気づいたことを書いていく"
date:   2024-01-29 14:00:00 +0900
---

## 2024-01-29
問題： .md に対応する .html が生成されておらず、そのため index.html 内の記事リンクも生成されていなかった。

原因：front matter に `categories: test` と書いていた。

対策：front matter の categories がなくても _site 内に .html が生成できたし、
記事分類のこうもり問題を避けるためにも categories はつかわないことにする。

なお、ビルド時に .md に対応する .html が _site/ に作られるための必要条件には以下のものがある。
1. dateが現在時刻よりまえ
2. markdownのファイル名が日付だけではない
3. titleが空欄ではない

.md ファイルを生成するスクリプトは
[create_article_file.sh](https://github.com/sakzk/sakzk.github.io/blob/main/create_article_file.sh)。
このスクリプトは_siteには不必要なので_config.ymlのexcludeに追加しておく。
