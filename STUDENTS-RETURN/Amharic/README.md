# Amharic-ASR-Dataset
speech recognition for Amharic language
--------------------------------------------------------------------
Text data is adobted from [Contemporary Amharic Corpus (CACO)](http://www.findke.ovgu.de/findke/en/Research/Data+Sets/Contemporary+Amharic+Corpus+%28CACO%29-p-1142.html)

## Length
--------------------------------------

- 2.3 hours 

## unsplitted 
------------------------------------------------------------
unsplitted row data can be found in `unsplitted` branch of this repository.

## Contents
--------------------------------------------------------------------

```
Amharic-ASR-Dataset
|
├── data
│   └── records
│       ├── train
│       │   └── *.wav
│       ├── val
│       │   └── *.wav
│       ├── test
│           └── *.wav
│       
└── README.md
└── chars.txt
└── charset.json
└── linker.txt
└── raw_text_file.txt
```
## Data collection App
-------------------------------
Dataset was recorded using [LIG-Aikuma app](https://lig-aikuma.imag.fr/download/)




## Dataset 
----------------------------------------
```
@inproceedings{gezmu-etal-2018-contemporary,
    title = "Contemporary {A}mharic Corpus: Automatically Morpho-Syntactically Tagged {A}mharic Corpus",
    author = {Gezmu, Andargachew Mekonnen  and
      Seyoum, Binyam Ephrem  and
      Gasser, Michael  and
      N{\"u}rnberger, Andreas},
    booktitle = "Proceedings of the First Workshop on Linguistic Resources for Natural Language Processing",
    month = aug,
    year = "2018",
    address = "Santa Fe, New Mexico, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W18-3809",
    pages = "65--70",
    abstract = "We introduced the contemporary Amharic corpus, which is automatically tagged for morpho-syntactic information. Texts are collected from 25,199 documents from different domains and about 24 million orthographic words are tokenized. Since it is partly a web corpus, we made some automatic spelling error correction. We have also modified the existing morphological analyzer, HornMorpho, to use it for the automatic tagging.",
}
```
