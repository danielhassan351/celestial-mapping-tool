import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('stars.csv')  # Ensure the CSV file contains columns: RA, Dec, Mag, Type, Name

# Filter for brighter stars
df = df[df['Mag'] <= 5.0]

# Plot
fig = px.scatter(
    df, x='RA', y='Dec',
    size=6 - df['Mag'],
    color='Type',
    hover_name='Name',
    hover_data={'RA': True, 'Dec': True, 'Mag': True},
    title='Interactive Celestial Map'
)

fig.update_layout(
    xaxis_title='Right Ascension (°)',
    yaxis_title='Declination (°)',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    legend_title='Star Type'
)

# Export
fig.write_html('interactive_celestial_map.html')
print("Map saved as interactive_celestial_map.html")