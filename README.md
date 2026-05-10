# Healthcare Premium Prediction

This project predicts health insurance premium cost using machine learning and provides a Streamlit web app for interactive predictions.

## Features

- Predict health insurance cost from demographic, financial, and medical inputs
- Streamlit UI for quick manual testing
- Pretrained model artifacts included in the repository
- Training and experimentation notebooks included in `notebooks/`

## Project Structure

```text
HealthcarePremiumPrediction/
├── app/
│   ├── main.py
│   ├── prediction_helper.py
│   └── artifacts/
├── artifacts/
├── notebooks/
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer is recommended
- `pip` for installing dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Run the Streamlit App

The Streamlit app code lives in the `app` folder. Run it from inside that directory so the artifact paths resolve correctly.

```bash
cd app
streamlit run main.py
```

## Model Inputs

The app uses the following fields for prediction:

- Age
- Number of Dependants
- Income in Lakhs
- Genetical Risk
- Insurance Plan
- Employment Status
- Gender
- Marital Status
- BMI Category
- Smoking Status
- Region
- Medical History

## Notebooks

The notebooks in `notebooks/` are used for data exploration, preprocessing, model training, and experimentation with different age groups and feature combinations.

Some notebooks use `xgboost`, which is included in `requirements.txt`.

## Notes

- Pretrained model and scaler files are already included in the repository.
- The app predicts cost using separate model pipelines for younger applicants and the rest of the population.
- If you move files around, update artifact paths in `app/prediction_helper.py`.
