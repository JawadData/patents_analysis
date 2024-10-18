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


1.  git clone https://github.com/JawadData/patents_analysis.git .
2.  open the diracory in the vs code or other
3.  navigate to GUI/register.py 
4.  change the registration info  of mysql db in the register. py file
5.  open the terminal
6.  cd GUI/register.py
7.  python register.py
---

