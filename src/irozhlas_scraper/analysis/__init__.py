# -*- coding: utf-8 -*-

import os
import requests as rq

from dataclasses import dataclass
from typing import Iterable, Dict, Generator

"""
Example how to use Geneea API in three simple steps:

1. Load the input data
2: Analyze them
3. Save the results

This is a simple pipeline: [load] -> [analyze] -> [save]

What about monadic API ? :)
see for example http://soshnikov.com/mPyPl/

"""

__all__ = tuple(["main"])


# #############################################################################
# Domain model: entities / value objects (mostly)
# #############################################################################

@dataclass(frozen=True, eq=True)
class AnalysisResult:
    """
    The text model contains the original and analyzed content.
    """
    original: str
    analyzed: str


# #############################################################################
# Application services
# #############################################################################

def load_texts() -> Iterable[Dict[str, str]]:
     for text in [
            {"text": "Lezec Ondra si po boulderingu polepšil, patří mu šestá postupová příčka."},
            {"text": "Hrozně jsem si přála hodit pro Janečka, posteskla si oštěpařka Špotáková"},
            {"text": "Jeden z největších přestupů fotbalové historie je skutečností, Lionel Messi je definitivně hráčem Paris Saint-Germain. Po úterním příletu do francouzské metropole a podpisu smlouvy probíhá v těchto chvílích oficiální představení a tisková konference, na které Messi poprvé v profesionální kariéře mluví k veřejnosti jako hráč jiného klubu než Barcelony."}
        ]: yield text


def analyze_texts(texts: Iterable[Dict[str, str]], key: str) -> 'Generator[AnalysisResult, None]':
    """
    Return the analyzed texts.
    """
    url="https://api.geneea.com/v3/analysis/T:CRo-transcripts"

    headers = {
        "Content-type": "application/json",
        "Authorization": f"user_key {key}"
    }

    for text in texts:
        json = rq.post(url, json=text, headers=headers).json()
        yield AnalysisResult(original=text, analyzed=json)


def save_texts(texts: Iterable[AnalysisResult]) -> None:
    print("The texts were saved!")


def main():
    try:
        # [1] Configure the application before run.
        GENEEA_PRIVATE_KEY: str = os.environ.get("GENEEA_KEY")

        # [2] Read the texts from storage and them in iterable.
        # [3] Analyze texts and store results somewhere.
        results = analyze_texts(
            texts=load_texts(),
            key=GENEEA_PRIVATE_KEY
        )

        # [4] Save the results
        save_texts(results)

        # Demo: print the content.
        for result in results:
            print(result)

    except Exception as ex:
        print(ex)
