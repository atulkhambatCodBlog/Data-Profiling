#pip install ydata-profiling
from ydata_profiling import ProfileReport
import pandas as pd
df = pd.read_csv('path of your data file')
df.head(5)


profile = ProfileReport(df, title="Data Report")
profile.to_file("output.html")
