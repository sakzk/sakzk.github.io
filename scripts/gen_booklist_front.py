import os
import re

# 読書メモは、./wiki/ においていく。

# スクリプトがあるディレクトリ
script_dir = "./scripts"

wiki_dir = "../wiki"

# wiki/ 直下のファイルを列挙する
files = os.listdir(wiki_dir)

# ブログ記事タイトルの【】に応じて、技術書、一般書をそれぞれ保存していく。
techbook_entries = []
generalbook_entries = []
for filename in files:
    filepath = os.path.join(wiki_dir, filename)
    teckbook_match = re.search(r'【技術書】*', filename)
    if teckbook_match:
        techbook_entries.append([filepath, filename])
        continue
    generalbook_match = re.search(r'【書籍】*', filename)
    if generalbook_match:
        generalbook_entries.append([filepath, filename])
        continue
    # 今後ジャンルが増えるかも
    continue

    # mdファイル名ではなく、フロントマターを使う場合はこちらに切り替える
    # ファイルを読みむ→フロントマターをパターンマッチの流れ
    # with open(filepath, 'r', encoding='utf-8') as file:
        # lines = file.readlines()
        # if len(lines) >= 1:
        #     match = re.search(r'category: tech-book', lines[1].strip())
        #     if not match:
        #         continue
            # techbook_entries.append([post_date_YYYY_MM_DD, post_title, filename])

# 書籍リスト記事を生成する。
booklist_header = "# 読んだ本一覧\n\n読書メモへのリンク集です。\n\n"
teckbook_header = "# 技術書一覧\n\n"
teckbook_content = []
# ブログのポストエントリーごとにテキスト化し、リストに追加していく
for filepath, filename in techbook_entries:
    teckbook_content.append(" [" + filename + "](" + filepath + ")\n\n")
generalbook_header = "# 一般書一覧\n\n"
generalbook_content = []
for filepath, filename in generalbook_entries:
    generalbook_content.append(" [" + filename + "](" + filepath + ")\n\n")

# ブログテキストを生成
booklist_text = "".join([booklist_header, teckbook_header, "".join(teckbook_content),
                                        generalbook_header, "".join(generalbook_content)])

# ファイルに書き出す例
output_filename = os.path.join(wiki_dir, "booklist-front.md")  # 出力ファイル名
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(booklist_text)

print(f"ブログ記事一覧を {output_filename} に出力しました。")
