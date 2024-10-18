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
5. **visualise the data**: visualise the data using power bi and tableua.
6. **integrat flask**: create a user friendly app to manae the user's using my sql as database for web app.
7. ---
8. 

## Setup Instructions


1. **setup the MySQLdb**: after cloneing the repo .  change the registeatioj info for my sql db in "GUI/register.py" file .

2. **Execution**:.

3. **Export the Repository**: After executing the notebook, the modifications will be automatically saved to the repository on your Google Drive. You can then export this repository.

4. **Run the Application**: Using a terminal, navigate to the extracted repository, then enter the "flask" directory. Run the following command to start the application:  
   ```bash
   python app.py
---

## Future Improvements
- Automate the retraining process using Airflow.
- Deploy the app via a cloud provider (e.g., AWS).
