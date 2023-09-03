import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    filtered_patients = patients[patients['conditions'].str.contains(r'\bDIAB1', case=False, regex=True)]
    result = filtered_patients[['patient_id', 'patient_name', 'conditions']]
    
    return result