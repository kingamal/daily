from fasthtml.common import FastHTML, serve, Html, Head, Body, Title, Main, Pre, Button, Script

app = FastHTML()

python_code = """
import folium
import pandas as pd

def load_data():
    return pd.read_csv("europe.csv")

data = load_data()

m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=4)

for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Country"],
        tooltip=row["Country"],
    ).add_to(m)

m.save("map.html")
"""

@app.get("/")
def home():
    page = Html(
        Head(
            Title("Python Code Viewer"),
        ),
        Body(
            Main(
                Title("Code Viewer Example"),
                Pre(python_code),
                Button("Copy Code", id="copy-button", type="button"),
                Script("""
                document.getElementById('copy-button').onclick = function() {
                    navigator.clipboard.writeText(`""" + python_code + """`);
                    alert("Code copied to clipboard!");
                };
                """)
            )
        )
    )
    return page

serve()
