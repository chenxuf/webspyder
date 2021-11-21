from selenium import webdriver
import time
import pandas as pd

d_path = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(d_path)
driver.get("https://www.artemis.bm/dashboard/cat-bonds-ils-expected-loss-coupon/")
time.sleep(2)

final_df = pd.DataFrame()

#%%
js1 = "return Highcharts.charts[0].axes[0].categories"
x_axis = driver.execute_script(js1)
final_df["year"] = x_axis

y_data_list = []
col_name = []
for i in range(3):
    js_y = "return Highcharts.charts[0].series[{index}].yData".format(index=i)
    js_y_label = "return Highcharts.charts[0].series[{index}].name".format(index=i)

    try:
        y_label = driver.execute_script(js_y_label)
        y_data = driver.execute_script(js_y)
        final_df[y_label] = y_data
    except:
        break

#%%
import matplotlib.pyplot as plt
#%%
plt.plot(y_data)
#%%
plt.show()
