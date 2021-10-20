# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset

"""
Let's acces to workspace
The work space was created before in the sricpt "create_workspace.py"
"""

ws = Workspace.from_config(path="./config")




"""
Create datastore in the workspace ws 
--------
Recall : 
--------------------------------------------------------------------------------------------------------------
Before to create a datastore on the workspace 
we should do manually on azure platforme some steps :
    ** create a storage account for the busninss data ==> account_name="azuremlstb1127"
    ** Inside storage account (azuremlstb1127), create container ==> container_name="azuremlstb1127blob"
    ** Inside container (azuremlstb1127blob) we can upload data or create empty folder and uploda data 
    ** Inside storage account (azuremlstb1127) we can get the key from the menu
    ==> account_key="P493nMozQCjAWYpe7O2R+O8rcqtTMoQ8JfD9nv1QF+MSBzjv7O72Hev9DFiq1PC7Ac+nNBOeluVNw4MZhuRXbQ=="
---------------------------------------------------------------------------------------------------------------
    
"""

az_store = Datastore.register_azure_blob_container(
                                                    workspace=ws, ### our workspace created before
                                                    datastore_name="azure_sdk_blob1127", # the name gived for datastore
                                                    account_name="azuremlstb1127", # from recall
                                                    container_name="azuremlstb1127blob", # from recall
                                                    account_key="P493nMozQCjAWYpe7O2R+O8rcqtTMoQ8JfD9nv1QF+MSBzjv7O72Hev9DFiq1PC7Ac+nNBOeluVNw4MZhuRXbQ==" # from recall
                                                    )
print("az_store : \n", az_store)










