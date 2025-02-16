## About Dataset

## Context

This dataset is a subset of Yelp's businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. In the most recent dataset you'll find information about businesses across 8 metropolitan areas in the USA and Canada. 

## Content 

This dataset contains five JSON files and the user agreement. More information about those files can be found [here](https://www.yelp.com/dataset).

## Code snippet to read the files

in Python, you can read the JSON files like this (using the json and pandas libraries):

```python
import json
import pandas as pd
data_file = open("yelp_academic_dataset_checkin.json")
data = []
for line in data_file:
&nbsp;data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
data_file.close()
```

```bash
kaggle datasets download -d yelp-dataset/yelp-dataset
```

## Metadata

```json
{
    "@context": {
        "@language": "en",
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
    "alternateName": "A trove of reviews, businesses, users, tips, and check-in data!",
    "conformsTo": "http://mlcommons.org/croissant/1.0",
    "license": {
        "@type": "sc:CreativeWork",
        "name": "Other (specified in description)"
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
            "description": "Archive containing all the contents of the Yelp Dataset dataset"
        },
        {
            "includes": "*.json",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/json",
            "@id": "application-json_fileset",
            "@type": "cr:FileSet",
            "name": "application/json files",
            "description": "application/json files contained in archive.zip"
        },
        {
            "includes": "*.pdf",
            "containedIn": {
                "@id": "archive.zip"
            },
            "encodingFormat": "application/pdf",
            "@id": "application-pdf_fileset",
            "@type": "cr:FileSet",
            "name": "application/pdf files",
            "description": "application/pdf files contained in archive.zip"
        }
    ],
    "version": 4,
    "keywords": [
        "subject \u003E earth and nature"
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
    "name": "Yelp Dataset",
    "url": "https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/versions/4",
    "description": "## Context\n\nThis dataset is a subset of Yelp\u0027s businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp\u0027s data and share their discoveries.  In the most recent dataset you\u0027ll find information about businesses across 8 metropolitan areas in the USA and Canada. \n\n## Content\u003Cbr\u003E\nThis dataset contains five JSON files and the user agreement.\nMore information about those files can be found [here](https://www.yelp.com/dataset).\n\n## Code snippet to read the files\n\nin Python, you can read the JSON files like this (using the json and pandas libraries):\n\n\u0060\u0060\u0060\nimport json\nimport pandas as pd\ndata_file = open(\u0022yelp_academic_dataset_checkin.json\u0022)\ndata = []\nfor line in data_file:\n\u0026nbsp;data.append(json.loads(line))\ncheckin_df = pd.DataFrame(data)\ndata_file.close()\n\n\u0060\u0060\u0060"
}
```

