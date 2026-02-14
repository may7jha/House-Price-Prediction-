import streamlit as st
import joblib
import pandas as pd

# ----------------------------------------
# TITLE
# ----------------------------------------
st.title("🏠 House Price Prediction")

st.write("Enter house details:")

# ----------------------------------------
# LOAD MODEL
# ----------------------------------------
model = joblib.load("notebooks/house_price_model.pkl")

# ----------------------------------------
# USER INPUTS
# ----------------------------------------
grlivarea = st.number_input("GrLivArea (Living Area)", value=1500)
overallqual = st.slider("Overall Quality", 1, 10, 5)
garagearea = st.number_input("Garage Area", value=400)
yearbuilt = st.number_input("Year Built", value=2000)
lotarea = st.number_input("Lot Area", value=8000)
totalbsmtsf = st.number_input("Basement Area", value=900)
fullbath = st.number_input("Full Bathrooms", value=2)
bedroom = st.number_input("Bedrooms", value=3)
fireplaces = st.number_input("Fireplaces", value=1)
totrms = st.number_input("Total Rooms", value=6)

# ----------------------------------------
# LOAD TRAINING COLUMNS
# ----------------------------------------
train_cols = joblib.load("notebooks/train_columns.pkl")

# ----------------------------------------
# CREATE INPUT DATAFRAME LIKE TRAINING
# ----------------------------------------
input_data = pd.DataFrame(columns=train_cols)

# Fill all columns with 0 first
input_data.loc[0] = 0

# ----------------------------------------
# PUT USER VALUES IN CORRECT COLUMNS
# ----------------------------------------
input_data["GrLivArea"] = grlivarea
input_data["OverallQual"] = overallqual
input_data["GarageArea"] = garagearea
input_data["YearBuilt"] = yearbuilt
input_data["LotArea"] = lotarea
input_data["TotalBsmtSF"] = totalbsmtsf
input_data["FullBath"] = fullbath
input_data["BedroomAbvGr"] = bedroom
input_data["Fireplaces"] = fireplaces
input_data["TotRmsAbvGrd"] = totrms

currency = st.selectbox(
    "Select Currency",
    ["USD ($)", "INR (₹)"]
)


# ----------------------------
# PREDICTION
# ----------------------------
if st.button("Predict Price"):

    price = model.predict(input_data)[0]

    # conversion rate
    usd_to_inr = 83

    if currency == "USD ($)":
        display_price = price
        symbol = "$"
    else:
        display_price = price * usd_to_inr
        symbol = "₹"

    st.success(f"Predicted Price = {symbol} {display_price:,.2f}")
