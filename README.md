# 🚗 Car Price Estimator

A machine learning-powered web application that predicts the **resale price of a used car** based on input features like car name, company, fuel type, and kilometers driven.

🔗 **Live Demo**: [https://car-price-estimator.onrender.com](https://car-price-estimator.onrender.com)

---

## 📌 Features

- Predict resale value of used cars
- Clean, user-friendly Streamlit interface
- One-hot encoding for categorical features
- Trained using Linear Regression model
- Deployed on Render

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas & NumPy**
- **Pickle**

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/shruti5155/car-price-estimator.git
cd car-price-estimator

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the Streamlit app
streamlit run application.py
