# Food Delivery Time Prediction

## Project Overview

Machine learning regression project to predict **food delivery time in minutes** using delivery, traffic, weather, vehicle, distance, and delivery-person features.

## Objective

* Predict food delivery time.
* Identify important factors affecting delivery duration.
* Compare regression models.
* Evaluate and select the best-performing model.

## Dataset

* **Records:** 41,953
* **Features:** 20
* **Target:** `Time_taken(min)`
* **Problem Type:** Regression
* **Train/Test Split:** 80% / 20%

### Key Features

* Delivery person age and rating
* Delivery distance
* Traffic density
* Weather conditions
* Vehicle condition
* Multiple deliveries
* Order and pickup time
* Order type and vehicle type
* Festival and city

## Project Workflow

`Data Understanding → Data Cleaning → Feature Engineering → EDA → Preprocessing → Model Building → Model Comparison → Overfitting Check → Prediction → Feature Importance`

## Feature Engineering

* Converted target time to numeric format.
* Created **Delivery_Distance** from geographical coordinates.
* Extracted **order hour** and **pickup hour**.
* Handled missing and inconsistent values.
* Encoded categorical features.

## Models

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor
* Fine-Tuned Gradient Boosting

## Evaluation Metrics

* **MAE** – Average prediction error in minutes.
* **RMSE** – Penalizes larger prediction errors.
* **R²** – Measures explained variance.

## Model Results

| Model                   |        MAE |       RMSE |         R² |
| ----------------------- | ---------: | ---------: | ---------: |
| Linear Regression       |     4.7693 |     6.0311 |     0.5778 |
| **Random Forest**       | **3.2274** | **4.0859** | **0.8062** |
| Gradient Boosting       |     3.6687 |     4.6121 |     0.7531 |
| Tuned Gradient Boosting |     3.6574 |     4.6031 |     0.7541 |

### Final Model

**Random Forest Regressor**

* **MAE:** 3.2274 minutes
* **RMSE:** 4.0859 minutes
* **R²:** 0.8062

## Overfitting Check

| Dataset  |    MAE |     R² |
| -------- | -----: | -----: |
| Training | 1.2012 | 0.9736 |
| Testing  | 3.2274 | 0.8062 |

The difference between training and testing performance indicates **some overfitting**.

## Unseen Data Prediction

```text
Actual Time       : 18.00 minutes
Predicted Time    : 15.24 minutes
Prediction Error  : 2.76 minutes
```

## Key Concepts

* Regression
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Categorical Encoding
* Random Forest
* Gradient Boosting
* Model Comparison
* Overfitting Analysis
* Feature Importance
* Unseen Data Prediction

## Technologies

**Python | Pandas | NumPy | Matplotlib | Seaborn | Scikit-learn | Google Colab**

## Conclusion

The project successfully predicts food delivery time using machine learning regression techniques. Among the evaluated models, Random Forest Regressor achieved the best test performance with an R² of 0.8062 and MAE of 3.23 minutes, making it the selected model for prediction.
