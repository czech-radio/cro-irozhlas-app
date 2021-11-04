# Requests

## Installation

Add `GENEEA_KEY` to environment variables.

## Usage

Run

    python geneea-demo

Results

    Result(original={'text': 'Lezec Ondra si po boulderingu polepšil, patří mu šestá postupová příčka.'}, analyzed={'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'Ondra', 'type': 'person'}], 'tags': [{'id': 't1', 'stdForm': 'Unknown', 'type': 'category', 'relevance': 0.0}], 'docSentiment': {'mean': 0.0, 'label': 'neutral', 'positive': 0.0, 'negative': 0.0}, 'itemSentiments': {'e0': {'mean': 0.0, 'label': 'neutral', 'positive': 0.0, 'negative': 0.0}}, 'usedChars': 100})
    Result(original={'text': 'Hrozně jsem si přála hodit pro Janečka, posteskla si oštěpařka Špotáková'}, analyzed={'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'Janeček', 'type': 'person'}, {'id': 'e1', 'stdForm': 'Špotáková', 'type': 'person'}], 'tags': [{'id': 't1', 'stdForm': 'Unknown', 'type': 'category', 'relevance': 0.0}], 'docSentiment': {'mean': 0.0, 'label': 'neutral', 'positive': 0.0, 'negative': 0.0}, 'itemSentiments': {'e1': {'mean': 0.0, 'label': 'neutral', 'positive': 0.0, 'negative': 0.0}, 'e0': {'mean': 0.0, 'label': 'neutral', 'positive': 0.0, 'negative': 0.0}}, 'usedChars': 100})
