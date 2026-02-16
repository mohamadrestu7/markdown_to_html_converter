import markdown

def convert_markdown_to_html(markdown_text):
    try:
        html = markdown.markdown(markdown_text, extensions=["fenced_code", "tables"])
        return html
    except Exception as e:
        return f"Error converting Markdow: {e}"
    
if __name__ == "__main__":
    sample_markdown = """

    # Hello World!

    this is a *simple* example.

    - Item 1
    - Item 2

    ```python
    print("hello from code block")

    """ 

    html_output = convert_markdown_to_html(sample_markdown)
    print(sample_markdown)
    print(html_output)