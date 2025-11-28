# Health Outcomes Analysis – Individual Project

As a junior data analyst, I have been tasked with exploring a health-related dataset and answering a set of statistical questions using Python.  
The focus of this project is to describe the data, visualise key patterns, and perform basic statistical inference.

---

## Project description

The analysis is carried out in a Jupyter Notebook and covers:

- descriptive statistics for selected health variables,
- visualisations to explore distributions and group differences,
- a simple simulation based on the observed disease probability,
- 95% confidence intervals for mean systolic blood pressure using both a normal approximation and a bootstrap method,
- a hypothesis test comparing smokers and non-smokers, with an interpretation in plain language,
- refactoring parts of the analysis into a small HealthAnalyzer class in src/health_analysis.py,
- fitting simple and multiple linear regression models for systolic blood pressure using age and weight as predictors, and visualising the model fit.

All work is done in Python as part of an individual assignment in an introductory data analysis course.

---

## Data

The dataset is provided by the course teacher and stored in the `data/` folder as a CSV file.

It contains individual-level observations with demographic and health-related variables (for example age, sex, and clinical measurements).  
The dataset is used solely for educational and analytical purposes within the course.

---

## Project structure

- `report.ipynb` – Main notebook with code, commentary, figures, and conclusions.
- `data/` – Contains the CSV file used in the analysis.
- `src/` – Contains helper module with the HealthAnalyzer class and realted functions.
- `requirements.txt` – Python dependencies required to run the notebook.
- `.gitignore` – Specifies files and folders that should not be tracked by Git.
- `README.md` - This file.

---

## Reproducibility and environment

This project uses Python 3.13.7 and common data analysis libraries.

To reproduce the analysis:

1. Create and activate a virtual environment.
2. Install dependencies from the project root:

   ```bash
   pip install -r requirements.txt