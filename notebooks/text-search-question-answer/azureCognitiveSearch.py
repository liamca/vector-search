from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient 
from azure.search.documents import SearchClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

# Set the service endpoint and API key from the environment
serviceName = ["Enter Search Service name -- DO NOT include .search.windows.net"]
adminKey = ["Search Service Admin API Key"]
indexName = "vec2text-msmarco"

# Create an SDK client
endpoint = "https://{}.search.windows.net/".format(serviceName)
adminClient = SearchIndexClient(endpoint=endpoint,
                      index_name=indexName,
                      credential=AzureKeyCredential(adminKey))

searchClient = SearchClient(endpoint=endpoint,
                      index_name=indexName,
                      credential=AzureKeyCredential(adminKey))
 
# Delete the index if it exists
def deleteIndex():
    try:
        result = adminClient.delete_index(indexName)
        print ('Index', indexName, 'Deleted')
    except Exception as ex:
        print (ex)
    
    
# Create the index
def createIndex():
    name = indexName
    fields = [
            SimpleField(name="Id", type=SearchFieldDataType.String, key=True),
            SearchableField(name="Content", type=SearchFieldDataType.String, facetable=False, filterable=True, sortable=True, analyzer_name="en.microsoft"),
            SearchableField(name="VecText", type=SearchFieldDataType.String, facetable=False, filterable=False, sortable=False)
        ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

    index = SearchIndex(
        name=name,
        fields=fields,
        cors_options=cors_options)

    try:
        result = adminClient.create_index(index)
        print ('Index', result.name, 'Created')
    except Exception as ex:
        print (ex)
        
def uploadDocuments(documents):
    try:
        result = searchClient.upload_documents(documents=documents)
        print("Upload of new document succeeded: {}".format(result[0].succeeded))
    except Exception as ex:
        print (ex.message)   
