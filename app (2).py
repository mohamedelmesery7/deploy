import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(page_title="Network Attack Detection", layout="centered")

def load_model():
    model_path = os.path.join(os.getcwd(), "model.pkl")
    return joblib.load(model_path)

def main():
    st.title("🔍 Network Attack Detection Model")
    st.write("Enter the feature values for prediction:")

    # Load the model
    try:
        model = load_model()
        st.success("✅ Model loaded successfully!")
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return

    # Define feature names
    feature_names = [
        "Time", "Length", "Packet Interarrival Time", "Bandwidth Usage",
        "Protocol_0x6002", "Protocol_ARP", "Protocol_CDP", "Protocol_DHCP",
        "Protocol_DTP", "Protocol_ICMP", "Protocol_ICMPv6", "Protocol_IGMPv3",
        "Protocol_LOOP", "Protocol_MDNS", "Protocol_OSPF", "Protocol_STP",
        "Source Encoded"
    ]

    # Create input fields for each feature
    features = []
    for name in feature_names:
        value = st.number_input(f"{name}", value=0.0)
        features.append(value)

    # Prediction
    if st.button("🔍 Predict"):
        try:
            features_array = np.array(features).reshape(1, -1)
            prediction = model.predict(features_array)[0]  # Get the first prediction
            
            # Map prediction to labels
            result = "🟢 Safe" if prediction == 0 else "🔴 Attack"
            
            st.success(f" Prediction: {result}")
        except Exception as e:
            st.error(f"❌ Prediction error: {e}")

if __name__ == "__main__":
    main()
