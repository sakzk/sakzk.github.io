# 定義
SHELL := /bin/bash
SCRIPTS_DIR := ./scripts

# デフォルトターゲット
# .PHONY: all
# all: front blog wiki

# フロントページを生成
.PHONY: front
front:
	$(SCRIPTS_DIR)/gen_front.sh

# ブログエントリーを生成
.PHONY: blog
blog:
	$(SCRIPTS_DIR)/gen_blog_entry.sh

# ウィキエントリーを生成
.PHONY: wiki
wiki:
	$(SCRIPTS_DIR)/gen_wiki_entry.sh

# すべてのスクリプトを実行
# .PHONY: generate-all
# generate-all: front blog wiki

# クリーンアップ（必要に応じて追加）
# .PHONY: clean
# clean:
# 	echo "Nothing to clean for now."