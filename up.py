import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Get the connection string from Shared Access Signature
# connect_str = "BlobEndpoint=https://bdacademy.blob.core.windows.net/ready?sp=racwdl&st=2022-08-08T18:38:18Z&se=2022-08-31T02:38:18Z&spr=https&sv=2021-06-08&sr=c&sig=k15nSE8XdCRYbRgOU9XfWORE48n4%2BootpCKHTcYmOTU%3D"
# container_name = "Robert"
# local_file_name = "merge.csv"
#
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

with open(local_file_name, "rb") as file:
	blob_client.upload_blob(file)

