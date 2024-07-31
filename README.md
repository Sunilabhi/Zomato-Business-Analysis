# Zomato Business Analysis Dashboard

This Streamlit app provides an interactive dashboard for analyzing Zomato's business data. The dashboard includes various charts and filters to help you explore the data and gain insights into different aspects of the business.

## Features

1. **Country-Specific Data Selection**
   - Choose a country to view data specific to that country.

2. **Charts and Analysis**
   - **Average Cost for Two in INR**: Bar chart showing the average cost for two in Indian Rupees.
   - **Rating Count**: Histogram showing the count of different rating texts.
   - **Costly Cuisines in India**: List of the top 5 costliest cuisines in India.
   - **Famous Cuisine in a City**: Displays the most famous cuisine in the selected city.
   - **Costlier Cuisine in a City**: Displays the costliest cuisine in the selected city.
   - **Online Delivery vs. Dine-in**: Pie chart comparing the counts of online delivery vs. dine-in.
   - **Comparison Between Cities in India**: Bar chart comparing the average cost for two in INR across different cities in India.
   - **Total Spending on Online Delivery by City**: Bar chart showing total spending on online delivery by city.
   - **Total Spending on Dine-in by City**: Bar chart showing total spending on dine-in by city.
   - **High Living Cost vs. Low Living Cost Areas in India**: Lists of high and low living cost areas in India.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- Plotly
- Pandas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/zomato-business-analysis-dashboard.git
    ```

2. Navigate to the project directory:
    ```bash
    cd zomato-business-analysis-dashboard
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Make sure your dataset `df_final` is saved as a CSV file in the project directory.

### Running the App

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the dashboard.

### Dataset

The dataset should be a CSV file with the following columns:

- `Restaurant ID`
- `Restaurant Name`
- `Country Code`
- `City`
- `Address`
- `Locality`
- `Locality Verbose`
- `Longitude`
- `Latitude`
- `Cuisines`
- `Average Cost for two`
- `Currency`
- `Has Table booking`
- `Has Online delivery`
- `Is delivering now`
- `Switch to order menu`
- `Price range`
- `Aggregate rating`
- `Rating color`
- `Rating text`
- `Votes`
- `Country`
- `Exchange Rate`

### Deployment

To deploy the app on Streamlit Cloud:

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repository.
4. Select the repository and branch.
5. Deploy the app.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Zomato for providing the data.
- Streamlit for the easy-to-use web app framework.
- Plotly for the interactive charts.

