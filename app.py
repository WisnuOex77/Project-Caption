# app.py

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load data from CSV
data = pd.read_csv('C:/Users/ACER/OneDrive/Documents/project/data_cleaning.csv')

@app.route('/')
def index():
    # Render index.html with data for table display
    return render_template('C:/Users/ACER/OneDrive/Documents/project/templates/index.html', tables=[data.to_html(classes='data')])

@app.route('/plot/<column_name>')
def plot(column_name):
    # Create a simple plot (for demonstration purposes)
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data[column_name])
    plt.title(f'Plot of {column_name} over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(column_name)
    plt.grid(True)

    # Convert plot to base64 image and embed in HTML
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('C:/Users/ACER/OneDrive/Documents/project/templates/index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)