import os
import re

# 定数の定義
SCRIPT_DIR = "../scripts"
POSTS_DIR = "../_posts"
WIKI_DIR = "../wiki"
OUTPUT_FILENAME_BLOG = os.path.join(WIKI_DIR, "blog-front.md")
OUTPUT_FILENAME_WIKI = os.path.join(WIKI_DIR, "wiki-front.md")
OUTPUT_FILENAME_BOOK = os.path.join(WIKI_DIR, "booklist-front.md")

def get_files_newest_first(posts_dir):
    """_posts ディレクトリ内のファイルを新着順に取得"""
    files = sorted(os.listdir(posts_dir), reverse=True)
    return files

def is_ready_publish(lines):
    """記事が有効かどうかを判定する"""
    if len(lines) < 2 or "" in lines:
        return False
    match = re.search(r'title: "(.*)"', lines[1].strip())
    return bool(match and match.group(1))

def extract_post_info(filename, lines):
    """記事情報（タイトル、日付、パス）を抽出"""
    match = re.search(r'title: "(.*)"', lines[1].strip())
    post_title = match.group(1) if match else ""
    post_date_YYYY_MM_DD = filename[:10]  # ファイル名から日付部分を取得
    return post_date_YYYY_MM_DD, post_title, filename

def process_files(files, posts_dir):
    """ファイルごとに処理を行い、記事情報をリストに追加"""
    post_entries = []
    for filename in files:
        if filename.startswith("_"):  # 下書きファイルをスキップ
            continue

        filepath = os.path.join(posts_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                if is_ready_publish(lines):
                    post_info = extract_post_info(filename, lines)
                    post_entries.append(post_info)
        except (OSError, IOError) as e:
            print(f"ファイル {filename} の処理中にエラーが発生しました: {e}")
    
    return post_entries

def generate_blog_list_page(post_entries):
    """ブログコンテンツを生成"""
    blog_header = "# ブログ記事一覧 (新着順)\n日記的性格の強いものは時系列でまとめています。\n\n"
    blog_content = []

    for post_date_YYYY_MM_DD, post_title, post_path in post_entries:
        post_link = f"{POSTS_DIR}/{post_path}"
        blog_content.append(f"{post_date_YYYY_MM_DD} [{post_title}]({post_link})\n\n")

    return blog_header + "".join(blog_content)

def write_blog_to_file(blog_text, output_filename):
    """ブログテキストをファイルに書き出す"""
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(blog_text)
        print(f"ブログ記事一覧を {output_filename} に出力しました。", end="")
    except (OSError, IOError) as e:
        print(f"ファイル {output_filename} の書き込み中にエラーが発生しました: {e}")

def main():
    # ファイルを処理し、記事情報を取得
    files = get_files_newest_first(POSTS_DIR)
    post_entries = process_files(files, POSTS_DIR)

    # ブログコンテンツを生成
    blog_text = generate_blog_list_page(post_entries)

    # ブログテキストをファイルに書き出す
    write_blog_to_file(blog_text, OUTPUT_FILENAME_BLOG)

if __name__ == "__main__":
    main()

# TODO: make でフラグ引数をオプショナルで受け取って、pythonスクリプトに渡す
# TODO: python スクリプトでコマンドライン引数を受け取る
# TODO: 引数ごとの分岐
# TODO: 関数名、変数名をいい感じに。
# TODO: 「ブログ」となっているところを、一般化（wiki, 書籍） article あたりでよさそう
    # DONE: OUTPUT_FILENAME_X 細分化