# Patent Analysis Project

Welcome to the Patent Analysis Project! This initiative is dedicated to building a robust data pipeline that extracts patents from various sources, analyzes the data using Apache Spark, and presents insightful visualizations through a user-friendly dashboard created with Flask.

---

## Project Architecture
![Project Architecture](architecture-diagram.png)

---

### Overview

This architecture diagram outlines the workflow of the Patent Analysis Project. Here’s a breakdown of the key components:

1. **Data Source**: Extract patent data from diverse sources using web scraping techniques, specifically with Beautiful Soup and Selenium.
  
2. **Load Data**: Import the extracted data into a MongoDB database for efficient storage and retrieval.
  
3. **Transform Data**: Utilize Apache Spark, particularly PySpark, to standardize and analyze the data from different sources, creating a unified dataset for comprehensive analysis.
  
4. **Reload Data**: Store the transformed data back into MongoDB Cloud for further accessibility and analysis.
  
5. **Visualize Data**: Create engaging visualizations using Power BI and Tableau to present the findings effectively.
  
6. **Integrate Flask**: Develop a user-friendly web application that manages user interactions, utilizing MySQL as the backend database for seamless data management.

---

## Setup Instructions

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/JawadData/patents_analysis.git
   
2. Open the directory in your preferred code editor (e.g., Visual Studio Code).
3. Navigate to the GUI/register.py file.
4. Update the registration information for the MySQL database in the register.py file.
5. Open a terminal window.
6. Change to the GUI directory:
   ```bash
   cd GUI
7. Run the registration script:
   python register.py

