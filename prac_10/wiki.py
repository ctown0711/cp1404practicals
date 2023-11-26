import wikipedia

search_prompt = input("Search for a page: ")
while search_prompt != '':
    try:
        page = wikipedia.page(search_prompt)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_prompt = input("Search for a page: ")

