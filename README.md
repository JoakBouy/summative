# MLOps Project: Cardiovascular Disease Classification Model

## Project Overview
This project involves building a machine learning model to classify whether a patient has cardiovascular disease or not. The project follows a comprehensive MLOps workflow, including data analysis, preprocessing, model training, testing, and integration with a Streamlit application.

## Features
- Data Analysis: Visualize and analyze the cardiovascular disease dataset.
- Data Preprocessing: Clean and prepare the data for model training.
- Data Splitting: Split the data into training and testing sets.
- Model Training: Train a machine learning model to classify cardiovascular disease based on health indicators.
- Model Testing: Evaluate the model's performance on test data.
- Streamlit Integration: Interactive user interface for navigating through the ML pipeline.
- Ngrok Integration: Expose the Streamlit app to the internet for easy sharing and testing.

## Getting Started

### Prerequisites
- Python 3.8+
- Virtual Environment (venv)
- Required Python packages (listed in requirements.txt)

### Installation
1. Clone the Repository:

```
git clone https://github.com/JoakBouy/cvd-cnn_pipeline.git

cd cardiovascular-disease-classification
 ```
2. Set Up Virtual Environment:

```
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```
3. Install Dependencies:

```
pip install -r requirements.txt
```
## Running the Application

Run the Streamlit App:
```
streamlit run app.py
```
The Streamlit application will be available at http://localhost:8501.

## Project Structure

The project is organized into several key components:

1. `analysis_visualizations.py`: Contains functions for data analysis and visualization.
2. `preprocessing.py`: Handles data cleaning and preparation.
3. `splitting.py`: Splits the data into training and testing sets.
4. `training.py`: Implements the model building and training process.
5. `testing.py`: Evaluates the trained model on test data.
6. `app.py`: Main Streamlit application that integrates all components.

## Usage

The Streamlit app provides a user-friendly interface to navigate through different stages of the machine learning pipeline:

1. Data Analysis: Explore visualizations and insights from the dataset.
2. Data Preprocessing: View the data cleaning and preparation process.
3. Data Splitting: See how the data is split for training and testing.
4. Model Training: Observe the model building and training process.
5. Model Testing: Review the performance metrics of the trained model.

Use the sidebar navigation to move between different sections of the pipeline.

## Ngrok Integration

The application uses Ngrok to create a public URL, allowing you to share your Streamlit app easily. The public URL will be printed in the console when you run the application.

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Deployed Link

[https://cvd-cnn-pipeline-v2.onrender.com/](url)



