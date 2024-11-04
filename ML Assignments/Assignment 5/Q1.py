import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sb.load_dataset('tips')
x = tips['total_bill'].values
y = tips['tip'].values