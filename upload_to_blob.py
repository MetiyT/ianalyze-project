
from azure.storage.blob import BlobServiceClient

connection_string = "Your_Connection_String"
container_name = "your-container-name"
local_file_path = "sample_data.xlsx"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample_data.xlsx")

with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)
print("File uploaded successfully to Azure Blob Storage!")
