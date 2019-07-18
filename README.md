OriMorph
========

OriMorph is a morphological analyzer and lemmatizer for Odia (Oriya). It only analyzes nouns right now.

OriMorph requires that the Foma binaries (specifically, `flookup`) be in your path. It expects the following files to be in the current directory:

* `fsinter.py` -- Python interface to `flookup`
* `orimorph.py` -- high-level interface to `ori.fst`
* `ori.fst` -- a compiled Foma FST. This can actually be anywhere but you need to supply the path.

Usage:

```python
>>> import orimorph
>>> m = orimorph.OriMorph('ori.fst')
>>> m.analyses(['ଓଡ଼ିଶାର', 'ଅନୁଭୂତିଗୁଡିକୁ', 'ଆକାଶରେ'])
[['ଓଡ଼ିଶା', 'SG', 'GEN'], ['ଅନୁଭୂତିଗୁଡି', 'SG', 'ACC'], ['ଆକାଶ', 'SG', 'INSTR']]
>>> m.lemmas(['ଓଡ଼ିଶାର', 'ଅନୁଭୂତିଗୁଡିକୁ', 'ଆକାଶରେ'])
['ଓଡ଼ିଶା', 'ଅନୁଭୂତିଗୁଡି', 'ଆକାଶ']
```
