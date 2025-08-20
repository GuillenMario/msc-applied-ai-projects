# Chicago Taxi Trips 2024 Dataset

This project uses the [Chicago Taxi Trips 2024 dataset](https://data.cityofchicago.org/Transportation/Taxi-Trips-2024-/ajtu-isnz/about_data) published on the City of Chicago Open Data Portal.

## 📖 Description
The dataset contains records of taxi trips in Chicago, including:

- **Trip start and end timestamps**
- **Pickup and drop-off locations**
- **Trip distance and duration**
- **Fare details** (fare, tips, tolls, extras, total)
- **Payment type** (cash, credit card, etc.)
- **Taxi company information**

This dataset is useful for:
- Time series forecasting (e.g., demand prediction by hour/day)
- Customer behavior analysis (e.g., tipping patterns)
- Route and distance analysis
- Anomaly detection (e.g., unusually high fares)
- Model building for regression and classification tasks

## 📂 File Access
The dataset is **not included** in this repository due to size.  
You can download it directly from the City of Chicago Open Data Portal:

- **Download CSV:** [Taxi Trips 2024 (CSV)](https://data.cityofchicago.org/api/views/ajtu-isnz/rows.csv?accessType=DOWNLOAD)  
- **Download JSON:** [Taxi Trips 2024 (JSON)](https://data.cityofchicago.org/resource/ajtu-isnz.json)  
- **API Endpoint:**  
  ```
  https://data.cityofchicago.org/resource/ajtu-isnz.json
  ```

## ⚡ Quick Start (Python)
Example code to download a subset via the API:

```python
import pandas as pd

# Load 10,000 records from the API
url = "https://data.cityofchicago.org/resource/ajtu-isnz.json?$limit=10000"
df = pd.read_json(url)

print(df.shape)
print(df.head())
```

## ⚠️ Notes
- Data is updated regularly by the City of Chicago.
- Some columns may contain missing or inconsistent values (e.g., GPS coordinates, company names).
- Always check the [About Data page](https://data.cityofchicago.org/Transportation/Taxi-Trips-2024-/ajtu-isnz/about_data) for schema details.

---

📌 Place this file in your repo under `data/README.md` and keep only **small sample extracts** (e.g., first 100 rows) in `data/sample/` for quick testing.
