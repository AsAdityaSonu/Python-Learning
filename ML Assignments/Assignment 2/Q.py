import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, KBinsDiscretizer
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
from geopy.geocoders import Nominatim
import time

# ----------------------------------------------------------------------
# Load data
customers_df = pd.read_csv('./archive/AWCustomers.csv')
print("Customers Data:")
print(customers_df.head())

sales_df = pd.read_csv('./archive/AWSales.csv')
print("\nSales Data:")
print(sales_df.head())

# ----------------------------------------------------------------------
# Merge data
merged_df = pd.merge(customers_df, sales_df, on='CustomerID', how='inner')
print("\nMerged Data:")
print(merged_df.head())

# ----------------------------------------------------------------------
# Select relevant columns
final_df = pd.DataFrame()
columns_to_select = ['CustomerID', 'Occupation', 'BirthDate', 'YearlyIncome', 'Gender', 
                     'PostalCode', 'AddressLine1', 'HomeOwnerFlag', 'NumberChildrenAtHome', 
                     'NumberCarsOwned', 'AvgMonthSpend', 'BikeBuyer']
final_df = merged_df[columns_to_select]
final_df.to_csv('final.csv', index=False)

# ----------------------------------------------------------------------
# Display data types and preview
print("\nData Types:")
print(final_df.dtypes)

print("\nData Preview:")
print(final_df.head())

# ----------------------------------------------------------------------
# Classify data type for each column
def classify_data_type(column):
    if column.dtype == 'object':
        unique_values = column.nunique()
        return 'Nominal' if unique_values < 10 else 'Ordinal'
    elif pd.api.types.is_numeric_dtype(column):
        return 'Ratio' if column.min() >= 0 else 'Interval'
    return 'Unknown'

print("\nColumn Classifications:")
for column in final_df.columns:
    print(f"Column '{column}': {classify_data_type(final_df[column])}")

# ----------------------------------------------------------------------
# Handle missing values
for column in final_df.columns:
    if final_df[column].dtype in ['int64', 'float64']:
        final_df[column].fillna(final_df[column].median(), inplace=True)
    elif final_df[column].dtype == 'object':
        final_df[column].fillna(final_df[column].mode()[0], inplace=True)

# ----------------------------------------------------------------------
# Impute missing values
imputer_numeric = SimpleImputer(strategy='mean')
numeric_data = final_df.select_dtypes(include=['float64', 'int64'])
numeric_data_imputed = pd.DataFrame(imputer_numeric.fit_transform(numeric_data), columns=numeric_data.columns)

imputer_categorical = SimpleImputer(strategy='most_frequent')
categorical_data = final_df.select_dtypes(include=['object'])
categorical_data_imputed = pd.DataFrame(imputer_categorical.fit_transform(categorical_data), columns=categorical_data.columns)

imputed_df = pd.concat([numeric_data_imputed, categorical_data_imputed], axis=1)
print("\nImputed Data:")
print(imputed_df.head())

# ----------------------------------------------------------------------
# Normalize numeric data
scaler = MinMaxScaler()
normalized_df = pd.DataFrame(scaler.fit_transform(numeric_data_imputed), columns=numeric_data_imputed.columns)
print("\nNormalized Data:")
print(normalized_df.head())

# ----------------------------------------------------------------------
# Bin numeric data
binner = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
binned_df = pd.DataFrame(binner.fit_transform(numeric_data_imputed), columns=numeric_data_imputed.columns)
print("\nBinned Data:")
print(binned_df.head())

# ----------------------------------------------------------------------
# Frequency encoding for categorical data
threshold = 0.01
for col in categorical_data_imputed.columns:
    value_counts = categorical_data_imputed[col].value_counts(normalize=True)
    rare_categories = value_counts[value_counts < threshold].index
    categorical_data_imputed[col] = categorical_data_imputed[col].replace(rare_categories, 'Rare')

print("\nFrequency Encoded Data:")
print(categorical_data_imputed.head())

# ----------------------------------------------------------------------
# One-hot encoding for categorical data
one_hot_encoded_df = pd.get_dummies(categorical_data_imputed)
print("\nOne-Hot Encoded Data:")
print(one_hot_encoded_df.head())

# ----------------------------------------------------------------------
# Standardize numeric data
scaler = StandardScaler()
standardized_df = pd.DataFrame(scaler.fit_transform(numeric_data_imputed), columns=numeric_data_imputed.columns)
print("\nStandardized Data:")
print(standardized_df.head())

# ----------------------------------------------------------------------
# Combine data for final dataset
final_processed_df = pd.concat([standardized_df, binned_df, one_hot_encoded_df], axis=1)
print("\nFinal Processed Data:")
print(final_processed_df.head())

# ----------------------------------------------------------------------
# Calculate Simple Matching Coefficient (SMC)
def simple_matching_coefficient(row_a, row_b):
    return np.sum(row_a == row_b) / len(row_a)

row_0 = final_processed_df.iloc[0]
row_1 = final_processed_df.iloc[1]
smc = simple_matching_coefficient(row_0, row_1)
print(f"\nSimple Matching Coefficient: {smc}")

# ----------------------------------------------------------------------
# Jaccard similarity
binary_row_0 = (row_0 > 0).astype(int)
binary_row_1 = (row_1 > 0).astype(int)
jaccard_similarity = jaccard_score(binary_row_0, binary_row_1, average='binary')
print(f"\nJaccard Similarity: {jaccard_similarity}")

# ----------------------------------------------------------------------
# Cosine similarity
cosine_similarity_score = cosine_similarity([row_0], [row_1])[0][0]
print(f"\nCosine Similarity: {cosine_similarity_score}")

# ----------------------------------------------------------------------
# Geolocation functions
geolocator = Nominatim(user_agent="geoapiExercises")

def get_lat_long(address_line, postal_code):
    time.sleep(1)
    location = geolocator.geocode(f"{address_line}, {postal_code}", timeout=10)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

final_df['Home Latitude'], final_df['Home Longitude'] = zip(*final_df.apply(lambda row: get_lat_long(row['AddressLine1'], row['PostalCode']), axis=1))
final_df['Work Latitude'], final_df['Work Longitude'] = zip(*final_df.apply(lambda row: get_lat_long(row['AddressLine1'], row['PostalCode']), axis=1))

# ----------------------------------------------------------------------
# Haversine function to calculate distance
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    r = 6371 # Radius of Earth 
    return c * r

# ----------------------------------------------------------------------
# Calculate commute distance
final_df['Commute Distance'] = final_df.apply(lambda row: haversine(row['Home Latitude'], row['Home Longitude'],
                                                                    row['Work Latitude'], row['Work Longitude']), axis=1)

print("\nCommute Distance:")
print(final_df['Commute Distance'])

# ----------------------------------------------------------------------
# Correlation analysis
pearson_corr = final_df['Commute Distance'].corr(final_df['YearlyIncome'])
spearman_corr = final_df['Commute Distance'].corr(final_df['YearlyIncome'], method='spearman')

print(f"\nPearson Correlation: {pearson_corr}")
print(f"Spearman Correlation: {spearman_corr}")

# ----------------------------------------------------------------------