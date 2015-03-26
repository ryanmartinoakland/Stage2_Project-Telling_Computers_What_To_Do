#This code takes a list of urls, and URL titles and creates html links for them.

def generate_link_HTML(url, url_text):
    html_text_1 = '''
<div class="stage2_project">
    <div class="concept-title">
        <a href="''' + url 
    html_text_2 = '">' + url_text
    html_text_3 = '''</a>
        </div>
    </div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(links_list):
    url = links_list[0]
    url_text = links_list[1]
    return generate_link_HTML(url, url_text)

EXAMPLE_LIST_OF_LINKS = [ ['http://www.google.com', 'Google'],
                             ['http://www.udacity.com', 'Udacity'],
                             ['http://www.amazon.com', 'Amazon'] ]


def make_HTML_for_many_links(list_of_links):
    HTML = ""
    for concept in list_of_links:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_links(EXAMPLE_LIST_OF_LINKS)
