import pandas as pd
from models.lego_model import lego_model

def get_excel_content(excel_file_path: str, sheet_name: str):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    print(df)
    return df


def transform_dataframe_2_lego_model(dataframe: pd.DataFrame):
    legos_objects_list = []
    for index, row in dataframe.iterrows():
        print(row['ID'])
        lego = lego_model(
            ID= row['ID'], 
            Nombre=row['Nombre'], 
            Link=row['Link'], 
            Unidades=row['Unidades'], 
            PrecioCompra=row['PrecioCompra'], 
            PrecioActual=row['PrecioActual'], 
            Beneficio=row['Beneficio'], 
            Rentabilidad=row['Rentabilidad'], 
        ) 
        legos_objects_list.append(lego)
    return legos_objects_list