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
Syntax:
```python
python dump_file_elk.py <index-name> <file-path>
```

```python
python dump_file_elk.py "japan-ner" "data.json"
```
### To perform search query in elasticsearch and saving data of ner in text format
Syntax:
```python
python main.py <search-phrase> <dumped-index-name> <output filename>
```

```python
python main.py "自動車保険" "japan-ner" "file-1.txt" 
```


### Expected output from file=1.txt file

Search Result -> 用途・車種が、自家用普通乗用車、自家用小型乗用車、自家用軽四輪乗用車、自家用小型貨物車、自家用軽四輪貨物車、自家用普通貨物車（最大積載量0.5トン以下）、自家用普通貨物車（最大積載量0.5トン超2トン以下）、特種用途自動車（キャンピング車）の自動車です。（注）二輪自動車や原動機付自転車は含まれません
+---------+----------+
| Token   | NER      |
+=========+==========+
| 0.5     | QUANTITY |
+---------+----------+
| トン      | QUANTITY |
+---------+----------+
| 0.5     | QUANTITY |
+---------+----------+
| トン      | QUANTITY |
+---------+----------+
| 2       | QUANTITY |
+---------+----------+
| トン      | QUANTITY |
+---------+----------+
| 二輪      | QUANTITY |
+---------+----------+
| 自動車     | QUANTITY |
+---------+----------+

Search Result -> 自らが所有・使用し自動車保険を締結している自動車が9台以下のご契約者です
+---------+----------+
| Token   | NER      |
+=========+==========+
| 9       | QUANTITY |
+---------+----------+
| 台       | QUANTITY |
+---------+----------+

Search Result -> 保険をつける対象のことです。火災保険では建物・家財、自動車保険では自動車です。
+---------+-------+
| Token   | NER   |
+=========+=======+
+---------+-------+

Search Result -> 自らが所有・使用し自動車保険を締結している自動車が10台以上のご契約者のことです
+---------+----------+
| Token   | NER      |
+=========+==========+
| 10      | QUANTITY |
+---------+----------+
| 台       | QUANTITY |
+---------+----------+

Search Result -> 買い替えなどで新たに取得した自動車を、保険契約者の請求により保険証券記載の自動車（被保険自動車）と入れ替えることをです。被保険自動車の入れ替えは通知義務があり、通知がないと保険金をお支払できない場合があります
+---------+-------+
| Token   | NER   |
+=========+=======+
+---------+-------+

Search Result -> 総排気量125cc以下の二輪自動車、および総排気量50cc以下の三輪以上の自動車です。ただし、総排気量50cc超125cc以下、または定格出力0.6kw超1.0kw以下の「側車（サイドカー）付二輪自動車」は対象となりません
+---------+----------+
| Token   | NER      |
+=========+==========+
| 125     | QUANTITY |
+---------+----------+
| cc      | QUANTITY |
+---------+----------+
| 二       | QUANTITY |
+---------+----------+
| 輪       | QUANTITY |
+---------+----------+
| 50      | QUANTITY |
+---------+----------+
| cc      | QUANTITY |
+---------+----------+
| 三       | QUANTITY |
+---------+----------+
| 輪       | QUANTITY |
+---------+----------+
| 50      | QUANTITY |
+---------+----------+
| cc      | QUANTITY |
+---------+----------+
| 125     | QUANTITY |
+---------+----------+
| cc      | QUANTITY |
+---------+----------+
| 0.6     | QUANTITY |
+---------+----------+
| kw      | QUANTITY |
+---------+----------+
| 1.0     | QUANTITY |
+---------+----------+
| kw      | QUANTITY |
+---------+----------+
| 二       | QUANTITY |
+---------+----------+
| 輪       | QUANTITY |
+---------+----------+

Search Result -> 「自動車損害賠償保障法」に基づく自動車損害賠償責任保険（いわゆる自賠責保険、強制保険）、「原子力損害の賠償に関する法律」にもとづく原子力損害賠償責任保険などがです。
+---------+-------+
| Token   | NER   |
+=========+=======+
| 原子      | ORG   |
+---------+-------+
| 力       | ORG   |
+---------+-------+
| 損害      | ORG   |
+---------+-------+
| 原子      | ORG   |
+---------+-------+
| 力       | ORG   |
+---------+-------+
| 損害      | ORG   |
+---------+-------+
| 賠償      | ORG   |
+---------+-------+
| 責任      | ORG   |
+---------+-------+
| 保険      | ORG   |
+---------+-------+

Search Result -> 自動車損害賠償保障法ですべての自動車やバイクに加入が義務付けられている強制保険（責任保険または責任共済）です。自動車、バイクの運行による対人賠償事故の損害が保険金支払対象です。保険金支払限度額は、死亡3,000万円、後遺障害4,000万円、傷害120万円です
+---------+-------+
| Token   | NER   |
+=========+=======+
| 3,000万  | MONEY |
+---------+-------+
| 円       | MONEY |
+---------+-------+
| 4,000万  | MONEY |
+---------+-------+
| 円       | MONEY |
+---------+-------+
| 120万    | MONEY |
+---------+-------+
| 円       | MONEY |
+---------+-------+

Search Result -> 損害保険は、リスク（事故にあう確率と予想される損害の大小）にもとづき保険料が決定されます。リスクをこれまで以上に細かく分けて保険料を算出する自動車保険です。
+---------+-------+
| Token   | NER   |
+=========+=======+
+---------+-------+

Search Result -> ご契約のお車と同一の用途、車種、車名、型式、仕様、年式で、同等の損耗度の自動車を自動車販売店などが顧客に販売する店頭渡現金販売価格相当額です。当社が別に定める「自動車保険車両標準価格表」などに記載した価格、または当社が別に定める方法に従ってその他の客観的資料により算出した価格です
+---------+-------+
| Token   | NER   |
+=========+=======+
+---------+-------+

