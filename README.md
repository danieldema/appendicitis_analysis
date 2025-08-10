# Pediatric Appendicitis Prediction System

A machine learning approach for predicting appendicitis in pediatric patients, featuring model comparison and web deployment of a 97% accurate random forest model.

## Project Overview

This project develops and compares multiple machine learning models to predict appendicitis diagnosis in children using clinical data from Children's Hospital St. Hedwig, Regensburg, Germany. The best-performing model is deployed as a containerized web application via Microsoft Azure.

## Tech Stack

**Machine Learning & Data Science:**
- Python (pandas, scikit-learn, matplotlib)
- Logistic Regression, Decision Trees, Random Forest
- Cross-validation and hyperparameter optimization

**Web Development:**
- Flask (backend API)
- HTML/CSS (frontend)

**Deployment:**
- Docker (containerization)
- Azure App Service (cloud hosting)

## Model Performance Comparison

| Model | Accuracy | AUC Score | Precision (Positive) | Precision (Negative) |
|-------|----------|-----------|---------------------|---------------------|
| **Random Forest** | **97%** | **0.98** | **100%** | **88%** |
| Decision Tree (Optimized) | 96% | 0.95 | 97% | 87% |
| Logistic Regression | 93% | 0.90 | 95% | 86% |

- **Feature Importance Hierarchy**: 
  1. Appendix Diameter (highest impact)
  2. Alvarado Score
  3. Body Temperature
  4. Binary symptoms (lower impact)

- **False Negative Rate**: 3% - Critical for patient safety

The application is containerized and deployed on Azure App Service for scalability and reliability.

**Live Demo**: [https://appendicitisapp-dnf3btg7btapemd4.eastus-01.azurewebsites.net/]

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
