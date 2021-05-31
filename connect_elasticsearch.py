from elasticsearch import Elasticsearch


def connect_elk():
    es = Elasticsearch([
        {
            'host': 'localhost',
            'port': 9200
        }
    ])
    return es