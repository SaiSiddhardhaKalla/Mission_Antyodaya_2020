# !pip install streamlit
# !pip install folium
# !pip install geopandas
import streamlit as st
import pandas as pd
import numpy as np
import folium
import streamlit.components.v1 as components
import json
import geopandas as gpd
from branca.element import Template, MacroElement
from template import template

# !pip install ipykernel>=5.1.2
# !pip install pydeck

from branca.element import Template, MacroElement

#!streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py

from branca.element import Template, MacroElement
from template import template
import branca.colormap as cm
st.header("Antyodaya Dashboard Rajasthan")

# Base Map##put centre of centriod of rajesthan
m = folium.Map(location=[26.5844, 73.8496],zoom_start=6, tiles='cartodbpositron')

# Reading state Data
df = pd.read_csv("Raj_dt_ma.csv")
geoData = open('Raj_dt_ma.geojson', 'r')

# Reading ac data
geo_ac_data = gpd.read_file("Raj_AC_ma.geojson")
districts = list(geo_ac_data['District'].unique())
districts.insert(0, "All")
ac_df = pd.read_csv('raj_ac_ma.csv')

# Reading gc data
geo_gc_data = gpd.read_file("Raj_GP_ma.geojson")


# Creating dropdowns
category = st.sidebar.selectbox("Select a Category", list(df.columns[2:]))
district = st.sidebar.selectbox("Select a District", districts)

# Function to calculate opacity
def calculate_opacity(df, category, i):
    colors = ['#F1EEF6', '#D4B9DA', '#C994C7',
                        '#DF65B0', '#E7298A', '#CE1256', '#91003F']
    temp = list(df[category])
    try:
        op = (temp[i] - min(temp)) / (max(temp) - min(temp))
        if op <= 1 and op > 0.75:
            return colors[1]
        elif op <= 0.75 and op > 0.5:
            return colors[2]
        elif op <= 0.5 and op > 0.25:
            return  colors[4]
        else:
            return colors[6]
        # if op <= 1 and op > 0.833:
        #     return colors[6]
        # elif op <= 0.833 and op > 0.666:
        #     return colors[5]
        # elif op <= 0.666 and op > 0.499:
        #     return  colors[4]
        # elif op <= 0.499 and op > 0.332:
        #     return colors[3]
        # elif op <= 0.332 and op > 0.165:
        #     return  colors[2]
        # else:
        #     return colors[1]

    except:
        return colors[1]

