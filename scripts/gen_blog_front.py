import os
import re

# スクリプトがあるディレクトリ
script_dir = "./scripts"

# _posts ディレクトリのパス
posts_dir = "../_posts"

wiki_dir = "../wiki"
# _posts ディレクトリ直下のファイルを列挙する
# 新着順にするために、ファイル名 (プレフィクスはYYYY-MM_DD) で逆順にソート
files = sorted(os.listdir(posts_dir), reverse=True)

post_entries = []

# ファイルごとに処理
for filename in files:
    filepath = os.path.join(posts_dir, filename)
    # 最初の3行を読み込む
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 最初の3行が取得できる場合のみ処理する
        if len(lines) >= 3:
            # title: "" はマッチしないタイトルとして弾く。
            match = re.search(r'title: "(.*)"', lines[1].strip())
            if not match:
                continue
            post_title = match.group(1)
            # タイトルが空文字でない場合のみリストに追加
            if post_title:
                post_date_YYYY_MM_DD = filename[:10]  # ファイル名から日付部分を取得
                post_path = filename  # ファイル名そのままをパスとする
                # [date, title, file_name] の形式でリストに追加
                post_entries.append([post_date_YYYY_MM_DD, post_title, post_path])

# ブログのコンテンツを格納するリスト
blog_content = []
blog_header = "# ブログ記事一覧 (新着順)\n日記的性格の強いものは時系列でまとめています。\n\n"

# ブログのポストエントリーごとにテキスト化し、リストに追加していく
for post_entry in post_entries:
    post_date_YYYY_MM_DD = post_entry[0]
    post_title = post_entry[1]
    post_path = post_entry[2]
    blog_content.append(post_date_YYYY_MM_DD + " [" + post_title + "](" + posts_dir + "/" + post_path + ")\n\n")

# ブログテキストを生成
blog_text = blog_header + "".join(blog_content)

# ファイルに書き出す例
output_filename = os.path.join(wiki_dir, "blog-front.md")  # 出力ファイル名
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(blog_text)

print(f"ブログ記事一覧を {output_filename} に出力しました。")
