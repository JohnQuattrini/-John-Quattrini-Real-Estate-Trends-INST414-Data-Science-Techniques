import pandas as pd


file_path = "C:/Users/jtqua/OneDrive/Desktop/INST414(0202) Data Science Techniques/capstone folder/2024_public_lar_csv/2024_public_lar_csv.csv"

# # Count rows quickly (subtract 1 for header)
# with open(file_path, 'r', encoding='utf-8') as f:
#     total_rows = sum(1 for line in f) - 1
# print(f"Total rows in dataset: {total_rows:,}")

# # Get column names and count
# cols = pd.read_csv(file_path, nrows=0).columns
# print(f"Number of columns: {len(cols)}")
# print(cols.tolist())


# Load only the first 100,000 rows
hmda_sample = pd.read_csv(file_path, nrows=100000)

# # Show the first few rows
# print(hmda_sample.head())



# # Show all unique values in the column
# print(hmda_sample['action_taken'].unique())

# # Count frequency of each code:
# print(hmda_sample['action_taken'].value_counts().sort_index())



# look for exact duplicate rows in the sample
# Count exact duplicates
num_duplicates = hmda_sample.duplicated().sum()
print(f"Number of exact duplicate rows: {num_duplicates}")

# Show the first few duplicates
duplicates = hmda_sample[hmda_sample.duplicated()]
print(duplicates.head())

duplicates = hmda_sample[hmda_sample.duplicated(keep=False)]
print(duplicates)


# # Load only the first 50,000 rows and preview specific columns to inspect structure
# # This confirms those columns exist and how they’re formatted (e.g., numeric vs string).
# hmda_preview = pd.read_csv(file_path, nrows=50000)
# print(hmda_preview[['state_code', 'county_code']].head())



#------------------------
# # Number of rows to load into memory at a time.
# # This prevents memory overload when reading a huge CSV.
# chunksize = 1000000   # 1 million rows per iteration

# # Fraction of each chunk to keep.
# sample_fraction = 0.01  

# # Initialize an empty list to hold each small sampled DataFrame.
# sample_list = []

# # ----- Simple Random Sampling (uncomment to use) -----
# # Read file in chunks to avoid memory overload
# for chunk in pd.read_csv(file_path, chunksize=chunksize, low_memory=False):
#     # Take a 1% random sample of the chunk (not stratified)
#     chunk_sample = chunk.sample(frac=sample_fraction, random_state=42)
#     sample_list.append(chunk_sample)

# # Combine all sampled chunks into one DataFrame
# hmda_sample = pd.concat(sample_list)

# # Check result
# print("Sample shape:", hmda_sample.shape)

# # Save sample to file (for later use)
# # --- OPTIONAL PERFORMANCE  --- 
# # hmda_sample.to_csv("hmda_random_1pct_sample.csv", index=False)
#---------------------------------




# # Reset sample list for stratified sampling
# sample_list = []
# # Read the file in chunks again for stratified sampling
# for chunk in pd.read_csv(file_path, chunksize=chunksize, low_memory=False):

    # # --- OPTIONAL PERFORMANCE --- Stratified Sampling by State Code ----- uncomment to use -----
    # # This is the most expensive operation.
    # # It groups the data by 'state_code' and then randomly samples 1% from each group.
    # # You can comment out this block to sample purely randomly (faster but less representative).

    # # Group by state_code so each state contributes proportionally to the sample.
    # chunk_sample = (
    #     chunk.groupby('state_code', group_keys=False)
    #     .apply(lambda x: x.sample(frac=sample_fraction, random_state=42))
    # )

#     # Collect each sampled mini DataFrame in a list.
#     sample_list.append(chunk_sample)

# # Combine all sampled chunks into one large DataFrame.
# hmda_sample = pd.concat(sample_list)

# # Print the size of your final sample (rows, columns).
# print("Sample shape:", hmda_sample.shape)



# Save the combined sample to disk for later use.
# --- OPTIONAL PERFORMANCE  ---
# You can comment this out while testing to avoid writing to disk every time.
# hmda_sample.to_csv("hmda_stratified_sample.csv", index=False)

# print("Missing Data Percentage by Column:")
# print(missing_percent.sort_values(ascending=False))





# #------------
# # Check missing data percentages for each column
# missing_percent = (hmda_sample.isnull().sum() / len(hmda_sample)) * 100

# # Filter to only columns with x% or more missing
# high_missing = missing_percent[missing_percent >= 1].sort_values(ascending=False)

# # Print those columns only
# print("Columns with ≥ x% missing data:")
# print(high_missing)
#----------------------------------------




