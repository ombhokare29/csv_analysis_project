#  CSV Analysis Tool 

##  Project Overview 
The CSV Analysis Tool is a Django-based web application designed to allow users to upload CSV files, analyze their contents, and view the results and visualizations directly on the web interface. This project showcases capabilities in backend development, data analysis, and data visualization using Django and Python libraries like `pandas`, `numpy`, `matplotlib`, and `seaborn`.

---

##  Features 
1.  File Upload :  
   Users can upload CSV files through an intuitive web interface.  

2.  Data Analysis :  
   - Displays the first few rows of the data.  
   - Calculates summary statistics such as mean, median, and standard deviation for numerical columns.  
   - Identifies and reports missing values.  

3.  Data Visualization :  
   - Automatically generates visualizations (e.g., histograms) for numerical columns.  
   - Displays visualizations directly on the results page.  

4.  Responsive UI :  
   - Styled with  Bootstrap  for enhanced user experience.  
   - Includes a clean layout with a navigation bar for easy access.  

---

##  Project Structure 
```
csv_analysis_project/
├── analysis/
│   ├── templates/
│   │   ├── analysis/
│   │   │   ├── base.html
│   │   │   ├── upload.html
│   │   │   ├── result.html
│   ├── static/
│   │   ├── analysis/
│   │   │   ├── styles.css
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
├── csv_analysis_project/
│   ├── settings.py
│   ├── urls.py
├── media/
│   ├── plot.png  # Automatically generated visualization
├── manage.py
├── README.md
```

---

##  Technologies Used 
-  Backend Framework : Django  
-  Frontend Framework : Bootstrap  
-  Programming Language : Python  
-  Data Analysis Libraries : `pandas`, `numpy`  
-  Data Visualization Libraries : `matplotlib`, `seaborn`  

---

##  Setup Instructions 

###  Step 1: Install Python 
Ensure Python is installed on your system.  
Download it from [python.org](https://www.python.org/downloads/).

###  Step 2: Install Dependencies 
Install the required libraries globally on your system:
```bash
pip install django pandas numpy matplotlib seaborn
```

###  Step 3: Run the Server 
Navigate to the project directory (where `manage.py` is located) and start the development server:
```bash
python manage.py runserver
```

###  Step 4: Access the Application 
Open your web browser and go to:  
`http://127.0.0.1:8000/`

---

##  Usage 
1.  Upload a File :  
   - Navigate to the homepage and upload a CSV file using the form provided.  

2.  View Results :  
   - See the first few rows of the uploaded data.  
   - Analyze summary statistics for numerical columns.  
   - Check for missing values.  

3.  Visualize Data :  
   - View automatically generated histograms for numerical columns.

---

##  Sample CSV File 
Here’s an example of a valid CSV file for testing:
```csv
Name,Age,Salary,Department,Joining Date
Alice,30,60000,IT,2020-01-15
Bob,35,75000,Finance,2019-06-10
Charlie,28,,Marketing,2021-03-12
David,42,90000,IT,
Eve,29,58000,HR,2022-08-19
```
Save this as `sample.csv` and upload it to test the application.

---

##  Deliverables 
1.  GitHub Repository :  
   - Includes the full Django project code.  
   - Contains a clean and well-documented `README.md` file.

2.  Sample CSV File :  
   - A file with data for testing the upload and analysis functionality.  

3.  Generated Visualization :  
   - Saved in the `media/` directory as `plot.png`.  

---

##  Screenshots 

###  File Upload Page 
![Upload Page](media/upload-page-example.png)

###  Analysis Results 
![Results Page](media/results-page-example.png)

---

##  Future Enhancements 
1.  Advanced Visualizations :  
   Include scatter plots, box plots, and correlation heatmaps.  

2.  Custom Analysis Options :  
   Allow users to select specific analysis tasks or data columns.  

3.  Export Features :  
   Enable users to download analysis results or visualizations as files.

---

##  Contact Information 
For queries, contact:  
 Om Balkrishna Bhokare   
- Email: [ombhokare29@gmail.com](mailto:ombhokare29@gmail.com)  
- GitHub: [ombhokare29](https://github.com/ombhokare29)  
- LinkedIn: [linkedin.com/in/om-bhokare-130137215](https://linkedin.com/in/om-bhokare-130137215)  

---