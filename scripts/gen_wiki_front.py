import os
import re

# スクリプトがあるディレクトリ
script_dir = "./scripts"

wiki_dir = "../wiki"
# _wikis ディレクトリ直下のファイルを列挙する
# 新着順にするために、ファイル名 (プレフィクスはYYYY-MM_DD) で逆順にソート
files = sorted(os.listdir(wiki_dir), reverse=True)

wiki_entries = []

# ファイルごとに処理
for filename in files:
    filepath = os.path.join(wiki_dir, filename)
    # 書籍は弾く。(`booklist-front.md` に一元化するため。)
    if "【技術書】" in filepath or "【書籍】" in filepath:
        continue
    # 最初の3行を読み込む
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 最初の3行が取得できない場合は不正な記事としみなして弾く。
        if len(lines) >= 3:
            # title: "" は不正な記事とみなして弾く。
            match = re.search(r'title: "(.*)"', lines[1].strip())
            if not match:
                continue
            wiki_title = match.group(1)
            # タイトルが空文字でない場合のみリストに追加
            if wiki_title:
                wiki_date_YYYY_MM_DD = filename[:10]  # ファイル名から日付部分を取得
                wiki_path = filename  # ファイル名そのままをパスとする
                # [date, title, file_name] の形式でリストに追加
                wiki_entries.append([wiki_date_YYYY_MM_DD, wiki_title, wiki_path])

# ブログのコンテンツを格納するリスト
article_content = []
article_header = "# wiki記事一覧 (新着順)\nwiki記事を時系列でまとめています。(読書メモ除く)\n読書メモは[こちら](https://sakzk.github.io/booklist-front)から\n\n"

# ブログのポストエントリーごとにテキスト化し、リストに追加していく
for wiki_entry in wiki_entries:
    wiki_date_YYYY_MM_DD = wiki_entry[0]
    wiki_title = wiki_entry[1]
    wiki_path = wiki_entry[2]
    article_content.append(wiki_date_YYYY_MM_DD + " [" + wiki_title + "](" + wiki_dir + "/" + wiki_path + ")\n\n")

# ブログテキストを生成
article_text = article_header + "".join(article_content)

# ファイルに書き出す例
output_filename = os.path.join(wiki_dir, "wiki-front.md")  # 出力ファイル名
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(article_text)

print(f"wiki記事一覧を {output_filename} に出力しました。")