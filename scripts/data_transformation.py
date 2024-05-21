import pandas as pd

def preprocess_data(data):
    df = pd.DataFrame(data)
    # Example preprocessing steps: removing duplicates, handling missing values, etc.
    df.drop_duplicates(inplace=True)
    df.fillna('No data', inplace=True)
    return df

def save_to_txt(df, file_path):
    with open(file_path, 'w') as file:
        for index, row in df.iterrows():
            file.write(f"Title: {row['title']}\nDescription: {row['description']}\nLink: {row['link']}\n\n")

if __name__ == "__main__":
    from data_extraction import main
    raw_data = main()
    cleaned_data = preprocess_data(raw_data)

    # Define the file path
    file_path = 'C:\\Users\\laiba\\OneDrive\\Desktop\\mlop_assignment_2\\scripts\\preprocessed_data.txt'
    
    # Save the data to a text file
    save_to_txt(cleaned_data, file_path)
    
    # Print the cleaned data to the terminal
    print(cleaned_data)
    print(f"Data has been saved to {file_path}")
