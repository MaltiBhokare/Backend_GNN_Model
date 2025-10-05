# from flask import Flask, jsonify
# from flask_cors import CORS     # 👈 allows React to call this API
# import pandas as pd

# app = Flask(__name__)
# CORS(app)                      # 👈 enable Cross-Origin Resource Sharing

# @app.route("/recommend/<category>")
# def recommend(category):
#     category = category.lower()
#     try:
#         df = pd.read_csv(f"top5_{category}.csv")
#         return jsonify(df.to_dict(orient="records"))
#     except FileNotFoundError:
#         return jsonify({"error": f"No data found for category '{category}'"}), 404

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend (React/Vercel) to access this API


# ✅ Root route (prevents 502 Bad Gateway on Render)
@app.route("/")
def home():
    return jsonify({"message": "Backend is running successfully!"})


# ✅ Main recommendation route
@app.route("/recommend/<category>")
def recommend(category):
    category = category.lower()
    try:
        file_path = f"top5_{category}.csv"

        if not os.path.exists(file_path):
            return jsonify({"error": f"No data found for category '{category}'"}), 404

        df = pd.read_csv(file_path)
        return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Use Render’s assigned port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses dynamic PORT
    app.run(host="0.0.0.0", port=port)
