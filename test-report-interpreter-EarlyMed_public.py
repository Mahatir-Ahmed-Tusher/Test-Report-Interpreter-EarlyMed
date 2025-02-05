import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="EarlyMed - Test Report Interpreter",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 32px 0 rgba(31,38,135,0.37);
        padding: 20px;
    }

    /* Input fields styling */
    .stNumberInput, .stTextInput {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        padding: 10px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #3498db, #2980b9) !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 10px 25px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.3) !important;
    }

    /* Success message styling */
    .stSuccess {
        background: linear-gradient(135deg, rgba(46,213,115,0.2), rgba(46,213,115,0.1)) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(46,213,115,0.3) !important;
        padding: 20px !important;
    }

    /* Error message styling */
    .stError {
        background: linear-gradient(135deg, rgba(255,71,87,0.2), rgba(255,71,87,0.1)) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255,71,87,0.3) !important;
        padding: 20px !important;
    }

    /* Title styling */
    h1, h2, h3 {
        background: linear-gradient(120deg, #3498db, #2980b9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* Card styling for sections */
    .css-1y4p8pa {
        border-radius: 20px !important;
        padding: 20px !important;
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        box-shadow: 0 8px 32px 0 rgba(31,38,135,0.37) !important;
    }
</style>
""", unsafe_allow_html=True)

try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Horizontal menu instead of sidebar
selected = option_menu(
    menu_title=None,
    options=['Home', 'Diabetes Prediction', 'Heart Risk Prediction', 'Parkinsons Prediction'],
    icons=['house-heart-fill', 'activity', 'heart-pulse-fill', 'person-walking'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(255,255,255,0.1)"},
        "icon": {"color": "#3498db", "font-size": "25px"}, 
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "0px",
            "padding": "10px",
            "--hover-color": "rgba(255,255,255,0.2)"
        },
        "nav-link-selected": {"background-color": "rgba(255,255,255,0.2)"},
    }
)

# Home Page
if selected == 'Home':
    
    st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=200)  

    st.title("Welcome to Test Report Interpreter - Your Early Disease Detection Tool")
    
    # Welcome text
    st.markdown("""
    ### 🩺 **About EarlyMed**
    EarlyMed is a platform designed by a team of VIT-AP University to help you understand your medical test results before visiting a doctor. 
    If you've recently undergone medical tests at a pathology lab but haven't had the chance to consult a doctor yet, 
    this tool can provide you with preliminary insights into your health.

    ### 🎯 **What will we do in this Test Report Interpreter?**
   If you've been diagnosed with any of the following diseases and have received your lab test report but haven't had the chance to consult a doctor yet, we're here to help. Currently, we support three diseases, but more disorders will be added soon!
    1. **Diabetes**: Predicts the likelihood of diabetes based on factors like glucose levels, blood pressure, and BMI.
    2. **Heart Disease**: Assesses the risk of heart disease using parameters like cholesterol levels, blood pressure, and ECG results.
    3. **Parkinson's Disease**: Evaluates the possibility of Parkinson's disease using voice analysis and other biomarkers.

    ### 🧪 **How to Use EarlyMed**
    To get started, you'll need the results of certain medical tests. If you haven't undergone these tests yet, 
    we recommend visiting a nearby diagnostic center or pathology lab. Here are some common tests you might need:

    #### Common Tests and Their Purposes:
    - **Lipid Profile**: Measures cholesterol levels (e.g., LDL, HDL, triglycerides) to assess heart health.
    - **Blood Sugar Test**: Measures glucose levels to check for diabetes or prediabetes.
    - **ECG (Electrocardiogram)**: Records the electrical activity of the heart to detect heart disease.
    - **Voice Analysis**: Used for Parkinson's disease diagnosis by analyzing vocal patterns.
    - **Complete Blood Count (CBC)**: Provides an overview of your overall health and detects various disorders.

    These values are typically included in standard medical reports. If you already have your test results, 
    you can proceed to the respective disease prediction section from the sidebar.

    ### ⚠️ **Important Note**
    EarlyMed is not a substitute for professional medical advice. Always consult a qualified healthcare provider 
    for a comprehensive diagnosis and treatment plan.
    """)

    # Call to action
    st.markdown("""
    ### 🚀 **Get Started**
    Use the sidebar to navigate to the disease prediction section of your choice. Enter your test results, 
    and EarlyMed will provide you with a preliminary assessment.
    """)

    # Footer
    st.markdown("---")
    st.markdown("© 2025 EarlyMed. All rights reserved.")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
     # Display the logo at the top of the page
    st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=200)  # Adjust width as needed
    st.title('Diabetes Prediction Based on Test Reports')
    # Description of terms
    st.markdown("""
    ### Understanding the Input Fields:
    Below are the descriptions of the terms used in this prediction model. Please provide accurate values for better results.

    - **Number of Pregnancies**: The number of times the person has been pregnant. (Normal range: 0–17)
    - **Glucose Level**: The concentration of glucose in the blood, measured in mg/dL. (Normal range: 70–140 mg/dL)
    - **Blood Pressure Value**: The systolic blood pressure, measured in mmHg. (Normal range: 90–120 mmHg)
    - **Skin Thickness Value**: The thickness of the skin fold at the triceps, measured in mm. (Normal range: 10–50 mm)
    - **Insulin Level**: The concentration of insulin in the blood, measured in µU/mL. (Normal range: 16–166 µU/mL)
    - **BMI (Body Mass Index)**: A measure of body fat based on height and weight. (Normal range: 18.5–24.9)
    - **Diabetes Pedigree Function**: A score that indicates the genetic influence of diabetes based on family history. (Normal range: 0.08–2.42)
    - **Age**: The age of the person in years. (Normal range: 21–81 years)
    """)

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0, help="Enter the number of pregnancies (0–17).")
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=200, value=0, help="Enter the glucose level in mg/dL (70–140 mg/dL is normal).")
    
    with col2:
        BloodPressure = st.number_input('Blood Pressure Value (mmHg)', min_value=0, max_value=150, value=0, help="Enter the systolic blood pressure in mmHg (90–120 mmHg is normal).")
        SkinThickness = st.number_input('Skin Thickness Value (mm)', min_value=0, max_value=100, value=0, help="Enter the skin thickness in mm (10–50 mm is normal).")
    
    with col3:
        Insulin = st.number_input('Insulin Level (µU/mL)', min_value=0, max_value=1000, value=0, help="Enter the insulin level in µU/mL (16–166 µU/mL is normal).")
        BMI = st.number_input('BMI Value', min_value=0.0, max_value=70.0, value=0.0, help="Enter the BMI value (18.5–24.9 is normal).")
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=3.0, value=0.0, help="Enter the diabetes pedigree function value (0.08–2.42 is normal).")
    
    with col2:
        Age = st.number_input('Age of the Person', min_value=0, max_value=120, value=0, help="Enter the age of the person (21–81 years is normal).")
    
    # Code for Prediction
    diab_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'We are sorry to say that, you are diabetic'
        else:
            diab_diagnosis = 'Congratulations! you are not diabetic'
        
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Risk Prediction':
    st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=200)
    st.title('Heart Risk Prediction Based on Test Reports')
    # Description of terms
    st.markdown("""
    ### Understanding the Input Fields:
    Below are the descriptions of the terms used in this prediction model. Please provide accurate values for better results.

    - **Age**: The age of the person in years. (Normal range: 29–77 years)
    - **Sex**: The gender of the person (0 = female, 1 = male).
    - **Chest Pain Type**: The type of chest pain experienced. (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic)
    - **Resting Blood Pressure**: The resting blood pressure in mmHg. (Normal range: 90–120 mmHg)
    - **Serum Cholesterol**: The serum cholesterol level in mg/dL. (Normal range: 126–200 mg/dL)
    - **Fasting Blood Sugar**: Indicates if fasting blood sugar is > 120 mg/dL (1 = true, 0 = false).
    - **Resting Electrocardiographic Results**: The results of the resting ECG. (0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy)
    - **Maximum Heart Rate Achieved**: The maximum heart rate achieved during exercise. (Normal range: 71–202 bpm)
    - **Exercise Induced Angina**: Indicates if angina was induced by exercise (1 = yes, 0 = no).
    - **ST Depression Induced by Exercise**: The ST depression induced by exercise relative to rest. (Normal range: 0–6.2 mm)
    - **Slope of the Peak Exercise ST Segment**: The slope of the peak exercise ST segment. (0 = upsloping, 1 = flat, 2 = downsloping)
    - **Number of Major Vessels Colored by Fluoroscopy**: The number of major vessels colored by fluoroscopy (0–3).
    - **Thalassemia**: A blood disorder called thalassemia. (0 = normal, 1 = fixed defect, 2 = reversible defect)
    """)

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=0, help="Enter the age of the person (29–77 years is normal).")
        sex = st.number_input('Sex (0 = female, 1 = male)', min_value=0, max_value=1, value=0, help="Enter 0 for female or 1 for male.")
    
    with col2:
        cp = st.number_input('Chest Pain Type (0–3)', min_value=0, max_value=3, value=0, help="Enter the type of chest pain (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic).")
        trestbps = st.number_input('Resting Blood Pressure (mmHg)', min_value=0, max_value=200, value=0, help="Enter the resting blood pressure in mmHg (90–120 mmHg is normal).")
    
    with col3:
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=0, max_value=600, value=0, help="Enter the serum cholesterol level in mg/dL (126–200 mg/dL is normal).")
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dL (1 = true, 0 = false)', min_value=0, max_value=1, value=0, help="Enter 1 if fasting blood sugar > 120 mg/dL, else 0.")
    
    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results (0–2)', min_value=0, max_value=2, value=0, help="Enter the resting ECG results (0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy).")
        thalach = st.number_input('Maximum Heart Rate Achieved (bpm)', min_value=0, max_value=300, value=0, help="Enter the maximum heart rate achieved during exercise (71–202 bpm is normal).")
    
    with col2:
        exang = st.number_input('Exercise Induced Angina (1 = yes, 0 = no)', min_value=0, max_value=1, value=0, help="Enter 1 if angina was induced by exercise, else 0.")
        oldpeak = st.number_input('ST Depression Induced by Exercise (mm)', min_value=0.0, max_value=10.0, value=0.0, help="Enter the ST depression induced by exercise (0–6.2 mm is normal).")
    
    with col3:
        slope = st.number_input('Slope of the Peak Exercise ST Segment (0–2)', min_value=0, max_value=2, value=0, help="Enter the slope of the peak exercise ST segment (0 = upsloping, 1 = flat, 2 = downsloping).")
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy (0–3)', min_value=0, max_value=3, value=0, help="Enter the number of major vessels colored by fluoroscopy (0–3).")
    
    with col1:
        thal = st.number_input('Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)', min_value=0, max_value=2, value=0, help="Enter the thalassemia value (0 = normal, 1 = fixed defect, 2 = reversible defect).")
    
    # Code for Prediction
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'Your Heart is at Risk' if heart_prediction[0] == 1 else 'Your Heart is not at risk'
            st.success(heart_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
     # Display the logo at the top of the page
    st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=200)
    st.title("Parkinson's Prediction Based on Test Reports")
 
    # Description of terms
    st.markdown("""
    ### Understanding the Input Fields:
    Below are the descriptions of the terms used in this prediction model. Please provide accurate values for better results.

    - **MDVP:Fo(Hz)**: Average vocal fundamental frequency. (Normal range: 88–260 Hz)
    - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency. (Normal range: 102–592 Hz)
    - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency. (Normal range: 65–239 Hz)
    - **MDVP:Jitter(%)**: Variation in fundamental frequency. (Normal range: 0.001–0.033%)
    - **MDVP:Jitter(Abs)**: Absolute variation in fundamental frequency. (Normal range: 0.000007–0.000260)
    - **MDVP:RAP**: Relative amplitude perturbation. (Normal range: 0.0006–0.021)
    - **MDVP:PPQ**: Five-point period perturbation quotient. (Normal range: 0.0006–0.019)
    - **Jitter:DDP**: Average absolute difference of differences between cycles. (Normal range: 0.0018–0.063)
    - **MDVP:Shimmer**: Variation in amplitude. (Normal range: 0.009–0.119)
    - **MDVP:Shimmer(dB)**: Shimmer in decibels. (Normal range: 0.085–1.302 dB)
    - **Shimmer:APQ3**: Three-point amplitude perturbation quotient. (Normal range: 0.004–0.031)
    - **Shimmer:APQ5**: Five-point amplitude perturbation quotient. (Normal range: 0.005–0.042)
    - **MDVP:APQ**: Amplitude perturbation quotient. (Normal range: 0.007–0.054)
    - **Shimmer:DDA**: Average absolute difference between consecutive differences of amplitudes. (Normal range: 0.013–0.169)
    - **NHR**: Noise-to-harmonics ratio. (Normal range: 0.0006–0.314)
    - **HNR**: Harmonics-to-noise ratio. (Normal range: 8.441–33.047)
    - **RPDE**: Recurrence period density entropy. (Normal range: 0.256–0.685)
    - **DFA**: Detrended fluctuation analysis. (Normal range: 0.574–0.825)
    - **spread1**: Nonlinear measure of fundamental frequency variation. (Normal range: -7.964–-2.434)
    - **spread2**: Nonlinear measure of fundamental frequency variation. (Normal range: 0.006–0.450)
    - **D2**: Correlation dimension. (Normal range: 1.423–3.671)
    - **PPE**: Pitch period entropy. (Normal range: 0.044–0.527)
    """)

    # Getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, value=0.0, help="Enter the average vocal fundamental frequency (88–260 Hz is normal).")
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=600.0, value=0.0, help="Enter the maximum vocal fundamental frequency (102–592 Hz is normal).")
    
    with col2:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, value=0.0, help="Enter the minimum vocal fundamental frequency (65–239 Hz is normal).")
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.0, help="Enter the variation in fundamental frequency (0.001–0.033% is normal).")
    
    with col3:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=1.0, value=0.0, help="Enter the absolute variation in fundamental frequency (0.000007–0.000260 is normal).")
        RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, value=0.0, help="Enter the relative amplitude perturbation (0.0006–0.021 is normal).")
    
    with col4:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, value=0.0, help="Enter the five-point period perturbation quotient (0.0006–0.019 is normal).")
        DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=1.0, value=0.0, help="Enter the average absolute difference of differences between cycles (0.0018–0.063 is normal).")
    
    with col5:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=1.0, value=0.0, help="Enter the variation in amplitude (0.009–0.119 is normal).")
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.0, help="Enter the shimmer in decibels (0.085–1.302 dB is normal).")
    
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=1.0, value=0.0, help="Enter the three-point amplitude perturbation quotient (0.004–0.031 is normal).")
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=1.0, value=0.0, help="Enter the five-point amplitude perturbation quotient (0.005–0.042 is normal).")
    
    with col2:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=1.0, value=0.0, help="Enter the amplitude perturbation quotient (0.007–0.054 is normal).")
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=1.0, value=0.0, help="Enter the average absolute difference between consecutive differences of amplitudes (0.013–0.169 is normal).")
    
    with col3:
        NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, value=0.0, help="Enter the noise-to-harmonics ratio (0.0006–0.314 is normal).")
        HNR = st.number_input('HNR', min_value=0.0, max_value=50.0, value=0.0, help="Enter the harmonics-to-noise ratio (8.441–33.047 is normal).")
    
    with col4:
        RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, value=0.0, help="Enter the recurrence period density entropy (0.256–0.685 is normal).")
        DFA = st.number_input('DFA', min_value=0.0, max_value=1.0, value=0.0, help="Enter the detrended fluctuation analysis (0.574–0.825 is normal).")
    
    with col5:
        spread1 = st.number_input('spread1', min_value=-10.0, max_value=0.0, value=0.0, help="Enter the nonlinear measure of fundamental frequency variation (-7.964–-2.434 is normal).")
        spread2 = st.number_input('spread2', min_value=0.0, max_value=1.0, value=0.0, help="Enter the nonlinear measure of fundamental frequency variation (0.006–0.450 is normal).")
    
    with col1:
        D2 = st.number_input('D2', min_value=0.0, max_value=5.0, value=0.0, help="Enter the correlation dimension (1.423–3.671 is normal).")
        PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, value=0.0, help="Enter the pitch period entropy (0.044–0.527 is normal).")
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            parkinsons_diagnosis = "Your patient has Parkinson's disease" if parkinsons_prediction[0] == 1 else "Congratulations! your patient does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Footer for all pages
st.markdown("---")
st.markdown("""
**Disclaimer**: This app is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any health concerns. It can only be used to get aware of the health before going to the doctor.
""")
