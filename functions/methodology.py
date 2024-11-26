import pandas as pd

introduction='''
    ### **Introduction**
    The essence of this exercise aims to provide insight on the practically of the United State of America (USA) being able to produce it's imports products and services internal thereby improving the gross domestic product (GDP) of the USA"

    ### **Objectives**
    
    1.   How many productive hours will it take the USA to produce its imports internally.
    2.   What is the percentage increase in the hours worked if the imports are produced internally.
    3.   What is the implication of this on the labour force in the USA

    ### **Prerequisite**

    To follow along, you should have a basic understanding of Python, data analysis libraries like Pandas, numpy etc and knowledge of Scikit learn for Marching Learning. 

    ### **Data Source**
    Here is a list of data used to achieve the objective of this study

    1.   [Trade Data](https://comtradeplus.un.org/)
    2.   [GDP at constant 2015](https://databank.worldbank.org/source/world-development-indicators#)
    3.   [GDP per Capita at constant 2015](https://databank.worldbank.org/source/world-development-indicators#)
    4.   [Population](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
    5.   [Labor Force Data](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
    6.   [Export value index (2015 = 100)](https://data.worldbank.org/indicator/TX.VAL.MRCH.XD.WD)

    ### **Data Description**

    **GDP data:** This data records the monetary and market value of all finished good and services produce within a country at a particular point in time.

    **GDP per capita Data:** This data is determine by the amount generate per household within an economy. This is gotten by dividing the GDP by the total population within an economy. It will be used to train the dataset to determine or predict the GDP per hour for countries the GDPper hour can not be determined for.

    **Workforce Population:** This data source is used to determining the GDP per hour as it is assumed that the contributor to the GDP is labor force and not the total population.

    **Average Work Hours:** This is the second part needed to determine the GDP per hours has we need to know what the average yearly work hours is in all countries.

    **Trade Data:** This exercise leverages the United Nations Comtrade Database and OECD database to explore import data for the United States.

    **Products data:** The United Nations Comtrade Database is one of the world’s largest and most comprehensive sources of international trade data, maintained by the United Nations Statistics Division (UNSD). It provides detailed information on trade flows between countries, covering thousands of products and services traded worldwide.

    **Services data:** Trade in services records the value of services exchanged between residents and non-residents of an economy, including services provided through foreign affiliates established abroad. - [link](https://www.oecd.org/en/data/indicators/trade-in-services).

    **Export value index (2015 = 100):** The Export Value Index (EVI) is an economic indicator that measures changes in the value of a country’s exports over time, with 2015 set as the base year (index = 100). EVI captures both price changes (e.g., inflation or price changes of commodities) and changes in the volume of exported goods, providing a broad measure of export trends.
    [link](https://databank.worldbank.org/source/world-development-indicators)
'''

objective = '''
    ### **Objectives**

    1.   How many productive hours will it take the USA to produce its imports internally.
    2.   What is the percentage increase in the hours worked if the imports are produced internally.
    3.   What is the implication of this on the labour force in the USA
'''
data_sources='''
    Here is a list of data used to achieve the objective of this study

    1.   [Trade Data](https://comtradeplus.un.org/) - Both goods and services
    2.   [GDP at constant 2015](https://databank.worldbank.org/source/world-development-indicators#)
    3.   [GDP per Capita at constant 2015](https://databank.worldbank.org/source/world-development-indicators#)
    4.   [Population](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
    5.   [Labor Force Data](https://rshiny.ilo.org/dataexplorer22/?lang=en&id=HOW_UEMP_SEX_NB_A)
    6.   [Export value index (2015 = 100)](https://data.worldbank.org/indicator/TX.VAL.MRCH.XD.WD)

'''

data_description= '''
    **GDP data:** This data records the monetary and market value of all finished good and services produce within a country at a particular point in time.

    **GDP per capita Data:** This data is determine by the amount generate per household within an economy. This is gotten by dividing the GDP by the total population within an economy. It will be used to train the dataset to determine or predict the GDP per hour for countries the GDPper hour can not be determined for.

    **Workforce Population:** This data source is used to determining the GDP per hour as it is assumed that the contributor to the GDP is labor force and not the total population.

    **Average Work Hours:** This is the second part needed to determine the GDP per hours has we need to know what the average yearly work hours is in all countries.

    **Trade Data:** This exercise leverages the United Nations Comtrade Database and OECD database to explore import data for the United States.

    **Products data:** The United Nations Comtrade Database is one of the world’s largest and most comprehensive sources of international trade data, maintained by the United Nations Statistics Division (UNSD). It provides detailed information on trade flows between countries, covering thousands of products and services traded worldwide.

    **Services data:** Trade in services records the value of services exchanged between residents and non-residents of an economy, including services provided through foreign affiliates established abroad. - [link](https://www.oecd.org/en/data/indicators/trade-in-services).

    **Export value index (2015 = 100):** The Export Value Index (EVI) is an economic indicator that measures changes in the value of a country’s exports over time, with 2015 set as the base year (index = 100). EVI captures both price changes (e.g., inflation or price changes of commodities) and changes in the volume of exported goods, providing a broad measure of export trends.
    [link](https://databank.worldbank.org/source/world-development-indicators)

'''
steps = '''

    ### **Procedure:**

    1. Extract the data from the data sources
    2. Determine the GDP per hour:

        a. Extract the GDP at constant 2015 dataset. The essence of this is to get the GDP values without adjusting for inflations(aka Real GDP).

        b. Extract the working population data and make sure to multiply the population by 1000 in order the ensure the data report its true value.

        c. Extract the average weekly work hours. To convert the weekly work hours to yearly work hours, it is assumed that there are 52 weeks in a year.

        d. Marge the working population and average weekly hours datasets in our to get the total hours worked within a country for the year.

        e. Once the total hours is determined, merged the new datasets with the GDP dataset. You will divide the GDP by the total hours worked in order to get the GDP per hour.
    3. Determine the Total value of Import into the US:

        a. Extract the Comtrade dataset to determine the value of export to the US with the corresponding exporting nation.

        b. Extract the services data set.

        c. Extract the export index in order to value the import at constant 2015. This means we need it to adjust for inflation.

        d. Merge the Comtrade and export index datasets in order to make the adjustments for inflation.

    4. Determine the total hours needed to produce the exports into the US. This is done by merging the resulting dataset from 2 and 3 above and then dividing the constant_USD export value by the GDP per hour in order to get the total hours needed to produce internally in the US.
    '''


