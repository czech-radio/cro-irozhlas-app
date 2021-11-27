# -*- coding: utf-8 -*-


"""
Example how to use Geneea API in three simple steps:

1. Load the input data
2: Analyze them
3. Save the results

This is a simple pipeline: [load] -> [analyze] -> [save]

What about monadic API ? :)
see for example http://soshnikov.com/mPyPl/

"""

import sys
import os
import requests as rq
from uuid import UUID

from dataclasses import dataclass
from typing import Dict, Optional
from requests.exceptions import RequestException


__all__ = tuple(["main"])

# ########################################################################### #
#                                  DOMAIN                                     #
# ########################################################################### #

@dataclass
class Article: # DTO?
    id: UUID
    content: str


@dataclass(frozen=True, eq=True)
class Analysis: # DTO?
    """
    The text model contains the original and analyzed Article.
    """
    id: UUID      # Original article id
    content: str  # Originla article analyzed content

# Work in progress

@dataclass
class Command: ...

@dataclass
class Event: ...

@dataclass
class AnalyzeArticle(Command): # DTO
    article_id: str
    article_content: str

@dataclass
class ArticleAnalyzed(Command): # DTO
    article_id: str
    analysis_content: str


# ########################################################################### #
#                                 SERVICE                                     #
# ########################################################################### #

class GeneeaClient:
    """
    The Geneea service client is responsible for calling Geneea REST service
    and analyze the provided article.
    """

    __URL__ = "https://api.geneea.com/v3/analysis/T:CRo-transcripts"

    def __init__(self, credentials: str) -> None:
        self._credentials = credentials

    @property
    def credentials(self) -> str:
        """
        :return The service credentials.
        """
        return self._credentials

    def process(self, article: Article) -> Analysis:
        """
        For each text from thegiven collection call tge GENEEA service
        process the text and yield a result.

        :param texts:
        :yield:
        """
        headers = {
            "Article-type": "application/json",
            "Authorization": f"user_key {self.credentials}"
        }

        response = rq.post(type(self).__URL__, json = {"text": article.content}, headers=headers)

        if response.status_code != 200:
            raise RequestException(f"Error for request with response status code {response.status_code}")

        return Analysis(id=article.id, content=response.json())


class ArticleRepository:
    """
    The article repository is responsible for loading a and saving the articles
    from and to the storage respectivelly.

    This is in-memory implementation.
    """
    def __init__(self) -> None:

        self._storage: Dict[UUID, Article] = {
            UUID("3107759e-fdf6-49ef-b224-3298926a20b7"): Article(UUID("3107759e-fdf6-49ef-b224-3298926a20b7"), "Lezec Ondra si po boulderingu polepšil, patří mu šestá postupová příčka."),
            UUID("a4b2eeda-af0e-40ea-a654-1b7c0a6e984e"): Article(UUID("a4b2eeda-af0e-40ea-a654-1b7c0a6e984e"), "Hrozně jsem si přála hodit pro Janečka, posteskla si oštěpařka Špotáková"),
        }

    def find_one(self, id: UUID) -> Optional[Article]:
        """
        Load a text from storage.
        """
        return self._storage[id] if id in self._storage else None

    def save_one(self, article: Article) -> None:
        """
        Save the text to storage.
        """
        if article.id not in self._storage:
            self._storage[article.id] = article


class AnalysisRepository:
    """
    The analysis repository is responsible for loading a and saving the analysis
    from and to the storage respectivelly.

    This is in-memory implementation.
    """
    def __init__(self) -> None:

        self._storage: Dict[UUID, Article] = {}

    def find_one(self, id: UUID) -> Optional[Analysis]:
        """
        Load a text from storage.
        """
        return self._storage[id] if id in self._storage else None

    def save_one(self, analysis: Analysis) -> None:
        """
        Save the text to storage.
        """
        if analysis.id not in self._storage:
            self._storage[analysis.id] = analysis


class ArticleAnalysisService: # Facade
    """
    The main application service facade.
    The methods reflects business requirements aka use-cases.

    - Analyze the article and store the analysis result.
    - Retrieve the analysis for the given article.
    """

    def __init__(self,
        geneea_client: GeneeaClient,
        article_storage: ArticleRepository,
        analysis_storage: AnalysisRepository
    ) -> None:
        self.geneea_client = geneea_client
        self.article_storage = article_storage
        self.analysis_storage = analysis_storage

    def analyze_article(self, article_id: str): # ->  Result[None]
        """
        Analyze an article with the given id.
        Return the analyzed article or None, when an article was not found in database.
        :raise: Exception when Geneea service is no reachable or article with given id was not found.
        """
        try:
            # Convert the raw string to UUID.
            # The primitive string values are send to service from outside the domain e.g
            # via HTTP REST or CLI application.
            article_id = UUID(article_id)

            # Retrive the article from storages.
            article = self.article_storage.find_one(article_id)

            # When the article is not found raise the exception or return failure result.
            if article is None:
                raise Exception(f"The article {article_id} could not be found.")

            # Analyze the article and get the resul by calling the Gennea service.
            analyzed = self.geneea_client.process(article)

            # When the Geneea serrvice fails to analyze the result raise the exception or return fauilure result.
            if analyzed is None:
                return Exception(f"The article {article_id} could not be processed.")

            # Create the analysis domain object and store it.
            analysis = Analysis(id = article_id, content = analyzed.content )
            self.analysis_storage.save_one(analysis)

        except Exception as ex:
            raise ex

    def retrive_analysis(self, article_id: str): # -> Result[None]
        try:
            self.analysis_storage.find_one(article_id)
        except Exception as ex:
            raise ex

# ########################################################################### #
#                                 MAIN                                        #
# ########################################################################### #

def main(args=None) -> None:
    """
    Parse the command line arguments.
    Execute the main function with arguments.
    Capture the result and return 0 on success or 1 on failure.
    """
    try:
        # ------------------------------------------------------------------------
        # CONFIGURE SERVICE
        # ------------------------------------------------------------------------
        geneea_key = os.environ.get("GENEEA_KEY")

        if geneea_key is None:
            print("Gennea key must be set!")
            sys.exit(1)

        geneea_client = GeneeaClient(geneea_key)
        article_storage = ArticleRepository()
        analysis_storage = AnalysisRepository()

        service = ArticleAnalysisService(
            geneea_client = geneea_client,
            article_storage = article_storage,
            analysis_storage = analysis_storage
        )

        # ------------------------------------------------------------------------
        # EXECUTE WORKFLOW
        # ------------------------------------------------------------------------

        # Some article ids for testing.
        ids = [
            UUID("3107759e-fdf6-49ef-b224-3298926a20b7"),
            UUID("a4b2eeda-af0e-40ea-a654-1b7c0a6e984e"),
        ]

        # Analyze articles.
        for id in ids:
            service.analyze_article(id)

        print(
            "\n=== SHOW THE RESULTS ===\n\n",
            analysis_storage.find_one(ids[0]).content,
            analysis_storage.find_one(ids[1]).content,
        )

        sys.exit(0)

    except Exception as ex:
        print(ex)
        sys.exit(1)
