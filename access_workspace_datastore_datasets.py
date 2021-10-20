# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset

"""
Let's acces to workspace
The work space was created before in the sricpt "create_workspace.py"
"""

ws = Workspace.from_config(path="./config")

"""
List all the workspaces within a subscription
"""
ws_list = Workspace.list(subscription_id='6f74f25f-29ed-4190-afa6-3c62a49a9393')
print("list all the workspace wthin a subscription : ")
print(ws_list)
print("-"*100)

"""
Access the defaut datastore from workspace 
"""
az_default_store = ws.get_default_datastore()
print("Access the defaut datastore from workspace ")
print(az_default_store)
print("-"*100)

"""
List all the datastores 
"""
store_list = list(ws.datastores)
print("List all the datastores")
print(store_list)
print("-"*100)

"""
Get the datasets from workspace
"""
az_dataset = Dataset.get_by_name(ws, "Post Verif Problem SDK")
print(" dataset from workspace : ")
print(az_dataset)
print("-"*100)

"""
List datasets from workspace
"""
ds_list = list(ws.datasets.keys())
print("List datasets from workspace")
print(ds_list)
print("-"*100)