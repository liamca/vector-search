# Image Search using Azure Cognitive Search


The following notebooks show how to ingest content into Azure Cognitive Search to allow you to perform searches that find similar images or photos.  For this example, a dataset of [holiday images](https://lear.inrialpes.fr/~jegou/data.php) which were based on the paper: Herve Jegou, Matthijs Douze and Cordelia Schmid, "Hamming Embedding and Weak geometry consistency for large scale image search", Proceedings of the 10th European conference on Computer vision, October, 2008

![Image Search](https://github.com/liamca/vector-search/raw/main/notebooks/image-search/demo.png)

## Usage

Before getting started, you will need to ensure you have created an Azure Cognitive Search index and have updated the file [azureCognitiveSearch.py](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/azureCognitiveSearch.py) with your search service name and API key:

* serviceName = ["Enter Search Service name -- DO NOT include .search.windows.net"]
* adminKey = ["Search Service Admin API Key"]

There are three notebooks that will be used:

- [vec2Text-images-train.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-train.ipynb): This notebook analyzes a set of existing images to determine a set of "cluster centers" that will be used to determine which "fake words" are generated for a vector
- [vec2Text-images-upload.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-upload.ipynb): This takes a set of images, extracts the vector (embedding) for it, converts it to a set of fake terms that is loaded into an Azure Cognitive Search index
- [vec2Text-images-test.ipynb](https://github.com/liamca/vector-search/blob/main/notebooks/image-search/vec2Text-images-test.ipynb): This allows you to test image search by loading an example image and searching for an image that is similar to it
