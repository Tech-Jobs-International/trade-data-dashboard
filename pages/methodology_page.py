import streamlit as st

from functions.data_fetch_function import df_data

# create tab for data set and visuals
methodology_tab, prcedure_tab, data_tab ,limitation_tab = st.tabs(['Methodology',"Procedure", 'Data','Limitations'])

with methodology_tab:
        # Header
        st.header("Could the US Produce Its Imports Internally?")

        # Introduction
        st.subheader("Introduction")
        st.markdown("""
        The essence of this exercise is to provide insight into the practicality of the United States of America (USA) producing its imported products and services internally.
        """)

        # Objectives
        st.subheader("Objectives")
        st.markdown("""
        1. Determine the number of productive hours required for the USA to produce its imports internally.
        2. Assess the percentage increase in hours worked if the imports are produced internally.
        3. Analyze the implications on the labor force in the USA.
        """)

        # Data Sources
        st.subheader("Data Sources")
        st.markdown("""
        The following data sources are utilized to achieve the study's objectives:

        1. [Trade Data as of 2022](https://comtradeplus.un.org/) - Both goods and services
        2. [GDP as of 2022 at constant 2015 prices](https://databank.worldbank.org/source/world-development-indicators#)
        3. [GDP per Capita as of 2022 at constant 2015 prices](https://databank.worldbank.org/source/world-development-indicators#)
        4. [Population Data](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
        5. [Labor Force Data as of 2022](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
        6. [Export Value Index as of 2022 (2015 = 100)](https://data.worldbank.org/indicator/TX.VAL.MRCH.XD.WD)
        """)

        # Data Description
        st.subheader("Data Description")
        st.markdown("""
        - **GDP Data:** Records the monetary and market value of all finished goods and services produced within a country at a particular point in time.

        - **GDP per Capita Data:** Reflects the amount generated per household within an economy, calculated by dividing GDP by the total population. It is used to train datasets to determine or predict GDP per hour for countries where direct measurement is not feasible.

        - **Workforce Population:** Helps determine the GDP per hour, assuming the labor force (rather than the total population) contributes to GDP.

        - **Average Work Hours:** Necessary to calculate GDP per hour, requiring knowledge of the average yearly work hours across countries.

        - **Trade Data:** Utilizes the United Nations Comtrade Database and OECD database to examine import data for the United States.

        - **Products Data:** Sourced from the United Nations Comtrade Database, one of the world's most comprehensive sources of international trade data, providing detailed information on trade flows between countries.

        - **Services Data:** Records the value of services exchanged between residents and non-residents of an economy, including services provided through foreign affiliates established abroad. [link](https://www.oecd.org/en/data/indicators/trade-in-services)

        - **Export Value Index (2015 = 100):** A measure of changes in the value of a country's exports over time, with 2015 as the base year (index = 100). It captures both price changes and changes in the volume of exported goods, providing a comprehensive measure of export trends. [link](https://databank.worldbank.org/source/world-development-indicators)
        """)


with prcedure_tab:

        # Page title
        st.header("Procedure Overview")

        # Section introduction
        st.write("""
        This section outlines the steps taken to analyze the feasibility of the United States producing its imported goods and services domestically.
        """)
        # Step 1: Extract Data
        st.subheader("1. Extract Data from Sources")
        st.markdown("""
        - **Gather data from various sources** to get relevant information about GDP, population, work hours, and imports.
        """)

        # Step 2: Determine GDP Per Hour
        st.subheader("2. Determine GDP Per Hour")
        st.markdown("""
        - Extract the GDP dataset at constant 2015 prices to ensure values are not adjusted for inflation (Real GDP).  
        - Extract the working population data, ensuring the population is multiplied by 1,000 to report its true value.  
        - Retrieve average weekly work hours. Convert weekly work hours to yearly by assuming 52 weeks in a year.  
        - Merge the working population and average weekly hours datasets to calculate the total hours worked within the country for the year.  
        - Once total hours are calculated, merge this dataset with the GDP dataset. **Divide GDP by total hours worked to get GDP per hour.**
        """)

        # Step 3: Determine Total Value of Imports
        st.subheader("3. Determine Total Value of Imports into the US")
        st.markdown("""
        - Extract the Comtrade dataset to identify export values to the US along with the exporting nation details.  
        - Extract the services dataset to complete the import data.  
        - Extract the export index to value imports at constant 2015 prices, adjusting for inflation.  
        - Merge Comtrade and export index datasets to account for inflationary adjustments.
        """)

        # Step 4: Calculate Total Hours for Domestic Production
        st.subheader("4. Calculate Total Hours Required to produce the Goods and Services")
        st.markdown("""
        - Merge the datasets resulting from steps 2 and 3.  
        - Divide the constant USD export value by GDP per hour to calculate the total hours needed for production.
        """)

        st.info("This procedure helps in assessing the feasibility of domestic production for imported goods and services.")

with data_tab: 
        st.subheader("Results")
        st.markdown("This dataset acts as the primary dataframe created after retrieving and merging data from various sources.")
        st.dataframe(df_data)

with limitation_tab:
        # Title of the page
        st.header("Data Assumptions and Limitations")

        # Assumptions section
        st.subheader("Assumptions")
        
        st.markdown("""
        1. We always use the latest available year for both GDP and working population, respectively.
        2. The working population includes everyone over 15 years of age.
        3. There are 52 working weeks per year.
        4. GDP is measured in constant 2015 USD.
        5. Countries without an inflation adjustment index are assigned an index of 100.
        6. Services GDP per hour is calculated as the average GDP/hour of all countries excluding the USA.
        """)

        # Limitations section
        st.subheader("Limitations")
        
        st.markdown("""
        **GDP per Hour Limitations:**

        1. Incomplete data for GDP and working population for many countries as of 2022.
        2. Lack of total working population data.
        3. Absence of data for the yearly average hours worked in various countries.

        **Comtrade Data Limitations:**

        5. Not all countries have an export index to adjust for inflation.
        6. Unable to find a breakdown of services data.
        """)

        # Additional explanation or context, if necessary
        st.subheader("Additional Context")
        st.write("""
        The assumptions and limitations listed above are essential for understanding the context and potential constraints of the data analysis. These considerations highlight the challenges in acquiring comprehensive and uniform datasets across different countries and underline the importance of cautious interpretation of the results.
        """)
        
        