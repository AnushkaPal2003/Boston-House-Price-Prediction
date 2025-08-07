# 🏠 Boston House Price Prediction

An end-to-end machine learning project to predict housing prices in Boston using regression models, visual dashboards, and a Streamlit web app.

## 📁 Project Structure
- `notebooks/`: Jupyter notebooks for EDA, modeling, and prediction
- `models/`: Saved models using Joblib
- `streamlit_dashboard/`: Streamlit for interactive prediction
- `dashboards/`: Visualizations of model performance
- `requirements.txt`: Python dependencies

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook 
```bash
jupyter notebook notebooks/Boston House Price Prediction.ipynb
```

### To see the Dashboard of the models 
```bash
streamlit run streamlit_dashboard/Boston.py 
```

### To see the Streamlit Prediction
```bash
streamlit run streamlit_dashboard/Final.py 
```

## 📊 Models Used
- LinearRegression 
- Ridge
- Lasso
- ElasticNet
- DecisionTreeRegressor
- RandomForestRegressor
- XGBRegressor
- KNeighborsRegressor
- SVR
- VotingRegressor
Models are saved using joblib and loaded for prediction in both the notebook and Streamlit app.

## 📈 Results
- Achieved an R² score of 0.89 using XGBRegressor
- Visual comparison of model performance available in dashboards/
- Feature importance and residual analysis included

## 🌐 Streamlit App Features
- 📌 Input sliders for key features (e.g., RM, LSTAT, PTRATIO)
- 📊 Real-time prediction using trained model
- 📈 Display of predicted price 

## 🧠 Tools & Libraries
- Python, Pandas, NumPy
- Scikit-learn, Joblib, Dtale
- Matplotlib, Seaborn
- Streamlit

### Git Hygiene

This project includes a `.gitignore` file to prevent tracking of:

- Python cache files and logs
- Jupyter notebook checkpoints
- Streamlit config and virtual environments
- IDE-specific settings and OS artifacts
- Model files and Excel exports (optional)

## 🚀 Live Demo

Check out the interactive house price prediction app 👉 [Streamlit App]https://boston-house-price-prediction-4ygrsef4n4kg27aauvedbg.streamlit.app/


## 📬 Contact
For questions or collaboration, feel free to reach out via GitHub or LinkedIn.

- 📁 Project Repository: [Boston House Price Prediction](https://github.com/AnushkaPal2003/Boston-House-Price-Prediction)
- 👤 GitHub Profile: [AnushkaPal2003](https://github.com/AnushkaPal2003)
- 💼 LinkedIn: [Anushka Pal](https://www.linkedin.com/in/anushka-pal-a677731ba)
- 📧 Email: palanushka416@gmail.com
