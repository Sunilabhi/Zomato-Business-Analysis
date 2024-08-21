import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df_final = pd.read_csv('zomato_final_data.csv')  # Update with your dataset path

# Add a column with prices in Indian Rupees
df_final['Average Cost for two in INR'] = df_final['Average Cost for two'] * df_final['Exchange Rate']

df_final = df_final[df_final['Average Cost for two in INR'] > 0]

# Streamlit app
st.title('Zomato Business Analysis Dashboard')

# Dropdown for country-specific data
country_options = df_final['Country'].unique()
default_country = 'India' if 'India' in country_options else country_options[0]
country = st.selectbox('Choose a Country', country_options, index=list(country_options).index(default_country))
filtered_df = df_final[df_final['Country'] == country]


# Chart 1: Average Cost for Two in INR
fig1 = px.bar(filtered_df, x='Restaurant Name', y='Average Cost for two in INR', color='City', title='Average Cost for Two in INR')
st.plotly_chart(fig1)

# Chart 2: Rating Count
fig2 = px.histogram(filtered_df, x='Rating text', title='Rating Count')
st.plotly_chart(fig2)

# Additional functionality

# Find which cuisines are costly in India
if country == 'India':
    st.subheader('Costly Cuisines in India')
    costly_cuisines = df_final[df_final['Country'] == 'India'].sort_values(by='Average Cost for two in INR', ascending=False).head(5)
    st.write(costly_cuisines[['Restaurant Name', 'City', 'Cuisines', 'Average Cost for two in INR']])

# Filter based on the city
city = st.selectbox('Choose a City', filtered_df['City'].unique())
city_filtered_df = filtered_df[filtered_df['City'] == city]

# Famous cuisine in the city
st.subheader(f'Famous Cuisines in {city}')
famous_cuisine = city_filtered_df['Cuisines'].mode()[0]
st.write(f'The most famous cuisine in {city} is {famous_cuisine}.')

# Costlier cuisine in the city
st.subheader(f'Costlier Cuisine in {city}')
costlier_cuisine = city_filtered_df.sort_values(by='Average Cost for two in INR', ascending=False).head(1)
st.write(costlier_cuisine[['Restaurant Name', 'Cuisines', 'Average Cost for two in INR']])

# Pie chart online delivery vs dine-in
st.subheader(f'Online Delivery vs Dine-in in {city}')
delivery_pie_chart = city_filtered_df['Has Online delivery'].value_counts().reset_index()
delivery_pie_chart.columns = ['Delivery Option', 'Count']
fig3 = px.pie(delivery_pie_chart, names='Delivery Option', values='Count', title='Online Delivery vs Dine-in')
st.plotly_chart(fig3)

# Comparison between the cities in India
if country == 'India':
    st.subheader('Comparison Between Cities in India')
    city_comparison = df_final[df_final['Country'] == 'India'].groupby('City')['Converted Cost (INR)'].mean().reset_index()
    fig4 = px.bar(city_comparison, x='City', y='Converted Cost (INR)', title='Converted Cost (INR)')
    st.plotly_chart(fig4)

    # Part of India that spends more on online delivery
    st.subheader('Part of India Spending More on Online Delivery')
    online_delivery = df_final[(df_final['Country'] == 'India') & (df_final['Has Online delivery'] == 'Yes')].groupby('City')['Converted Cost (INR)'].sum().reset_index()
    fig5 = px.bar(online_delivery, x='City', y='Converted Cost (INR)', title='Total Spending on Online Delivery by City')
    st.plotly_chart(fig5)

    # Part of India that spends more on dine-in
    st.subheader('Part of India Spending More on Dine-in')
    dine_in = df_final[(df_final['Country'] == 'India') & (df_final['Has Online delivery'] == 'No')].groupby('City')['Converted Cost (INR)'].sum().reset_index()
    fig6 = px.bar(dine_in, x='City', y='Converted Cost (INR)', title='Total Spending on Dine-in by City')
    st.plotly_chart(fig6)

    # Compare high living cost vs low living cost areas in India
    st.subheader('High Living Cost vs Low Living Cost Areas in India')
    low_cost_areas = df_final[df_final['Country'] == 'India'].sort_values(by='Converted Cost (INR)').head(5)
    high_cost_areas = df_final[df_final['Country'] == 'India'].sort_values(by='Converted Cost (INR)', ascending=False).head(5)
    
    st.write('High Living Cost Areas:')
    st.write(high_cost_areas[['City', 'Converted Cost (INR)']])
    
    st.write('Low Living Cost Areas:')
    st.write(low_cost_areas[['City', 'Converted Cost (INR)']])



