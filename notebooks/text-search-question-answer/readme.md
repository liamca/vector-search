# UNDER CONSTRUCTION

# Text Search using Vector Embeddings & Azure Cognitive Search

The following notebooks show how to ingest textual content in the form of an embedding (vector) into Azure Cognitive Search to allow you to perform searches that find similar text based on the similarity of the embeddings.  For this example, a subset of the [msmarco](https://microsoft.github.io/msmarco/) machine reading comprehension dataset is used.

## Usage

Before getting started, you will need to ensure you have created an Azure Cognitive Search index and have updated the file [azureCognitiveSearch.py](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/azureCognitiveSearch.py) with your search service name and API key:

* serviceName = ["Enter Search Service name -- DO NOT include .search.windows.net"]
* adminKey = ["Search Service Admin API Key"]

There are three notebooks that will be used:

- [vec2Text-msmarco-train.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-train.ipynb): This notebook analyzes a set of existing text documents to determine a set of "cluster centers" that will be used to determine which "fake words" are generated for a vector
- [vec2Text-msmarco-upload.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-upload.ipynb): This takes a set of text, extracts the vector (embedding) for it, converts it to a set of fake terms that is loaded into an Azure Cognitive Search index
- [vec2Text-msmarco-test.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-test.ipynb): This allows you to perform textual search search 

