# iRozhlas Analysis with Geneea API

## Installation

Add `GENEEA_KEY` to environment variables.

## Usage

Run

    python geneea-demo

Results

```json
{
  "text":"Jeden z největších přestupů fotbalové historie je skutečností, Lionel Messi je definitivně hráčem Paris Saint-Germain. Po úterním příletu do francouzské metropole a podpisu smlouvy probíhá v těchto chvílích oficiální představení a tisková konference, na které Messi poprvé v profesionální kariéře mluví k veřejnosti jako hráč jiného klubu než Barcelony."
},
"analyzed="{
  "version":"3.2.1",
  "language":{
    "detected":"cs"
  },
  "entities":[
    {
      "id":"e0",
      "gkbId":"G615",
      "stdForm":"Lionel Messi",
      "type":"person"
    },
    {
      "id":"e1",
      "gkbId":"G483020",
      "stdForm":"Paris Saint-Germain FC",
      "type":"organization"
    },
    {
      "id":"e2",
      "gkbId":"G1492",
      "stdForm":"Barcelona",
      "type":"location"
    },
    {
      "id":"e3",
      "gkbId":"G309",
      "stdForm":"historie",
      "type":"general"
    },
    {
      "id":"e4",
      "stdForm":"představení",
      "type":"general"
    },
    {
      "id":"e5",
      "gkbId":"G272281",
      "stdForm":"tisková konference",
      "type":"general"
    },
    {
      "id":"e6",
      "gkbId":"G282049",
      "stdForm":"kariéra",
      "type":"general"
    }
  ],
  "tags":[
    {
      "id":"t3",
      "stdForm":"Unknown",
      "type":"category",
      "relevance":0.0
    }
  ],
  "docSentiment":{
    "mean":0.0,
    "label":"neutral",
    "positive":0.0,
    "negative":0.0
  },
  "itemSentiments":{
    "e5":{
      "mean":0.3,
      "label":"positive",
      "positive":0.3,
      "negative":0.0
    },
    "e6":{
      "mean":0.3,
      "label":"positive",
      "positive":0.3,
      "negative":0.0
    },
    "e0":{
      "mean":0.1,
      "label":"positive",
      "positive":0.1,
      "negative":0.0
    },
    "e1":{
      "mean":0.0,
      "label":"neutral",
      "positive":0.0,
      "negative":0.0
    },
    "e2":{
      "mean":0.3,
      "label":"positive",
      "positive":0.3,
      "negative":0.0
    },
    "e3":{
      "mean":0.0,
      "label":"neutral",
      "positive":0.0,
      "negative":0.0
    },
    "e4":{
      "mean":0.3,
      "label":"positive",
      "positive":0.3,
      "negative":0.0
    }
  },
  "usedChars":353
}
```