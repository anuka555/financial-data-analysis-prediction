# Example Python code snippet
print("Hello, World!")

# Example Pandas code snippet for reading a CSV file
import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())


# Example NumPy code snippet for creating an array
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Display the array
print(arr)

# Example Matplotlib code snippet for plotting data
import matplotlib.pyplot as plt

# Plot a simple line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()


# Example Scikit-learn code snippet for training a machine learning model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


# Example NLTK code snippet for tokenization and stemming
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Tokenize text
text = "Natural language processing is a fascinating field."
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Stemmed Words:", stemmed_words)
