import pandas as pd

meta = pd.read_csv("C:/Users/PC/Documents/Studia/DS semestr 0/Język Python/Projekt/GutMicrobiome-PyCharm/metadata.tsv", sep='\t')
paths = pd.read_csv("C:/Users/PC/Documents/Studia/DS semestr 0/Język Python/Projekt/GutMicrobiome-PyCharm/pathways_relative_abundance.tsv", sep='\t')
tax = pd.read_csv("C:/Users/PC/Documents/Studia/DS semestr 0/Język Python/Projekt/GutMicrobiome-PyCharm/taxonomy_relative_abundance.tsv", sep='\t')

canc = meta[meta['study_condition'].isin(['CRC', 'adenoma'])]
diab = meta[meta['study_condition'].isin(['T2D', 'IGT'])]
digest = meta[meta['study_condition'].isin(['IBD', 'cirrhosis', 'STH'])]
cardio = meta[meta['study_condition'].isin(['ACVD', 'CAD', 'hypertension', 'pre-hypertension', 'HF'])]

print(len(canc['study_condition']))
print(len(diab['study_condition']))
print(len(digest['study_condition']))
print(len(cardio['study_condition']))