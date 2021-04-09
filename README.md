# Image, Text, Video and Audio Search Using Azure Cognitive Search (Vector Search) -- [Experimental]

PLEASE NOTE: This is an experimental capability.  It should not be used for production purposes at this time.

The goal of this is to enable search over Text, Images, Videos and Audio using [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/).  The technique was inspired by the following [research article](http://nmis.isti.cnr.it/falchi/Draft/2016-DaWaK-DRAFT.pdf), which converts vectors (embeddings) to text which allows the Cognitive Search service to leverage the inverted index to quickly find the most relevant items.  For this reason, any model that will convert an object to a vector can be leveraged as long as the number of dimensions in the resulting vector is less than 3000.  It also allows users to leverage existing pretrained or fine-tuned models.

This technique has shown to be incredibly effective and easy to implement.  Many pretrained models create vast numbers of dimensions and performance tends to degrade as the number of dimensions increase.  

## Configuring Python Environment
The samples below leverage [sentence transformers](https://github.com/UKPLab/sentence-transformers), however, it should be fairly straightforward to convert to other pretrained models or the vast number of existing [sentence transformer models](https://www.sbert.net/docs/pretrained_models.html) as needed.  This has been tested on Ubuntu and Windows and the requirements.txt includes the package versions used.  

```
conda create --name py37-vector-search --file requirements.txt
```

Alternatively, these were the conda commands used to install the required packages:

```
conda create -n py37-vector-search python=3.7
conda activate py37-vector-search
conda install -c conda-forge jupyterlab
conda install pytorch torchvision torchaudio cpuonly -c pytorchconda install pytorch torchvision torchaudio cpuonly -c pytorch
conda install -c anaconda gensim
conda install smart_open==2.0.0
pip install azure-search-documents
pip install -U sentence-transformers
```

## Samples
The following samples have been created to help you get started:
- [Image Search](https://github.com/liamca/vector-search/tree/main/notebooks/image-search)
- [Text Search with Question and Answer](https://github.com/liamca/vector-search/blob/main/notebooks/text-search-question-answer)

## How it Works

The goal is to be able to use the inverted index within Azure Cognitive Search to be able to quickly find vectors stored in the search index that are similar to a vector provided as part of a search query.  Unlike techniques like cosine similarity which are slow to process large numbers of items, this leverages an inverted index which enables much more data to be indexed and searched.  

![Vector Search Index in Azure Cognitive Search](https://github.com/liamca/vector-search/raw/main/imgs/azure-cognitive-search-index.png)

![Pivot Test Embeddings](https://github.com/liamca/vector-search/raw/main/imgs/pivot-embeddings.png)

![CLuster Dimensions](https://github.com/liamca/vector-search/raw/main/imgs/find-cluster-centers.png)

![Find Optimal Cluster Centers](https://github.com/liamca/vector-search/raw/main/imgs/find-optimal-center-clusters.png)

![Define Fake Terms](https://github.com/liamca/vector-search/raw/main/imgs/define-fake-terms.png)

### Upload Text Embeddings to Cognitive Search

Load the saved Cluster Centers
New embedding to be indexed: [-0.15, 0.22 ,… 0.41]

Choose Fake Term based on cluster closest embedding: [A1, B3, …, FED0]

Convert to string and index: “A1 B3 … FED0”

### Query Text Embeddings

Load the saved Cluster Centers
New embedding to be searched: [-0.15, 0.22 ,… 0.41]

Choose Fake Term based on cluster closest embedding: [A1, B3, …, FED0]

Convert to string and search: “A1 B3 … FED0”

