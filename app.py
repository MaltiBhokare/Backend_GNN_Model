from flask import Flask, jsonify
from flask_cors import CORS     # 👈 allows React to call this API
import pandas as pd

app = Flask(__name__)
CORS(app)                      # 👈 enable Cross-Origin Resource Sharing

@app.route("/recommend/<category>")
def recommend(category):
    category = category.lower()
    try:
        df = pd.read_csv(f"top5_{category}.csv")
        return jsonify(df.to_dict(orient="records"))
    except FileNotFoundError:
        return jsonify({"error": f"No data found for category '{category}'"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

