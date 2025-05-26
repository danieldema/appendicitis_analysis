# Pediatric Appendicitis Prediction System

A comprehensive machine learning solution for predicting appendicitis in pediatric patients, featuring model comparison, web deployment, and clinical decision support.

## Project Overview

This project develops and compares multiple machine learning models to predict appendicitis diagnosis in children using clinical data from Children's Hospital St. Hedwig, Regensburg, Germany. The best-performing model is deployed as a containerized web application on Azure App Service.

## Architecture

```
Data Pipeline → Model Training → Model Comparison → Web App → Docker → Azure Deployment
```

## Technology Stack

**Machine Learning & Data Science:**
- Python (pandas, scikit-learn, matplotlib)
- Logistic Regression, Decision Trees, Random Forest
- Cross-validation and hyperparameter optimization

**Web Development:**
- Flask (backend API)
- HTML/CSS (frontend)

**DevOps & Deployment:**
- Docker (containerization)
- Azure App Service (cloud hosting)

## Model Performance Comparison

| Model | Accuracy | AUC Score | Precision (Positive) | Precision (Negative) |
|-------|----------|-----------|---------------------|---------------------|
| **Random Forest** | **97%** | **0.98** | **100%** | **88%** |
| Decision Tree (Optimized) | 96% | 0.95 | 97% | 87% |
| Logistic Regression | 93% | 0.90 | 95% | 86% |

## Key Features

### Data Analysis & Preprocessing
- **Feature Engineering**: 12 clinical features including Alvarado Score, appendix diameter, and symptom indicators
- **Data Quality**: Systematic handling of missing values and outliers
- **Statistical Analysis**: Correlation analysis and feature importance evaluation

### Model Development
- **Multiple Algorithms**: Comprehensive comparison of ML approaches
- **Hyperparameter Tuning**: GridSearchCV optimization for best performance
- **Cross-Validation**: Robust model evaluation and selection
- **Feature Importance Analysis**: Identification of key diagnostic indicators

### Web Application
- **User-Friendly Interface**: Intuitive form for clinical data input
- **Real-Time Predictions**: Instant probability calculations

### Production Deployment
- **Containerization**: Docker for consistent environments
- **Cloud Hosting**: Scalable Azure App Service deployment

## Clinical Impact & Insights

### Key Findings
- **Feature Importance Hierarchy**: 
  1. Appendix Diameter (highest impact)
  2. Alvarado Score
  3. Body Temperature
  4. Binary symptoms (lower impact)

- **False Negative Rate**: 2.5% - Critical for patient safety
- **False Positive Rate**: 27% - Acceptable for screening tool

### Clinical Significance
- Supports rapid triage decisions in emergency departments
- Reduces diagnostic uncertainty in pediatric cases
- Provides objective probability assessments alongside clinical judgment

## Deployment

The application is containerized and deployed on Azure App Service for scalability and reliability.

**Live Demo**: [https://appendicitisapp-dnf3btg7btapemd4.eastus-01.azurewebsites.net/]

### Local Development
```bash
# Clone repository
git clone https://github.com/danieldema/appendicitis_analysis

# Install dependencies
pip install -r requirements.txt

# Run Flask application
python app.py

# Or run with Docker
docker build -t appendicitis-app .
docker run -p 5000:5000 appendicitis-app
```

## Project Structure

```
├── app_analysis.ipynb         # Exploratory data analysis
├── app_logreg.ipynb           # Logistic regression models
├── app_decisiontree.ipynb     # Decision tree implementation
├── app_randomforest.ipynb     # Random forest model
├── flask_app/                 # Web application
│   ├── app.py
│   ├── templates/
│   └── static/
├── models/                    # Trained model files
├── Dockerfile                 # Container configuration
└── requirements.txt           # Dependencies
```

## Data Source

Dataset sourced from Kaggle: [Regensburg Pediatric Appendicitis Dataset](https://www.kaggle.com/datasets/joebeachcapital/regensburg-pediatric-appendicitis/data)

## Clinical Disclaimer

This tool is designed to support clinical decision-making and should not replace professional medical judgment. Always consult with qualified healthcare providers for patient care decisions.

---

**Contact**: [https://www.linkedin.com/in/danieldema/] | [danieldema42@gmail.com]

**Repository**: [https://github.com/danieldema/appendicitis_analysis]

**Live Demo**: [https://appendicitisapp-dnf3btg7btapemd4.eastus-01.azurewebsites.net/]
