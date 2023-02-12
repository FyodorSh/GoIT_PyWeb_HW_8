import json

from models import Author, Quote
import connect

authors = []
with open('authors.json', encoding='utf-8') as f:
    authors = json.load(f)

    for author in authors:
        authors_obj = Author.objects(fullname=author['fullname'])
        if not authors_obj:
            author_new = Author(**author)
            author_new.save()


with open('qoutes.json', encoding='utf-8') as f:
    qoutes = json.load(f)

    for quote in qoutes:
        quotes_obj = Quote.objects(quote=quote['quote'])
        if quotes_obj:
            break

        quote_new = Quote()
        quote_new.quote = quote['quote']
        quote_new.tags = quote['tags']
        authors = Author.objects(fullname=quote['author'])
        if authors:
            quote_new.author = authors[0]
        quote_new.save()
