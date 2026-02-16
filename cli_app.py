import argparse
import sys
from core_converter import convert_markdown_to_html

def main():
    parser = argparse.ArgumentParser(description="convert markdown text or file to html")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help="direct markdown text to convert")
    group.add_argument('-f', '--file', help="path to a markdown file convert")

    parser.add_argument('-o', '--output', help="Optional: Path to save the html output file")

    args = parser.parse_args()

    markdown_content = ""
    input_source = ""

    if args.text:
        markdown_content = args.text
        input_source = "direct text"
    elif args.file:
        input_source = args.file
        try:
            with open(args.file, 'r', encoding="utf-8") as f:
                markdown_content = f.read()
        except FileNotFoundError:
            print(f"error: input file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"error: reading file {args.file} : {e}", file=sys.stderr)
            sys.exit(1)

    html_output = convert_markdown_to_html(markdown_content)

    if args.output:
        try:
            with open(args.output, 'w', encoding="utf-8") as f:
                f.write(html_output)
            print(f"successfully converted {input_source} to html: {args.output}")
        except Exception as e:
            print(f"error: writing to output file {args.output} : {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(html_output)

if __name__ == "__main__":
    main()

#command python cli_app.py -f sample_markdown.md -o "converted_html.html"
#command pyinstaller --onefile cli-app.py
#pip freeze > requirements.txt
#python web_app.py