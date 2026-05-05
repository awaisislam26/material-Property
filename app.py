import streamlit as st

# Page layout
st.set_page_config(page_title="Mech-ICT Toolbox", layout="wide")

st.title("⚙️ Mechanical Engineering ICT Toolbox")
st.write("A professional utility for Unit Conversion and Material Properties.")

# Create two columns for two different tools
col1, col2 = st.columns(2)

with col1:
    st.header("📏 Pressure Unit Converter")
    st.info("Essential for Fluid Mechanics & Thermodynamics")
    
    input_val = st.number_input("Enter Value:", value=1.0)
    from_unit = st.selectbox("From:", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere (atm)"])
    to_unit = st.selectbox("To:", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere (atm)"])

    # Conversion Logic (Reference: 1 Bar = 100,000 Pa, 1 PSI = 6894.76 Pa)
    to_pascal = {
        "Pascal (Pa)": 1.0,
        "Bar": 100000.0,
        "PSI": 6894.76,
        "Atmosphere (atm)": 101325.0
    }
    
    # Logic: Convert input to Pascal first, then to target unit
    val_in_pa = input_val * to_pascal[from_unit]
    final_result = val_in_pa / to_pascal[to_unit]
    
    st.success(f"**Result:** {round(final_result, 4)} {to_unit}")

with col2:
    st.header("🧪 Material Property Finder")
    st.info("Quick reference for Mechanics of Materials")
    
    material = st.selectbox("Select Material:", ["Mild Steel", "Aluminum Alloy", "Copper", "Titanium"])
    
    # Data Dictionary
    properties = {
        "Mild Steel": {"Elastic Modulus (E)": "200 GPa", "Density": "7850 kg/m³", "Yield Strength": "250 MPa"},
        "Aluminum Alloy": {"Elastic Modulus (E)": "70 GPa", "Density": "2700 kg/m³", "Yield Strength": "275 MPa"},
        "Copper": {"Elastic Modulus (E)": "110 GPa", "Density": "8960 kg/m³", "Yield Strength": "70 MPa"},
        "Titanium": {"Elastic Modulus (E)": "116 GPa", "Density": "4500 kg/m³", "Yield Strength": "434 MPa"}
    }
    
    selected_props = properties[material]
    
    st.write(f"**Properties of {material}:**")
    for key, val in selected_props.items():
        st.write(f"- {key}: `{val}`")

st.write("---")
st.caption("Developed for BSc Mechanical Engineering - ICT Project 2026")