if district == "All":

    choropleth = folium.Choropleth(
        geo_data=json.load(geoData),
        name='choropleth',
        data=df,
        columns=['District Name', str(category)],
        key_on='feature.properties.District Name',
        fill_color='YlGnBu',
        fill_opacity=0.9,
        line_opacity=1,
        legend_name=str(category)
    ).add_to(m)

    # folium.LayerControl().add_to(m)
    choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(
                fields=['District Name', str(category)],
                aliases=['District:', str(category)+":"],
                style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))

    m.save('map2.html')
    HtmlFile = open("map2.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    HtmlFile.close()

    # Showing map in streamlit
    components.html(source_code,width=700, height=500)

else:
    new_geo_gc_data = geo_gc_data[geo_gc_data['District'] == str(district)]

    assembly_constituencies = list(new_geo_gc_data['Assembly Constituency'].unique())
    assembly_constituencies.insert(0, "None")

    assembly_const = st.sidebar.selectbox("Select an Assembly Constituency", assembly_constituencies)

    if assembly_const == "None":
        
        dist_data = geo_ac_data[geo_ac_data['District'] == district]
        dist_data_geojson = dist_data.to_json()
        ac_df = ac_df[ac_df['District'] == district]

        dist_data.reset_index(drop=True, inplace=True)
        print(dist_data['geometry'])
        #input()
        
        #print(dist_data['geometry'])
#for polynomial
        try:
            lon = dist_data['geometry'][0][0].exterior.coords.xy[0][0]
            lat = dist_data['geometry'][0][0].exterior.coords.xy[1][0]
#for Multipolynomial
        except:
            lon = dist_data['geometry'][0].exterior.coords.xy[0][0]
            lat = dist_data['geometry'][0].exterior.coords.xy[1][0]
        # Change location to dynamic
        m = folium.Map(location=[lat, lon], zoom_start=8, tiles='cartodbpositron')
        choropleth = folium.Choropleth(
            geo_data=dist_data_geojson,
            name='GMAP',
            data=ac_df,
            columns=['Assembly Constituency', str(category)],
            key_on='feature.properties.Assembly Constituency',
            fill_color='PuRd_r',
            fill_opacity=0.7,
            line_opacity=1,
            legend_name=str(category)).add_to(m)

        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(
                fields=['Assembly Constituency', str(category)],
                aliases=['Assembly Constituency:', str(category)+":"],
                style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))

        m.save('ac_map.html')
        HtmlFile = open("ac_map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        HtmlFile.close()


        # Showing map in streamlit
        components.html(source_code, width=700, height=500)


    elif assembly_const != "None":
        new_gc_data = new_geo_gc_data[new_geo_gc_data['Assembly Constituency'] == str(assembly_const)]
        new_gc_data.reset_index(drop=True, inplace=True)
        # Change location to dynamic
        
        try:
            m = folium.Map(location=[list((new_gc_data.iloc[0]['geometry']).coords)[0][1], list((new_gc_data.iloc[0]['geometry']).coords)[0][0]],zoom_start=10, tiles='cartodbpositron')
        except:
            m = folium.Map(location=[list((new_gc_data.iloc[0]['geometry']).coords)[0][0], list((new_gc_data.iloc[0]['geometry']).coords)[0][0]],zoom_start=10, tiles='cartodbpositron')
        
        
    
    
    
        dist_data = geo_ac_data[(geo_ac_data['District'] == district) & (geo_ac_data['Assembly Constituency'] == assembly_const)]
        dist_data_geojson = dist_data.to_json()
        style = {
            'fillColor': None,
                'fillOpacity': 0,
                'color':'black'
                }
        folium.GeoJson(dist_data_geojson, style_function=lambda x:style).add_to(m)

        for i in range(0, len(new_gc_data)):
            if new_gc_data.iloc[i]['geometry'] != None:
                try:
                    temp = [list((new_gc_data.iloc[i]['geometry']).coords)[0][1], list((new_gc_data.iloc[i]['geometry']).coords)[0][0]]
                except:
                    temp = [list((new_gc_data.iloc[i]['geometry']).coords)[1][0], list((new_gc_data.iloc[i]['geometry']).coords)[0][0]]
            
            folium.vector_layers.Circle(
                location=tuple(temp),
                tooltip= f"<b>Gram Panchayat:</b> {str(new_gc_data.iloc[i]['gp_name'])} <br><b>{str(category)}:</b> {str(new_gc_data.iloc[i][str(category)])}",
                # tooltip=["Gram Panchayat: " + str(new_gc_data.iloc[i]['gp_name']),
                #          str(category) + ": " + str(new_gc_data.iloc[i][str(category)])],
                # popup=[new_gc_data.iloc[i]['gp_name'], new_gc_data.iloc[i][str(category)]],
                radius=float(new_gc_data.iloc[i][str(category)]) * 300+100,
                color=calculate_opacity(new_gc_data, str(category), i),
                fill=True,
                weight=0.6,
                fill_opacity=0.6,
                fill_color=calculate_opacity(new_gc_data, str(category), i)
            ).add_to(m)
            # folium.vector_layers.path_options(weight=0)
        macro = MacroElement()
        #macro._template = Template(template)
        _template = Template(u'')

        m.get_root().add_child(macro)

        m.save('gc_map.html')

        HtmlFile = open("gc_map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        HtmlFile.close()

        # Showing map in streamlit
        components.html(source_code, width=700, height=500)

