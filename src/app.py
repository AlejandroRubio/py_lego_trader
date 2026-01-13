import os
import pandas as pd

from utils.amazon_scrapper import get_current_price
from utils.excel_service import get_excel_content, transform_dataframe_2_lego_model
from models.lego_model import lego_model

EXCEL_INPUT_FILE_PATH = os.getcwd().replace("src","")+ "/listado_legos.xlsx"
EXCEL_OUTPUT_FILE_PATH = os.getcwd().replace("src","")+ "/listado_legos_out.xlsx"
SHEET_NAME= "Listado"


def calc_profitability(lego_object: lego_model, current_price_str: str):

    if current_price_str:
        current_price = float(
            current_price_str
            .replace(" ", "")
            .replace("€", "")
            .replace("EUR", "")
            .replace("\\xa0", "")
        )
        lego_object.PrecioActual = current_price
        lego_object.Beneficio = lego_object.PrecioActual - lego_object.PrecioCompra

        if lego_object.PrecioCompra != 0:
            lego_object.Rentabilidad = lego_object.Beneficio *100/ lego_object.PrecioCompra
        else:
            lego_object.Rentabilidad = 0

    return lego_object


def main():
    legos_output_list = []
    
    legos_input_dataframe = get_excel_content(EXCEL_INPUT_FILE_PATH, SHEET_NAME)
    legos_input_list = transform_dataframe_2_lego_model(legos_input_dataframe)
    for lego in legos_input_list:
        if lego.Link != "-":
            print(f"Scrapping price for set with ID: {lego.ID}")
            amazon_recovered_object = get_current_price(lego.Link)
            current_price = amazon_recovered_object["price"]
            lego_output = calc_profitability(lego, current_price)
            legos_output_list.append(lego_output)
        else:
            current_price=str(lego.PrecioCompra)
            lego_output = calc_profitability(lego, current_price)
            legos_output_list.append(lego_output)

    
    legos_output_datafram=pd.DataFrame(lego.model_dump() for lego in legos_output_list)
    legos_output_datafram.to_excel(EXCEL_OUTPUT_FILE_PATH)


if __name__=="__main__":
    main()