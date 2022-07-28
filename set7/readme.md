WEEK 8: We chilling

panda.read_csv refer to this docs when using pandas

Python strftime cheatsheet

Groupby - split data into different groups by categories

---

sad.groupby("Species").value column name.mean()
Split up and aggregated it together

- max
- min
- mean

---

sad.species.value_counts()

---

Fancy distribution graph
for name, df in sad.groupby("Species")
print(name, df.shape)

    SPECIES (#rows, # coloumns)

---

for name, df in sad.groupby("Species")
df.Species.hist()

    (prints histogram)

---
