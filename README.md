OriMorph
========

OriMorph is a morphological analyzer and lemmatizer for Odia (Oriya). It only analyzes nouns right now.

Usage:

```python
>>> import orimorph
>>> m = orimorph.OriMorph('ori.fst')
>>> m.analyses(['ଓଡ଼ିଶାର', 'ଅନୁଭୂତିଗୁଡିକୁ', 'ଆକାଶରେ'])
[['ଓଡ଼ିଶା', 'SG', 'GEN'], ['ଅନୁଭୂତିଗୁଡି', 'SG', 'ACC'], ['ଆକାଶ', 'SG', 'INSTR']]
>>> m.lemmas(['ଓଡ଼ିଶାର', 'ଅନୁଭୂତିଗୁଡିକୁ', 'ଆକାଶରେ'])
['ଓଡ଼ିଶା', 'ଅନୁଭୂତିଗୁଡି', 'ଆକାଶ']
```
