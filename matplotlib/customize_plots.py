import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1 = np.array([20,25,30,15])
y2 = np.array([14,18,37,25])
y3 = np.array([10,20,30,14])
line_style = dict( marker="." # v , o , * , ........
            , markersize=20 # or ms =
            , markerfacecolor="cyan" # or mfc =
            , markeredgecolor="#002872" # or mec =
            , linestyle="solid" # dotted , dashdot , dashed , None 
            , linewidth = 3
            )

plt.plot(x,y1,**line_style ,color = "#0029df" #, marker="."    # use dict better to prevent duplicates
            #, markersize=20                       
            #, markeredgecolor="#002872" 
            #, linestyle="solid" 
            #, linewidth = 3
            )
plt.plot(x,y2,**line_style ,color = "#00df1e")
plt.plot(x,y3,**line_style ,color = "#B90000")
plt.show()  