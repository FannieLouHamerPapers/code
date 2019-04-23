import pandas as pd

#read in data
entities = pd.read_csv('https://raw.githubusercontent.com/FannieLouHamerPapers/NamedEntities/master/flh_ner_all.csv')
metadata = pd.read_csv('flhmetadata.csv')

#cut '.txt' from the doc names
entities.doc = entities.doc.str[:16]

#join dataframes; select only some 
merged = pd.merge(entities, metadata[['id','title_full','description','imprint_year']], how='inner', left_on='doc', right_on='id')

#doc and id are duplicates; remove id
flh_ner_all = merged.drop('id', axis=1)

#print to csv
flh_ner_all.to_csv('flh_ner_all.csv', index=False)