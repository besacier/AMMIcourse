# AMMI Course - laurent besacier - week 2

# 1. Lecture on self supervised representation learning for pre-training speech systems (3h)

By Laurent Besacier, Univ. Grenoble Alpes

This course is scheduled on **Wed 24th, lecture review and Q&A at 4pm (GMT+2)** during the 2020 African Master’s in Machine Intelligence (https://aimsammi.org). 

Such approaches are very important to reduce dependence on labeled data for building speech systems. This is particularly relevant for languages with poorly standardized orthography or even for unwritten languages. 

See course here: https://github.com/besacier/AMMIcourse/edit/master/SelfSupervisedLearningFromSpeech

Here is the link to the **videos** of my course:

Part1: https://youtu.be/Ka-eNfGFEeE

Part2: https://youtu.be/cfEyLLcvoQ8 

Part3: https://youtu.be/pWAJORFey-E 

Part4: https://youtu.be/m_mkUUs99X4

Part5: https://youtu.be/v5qhyJT-Ga4 

Part6: https://youtu.be/naL5noNnKfc 

Part7: https://youtu.be/hE9ODFChrvI 

Q&A part1: https://youtu.be/1a3h4-LnUms

Q&A part2: https://youtu.be/sLeSYaNxKUM

Q&A part3: https://youtu.be/mbXgfOaA6GI

Q&A part4: https://youtu.be/3MJtyHfzNv0

Q&A part5: https://youtu.be/LqYCswM8rec


# 2. Beyond sentences: lecture / reading group on on-line speech transcription and translation and on dialog level speech transcription and translation (3h)

By Laurent Besacier, Univ. Grenoble Alpes

This course is scheduled on **on Fri 26th, in a reading group mode at 11am (GMT+2)** during the 2020 African Master’s in Machine Intelligence (https://aimsammi.org). 

Slides available here: https://github.com/besacier/AMMIcourse/blob/master/readinggroup.pdf

# 3. Data collection project (6h)

By Laurent Besacier, Univ. Grenoble Alpes. 

**Todo before starting the project (3h)**

The steps below must be done on your own **Mon 22d between 4pm and 7pm (GMT+2)**

(1) read the lig-aikuma publication on : https://hal.archives-ouvertes.fr/hal-02264418/document 

(2) install lig-aikuma on your tablet or smartphone: https://lig-aikuma.imag.fr/download/

(3) watch the video tutorial (French with English CCs !) online on: https://lig-aikuma.imag.fr/tutorial/
 
(4) read the documentation available on: https://lig-aikuma.imag.fr/wp-content/uploads/2017/06/LIG-Aikuma_tutorial.pdf

(5) do the 90mn tutorial on : https://lig-aikuma.imag.fr/lig-aikuma-in-90mn/ 


**Project itself (3h)**

I will be online on **Tue 23d, Wed 24th, at 5pm (GMT+2)** for Q&A on this project. 

You must at least achieve part 1 of this project (part 2 is optional)

**part 1 (collecting 2h of read speech in your own language)**

You should first gather a text (in your own language) to be read. To record 2h of speech, this text should be at least 20,000 words long and be tokenized in sentences.

You should record sentences **in your native language** using Lig-AIkuma. For this, use the **ellicitation (from text) mode** and record utterances. Before that, you should **carefully fill the speaker metadata information**.

The final recordings should be split in two parts **dev and test** of 1h each.

**part 2 (collecting raw speech)**

You should ellicitate additional raw speech **in your native language** using Lig-AIkuma. For this, use the **ellicitation (from text or image) mode**. One possibility is to describe images of your choice or record from the following English utterances (https://github.com/besacier/AMMIcourse/blob/master/BTEC-en-fr.ammi.zip) or simply find pre-existing spoken corpora. Before that, you should **carefully fill the speaker metadata information**.


**dataset return for assessment**

You should share all your recordings and transcripts on a github page and add a README file that reports your data collection details: number of recordings made, problems encoutered during recording, comments, etc.
In case you would agree to share your recorded dataset for future research, please add a LICENSE file to your github repo. Examples of license types are MIT (see https://github.com/getalp/mass-dataset/blob/master/LICENSE for an example) or "Creative Commons" (see https://github.com/getalp/Flaubert/blob/master/LICENSE for an example).
Once data and README are ready, please send an email to **laurent.besacier@imag.fr** and i will clone your repo into https://github.com/besacier/AMMIcourse/tree/master/STUDENTS-RETURN 
You will be evaluated based on the quality and quantity of data recorded (and metadata provided).

 
**IMPORTANT**

If you encounter problems with lig-aikuma (no android phone/tablet to install it, problem with installation), you can use another recording software of your choice. For instance https://www.phon.ucl.ac.uk/resource/prorec/ (windows only) or  https://www.bas.uni-muenchen.de/Bas/software/speechrecorder/ (multiplatform) allow you to upload text prompts and then record them.

# 3. Project outcome

A post-course informal collaboration lead to the following paper published to the **AfricaNLP2021 workshop** !

@article{DBLP:journals/corr/abs-2103-08993,
  author    = {Jama Hussein Mohamud and
               Lloyd Acquaye Thompson and
               Aissatou Ndoye and
               Laurent Besacier},
  title     = {Fast Development of {ASR} in African Languages using Self Supervised
               Speech Representation Learning},
  journal   = {CoRR},
  volume    = {abs/2103.08993},
  year      = {2021},
  url       = {https://arxiv.org/abs/2103.08993},
  eprinttype = {arXiv},
  eprint    = {2103.08993},
  timestamp = {Tue, 23 Mar 2021 16:29:47 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2103-08993.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}



