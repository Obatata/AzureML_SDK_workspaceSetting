# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset


"""
Access the workspace, Datastore and Datasets
"""

ws = Workspace.from_config("./config")
az_store = Datastore.get(ws, "azure_sdk_blob1127")
az_dataset = Dataset.get_by_name(ws, "Post Verif Problem SDK")
az_default_store = ws.get_default_datastore()



"""
Upload local files to the storage account using datastore
We create sample data on the "data" folder ! 
"""

files_list = ["./data/check_merge_all_son.csv", "./data/checkAttributs_ACCESS-TV.xlsx.csv"]

az_store.upload_files(files=files_list,
                      target_path="Loan Data/", ## path of folder data on the container created inside the storage account !
                      relative_root="./data/", ### provide relative root in local location
                      overwrite=True ## possible to update if file existe by setting True
                      )


"""
Upload entire fold directory to the storage account using datastore

"""

az_store.upload(
                src_dir="./data",
                target_path="Loan Data/data",
                overwrite=True,
               )