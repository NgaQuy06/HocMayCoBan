import numpy as np 
import pandas as pd

df = pd.read_csv("D:/laptrinh/pythonn/hocmay/baitap/bai1/movies.csv")

ten = "Next Karate Kid"
phim = df[df["title"].str.contains(ten)]
tl_phim = set(phim.iloc[0]["genres"].split("|"))

ds_phim = df.head(10)

the_loai = []
for i in tl_phim:
    if i not in the_loai:
        the_loai.append(i)

bang = pd.DataFrame(columns=["Phim  ", "The loai  ", "Vector  ", "Dot  ", "Cosine  "])
for _, row in df.head(10).iterrows():
    ten_phim = row["title"]
    tl_phim = set(row["genres"].split("|"))

    the_loai_chung = []
    for i in tl_phim:
        if i not in the_loai_chung:
            the_loai_chung.append(i)
    for j in the_loai:
        if j not in the_loai_chung:
            the_loai_chung.append(j)

    vt_1 = []
    vt_2 = []
    for i in the_loai_chung:
        if i in the_loai:
            vt_1.append(1)
        else:
            vt_1.append(0)
        if i in tl_phim:
            vt_2.append(1)
        else:
            vt_2.append(0)

    dot = np.dot(vt_1, vt_2)
    l2_1 = np.sqrt(np.sum(np.array(vt_1)**2))
    l2_2 = np.sqrt(np.sum(np.array(vt_2)**2))

    if l2_1 != 0 or l2_2 != 0:
        cosine = dot / (l2_1 * l2_2)
    else:
        cosine = 0

    print("Phim:", ten_phim, "cosine =", round(cosine, 4))