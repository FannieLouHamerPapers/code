# Code used to process data

## NamedEntities
1. Text files were processed using [batchner](https://github.com/brandontlocke/batchner/blob/master/README.md).
2. Used [OpenRefine](http://openrefine.org/) to merge together entities that were synonyms (e.g. N.Y. -> New York, MLK-> Martin Luther King)
3. Used [link to code forthcoming]() script to merge together and re-count rows with the same doc, entity, and entityType.
4. Used [flh-metadatamerge.py](https://github.com/FannieLouHamerPapers/code/blob/master/flh-metadatamerge.py) script to join metadata from *Archives Unbound* (`doc_title_full, doc_description, doc_imprint_year`) with the document and entity data.

# Additional code
* [link forthcoming]() divides the NER data by series and creates networks for each
