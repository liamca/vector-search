#!/usr/bin/env python
# coding: utf-8

#pip install -U sentence-transformers

from sentence_transformers import SentenceTransformer, util
import numpy as np
from nltk.tokenize import sent_tokenize

# These are for question answer -- https://www.sbert.net/examples/applications/image-search/README.html
# model = SentenceTransformer('paraphrase-distilroberta-base-v1')
model = SentenceTransformer('msmarco-distilbert-base-v3')

def calculateDimensions(content):
    return contentToMeanEmbedding(content).shape[0]

def contentToMeanEmbedding(content):
    sentences = sent_tokenize(content)
    sentenceEmbeddings = model.encode(sentences)
    return np.mean(np.array(sentenceEmbeddings), axis=0)
