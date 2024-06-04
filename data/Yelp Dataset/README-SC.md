## 关于数据集

## 背景

此数据集是Yelp商家、评论和用户数据的一个子集。它最初是为Yelp数据集挑战赛组织的，这是一个让学生对Yelp的数据进行研究或分析并分享他们的发现的机会。在最新的数据集中，您将找到关于美国和加拿大8个大都市区的商家信息。

## 内容

该数据集包含五个JSON文件和用户协议。
更多关于这些文件的信息可以在[这里](https://www.yelp.com/dataset)找到。

## 读取文件的代码片段

在Python中，您可以使用json和pandas库来读取JSON文件，如下所示：

```python
import json
import pandas as pd
data_file = open("yelp_academic_dataset_checkin.json")
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
data_file.close()
```

```bash
kaggle datasets download -d yelp-dataset/yelp-dataset
```

## 元数据

```json
{
    "@context": {
        "@language": "zh",
        "@vocab": "https://schema.org/",
        "citeAs": "cr:citeAs",
        "column": "cr:column",
        "conformsTo": "dct:conformsTo",
        "cr": "http://mlcommons.org/croissant/",
        "data": {
            "@id": "cr:data",
            "@type": "@json"
        },
        "dataBiases": "cr:dataBiases",
        "dataCollection": "cr:dataCollection",
        "dataType": {
            "@id": "cr:dataType",
            "@type": "@vocab"
        },
        "dct": "http://purl.org/dc/terms/",
        "extract": "cr:extract",
        "field": "cr:field",
        "fileProperty": "cr:fileProperty",
        "fileObject": "cr:fileObject",
        "fileSet": "cr:fileSet",
        "format": "cr:format",
        "includes": "cr:includes",
        "isEnumeration": "cr:isEnumeration",
        "jsonPath": "cr:jsonPath",
        "key": "cr:key",
        "md5": "cr:md5",
        "parentField": "cr:parentField",
        "path": "cr:path",
        "personalSensitiveInformation": "cr:personalSensitiveInformation",
        "recordSet": "cr:recordSet",
        "references": "cr:references",
        "regex": "cr:regex",
        "repeated": "cr:repeated",
        "replace": "cr:replace",
        "sc": "https://schema.org/",
        "separator": "cr:separator",
        "source": "cr:source",
        "subField": "cr:subField",
        "transform": "cr:transform",
        "wd": "https://www.wikidata.org/wiki/"
    },
    "alternateName": "评论、商家、用户、提示和签到数据的宝库！",
    "conformsTo": "http://mlcommons.org/croissant/1.0",
    "license": {
        "@type": "sc:CreativeWork",
        "name": "其他（说明中指定）"
    },
    "distribution": [
        {
            "contentUrl": "https://www.kaggle.com/api/v1/datasets/download/yelp-dataset/yelp-dataset?datasetVersionNumber=4",
            "contentSize": "4.074 GB",
            "md5": "HCum2fdmoPkhtjie2rukYg==",
            "encodingFormat": "application/zip",
            "@id": "archive.zip",
            "@type": "cr:FileObject",
            "name": "archive.zip",
            "description": "包含Yelp数据集所有内容的压缩包"
        },
        {
            "includes": "*.json",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/json",
            "@id": "application-json_fileset",
            "@type": "cr:FileSet",
            "name": "application/json文件",
            "description": "包含于archive.zip中的application/json文件"
        },
        {
            "includes": "*.pdf",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/pdf",
            "@id": "application-pdf_fileset",
            "@type": "cr:FileSet",
            "name": "application/pdf文件",
            "description": "包含于archive.zip中的application/pdf文件"
        }
    ],
    "version": 4,
    "keywords": [
        "主题> 地球与自然"
    ],
    "isAccessibleForFree": true,
    "includedInDataCatalog": {
        "@type": "sc:DataCatalog",
        "name": "Kaggle",
        "url": "https://www.kaggle.com"
    },
    "creator": {
        "@type": "sc:Organization",
        "name": "Yelp, Inc.",
        "url": "/organizations/yelp-dataset",
        "image": "https://storage.googleapis.com/kaggle-organizations/1029/thumbnail.png%3Fr=326"
    },
    "publisher": {
        "@type": "sc:Organization",
        "name": "Kaggle",
        "url": "https://www.kaggle.com/organizations/kaggle",
        "image": "https://storage.googleapis.com/kaggle-organizations/4/thumbnail.png"
    },
    "thumbnailUrl": "https://storage.googleapis.com/kaggle-datasets-images/10100/14228/93b5be3d6f8ba782a81c55f0cd76c8ba/dataset-card.png?t=2018-01-17-17-50-01",
    "dateModified": "2022-03-17T22:59:01.257",
    "datePublished": "2018-01-17T17:27:37.527",
    "@type": "sc:Dataset",
    "name": "Yelp数据集",
    "url": "https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/versions/4",
    "description": "## 背景\n\n该数据集是Yelp的商家、评论和用户数据的一个子集。最初为Yelp数据集挑战赛组织，这是一个让学生对Yelp的数据进行研究或分析并分享他们的发现的机会。在最新的数据集中，您会发现美国和加拿大地区8个都会区的商家信息。\n\n## 内容\u003Cbr\u003E\n这个数据集包含五个JSON文件和用户协议。\n更多关于这些文件的信息可以在[这里](https://www.yelp.com/dataset)找到。\n\n## 代码片段来读取文件\n\n在Python中，您可以这样读取JSON文件（使用json和pandas库）:\n\n\u0060\u0060\u0060\nimport json\nimport pandas as pd\ndata_file = open(\u0022yelp_academic_dataset_checkin.json\u0022)\ndata = []\nfor line in data_file:\n\u0026nbsp;data.append(json.loads(line))\ncheckin_df = pd.DataFrame(data)\ndata_file.close()\n\n\u0060\u0060\u0060"
}
```
