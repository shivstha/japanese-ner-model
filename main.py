import spacy
from elasticsearch import Elasticsearch
import pandas as pd
from tabulate import tabulate
import sys

query_name = sys.argv[1]
index_name = sys.argv[2]
output_filename = sys.argv[3]

es = Elasticsearch([
    {
        'host': 'localhost',
        'port': 9200
    }
])


# search query for elastic search
search_query = {
    "size": 10,
    "query": {
        "multi_match": {
            "query": query_name,
            "fields": [
                "title",
                "discription"]
        }
    }
}

search_data = es.search(body=search_query, index=index_name)

datas = search_data['hits']['hits']
s_df = pd.DataFrame(datas)
source_data = s_df['_source']

nlp = spacy.load("ja_core_news_md")


def japan_ner(nlp, sentence):
    doc = nlp(sentence)
    headers = ['Token', 'NER']
    list1 = list()
    for token in doc:
        if token.ent_type != 0:
            list1.append([token.text, token.ent_type_])
    return doc.text, tabulate(list1, headers, tablefmt="grid")


f = open(output_filename, "a+", encoding='utf8')
for i in source_data:
    headline, listvalues = japan_ner(nlp, i['discription'])
    f.write(f'Search Result -> {headline}')
    f.write('\n')
    f.write(listvalues)
    f.write('\n\n')
f.close()
