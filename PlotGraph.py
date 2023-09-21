from streamlit.logger import get_logger
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


LOGGER = get_logger(__name__)


def run():
  df = pd.read_csv('toy_dataset.csv')
  city_counts = df['City'].value_counts()

  city_counts.plot(kind='bar', color='skyblue')
  plt.xlabel('City')
  plt.ylabel('Count')
  plt.title('Number of Individuals in Each City')
  plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
  plt.tight_layout()
  st. pyplot(plt.show())

if __name__ == "__main__":
    run()