# new_labor_force function
def new_labor_force_country_filt(df, country_iso3 = None):
    new_df = df.copy()

    # search by country code
    new_df = new_df[new_df['country_iso3'] == country_iso3]
    if new_df.empty:
        print(f'country_iso3 {country_iso3} does not exist')
    else:
        top_exported_product = new_df[new_df['country_iso3'] == country_iso3].sort_values(by='constant_usd', ascending=False).head(1)['cmdDesc'].iloc[0]
        top_exported_value = round(new_df[new_df['country_iso3'] == country_iso3].sort_values(by='constant_usd', ascending=False).head(1)['constant_usd'].iloc[0],2)
        product_df = round(new_df[new_df['country_iso3'] == country_iso3]['total_hours_needed_to_produce_in_USA'].sum(),2)
        # partnerDesc = new_df[new_df['country_iso3'] == country_iso3]['partnerDesc'].iloc[0]

        dic = {
            'Total annual hours to produce': "{:,}".format(product_df),
            'Top exported product' : top_exported_product,
            'Top exported product in $' : "{:,}".format(top_exported_value)
        }

        return dic

def new_labor_force_country_filt_USA(df, country_iso3 = None):
    new_df = df.copy()

    # search by country code
    new_df = new_df[new_df['country_iso3'] == country_iso3]
    if new_df.empty:
        print(f'country_iso3 {country_iso3} does not exist')
    else:
        total_hours_worked_US = 523670559867
        product_df = round(new_df[new_df['country_iso3'] == country_iso3]['total_hours_needed_to_produce_in_USA'].sum(),2)
        # partnerDesc = "United States of America"
        hours_increase_percentage = (product_df  / total_hours_worked_US)
        # new_labor_force = round((263973465 * (1 + (hours_increase_percentage / 100))-263973465),2)

        dic = {
            'Annual Hours worked in the USA ':"{:,}".format(total_hours_worked_US),
            'USA Labor Force':"{:,}".format(263973465),
            'Percentage share of Working hours': "{:.2%}".format(hours_increase_percentage)
            # 'Labour Force growth': "{:,}".format(new_labor_force)
        }

        return dic

def new_labor_force_product_filt(df, cmdCode = None):
    new_df = df.copy()

    # search by country code
    new_df = new_df[new_df['cmdCode'] == cmdCode]
    if new_df.empty:
        print(f'product code {cmdCode} does not exist')
    else:
        total_hours_worked_US = 523670559867
        product_df = round(new_df[new_df['cmdCode'] == cmdCode]['total_hours_needed_to_produce_in_USA'].sum(),2)
        hours_increase_percentage = (product_df  / total_hours_worked_US)
        new_labor_force = round(263973465 * (1 + (hours_increase_percentage / 100))-263973465,2)
        top_exporting_country = new_df[new_df['cmdCode'] == cmdCode].sort_values(by='constant_usd', ascending=False).head(1)['partnerDesc'].iloc[0]
        top_exporting_value = round(new_df[new_df['cmdCode'] == cmdCode].sort_values(by='constant_usd', ascending=False).head(1)['constant_usd'].iloc[0],2)

        dic = {
            'Total annual hours to produce': "{:,}".format(product_df),
            'Top exporting country' : top_exporting_country,
            'Top exporting value in $': "{:,}".format(top_exporting_value),
            'USA Labor Force': "{:,}".format(263973465),
            'Percentage share of Working hours': "{:.2%}".format(hours_increase_percentage)
        }

    return dic

# Limitation assumption
assumption = '''
    1. We always the latest available year for both GDP and working population respectively

    2. Working population is everyone > 15 years

    3. 52 working weeks

    4. USD constant for 2015

    5. Countries without inflation adjustment index are set to an index of 100
    
    6. Services GDP per Hour is the average of GDP/hour of all countries excluding the USA

'''

limitation = '''
    GDP per hours:

        1. Unable to find GDP and working population data as 2022 for a lot of countries.

        2. Could not find total working population data

        3. Could not find data for yearly average hours works for countries

    Comtrade Data:

        5. Not all countries have the export index to adjust for inflation

        6. could not find breakdown of services

'''
