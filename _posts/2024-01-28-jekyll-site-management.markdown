---
layout: post
title:  "jekyllの使い方で気づいたことを書いていく"
date:   2024-01-29 14:00:00 +0900
---

## 2024-01-29 _site/foo.html が生成されない問題を解決した。
問題： _posts/foo.md に対応する _site/foo.html が生成されておらず、そのため index.html 内の記事リンクも生成されていなかった。

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

## 2024-01-30 画像ファイルをpngからwebpにした。
手順：
1. `brew install webp` で cwebp をインストールする
- `brew install cwebp` ではだめ。 `Warning: No available formula with the name "cwebp". Did you mean cweb or webp?` という警告がでるので webp を選ぶ。
2. ブログのディレクトリに移動して、`find . -type f -name "*.png"` で png ファイルを探す。
3. `webp foo.png -o bar.webp` でファイルを変換する。
4. リンクの置換はVSCodeから行った。

今回はファイルが一つしかないことがわかっていたので手作業でやった。今後、画像はwebp ファイルでアップロードしていく。

## 2024-02-22 ローカルサーバーを停止するワンライナーを書いた。

`jekyll serve` で起動したローカルサーバーを止めるワンライナー：
```bash
ps aux | grep "jekyll" | grep -v "grep" | awk "{print \$2}" | xargs kill -SIGINT
```

動機：
ローカルサーバーを起動しているターミナルを探して `Ctrl+C` を入力しにいくのがめんどくさかったから。


以下はメモ：
1. `ps aux` :実行中のプロセスの状態をリストアップするコマンド
2. grepコマンドでjekyllのローカルサーバーが走っているプロセスを特定する。grepコマンドを実行しているプロセス自身もひっかかるので-vで除外する。扱うキーワードが多いときは、-E オプションをつかってもいいけど、パイプでgrepを複数つなぐのが頭を使わずにすむ。
3. awkの2列めのフィールドは `\$2` で指定する。`\`がないと、シェルの早期評価でシェル変数の`$2`がセットされてしまう。
4. `|xargs kill` だけでもプロセスは停止されるが、`SIGTERM`で止めることになり長ったらしいメッセージが表示される。 `-SIGINT` でkillすると、推奨されている Ctrl+C での停止と同様に、なにも表示されずにとまる。

ブログ関連のコマンドは 以下のようにまとめて alias して、`.zshrc` に記述している。

```bash
# commands for blog
# 処理を追加する場合、`bundle exec jekyll serve`は最後におく。
alias blog='cd ~/sakzk-Mysite && ./create_article_file.sh && code . && open -a "/Applications/Microsoft Edge.app" && bundle exec jekyll serve'
alias serv='ps aux | grep "jekyll" | grep -v "grep" | awk "{print \$2}" | xargs kill -SIGINT |
			cd ~/sakzk-mysite && open -a "/Applications/Microsoft Edge.app" && bundle exec jekyll serve'
			# 既存のプロセスが存在するかもしれないので、止めてからserveする。
alias unserv='ps aux | grep "jekyll" | grep -v "grep" | awk "{print \$2}" | xargs kill -SIGINT'
```
