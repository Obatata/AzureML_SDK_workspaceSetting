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
Laod the azureml Dataset into dataFrame

"""
df = az_dataset.to_pandas_dataframe()

print(" dataframe from dataset of ws : ")
print(df.head())
print("-"*100)
print()


"""
Upload the dataframe to the azurml dataset 

"""
az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
                                                            dataframe=df, ### the dataFrame loaded locally
                                                            target=az_store, ### the datastore from ws on the azure account
                                                            name="Post verif Problem from Dataframe"
                                                          )
