# Urban Air Quality and Health Impact Analysis

## Overview

This project analyzes urban air quality and its impact on public health using data from various sources. The main components of this project include data processing, visualization, and generating reports. The project utilizes Python libraries like `pandas`, `matplotlib`, and `ydata_profiling` to profile, analyze, and visualize the dataset.


## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/urban-air-quality.git
    ```
2. Set up the virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Profile Report**:
    To generate a profiling report for the dataset, use the following command:
    ```bash
    venv/bin/python3 ./src/profile.report.py
    ```

2. **Generate and View the Graph**:
    You can visualize the average temperature and feels-like temperature data over time using:
    ```bash
    venv/bin/python3 ./src/lib.py
    ```


# Requirements

- [x] Jupyter notebook that perform descriptive statistics
- [ ] Jupyter notebook that use nbval plugin for pytest
- [x] Makefile command that run all tests, including, but not limited to, notebook, script, and lib
- [x] Makefile command that formats code with Python black
- [x] Makefile command that lint code with Ruff
- [x] Makefile command that installs code via:  pip install -r requirements.txt
- [x] test_script.py to test script
- [x] test_lib.py to test library
- [x] Generate summary statistics (mean, median, standard deviation)
- [x] Create at least one data visualization
- [ ] Gitlab Actions performs all four Makefile commands with badges for each one in the README.md
- [ ] Generated summary report (PDF or markdown) via CI/CD for extra credit or making your own PDF or MD file and pushing itTemp - Mean: 76.13, Median: 76.01, Std Dev: 0.96

___
Temp - Mean: 76.13, Median: 76.01, Std Dev: 0.96
Feels - Mean: 76.34, Median: 76.09, Std Dev: 1.06
![graph](./output_graph.png)
