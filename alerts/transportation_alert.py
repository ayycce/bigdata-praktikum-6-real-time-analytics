def generate_alert(df):
    alerts = []
    # Jika jumlah trip lebih dari 100, berikan alert volume tinggi
    if len(df) > 100:
        alerts.append("⚠️ High traffic volume")
        
    # Jika ada tarif yang melebihi 90000, berikan alert tarif tinggi
    if df["fare"].max() > 90000:
        alerts.append("🚨 High fare detected")
        
    return alerts