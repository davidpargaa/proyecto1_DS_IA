📊 Análisis del sector de campings en España (INE)

⸻

1) Objetivo

Analizar la evolución estructural del sector de campings en España, con especial foco en la provincia de A Coruña, utilizando datos oficiales del Instituto Nacional de Estadística (INE).

El objetivo principal es:
	•	Construir un pipeline reproducible de limpieza y transformación de datos.
	•	Generar nuevas variables (feature engineering) que permitan un análisis más profundo.
	•	Explorar patrones de ocupación, estacionalidad y presión de demanda.
	•	Evaluar, desde una perspectiva estratégica, el potencial de crecimiento y ampliación en el mercado.

⸻

2) Dataset
	•	Fuente: Instituto Nacional de Estadística (INE) – Encuesta de ocupación en campings
	•	Archivo utilizado: 2064.csv
	•	Periodo analizado: 2017–2025 (excluyendo 2019 en análisis de ocupación por anomalía detectada)
	•	Frecuencia: Mensual
	•	Nivel geográfico: Provincial

Variables clave:
	•	provincia
	•	date
	•	Establecimientos
	•	Parcelas
	•	Parcelas_Ocupadas
	•	Personal
	•	ocupacion_real (feature construida)

⸻

3) Preguntas de análisis
	•	¿Cómo ha evolucionado la ocupación media anual en A Coruña desde 2017?
	•	¿Qué grado de estacionalidad presenta el mercado?
	•	¿Existe evidencia de saturación en la provincia?
	•	¿Cómo se posiciona A Coruña frente a otras provincias cantábricas?
	•	¿Existe relación entre número de establecimientos y ocupación?
	•	¿El crecimiento de personal está alineado con la demanda?

⸻

4) Data issues & fixes

Durante el proceso de limpieza se detectaron los siguientes problemas:

🔹 Valores no numéricos y formato incorrecto
	•	Separadores de miles con punto (.)
	•	Valores especiales del INE

Solución:
Conversión robusta a tipo numérico y tratamiento de valores faltantes en src/cleaning.py.

⸻

🔹 Formato temporal
	•	Periodo en formato YYYYMmm

Solución:
Transformación a columna date tipo datetime para análisis temporal.

⸻

🔹 Transformación estructural
	•	Dataset en formato largo

Solución:
Pivot para obtener variables en formato ancho por provincia y mes.

⸻

🔹 Anomalía año 2019

Se detectó que en 2019 la variable Parcelas_Ocupadas coincide exactamente con Parcelas en todos los meses, generando una ocupación artificial constante.

Tras validar el CSV original, se concluye que se trata de una inconsistencia en la fuente.

Decisión metodológica:
Excluir 2019 únicamente en los análisis de ocupación para evitar distorsión de tendencias.

⸻

5) Pipeline

El proyecto sigue un flujo reproducible:
raw → clean → features → viz → export

	1.	load_csv() → carga de datos
	2.	clean() → limpieza y transformación
	3.	build_features() → construcción de nuevas variables
	4.	Análisis y visualización en notebooks/eda.ipynb
	5.	Export opcional a data/processed/
6) Features construidas

Se generaron nuevas variables para enriquecer el análisis:
	•	empleados_por_establecimiento
	•	empleados_por_parcela
	•	parcelas_por_establecimiento
	•	ocupacion_real
(ajustada por número de días del mes)

Estas variables permiten evaluar eficiencia operativa y presión de demanda real.

⸻

7) Hallazgos principales

Insight 1 – Tendencia creciente post-2020

Tras excluir 2019, la ocupación media anual muestra una tendencia ascendente clara desde 2020, alcanzando máximos en 2025.

⸻

Insight 2 – Alta estacionalidad

El análisis mensual revela una concentración extrema en julio y agosto, con ocupaciones muy superiores al resto del año.
Existe margen estratégico para mejorar meses intermedios.

⸻

Insight 3 – Ausencia de saturación estructural

La comparación con provincias similares indica que A Coruña presenta niveles de ocupación inferiores a otras provincias cantábricas, pero con crecimiento sostenido.

No se observa una relación negativa clara entre número de establecimientos y ocupación, lo que sugiere que el mercado no está saturado estructuralmente.

⸻

Insight 4 – Crecimiento operativo alineado

El personal empleado crece en paralelo a la ocupación, lo que refleja ajuste operativo coherente con la demanda.

⸻

8) Estructura del proyecto
project/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

	•	src/ contiene funciones reutilizables.
	•	main.py ejecuta el pipeline completo.
	•	eda.ipynb orquesta el análisis y documenta la narrativa.

⸻

9) Cómo ejecutar
	1.	Instalar dependencias:
    pip install -r requirements.txt
    2.	Ejecutar pipeline completo:
    python main.py
    3.	Abrir el notebook:
    jupyter notebook notebooks/eda.ipynb


10) Conclusión general

El sector de campings en A Coruña muestra una tendencia de crecimiento estructural moderado con fuerte estacionalidad y sin evidencias claras de saturación.

Los resultados sugieren que existen oportunidades estratégicas de expansión bajo una planificación prudente y con foco en la optimización de la temporada media.
