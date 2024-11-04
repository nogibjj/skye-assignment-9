# Assignment 9
[![action](https://github.com/nogibjj/skye-assignment-9/actions/workflows/action.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-9/actions/workflows/action.yml)
## Project Overview
**Assignment 9** is a data analysis project that focuses on processing and summarizing data from a given dataset. The project includes various operations such as calculating value counts, formatting outputs for better readability, and generating reports based on the data.

## Features
- **Data Counting and Summarization**: Includes methods to count and display the top 10 most frequent values in specific columns.
- **Date Analysis**: Extracts and counts data by year for temporal analysis.
- **Custom Output Formatting**: Outputs data in a tabular format without unnecessary index numbers for cleaner presentation.

## Code Highlights
### Displaying the Top 10 Value Counts
The project includes code to display the top 10 value counts for the 'Federation' column without displaying the index numbers:

```python
print(
    df["Federation"]
    .value_counts()
    .head(10)
    .rename_axis("Federation")
    .reset_index(name="count")
    .to_string(index=False)
)
```

### Counting Transfers by Year
The project analyzes the number of data transfers per year and prints them in a formatted manner:

```python
transfers_per_year = df["Transfer Date"].dt.year.value_counts().sort_index()
print("\nNumber of transfers per year:")
print(transfers_per_year.to_frame('Number of Transfers').rename_axis('Year'))
```

## Requirements
- Python 3.9 or higher
- Libraries:
  - `pandas`
  - `pytest` (for running tests)

## Project Structure
```
assignment-9/
│
├── src/
│   └── model.ipynb  # Jupyter Notebook with the main analysis code
└── README.md         # Project documentation
```

## Notes
- The project includes formatted printing to enhance readability and ensure outputs align with expectations.
- Custom formatting ensures cleaner printouts for reports and avoids showing row indices in the output.

## License
This project is licensed under the MIT License.