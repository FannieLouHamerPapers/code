import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite

fullset=pd.read_csv('https://raw.githubusercontent.com/FannieLouHamerPapers/NamedEntities/master/flh_ner_all.csv', low_memory=False)

Delta_Opportunities_Corporation_DOC_Series=fullset.loc[fullset.doc_title_full.str.contains('Delta Opportunities Corporation (D', regex=False)]
Freedom_Farms_Corporation_FFC_Series=fullset.loc[fullset.doc_title_full.str.contains('Freedom Farms Corporation (FFC) Series', regex=False)]
Other_Organization_Series_I=fullset.loc[fullset.doc_title_full.str.contains('Other Organization Series I:|Other Organization Series I,|Other Organization Series I ', regex=True)]
Other_Organization_Series_II=fullset.loc[fullset.doc_title_full.str.contains('Other Organization Series II:', regex=False)]
Other_Organizational_Series_I=fullset.loc[fullset.doc_title_full.str.contains('Other Organizational Series I:', regex=False)]
Other_Organizational_Series_II=fullset.loc[fullset.doc_title_full.str.contains('Other Organizational Series II:', regex=False)]
Other_Material=fullset.loc[fullset.doc_title_full.str.contains('Other Material:', regex=False)]
Mississippians_United_To_Elect_Negro_Candidates_Series=fullset.loc[fullset.doc_title_full.str.contains('ippians United To Elect Negro Candidates Series', regex=False)]
Delta_Ministry_Series=fullset.loc[fullset.doc_title_full.str.contains('Delta Ministry Series:', regex=False)]
Personal_Series=fullset.loc[fullset.doc_title_full.str.contains('Personal:|Personal Series Correspondence|Personal Series:', regex=True)]
Mississippi_Freedom_Democratic_Party_MFDP_Series=fullset.loc[fullset.doc_title_full.str.contains('Mississippi Freedom Democratic Party (M', regex=False)]

Delta_Opportunities_Corporation_DOC_Series.name='DeltaOpportunitiesCorporationDOCSeries'
Freedom_Farms_Corporation_FFC_Series.name='FreedomFarmsCorporationFFCSeries'
Mississippians_United_To_Elect_Negro_Candidates_Series.name='MississippiansUnitedToElectNegroCandidatesSeries'
Delta_Ministry_Series.name='DeltaMinistrySeries'
Personal_Series.name='PersonalSeries'
Mississippi_Freedom_Democratic_Party_MFDP_Series.name='MississippiFreedomDemocraticPartyMFDPSeries'

series_name = [Delta_Opportunities_Corporation_DOC_Series, Freedom_Farms_Corporation_FFC_Series, Mississippians_United_To_Elect_Negro_Candidates_Series, Delta_Ministry_Series, Personal_Series, Mississippi_Freedom_Democratic_Party_MFDP_Series]
all_freq=[5,10]

for series in series_name:
    nodes_full=series['entity'].drop_duplicates()

    #create empty multigraph - multigraph is an undirected graph with parallel edges
    G = nx.MultiGraph()

    #import edge dataframe and create network
    G = nx.from_pandas_edgelist(series, source='doc', target='entity', edge_attr=True)

    #project the graph onto entities, removing documents from the graph
    full_graph = bipartite.weighted_projected_graph(G, nodes_full)

    #convert the projected edge list
    full_proj = nx.to_pandas_edgelist(full_graph)

    #pull nodes list from the projected edge lists
    nodes=full_proj['source'].append(full_proj['target']).drop_duplicates()
    nodes_proj = pd.DataFrame({'id': nodes, 'label': nodes})

    #print node & edge list for the full projected graph
    full_proj.to_csv('flh_' + series.name +'_ner_all_proj_edges.csv', index=False)
    nodes_proj.to_csv('flh_' + series.name +'_ner_all_proj_nodes.csv', index=False)

    for x in all_freq:
        #filter data
        filtered_edges=full_proj.loc[full_proj.weight >= x]
        nodes=filtered_edges['source'].append(filtered_edges['target']).drop_duplicates()
        filtered_nodes = pd.DataFrame({'id': nodes, 'label': nodes})
        #print csvs
        filtered_edges.to_csv('flh_' + series.name +'_ner_all_proj_edges_freq'+ str(x) + '.csv', index=False)
        filtered_nodes.to_csv('flh_' + series.name +'_ner_all_proj_nodes_freq'+ str(x) + '.csv', index=False)

