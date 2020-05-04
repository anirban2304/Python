from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv(r"Graphs\bachelors.csv")
press = pandas.read_excel(r"Graphs\verlegenhuken.xlsx")

Year = df["Year"]
Engg_Percentage = df["Engineering"]

temperature = press["Temperature"]
pressure = press["Pressure"]

output_file(r"Graphs\per_plot.html")

f = figure()

f.line(Year, Engg_Percentage)
show(f)

output_file(r"Graphs\press_plot.html")

f2 = figure()

f2.circle(temperature/10, pressure/10, size = 0.5)
show(f2)