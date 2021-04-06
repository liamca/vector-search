# Image, Text, Video and Audio Search Using Azure Cognitive Search (Vector Search) -- [Experimental]

The goal of this is to enable search over Text, Images, Videos and Audio using Azure Cognitive Search.  The technique was inspired by the following [research article](http://nmis.isti.cnr.it/falchi/Draft/2016-DaWaK-DRAFT.pdf), which converts vectors (embeddings) to text which allows the Cognitive Search service to leverage the inverted index to quickly find the most relevant items.  For this reason, any model that will convert an object to a vector can be leveraged as long as the number of dimensions in the resulting vector is less than 3000.  It also allows users to leverage existing pretrained or fine-tuned models.

This technique has shown to be incredibly effective and easy to implement.  Many pretrained models create vast numbers of dimensions and performance tends to degrade as the number of dimensions increase.  
