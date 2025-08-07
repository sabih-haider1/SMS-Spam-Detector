import pandas as pd

# Load and normalize Dataset_1
df1 = pd.read_csv('Dataset_1.csv')
df1 = df1.rename(columns={'LABEL': 'label', 'TEXT': 'text'})[['label', 'text']]

# Load and normalize email.csv
df2 = pd.read_csv('emails.csv')
df2['label'] = df2['spam'].map({0: 'ham', 1: 'spam'})
df2 = df2.rename(columns={'text': 'text'})[['label', 'text']]

# Load and normalize eron_spam_data.csv
df3 = pd.read_csv('enron_spam_data.csv')
df3 = df3.rename(columns={'Spam/Ham': 'label', 'Message': 'text'})[['label', 'text']]
df3 = df3.dropna(subset=['text'])  # drop rows with missing messages

# Load and normalize Dataset_2.txt
df4 = pd.read_csv('Dataset_2.txt', sep='\t', header=None, names=['label', 'text'])

# Merge all
merged = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Optional: Clean labels (capitalize)
merged['label'] = merged['label'].str.strip().str.lower()

# Save the final merged dataset
merged.to_csv('merged_spam_dataset.csv', index=False)

print("Merged dataset saved as 'merged_spam_dataset.csv'")
