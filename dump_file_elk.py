import sys
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from data_wrangling import data_wrangling

index_name = sys.argv[1]
filepath = sys.argv[2]

es = Elasticsearch([
    {
        'host': 'localhost',
        'port': 9200
    }
])

# settings for mapping data types in file
settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text"
            },
            "category": {
                "type": "text"
            },
            "discription": {
                "type": "text"
            },

        }
    }
}


# create index in elasticsearch
es.indices.create(index=index_name, ignore=[
    400, 404], body=settings)

# dump json file into created index
try:
    res = helpers.bulk(es, data_wrangling(
        filepath), index=index_name)
    print('Elastic data loaded')
except Exception as e:
    print(f'error--> {e}')
