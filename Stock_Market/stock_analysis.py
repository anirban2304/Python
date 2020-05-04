from pandas_datareader import data
import datetime
from bokeh.plotting import figure, output_file, show

start = datetime.datetime(2020,3,1)
end = datetime.datetime(2020,5,1)

df = data.DataReader(name = "AAPL", data_source= "yahoo", start = start, end = end)

def inc_dec(c, o):
    if c > o:
        value = "increase"
    elif c < o:
        value = "decrease"
    else:
        value = "equal"
    return value

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]

print(df)

p = figure(x_axis_type = 'datetime', width = 1000, height = 300)
#p.title = Title("Financial Analysis")

hours_12 = 12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, line_color = "black")

p.rect(df.index[df.Status == "increase"], (df.Open[df.Status == "increase"] + df.Close[df.Status == "increase"])/2, 
hours_12, abs(df.Open[df.Status == "increase"]-df.Close[df.Status == "increase"]), fill_color = "blue", line_color = "black")

p.rect(df.index[df.Status == "decrease"], (df.Open[df.Status == "decrease"] + df.Close[df.Status == "decrease"])/2, 
hours_12, abs(df.Open[df.Status == "decrease"]-df.Close[df.Status == "decrease"]), fill_color = "red", line_color = "black")

output_file(r"Stock_Market\finance.html")
show(p)