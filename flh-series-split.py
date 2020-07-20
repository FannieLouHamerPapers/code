#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re

fullset = pd.read_csv('https://media.githubusercontent.com/media/FannieLouHamerPapers/NamedEntities/master/flh_ner_all.csv')

# FREQUENCY
freq5=fullset.loc[fullset['count'] >= 5]
freq5.to_csv('flh_ner_all_freq5.csv', index=False)

freq10=fullset.loc[fullset['count'] >= 10]
freq10.to_csv('flh_ner_all_freq10.csv', index=False)

# ENTITY
person=fullset.loc[fullset.entityType.str.match(pat = 'person')] 
person.to_csv('flh_ner_person.csv', index=False)

organization=fullset.loc[fullset.entityType.str.match(pat = 'organization')] 
organization.to_csv('flh_ner_organization.csv', index=False)

location=fullset.loc[fullset.entityType.str.match(pat = 'location')] 
location.to_csv('flh_ner_location.csv', index=False)

# SERIES
Delta_Opportunities_Corporation_DOC_Series=fullset.loc[fullset.doc_title_full.str.contains('Delta Opportunities Corporation (D', regex=False)]
Delta_Opportunities_Corporation_DOC_Series.to_csv('flh-DOC_ner.csv', index=False)

Freedom_Farms_Corporation_FFC_Series=fullset.loc[fullset.doc_title_full.str.contains('Freedom Farms Corporation (FFC) Series', regex=False)]
Freedom_Farms_Corporation_FFC_Series.to_csv('flh-FFC_ner.csv', index=False)

Other_Organization_Series_I=fullset.loc[fullset.doc_title_full.str.contains('Other Organization Series I:|Other Organization Series I,|Other Organization Series I ', regex=True)]
Other_Organization_Series_I.to_csv('flh-Other-Organization-Series-I_ner.csv', index=False)

Other_Organization_Series_II=fullset.loc[fullset.doc_title_full.str.contains('Other Organization Series II:', regex=False)]
Other_Organization_Series_II.to_csv('flh-Other-Organization-Series-II_ner.csv', index=False)

Other_Organizational_Series_I=fullset.loc[fullset.doc_title_full.str.contains('Other Organizational Series I:', regex=False)]
Other_Organizational_Series_I.to_csv('flh-Other-Organizational-Series-I_ner.csv', index=False)

Other_Organizational_Series_II=fullset.loc[fullset.doc_title_full.str.contains('Other Organizational Series II:', regex=False)]
Other_Organizational_Series_II.to_csv('flh-Other-Organizational-Series-II_ner.csv', index=False)

Other_Material=fullset.loc[fullset.doc_title_full.str.contains('Other Material:', regex=False)]
Other_Material.to_csv('flh-Other-Material_ner.csv', index=False)

Mississippians_United_To_Elect_Negro_Candidates_Series=fullset.loc[fullset.doc_title_full.str.contains('ippians United To Elect Negro Candidates Series', regex=False)]
Mississippians_United_To_Elect_Negro_Candidates_Series.to_csv('flh-Mississippians-United-To-Elect-Negro-Candidates-Series_ner.csv', index=False)

Delta_Ministry_Series=fullset.loc[fullset.doc_title_full.str.contains('Delta Ministry Series:', regex=False)]
Delta_Ministry_Series.to_csv('flh-Delta-Ministry-Series_ner.csv', index=False)

Personal_Series=fullset.loc[fullset.doc_title_full.str.contains('Personal:|Personal Series Correspondence|Personal Series:', regex=True)]
Personal_Series.to_csv('flh-Personal-Series_ner.csv', index=False)

Mississippi_Freedom_Democratic_Party_MFDP_Series=fullset.loc[fullset.doc_title_full.str.contains('Mississippi Freedom Democratic Party (M', regex=False)]
Mississippi_Freedom_Democratic_Party_MFDP_Series.to_csv('flh-NFDP_ner.csv', index=False)