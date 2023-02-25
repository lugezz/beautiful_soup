

def get_html_content(this_url: str, parser: str = 'lxml') -> str:
    with open(this_url, 'r') as html_file:
        content = html_file.read()

    return content


def cache_html_file(path_to_html_file: str, html_content: str):
    with open(path_to_html_file, 'w') as f:
        f.write(html_content)


def clean_text_element(text_element: str):
    return text_element.replace('\n', '').strip()
