# Azure HTTP Trigger on Blob Event  

The following code is used for creating and or updating a cognitive services index with a file that was uploaded to a targeted blob container path.  
The file is scanned and chunked and stored in a designated storage account. This repository can be used for any project that focuses on creating  
a Cog Search index to be used in conjunction with Azure OpenAI Document chat. The project currently supports the indexing of PDF files with the intention to support Microsoft Files as the technology allows. To leverage the code you can connect VS Code to your Azure instance using the Azure Extension.  

## Environment Variables

It is encouraged to use environment variables to safely create the necessary connections to Azure Services without hard coding the keys or connection strings. Future development will use Managed Identity thus eliminating the use of Keys. You can find and example of an environment file that can be leverages using the Python_DotEnv libary `.env.sample`.

Create a .env file in the parent directory

```
blob_connection_string=""
blob_trigger_account=""
BLOB_ACCOUNT_KEY=""
STORAGEACCOUNT=""
CONTAINER=""
STORAGEKEY=""
TENANTID=""
SEARCHSERVICE=""
SEARCHKEY=""
OPENAISERVICE=""
OPENAIDEPLOYMENT=""
OPENAIKEY=""
FORMRECOGNIZERSERVICE=""
FORMRECOGNIZERKEY=""
```

### Updating your Azure Function App Settings

You can use the Azure CLI to update the Function Apps Application settings with the local environment *.env*. Please see [Az CLI command](https://learn.microsoft.com/en-us/cli/azure/functionapp/config/appsettings?view=azure-cli-latest#az-functionapp-config-appsettings-set) for updating your function app


## Virtual Environments

You need to create a virtual environment that can deploy all the required python packages for the function app. There two most popular ways to create a virtual environment using python is to use the native `venv` or `virtualenv`.

#### venv  

```
python -m venv .venv
```

**In Linux or Mac, activate the new python environment**
```
source env_name/bin/activate
```

**Or in Windows**
```
.\env_name\Scripts\activate
```


#### virtualenv

To use virtualenv you will need to install the package using pip. You can follow the link to the documentation for official installation and how to use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) in your python application.


##### via pipx
virtualenv is a CLI tool that needs a Python interpreter to run. If you already have a Python 3.7+ interpreter the best is to use pipx to install virtualenv into an isolated environment. This has the added benefit that later you’ll be able to upgrade virtualenv without affecting other parts of the system.
```
pipx install virtualenv
virtualenv --help
```

##### via pip
Alternatively you can install it within the global Python interpreter itself (perhaps as a user package via the --user flag). Be cautious if you are using a python install that is managed by your operating system or another package manager. pip might not coordinate with those tools, and may leave your system in an inconsistent state. Note, if you go down this path you need to ensure pip is new enough per the subsections below:

```
python -m pip install --user virtualenv
python -m virtualenv --help
```

##### Using virtualenv

Please follow the [virtualenv guide](https://virtualenv.pypa.io/en/latest/user_guide.html) for creating virtual environments for your application. The following code is extracted from the official documentation.


**Quick start**

Create the environment (creates a folder in your current directory)
```
virtualenv env_name
```

**In Linux or Mac, activate the new python environment**
```
source env_name/bin/activate
```

**Or in Windows**
```
.\env_name\Scripts\activate
```

**Confirm that the env is successfully selected**
```
which python3
```

### Installing app packages

The following requirements.txt file contain the python packages needed for the application to run locally or as deployed. After activating the virtural python environment from the above step you can install the packages via pip.

```
pip install -r requirements.txt
```