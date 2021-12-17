#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np


st.title("MoneyBBall")
st.write("Predict the market value of NBA Players from their current-season stats")



st.sidebar.markdown("Select from the menus below:")
dataset_name = st.sidebar.selectbox("Select Dataset",
                                   ("Iris Dataset", "Breast Cancer Dataset", "Wine Dataset"))
classifier_name = st.sidebar.selectbox("Select Classifier",
                                      ("KNN", "SVM", "Random Forest"))
