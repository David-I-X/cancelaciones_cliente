---

# 📉 Telecom X – Análisis de Cancelación de Clientes

 📊 **¿Por qué los clientes están cancelando el servicio?**  
Este proyecto explora, limpia y analiza los datos de clientes de Telecom X para descubrir los **factores clave de evasión** y guiar futuras estrategias de retención.

---

## 🚀 Objetivo

Telecom X enfrenta una **alta tasa de cancelaciones**.  
Nuestro reto es **descubrir los motivos detrás de esta fuga**, analizando los datos a fondo con Python, para que el equipo de Data Science pueda:

- Crear modelos predictivos de cancelación
- Diseñar campañas de fidelización efectivas
- Optimizar los tipos de contrato y servicios ofrecidos

---

## 🛠️ Tecnologías y Librerías Usadas

- **Python 3.11**
- Jupyter Notebook
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- Git + GitHub (versionado local)
- 📁 Proyecto ejecutado 100% en entorno **local Linux (Ubuntu 24.04 LTS)**

---

## 🔍 Etapas del Proyecto

### 1. 📥 **Extracción y carga de datos**
- Se importaron datos JSON desde una API simulada de GitHub
- Conversión y limpieza de estructuras anidadas con `json_normalize`

### 2. 🧼 **Limpieza y transformación de datos**
- Estandarización de columnas y valores (`Sí/No` → `Activo/Inactivo`)
- Separación de categorías (cliente, contrato, servicios) para análisis modular
- Rango de cargos mensuales creados como variable categórica

### 3. 📊 **Análisis Exploratorio de Datos (EDA)**
- Gráficos de barras, histogramas con KDE, scatterplots y mapas de calor
- Identificación de patrones de cancelación por tipo de cliente
- Segmentación por contrato, método de pago, y facturación

### 4. 🧠 **Insights clave**
| Variable              | Impacto | Acción Recomendable |
|-----------------------|---------|----------------------|
| Tipo de contrato      | 🔥 Muy Alto | Incentivar contratos a largo plazo |
| Método de pago        | Alto    | Revisar percepción de pago automático |
| Cargo mensual elevado | Alto    | Personalizar planes y descuentos |
| Facturación electrónica | Moderado | Mejorar claridad de factura |

> 📌 *Ver el archivo del notebook para visualizaciones y análisis detallado.*

---

## 📁 Estructura del Proyecto

```

cancelaciones_cliente/
├── data
│   └── datos_telecomx.csv
├── src
│   └── etl.py
├── notebooks
│   ├── analisis_json.ipynb
│   └── eda.ipynb
├── README.md
├── requirements.txt

```

---

## 📎 Reproducción local

### 🔧 Para Linux / macOS

1. Clona este repositorio:
   ```bash
   git clone https://github.com/David-I-X/cancelaciones_cliente.git
   cd cancelaciones_cliente
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el pipeline ETL (opcional si quieres datos limpios listos):

   ```bash
   python src/etl.py
   ```

5. Ejecuta el notebook de análisis:

   ```bash
   jupyter notebook
   ```

   O abre el proyecto en tu **editor de código preferido** (VS Code, PyCharm, etc.) y ejecuta desde allí el notebook o scripts.

---

### 🪟 Para Windows

1. Abre PowerShell o CMD y clona el repositorio:

   ```powershell
   git clone https://github.com/David-I-X/cancelaciones_cliente.git
   cd cancelaciones_cliente
   ```

2. Crea y activa un entorno virtual:

   ```powershell
   python -m venv env
   .\env\Scripts\activate
   ```

3. Instala las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

4. Ejecuta el pipeline ETL:

   ```powershell
   python src\etl.py
   ```

5. Ejecuta el notebook:

   ```powershell
   jupyter notebook
   ```

   O abre el proyecto con tu editor favorito (VS Code, PyCharm) y trabaja desde allí.

> 💡 *Si no tienes Jupyter, puedes instalarlo con:*

```powershell
pip install notebook
```

---

## 📌 Próximos pasos

* 📈 Entrenamiento de modelos de clasificación para predecir cancelación
* 🧠 Implementación de árbol de decisiones / regresión logística
* 📊 Dashboard dinámico con **Streamlit** para el área de negocios

---

## 🙌 Autor

**David Aguirre**
📍 Colombia | 🐧 Linux Lover | 💼 Data Analyst en progreso
💬 *"Los datos no mienten, pero sí necesitan que los escuchen bien."*

---

## ⭐ ¿Te fue útil?

¡Dale una estrella ⭐ al repo si te gustó o aprendiste algo útil!
