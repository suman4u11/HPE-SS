
description = 'Search an article in Wikipedia'

pages = []

def setup(data):
    pass

def test(data):
    navigate('http://en.wikipedia.org/')
    send_keys(('id', 'searchInput'), 'automation')
    click(('id', 'searchButton'))
    verify_text_in_element(('id', 'firstHeading'), 'Automation')

def teardown(data):
    close()
