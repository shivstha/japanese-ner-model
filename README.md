# Named Entity Recognition Using Python spaCy of Elasticsearch Index Data
## What is Named Entity Recognition?

Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

## Named-entity recognition platforms
Notable NER platforms include:

- SpaCy features fast statistical NER as well as an open-source named-entity visualizer.
- GATE supports NER across many languages and domains out of the box, usable via a graphical interface and a Java API.
- OpenNLP includes rule-based and statistical named-entity recognition.


## About spaCy Natural Language Processing
spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.

spaCy features an extremely fast statistical entity recognition system, that assigns labels to contiguous spans of tokens. The default trained pipelines can indentify a variety of named and numeric entities, including companies, locations, organizations and products. You can add arbitrary classes to the entity recognition system, and update the model with new examples.

spaCy provides different language supported models such small, medium, and large trained models that we can use to find named entity from the text.

We can also customized the model according to our data to grasp the maximum accuracy by training the model which is the wonderful feature supported by spaCy.

## What we have done in this project?

- Use of elasticsearch to index data for faster retrieval of information
- Pandas library of Python for performing data wrangling of provided json, csv or any other supported files.
- Use of spaCy library to detect named entity recognition of data fetch from search query in elasticsearch.
- Finally save the output file of obtained data in the text format. 

## To run this project follow these steps:
```javascript
git clone https://github.com/shivstha/japanese-ner-model.git
```
```python
pip install -r requirements.txt
```
Note: Make sure to run elasticsearch in your pc

### To dump json file into elasticsearch
```python
python dump_file_elk.py "japan-ner" "data.json"
```
### To perform search query in elasticsearch and saving data of ner in text format
```python
python main.py "自動車保険" "japan-ner" "file-1.txt" 
```



