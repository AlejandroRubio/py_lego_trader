<p align="center">
  <img src="img/logo.png" alt="Logo Seguimiento de Precios" >
</p>


# Seguimiento de precios Lego / Playmobil en Amazon

Script en Python para obtener automáticamente desde Amazon el **precio
actual** de tu colección de sets de **Lego y Playmobil** usando un
fichero Excel como entrada.

## 🧩 Funcionalidad

-   Lee un Excel con tus sets.
-   Recupera el precio actual desde Amazon (si hay URL).
-   Calcula beneficio y rentabilidad.
-   Genera un Excel actualizado.

## 📊 Formato del Excel de entrada

Debe llamarse `listado_legos.xlsx` e incluir una hoja `Listado` con:

  Campo                  Descripción
  ---------------------- --------------------------------------------
  ID                     Identificador del set
  Nombre / Descripción   Nombre del set
  PrecioCompra           Precio original
  Link                   URL de Amazon (o '-' para saltar scraping)

## ▶️ Ejecución

``` bash

python src/main.py
```

## 📤 Salida

Se genera `../listado_legos_out.xlsx` con:

-   PrecioActual\
-   Beneficio\
-   Rentabilidad

## 🛠 Requisitos

- Python 3.10+
- requests==2.32.3
- pandas==2.2.2
- beautifulsoup4==4.12.3
- pydantic==2.7.4
- openpyxl==3.1.5

Instalar dependencias:

``` bash
pip install -r requirements.txt
```

## ⚠️ Notas

-   El scraping puede fallar si Amazon modifica su HTML.
-   Uso personal recomendado.
