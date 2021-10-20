# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset

"""
Let's acces to workspace
The work space was created before in the sricpt "create_workspace.py"
"""

ws = Workspace.from_config(path="./config")


"""
Let's access  to datastore (in Azure cloud)
--------
recall :
-----------------------------------------------------------------------
we can get the Datastore by two args : 
    ** workspace : ws
    ** name of Datastore : "azure_sdk_blob1127" 
    ==> check script create_and_register_dataStore.py (name gived here)
------------------------------------------------------------------------
"""
az_store = Datastore.get(ws, "azure_sdk_blob1127")





"""
Create the path of the csv file

Think that inside the container of datastore we have :
   ** folder : Loan Data
   ** inside folder : post_verif_all_problems.csv
   ** ==> path : "Loan Data/post_verif_all_problems.csv"
"""

csv_path = [(az_store, "Loan Data/post_verif_all_problems.csv")]





"""
Let's create the dataset


We have two steps : 
    Step 1 : get data from datastore :
    ---------------------------------- 
        ** path : csv_path  from the previews step
        ** indicate separator : in our case ";"
    
    Step 2 : register the data (from datasrote) on the workspace :
    --------------------------------------------------------------
        ** workspace : ws
        ** name : we gived name "Post Verif Problem SDK"
        ** create_new_version : True, if existe create new version
     
"""

post_verif_problem_dataset = Dataset.Tabular.from_delimited_files(path=csv_path, # step 1
                                                                  separator=";" # step 1
                                                                  )

post_verif_problem_dataset = post_verif_problem_dataset.register(workspace=ws, # the workspace created before, Step 2
                                                                 name="Post Verif Problem SDK", # name gived here, Step 2
                                                                 create_new_version=True # if existe create new version, Step 2
                                                                 )

print(post_verif_problem_dataset)