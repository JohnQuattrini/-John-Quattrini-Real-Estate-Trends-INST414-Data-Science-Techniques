

READ ME
John Quattrini 
INST414
Sprint 2

the data set can be found at https://ffiec.cfpb.gov/data-publication/snapshot-national-loan-level-dataset/2024
it is large file Total rows in dataset: 12,229,298 columns: 99

Data Cleaning:
loaded data using pandas (subset)
remove unnecessary columns (missing data)
removed duplicate rows
transform datatypes as necessary

Feature Engineering Plan:
create derived or binned variables 
convert numerical codes to categorical labels for readability.
Scaled or normalized features where needed.

Exploratory Data Analysis (EDA)
Analyzed distribution of key variables such as loan_amount, income, and action_taken.
Visualized missing data and correlations to identify trends.
Sampled random 1% of data for exploratory work to improve efficiency.
