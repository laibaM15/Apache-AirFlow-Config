from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Step 1: Create a GoogleAuth object
gauth = GoogleAuth()

# Step 2: Load client secrets from the downloaded JSON file
gauth.LoadClientConfigFile("C:\\Users\\laiba\\OneDrive\\Desktop\\mlop_assignment_2\\scripts\\credentials.json")

# Step 3: Authenticate the client
gauth.LocalWebserverAuth()  # Creates a local webserver and automatically handles authentication.

# Step 4: Create Google Drive client
drive = GoogleDrive(gauth)

# To test, let's upload a simple text file
file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello World aik baar deobara check karne kai liya yai gayi hai ya nahiiiii!')
file1.Upload()
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))
