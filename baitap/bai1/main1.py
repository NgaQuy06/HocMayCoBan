import numpy as np 
import pandas as pd

df = pd.read_csv("D:/laptrinh/pythonn/hocmay/baitap/bai1/movies.csv")

def tat_ca_the_lai():
    tc = []
    for i in df["genres"]:
        for j in i.split("|"):
            if j not in tc:
                tc.append(j)
    return tc

ten_1 = "Next Karate Kid"
phim_1 = df[df["title"].str.contains(ten_1)]
tl_phim_1 = set(phim_1.iloc[0]["genres"].split("|"))

ten_2 = "Executive Decision"
phim_2 = df[df["title"].str.contains(ten_2)]
tl_phim_2 = set(phim_2.iloc[0]["genres"].split("|"))

the_loai_chung = []
for i in tl_phim_1:
    if i not in the_loai_chung:
        the_loai_chung.append(i)
for j in tl_phim_2:
    if j not in the_loai_chung:
        the_loai_chung.append(j)

print(the_loai_chung)

vt_1 = []
vt_2 = []
for i in the_loai_chung:
    if i in tl_phim_1:
        vt_1.append(1)
    else:
        vt_1.append(0)
    if i in tl_phim_2:
        vt_2.append(1)
    else:
        vt_2.append(0)

print(vt_1)
print(vt_2)

dot = np.dot(vt_1, vt_2)
l2_1 = np.sqrt(np.sum(np.array(vt_1)**2))
l2_2 = np.sqrt(np.sum(np.array(vt_2)**2))

if l2_1 != 0 or l2_2 != 0:
    cosine = dot / (l2_1 * l2_2)
else:
    cosine = 0

print ("dot =", dot)
print ("l2 phim 1 =", l2_1)
print ("l2 phim 2 =", l2_2)
print ("cosine =", cosine)