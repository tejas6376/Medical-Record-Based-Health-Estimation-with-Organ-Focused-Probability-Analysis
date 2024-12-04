
# Medical-Record-Based-Health-Estimation-with-Organ-Focused-Probability-Analysis
Research paper based on the project submitted for publication(Also available in the repo)


This project is a Disease Prediction System capable of diagnosing diseases related to Kidney, Heart, and Liver. It leverages machine learning models trained on medical datasets to predict the likelihood of these diseases based on input patient data.

The healthcare industry is constantly
developing, and there is a need for precise and
qualified methods for medical treatment. Machine
learning algorithms likely offer faster processing of
medical data as compared to the analysis done by the
doctors manually. The main idea of the project is to
develop and implement a ml-based system that will
analyze the medical report for kidney, liver, and blood
related disease in the industry of healthcare. The
system makes use of the natural language processes
techniques for extracting the data, which is relevant
from the medical reports, and then it is preprocessed
and with the help of machine learning algorithm it is
classified. The health status of the patient is presented
in the concise dashboard made using sensible
decisions by the healthcare professionals with the help
of comparison of the models. The most proficient
model among these will be used to predict the
presence of a particular disease in the patient. This
streamlines healthcare operations, saves time for
analysis of medical reports, and overall efficiency is
improved.


The application is user-friendly and can be deployed as a web application.


## 🌟 Features
- Multi-Disease Prediction: Predicts diseases for Kidney, Heart, and Liver using trained models. 
- User-Friendly Interface: Simple web interface for easy input and prediction. 
- Scalable: Can be enhanced with more disease categories. 
- Open-Source: Contributions are welcome!
## 📂 File Structure
- Data: Contains the datasets used for training and testing the models. 
- Data Preprocessing and Training: Python scripts used for cleaning the data and training machine learning models. 
- models: Serialized machine learning models (.pkl files) for Kidney, Heart, and Liver prediction. 
- OrganDiseasePrediction.py: Main script for running predictions. 
- runwebapp: Script to launch the web application. 
- requirements.txt: Dependencies required to run the project. 
-README.md: Project documentation.
## 🖥️ Installation
Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

Steps

1. Clone the repository:

```bash 
    git clone https://github.com/tejas6376/disease-prediction-system.git
    cd disease-prediction-system
```   

2. Install the required dependencies:

```bash 
    pip install -r requirements.txt
```   

3. Run the web application:

```bash 
    streamlit run "OrganDiseasePrediction.py"
```   
## 🔗 Dataset
Download the datasets from the Data folder in the repository
## Usage
1. Launch the web application.
2. Input patient data into the form fields for Kidney, Heart, and Liver health metrics.
3. Submit the form to get predictions on the likelihood of diseases.
## Models
The system uses separate models for each organ:  
- Kidney: Trained with kidney-related health metrics. 
- Heart: Predicts heart disease based on cardiovascular data. 
- Liver: Evaluates liver function metrics for disease prediction.
## 🚀 Working

Data Preprocessing:
![image](https://github.com/user-attachments/assets/7406b47d-3be5-4912-829c-176703371ae3)

Proposed Architecture:
![image](https://github.com/user-attachments/assets/b257320a-8377-4d22-8e53-59bc8fed5574)

Model Accuracy Scores on each organ:
![image](https://github.com/user-attachments/assets/7f86eeaf-ea39-473c-9c7e-23466f012678)

We have compared all the models in the above table for all
the three organs and we get the desired result and
their accuracy. SVM Model has the maximum
accuracy with 98 % in Kidney, 81.9% in Heart and
74% in Liver
## Future Scope
- Add more disease categories.
- Enhance the prediction accuracy with deep learning techniques.
- Improve the UI/UX of the web application.
- Integrate with a database for patient record management.
## CONCLUSION
In Conclusion, the project is based on machine learning
that will analyze the medical report for kidney, liver
and blood- related diseases. The system extracts the
suitable data, classifies it and displays the patient's
health information on the dashboard. The most
proficient model among these will be used to predict
the presence of a particular disease in the patient. With
the help of this system, the potential of machine
learning will be manifested for improving the patient's
health more efficiently. Compared to the traditional
methods, this system will be more accurate and show
quick diagnosis of the patient.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.
## 📧 Contact
For any queries or suggestions, feel free to reach out:
- [Tejas Mahajan] 
- [tejasmahajan101@gmail.com] 
- [https://linkedin.com/in/tejas-mahajan-185270285/]
- [https://github.com/tejas6376]