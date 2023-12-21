import azure.functions as func
import logging
import os
import readblob as rb

app = func.FunctionApp()
@app.blob_trigger(arg_name="myblob", path="openaiindexer",
                               connection="AzureWebjobsStorage") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    rb.iterate_blob()
    
 