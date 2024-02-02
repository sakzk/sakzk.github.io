---
layout: post
title:  "浅井健一『プログラミングの基礎』を読みはじめる Day 1"
date:   2024-02-02 08:00:00 +0900
---
# やったこと
浅井健一『プログラミングの基礎』を読むために、M1 mac 上で Ocaml の開発、実行環境を整えた。


# 環境構築のためにターミナル上で実行したコマンドは以下の通り。
```
brew install opam
opam init --compiler=4.12.0 		# --compiler=3.09.3 はエラー
eval $(opam env --switch=4.12.0)	# Ocamlのバージョンを指定する
opam install dune			# ビルドツール
opam install merlin			# Ocaml Platform を使うのに必要
opam install utop			# 高機能なREPL環境
```

これで、opam のインストールと opam 実行環境の初期化が完了し、高機能なREPLがゲットできた。

これらの動作を確認したあと、Visual Studio Code の拡張である Ocaml Platform をインストールした。


# `opam init` で生じた問題と解決
問題：`opam init --compiler=3.09.3` (『プログラミングの基礎』1章に記載のバージョン, M1 mac上)  と実行すると、以下のようなエラーが出た。

```
❯ opam init --compiler=3.09.3
(中略)
<><> Installing new switch packages <><><><><><><><><><><><><><><><><><><><><><>
Switch invariant: ["ocaml-base-compiler" {= "3.09.3"} | "ocaml-system" {= "3.09.3"}]
[ERROR] Could not determine which packages to install for this switch:
  * Missing dependency:
    - ocaml-base-compiler = 3.09.3 | ocaml-system = 3.09.3
    unmet availability conditions: 'arch != "arm64" & arch != "arm32" & arch != "ppc64"'
    unmet availability conditions: 'sys-ocaml-version = "3.09.3"'

Switch initialisation failed: clean up? ('n' will leave the switch partially installed) [Y/n]
[NOTE] Opam has been initialised, but the initial switch creation failed.
       Use 'opam switch create <compiler>' to get started.
```

解決：`opam init --compiler=4.12.0` でやる。
.zshrc に書き込むか？と問われるので y を押す。


# REPL おためし
- `ocaml` コマンドでREPLを起動する。

```
❯ ocaml
        OCaml version 4.12.0

# "あ"
  ;;
- : string = "あ"
#
```

- Ctrl+D でREPLから抜ける。

- `# use "foo.ml";;` でREPLからファイルを実行する。

```
❯ cat sample.ml
print_endline "Do you see me? 見えてる？";;
❯ ocaml
        OCaml version 4.12.0

# #use "sample.ml";;
Do you see me? 見えてる？
- : unit = ()
```

- `rlwrap ocaml` で起動するとシェルのキーバインディングが有効になるので便利。
例は割愛

## utop おためし

標準のREPLは出力が見にくいしシェルのキーバインディングも効かない。ハイライティングを求めて [utop](https://opam.ocaml.org/packages/utop/) を見つけたのでつかうことにする。

ビフォー：
```
❯ ocaml
        OCaml version 4.12.0

# "Salut OCaml, enchanté !";;
- : string = "Salut OCaml, enchanté !"
```
アフター：
```
❯ utop
────────┬──────────────────────────────────────────────────────────────┬────────
        │ Welcome to utop version 2.13.1 (using OCaml version 4.12.0)! │
        └──────────────────────────────────────────────────────────────┘

Type #utop_help for help about using utop.

─( 12:56:55 )─< command 0 >──────────────────────────────────────{ counter: 0 }─
utop # "Salut OCaml, enchanté !";;
- : string = "Salut OCaml, enchanté !"
─( 12:56:55 )─< command 1 >──────────────────────────────────────{ counter: 0 }─
utop #
┌───┬─────┬───────────┬──────────────┬──────┬────────┬────┬──────┬─────┬───────┐
│Arg│Array│ArrayLabels│Assert_failure│Atomic│Bigarray│Bool│Buffer│Bytes│BytesLa│
└───┴─────┴───────────┴──────────────┴──────┴────────┴────┴──────┴─────┴───────┘
```
(実際の出力はシンタックスハイライティングが効いている)

入力候補も表示され、とても見やすくなった！

# dune を使ったビルドについて
索引に dune が乗っていなかったので、教科書内では dune を使用しないと思われる。dune コマンドの使い方は調べきれていないので割愛。
