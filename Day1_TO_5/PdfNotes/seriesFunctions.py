"""Common Methods

1. s.head(n):  Returns the first n (rows)elements of the Series.
Default is 5

2. s.tail(n):  Returns the last n elements of the Series.
Default is 5

3. s.sample(n):Returns a random sample of n elements from the Series.(random Rows)
Default is 1

4. s.describe():Returns descriptive statistics like count, mean, std, min, max, quartiles, etc.
# Usefull to get all Mathmatical things

5. s.count() : it return the number of NON Nan Values
s.size : it returns all values(including Nan)

6. s.info() :Info (only works on DataFrame, not Series directly)


Mathematical & Statistical
7. s.sum()            # Sum of all values

8. s.mean()           # Average

9. s.median()         # Median

10. s.min(), s.max()   # Min and Max

11. s.std()            # Standard deviation

12. s.var()            # Variance



Value Counts and Frequencies
13. s.value_counts()                 # number of Counts of each unique value (Means How Many Times Each value Comes)

14. s.value_counts(normalize=True)   # Proportions

15. s.unique()                       # Unique values

16. s.nunique()                      # Number of unique values



Sorting & Ranking
17. s.sort_values()             # Sort by values

18. s.sort_index()              # Sort by index

19. s.rank()                    # Ranking of values


String Methods (only for string Series)
20. s.str.lower()         # Convert to lowercase

21. s.str.upper()         # Uppercase

22. s.str.contains("abc") # Boolean mask

23. s.str.len()           # Length of each string

24. s.str.replace("old", "new")


Null Handling
25. s.isnull()            # Boolean mask for NaNs

26. s.notnull()           # Opposite

27. s.dropna()            # Remove nulls

28. s.fillna(value)       # Replace nulls


# OTher Methods
1. astype() 
Change Data Type

2. between(): 
Check if values fall in range

3. clip()
Limit values to a range

4.drop_duplicates():
 Remove duplicate values

5.isin():
   Check if values exist in a list

6.apply(): 
Apply a custom function


"""








# read This At Last For Revision
import pandas as pd

# All Functions In One FIle
s = pd.Series([88, 92, 79, 85, 92], index=['Asha', 'Rohan', 'Priya', 'Karan', 'Riya'])

# 1. Exploring the Series
print("1. head():")
print(s.head())

print("\n2. tail():")
print(s.tail())

print("\n3. sample():")
print(s.sample(2))

print("\n4. describe():")
print(s.describe())

# 2. Indexing & Filtering
print("\n5. loc[]:")
print(s.loc['Rohan'])

print("\n6. iloc[]:")
print(s.iloc[1])

print("\n7. Conditional filtering:")
print(s[s > 85])

# 3. Mathematical & Statistical
print("\n8. sum():")
print(s.sum())

print("\n9. mean():")
print(s.mean())

print("\n10. median():")
print(s.median())

print("\n11. min():")
print(s.min())

print("\n12. max():")
print(s.max())

print("\n13. std():")
print(s.std())

print("\n14. var():")
print(s.var())

print("\n15. count():")
print(s.count())

# 4. Value Counts and Frequencies
print("\n16. value_counts():")
print(s.value_counts())

print("\n17. value_counts(normalize=True):")
print(s.value_counts(normalize=True))

print("\n18. unique():")
print(s.unique())

print("\n19. nunique():")
print(s.nunique())

# 5. String Methods (let's create a string series)
names = pd.Series(['Asha', 'Rohan', 'Priya', 'Karan', 'Riya'])

print("\n20. str.lower():")
print(names.str.lower())

print("\n21. str.upper():")
print(names.str.upper())

print("\n22. str.contains('a'):")
print(names.str.contains('a'))

print("\n23. str.len():")
print(names.str.len())

print("\n24. str.replace('a', '@'):")
print(names.str.replace('a', '@'))

# 6. Null Handling
s_with_nan = pd.Series([88, None, 79, None, 92])

print("\n25. isnull():")
print(s_with_nan.isnull())

print("\n26. notnull():")
print(s_with_nan.notnull())

print("\n27. dropna():")
print(s_with_nan.dropna())

print("\n28. fillna():")
print(s_with_nan.fillna(0))

# 7. Sorting & Ranking
print("\n29. sort_values():")
print(s.sort_values())

print("\n30. sort_index():")
print(s.sort_index())

print("\n31. rank():")
print(s.rank())

# 8. Apply Functions
print("\n32. apply():")
print(s.apply(lambda x: x + 5))

print("\n33. map():")
print(s.map(lambda x: x * 2))
