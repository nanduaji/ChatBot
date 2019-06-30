import pandas as pd
import numpy as np

def controller():
    data = pd.read_tsv("Bot_Customization.tsv")
    print (data)
controller()