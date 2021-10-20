

#Let's to import workspace class
#from azureml.core
from azureml.core import Workspace

def main():
    """
    Le's to create a workspace
    """
    print(Workspace.__doc__)
    ws = Workspace.create(name='Azureml-SDK-WS1127',
                          subscription_id='6f74f25f-29ed-4190-afa6-3c62a49a9393',
                          resource_group='AzuremlSDKRG1127',
                          create_resource_group=True,
                          location='eastus2'
                          )

    """
    Let's save a config data connexion in 
    config folder 
    """
    ws.write_config(path="./config")


if __name__ == "__main__":
    main()
