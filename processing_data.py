import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df):
    # Handling missing values
    df['place of publication'].fillna('Unknown', inplace=True)
    df['DOI'].fillna('No DOI', inplace=True)

    # Convert  columns to numeric
    columns_to_convert = ['Citations', 'Recommendations', 'Research Interest Score', 'Reads']
    for col in columns_to_convert:
        df[col].replace('- -', '0', inplace=True)
    # Columns to remove commas from and convert to integers
    columns_to_convert = ['Reads', 'Recommendations', 'Citations']
    for col in columns_to_convert:
        df[col] = df[col].replace(',', '', regex=True)
    df[columns_to_convert] = df[columns_to_convert].astype(int)

    scaler = MinMaxScaler()
    # Columns to normalize
    columns_to_normalize = [ 'Citations', 'Recommendations', 'Reads']
    # Convert "Research Interest Score" to numeric (from percentage to 0-1 range)
    df['Research Interest Score'] = df['Research Interest Score'].str.rstrip('%').astype('float') / 100

    # Apply Min-Max Scaling to the selected columns
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    def preprocess_text(text):
        text = text.lower()  # Convert to lowercase
        tokens = text.split()  # Tokenization
        return " ".join(tokens)
    # Preprocess text in "Title" and "Abstract" columns
    df['Title'] = df['Title'].apply(preprocess_text)
    df['Abstract'] = df['Abstract'].apply(preprocess_text)


    return df


def main():
    # Load the CSV file into a pandas DataFrame
    csv_file_path = 'output.csv'
    df = pd.read_csv(csv_file_path)
    # Check for missing values
    missing_values = df.isnull().sum()
    print("Missing Values:\n", missing_values)
    # Display the original DataFrame
    print("Original DataFrame:")
    print(df.head())

    # Count occurrences of '__' in specific columns
    count_citations_underscore = (df['Citations'] == '- -').sum()
    count_reads_underscore = (df['Reads'] == '- -').sum()
    count_recommendations_underscore = (df['Recommendations'] == '- -').sum()
    count_interest_score_underscore = (df['Research Interest Score'] == '- -').sum()

    print("Counts of '__' in columns:")
    print(f"Citations: {count_citations_underscore}")
    print(f"Reads: {count_reads_underscore}")
    print(f"Recommendations: {count_recommendations_underscore}")
    print(f"Research Interest Score: {count_interest_score_underscore}")

    # Preprocess data and create the cleaned DataFrame
    cleaned_df = preprocess_data(df)
    print(cleaned_df)
    # Display the cleaned DataFrame
    print("\nCleaned DataFrame:")
    columns_to_print = ['Research Interest Score','Citations', 'Recommendations',  'Reads']
    col=['Abstract']
    print(cleaned_df[col].head())
    print(df[columns_to_print].head())
    cleaned_csv_file_path = 'cleaned_output.csv'
    cleaned_df.to_csv(cleaned_csv_file_path, index=False)
    print(f"Cleaned DataFrame saved to {cleaned_csv_file_path}")


if __name__ == "__main__":
    main()

