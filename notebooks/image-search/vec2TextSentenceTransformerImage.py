#!/usr/bin/env python
# coding: utf-8

from sentence_transformers import SentenceTransformer, util
import numpy as np
from PIL import Image

#Load CLIP model
model = SentenceTransformer('clip-ViT-B-32')


def calculateDimensions(file):
    return imageEmbedding(file).shape[0]

def imageEmbedding(file):
    img_emb = model.encode(Image.open(file))
    return np.array(img_emb)

def textEmbedding(query):
    img_emb = model.encode(query)
    return np.array(img_emb)

