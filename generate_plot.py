import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # EuroSAT data
# eurosat_dicts = {
#     "Descriptions": [20,30,40,50,60],
#     "Accuracy": [73.06, 72.74, 73.8, 74.63, 72.13]
# }
# df_eurosat = pd.DataFrame(eurosat_dicts)
# plt.plot(df_eurosat["Descriptions"], df_eurosat["Accuracy"], marker="d", label="EuroSAT")

# # UCM data
# ucm_dicts = {
#     "Descriptions": [20,30,40,50,60],
#     "Accuracy": [87.38,86.19,85.95,87.38,85.95]
# }

# df_ucm = pd.DataFrame(ucm_dicts)
# plt.plot(df_ucm["Descriptions"], df_ucm["Accuracy"], marker="d", label="UCM")

# # Resisc data
# resis_dicts = {
#     "Descriptions": [20,30,40,50,60],
#     "Accuracy": [75.4,75.57,75.59,76.2,76.24]
# }

# df_res = pd.DataFrame(resis_dicts)
# plt.plot(df_res["Descriptions"], df_res["Accuracy"], marker="d", label="Resisc-45")

# #Patternnet
# pn_dicts = {
#     "Descriptions": [20,30,40,50,60],
#     "Accuracy": [81.73,82.14,81.76,83.59,82.68]
# }

# df_pat = pd.DataFrame(pn_dicts)
# plt.plot(df_pat["Descriptions"], df_pat["Accuracy"], marker="d", label="PatternNet")

# plt.legend()
# plt.xlabel("Descriptions Per Class")
# plt.ylabel("Accuracy %")
# plt.ylim(60, 90)  # Setting a common y-axis limit for both plots
# # plt.show()
# plt.savefig("accuracy_nos_desc.png")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# EuroSAT data
eurosat_dicts = {
    "Descriptions": [20,30,40,50,60],
    "Accuracy": [73.06, 72.74, 73.8, 74.63, 72.13]
}
df_eurosat = pd.DataFrame(eurosat_dicts)
plt.plot(df_eurosat["Descriptions"], df_eurosat["Accuracy"], marker="d", label="EuroSAT")
plt.legend()
plt.xlabel("Descriptions Per Class")
plt.ylabel("Accuracy %")
plt.ylim(70, 75)
plt.savefig("eurosat_accuracy.png")
plt.close()

# UCM data
ucm_dicts = {
    "Descriptions": [20,30,40,50,60],
    "Accuracy": [87.38,86.19,85.95,87.38,85.95]
}

df_ucm = pd.DataFrame(ucm_dicts)
plt.plot(df_ucm["Descriptions"], df_ucm["Accuracy"], marker="d", label="UCM", color='green')
plt.legend()
plt.xlabel("Descriptions Per Class")
plt.ylabel("Accuracy %")
plt.ylim(85, 90)
plt.savefig("ucm_accuracy.png")
plt.close()

# Resisc data
resis_dicts = {
    "Descriptions": [20,30,40,50,60],
    "Accuracy": [75.4,75.57,75.59,76.2,76.24]
}

df_res = pd.DataFrame(resis_dicts)
plt.plot(df_res["Descriptions"], df_res["Accuracy"], marker="d", label="Resisc-45", color='red')
plt.legend()
plt.xlabel("Descriptions Per Class")
plt.ylabel("Accuracy %")
plt.ylim(73, 78)
plt.savefig("resisc_accuracy.png")
plt.close()

# PatternNet data
pn_dicts = {
    "Descriptions": [20,30,40,50,60],
    "Accuracy": [81.73,82.14,81.76,83.59,82.68]
}

df_pat = pd.DataFrame(pn_dicts)
plt.plot(df_pat["Descriptions"], df_pat["Accuracy"], marker="d", label="PatternNet", color='orange')
plt.legend()
plt.xlabel("Descriptions Per Class")
plt.ylabel("Accuracy %")
plt.ylim(80, 85)
plt.savefig("patternnet_accuracy.png")
plt.close()
