# patent analysis 
this project dedicated make in production a data pipline dedicated to extract patent from different source analys it using spark and load it finaly creat a siginficatif dashbord and use flask to create  a user friendly iterface .
---

## Project Architecture
![Project Architecture](architecture-diagram.png)
---

### Overview

This architecture diagram outlines the workflow of the patent analysis project. Below is a breakdown of the key components:

1. **Data Source**: extracting data from differet source using web scraping technique ((beutiful soup et seleniom.
2. **load the data**: load the data that came from diferent source into mongo db database.
3. **transform the data**: using spark et specialy py spark to analyse the data and stondarise the data from difirent source to create a combined data source unified and analyse it.
4. **load data**: reload data after tyransformation into mongo db cloud.
5. **Additional Data Processing**: The predictions from the regression models are integrated into the original Parquet file to generate new rules for the next day's predictions, which are then used as input for the classification model.
6. **Second Output**: Predictions from the classification model (Buy/Sell actions) are also stored in JSON format for easy access.
7. **Web Interface**: A Flask-based web application provides users with an interactive interface to view the predictions.
---

## Setup Instructions

1. **Repository Location**: Upload the repository to the "My Drive" section of your Google Drive account. Ensure that you are using the same account you log in to Google Colab with.

2. **Notebook Execution**: Import the notebook named "run_me" into Colab and execute it. This will train the models and automatically save the results.

3. **Export the Repository**: After executing the notebook, the modifications will be automatically saved to the repository on your Google Drive. You can then export this repository.

4. **Run the Application**: Using a terminal, navigate to the extracted repository, then enter the "flask" directory. Run the following command to start the application:  
   ```bash
   python app.py
---

## Future Improvements
- Automate the retraining process using Airflow.
- Deploy the app via a cloud provider (e.g., AWS).
