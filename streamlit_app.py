import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites') 
streamlit.text('ð¥£ Omega 3 and Blueberry Oatmeal')
streamlit.text('ð¥ Kale, Spinach & Rocket Smoothie')
streamlit.text('ð¥ Hard-Boiled Free-Range egg')
streamlit.text('ð¥ Avocado Toast')


streamlit.header('ðBuild Your Own Fruit Smoothie ð')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's puta picklist here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)
