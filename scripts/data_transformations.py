import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from data_extraction import main as extract_data

def preprocess_data(data):
    df = pd.DataFrame(data)
    # Example preprocessing steps: removing duplicates, handling missing values, etc.
    df.drop_duplicates(inplace=True)
    df.fillna('No data', inplace=True)
    return df

def save_to_txt(df, file_path):
    df.to_csv(file_path, sep='\t', index=False)
    print(f'Data saved to {file_path}')

def upload_to_drive(file_path, title):
    # Step 1: Create a GoogleAuth object
    gauth = GoogleAuth()

    # Step 2: Load client secrets from the downloaded JSON file
    gauth.LoadClientConfigFile("C:\\Users\\laiba\\OneDrive\\Desktop\\mlop_assignment_2\\scripts\\credentials.json")

    # Step 3: Authenticate the client
    gauth.LocalWebserverAuth()  # Creates a local webserver and automatically handles authentication.

    # Step 4: Create Google Drive client
    drive = GoogleDrive(gauth)

    # Upload the file to Google Drive
    file1 = drive.CreateFile({'title': title})
    file1.SetContentFile(file_path)
    file1.Upload()
    print(f'Uploaded file {title} to Google Drive with mimeType {file1["mimeType"]}')

if __name__ == "__main__":
    # Extract and preprocess data
    raw_data = extract_data()
    cleaned_data = preprocess_data(raw_data)
    
    # Save to a text file
    file_path = 'C:\\Users\\laiba\\OneDrive\\Desktop\\mlop_assignment_2\\scripts\\cleaned_data.txt'
    save_to_txt(cleaned_data, file_path)
    
    # Upload the text file to Google Drive
    upload_to_drive(file_path, 'cleaned_data.txt')
