# Vocal Imitation Set
v1.1 2018-08-18
   
## Overview
Imitating sounds with one's voice is a natural way of delivering an audio concept in human-to-human communication. If a machine could understand human's vocal imitation, users could be able to interact with machine in this natural way for various audio-related tasks. 

The VocalImitationSet is a collection of crowd-sourced vocal imitations of a large set of diverse sounds collected from Freesound (https://freesound.org/), which were curated based on Google's AudioSet ontology (https://research.google.com/audioset/). We expect that this dataset will help research communities obtain better understanding of human's vocal imitation and build a machine understand the imitations as humans do.

## Usage
For citations, please use this reference:

Bongjun Kim, Madhav Ghei, Bryan Pardo, and Zhiyao Duan, "Vocal Imitation Set: a dataset of vocally imitated sound events using the AudioSet ontology," *Proceedings of the Detection and Classification of Acoustic Scenes and Events 2018 Workshop (DCASE2018)*, Nov. 2018.

## Contact info
Interactive Audio Lab
* http://music.eecs.northwestern.edu

Bongjun Kim
* bongjun@u.northwestern.edu
* http://www.bongjunkim.com

Bryan Pardo
* pardo@northwestern.edu
* http://www.bryanpardo.com

## Acknowledgement
This dataset was supported by NSF Grant 1617497.

## Sound category structure
The sound classes are based on the Google AudioSet ontology. Some sound classes that are not imitable, such as *guitar amplifier*, or music genres were removed. We finally selected 302 different sound classes from the Audioset ontology and collected audio recordings of each classes from Freesound. A single high-quality recording was selected for each class, which means we selected 302 recordings to be imitated. The list of included sound classes is in `original_recordings_classes.txt`.

## Vocal imitation collection method
We collected crowd-sourced vocal imitations through Amazon Mechanical Turk using the VocalSketch data collection interface presented in [1].

Given a reference recording (a clean recording downloaded from Freesound), participants were asked to imitate the sound. The first imitations of each participant in a new session were saved as *training* recordings. participants were also allowed to rerecord their vocal imitations unlimited times before submitting the final one. These discarded imitations were saved as *draft* recordings. For more detailed procedures of imitation collection, please refer to [1].

We collected 6,115 vocal imitations (i.e. recordings that participants submitted as final versions NOT including *draft* and *training* recordings), 4,444 *draft* recordings, and 683 *training* recordings. The final 6,115 vocal imitations consist of roughly 20 imitations for each of 302 reference recordings.

## Quality assessment and rating
We conducted an internal quality assessment task where experts evaluated the quality of all the final collected imitations (6,115). Training and draft vocal recordings were not evaluated. The people who performed quality assessment were experts in audio processing: students and researchers from the Interactive Audio Lab (http://music.cs.northwestern.edu/) at Northwestern University and the Audio Information Research Lab (http://www2.ece.rochester.edu/projects/air/index.html) at the University of Rochester. There were 15 evaluators, who listened to 6,115 vocal imitations on a web interface designed for this particular listening task. 

A single quality assessment consisted of listening to a pair of recordings: one reference recording and one vocal imitation. The evaluator was asked if the imitation was a vocal imitation of the reference recording. If the answer was "yes," the evaluator was asked to assess the quality of the imitation on a scale from 0: It is a very poor imitation to 100: It is almost identical to the original sound. If the answer was "no" the, recording was removed from the set to be evaluated for quality and the evaluator was asked if this was a vocal imitation at all and this answer was saved.

Through this assessment session, we removed 514 vocal imitations that evaluators reported as not being a vocal imitation of the reference sound. This left us with 5,601 recordings that have quality ratings. The 5,601 vocal imitations are stored in the `included` directory. All the other recordings including the removed 514 imitations, 4,444 *draft* recordings, and 683 *training* recordings are stored in the `excluded` directory.

Due to the size of the dataset, each vocal imitation was evaluated by a single rator. However, we measured the consistency of each rator in two ways. First an average of 2 out of every 30 pairs evaluated by an individual were incorrect pairs. We paired vocal imitations with reference recordings that they were not an imitation of. This let us measure how well reviewers were able to detect incorrect pairs. Second, an average of 4 out of every 30 pairs presented to an evaluator were repeat pairs, previously presented. This lets us measure the consistency of evaluation scores for each reviewer.

The quality assessment data includes all the data from the quality assessment tasks, including repeated pairs and intentionally incorrect pairings.


## Description of directories and files
* **`vocal_imitations/included/`**: This directory contains all of the vocal imitations recordings that our human rators deemed a vocal imitation of the paired reference audio recordings.
* **`vocal_imitations/excluded/`**: This directory contains all of the vocal imitations recordings from participant's practice sessions. It also contains other vocal recordings. These include the vocal recordings that evaluators did not think were a vocal imitation of their reference audio. Training recordings and draft recordings are also included.
* **`original_recordings/reference/`**: This directory contains the audio files that participants were asked to listen to and imitate.
* **`original_recordings/non_reference/`**: This directory contains the audio files that were not imitated. These recordings can be used to test fine-grained search.
* **`original_recordings_license.csv`**: This file contains the credit information about all the original recordings we downloaded from Freesound.
* **`original_recordings_classes.txt`** (tab-delimited): This file contains class name and ontological labels of original recordings. The labels were taken from the AudioSet onotlogy.

* **`vocal_imitations.txt`** (tab-delimited): This file contains information about all the crowd-sourced vocal imitation recordings.

* **`vocal_imitations_rating.txt`** (tab-delimited): This file contains evaluation data of all the vocal imitations collected by our expert raters.
* **`participant_survey.csv`** This file contains the background survey data provided by participants providing vocal imitations.



## Description of the column of the text files
### Column descriptions for `original_recordings_classes.txt` (tab-delimited)
* **filename** - file name of the original recording
* **classname** - class name of the original recording
* **category_d1** - category name at the depth-1 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d2** - category name at the depth-2 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d3** - category name at the depth-3 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d4** - category name at the depth-4 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d5** - category name at the depth-5 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d6** - category name at the depth-6 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **is_reference** - Boolean of whether this original recording was used as a reference recording that was imitated.
* **multi_labeled** - Boolean of whether this original recording was used for multiple classes


### Column descriptions for `vocal_imitations.txt` (tab-delimited)
* **imitation_id** - unique Id of the vocal imitation
* **imitation_filename** - file name of the vocal imitation
* **category_id** - id of categories of reference recordings
* **category_d1** - category name at the depth-1 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d2** - category name at the depth-2 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d3** - category name at the depth-3 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d4** - category name at the depth-4 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d5** - category name at the depth-5 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **category_d6** - category name at the depth-6 in the hierarchy of the ontology (The name exactly matches with Google's AudioSet ontology)
* **reference_filename** - File names of the reference recordings of this vocal imitation
* **included** - Boolean of whether this vocal imitation met our inclusion criteria and was used in our analysis
* **draft** - Boolean of whether this vocal imitation was a 'draft' vocal imitation
* **training** - Boolean of whether this vocal imitation was for practice and discarded in analysis
* **participant\_id** - The id of the participant who performed the vocal imitation
* **satisfaction** - The participant's satisfaction with their vocal imitation on a 7- level likert scale (*Completely dissatisfied, Mostly dissatisfied, Somewhat dissatisfied, Neither satisfied or dissatisfied, Somewhat satisfied, Mostly satisfied, Completely satisfied*)
* **participants\_sound\_recording\_description** - The participant's description of the stimulus sound recording (if a stimulus\_type='sound recording')
* **participants\_sound\_recording\_description\_confidence** - The participant's confidence in their sound recording description on 5-level Likert scale (*Not at all confident, Not so confident, Neutral, Confident, Very confident*)


### Column descriptions for `vocal_imitations_assessment.txt` (tab-delimited)
* **id** - unique Id of the listening task
* **imitation_filename** - File name of the vocal imitation presented in the listening task
* **reference_recording** - File name of the reference recording presented with the vocal imitation
* **listener_id** - The id of the rator who listened to the vocal imitation and evaluated.
* **is_imitation** - Boolean of whether this vocal imitation is someone imitating any sound with vocalization
* **is_right_imitation** - Boolean of whether this vocal imitation was identified as someone imitating the assigned reference recording.
* **rating** - rating (between 0 and 100) of how good this imitation is. If the vocal recording was deemed to not be an imitation of the reference recording, its quality was not evaluated and this field is intentionally left blank.
* **wrong_pair** - Boolean of whether the pair of this vocal imitation and the reference recording is an incorrect pair (True: incorrect, False: correct)


### Column descriptions for `participant_survey.csv`
* **participant\_id** - The id of the participant
* **age** - The reported age of the participant
* **gender** - The reported gender of the participant
* **hearing\_problems** - The participant's response to the question: "Have you ever been diagnosed with a hearing problem?"
* **speech\_problems** - The participant's response to the question: "Have you ever been diagnosed with a speech problem?""
* **years\_actively\_using\_music\_tech** - The participant's response to the question: "Estimate (in years and months, e.g. 5 years 2 months) how long you have been actively using ﻿audio/music production technology (e.g. recording, mixing, synthesis technology)."
* **frequency\_using\_music\_tech** - The participant's response to the question: "How frequently do you use audio/music production technology (e.g. recording, mixing, synthesis technology)?" (*Never, Less than once or twice a year, Once or twice a year, Once or twice a month, Once or twice a week, More than once or twice a week*)
* **years\_actively\_making\_music** - The participant's response to the question: "Estimate (in years and months, e.g. 5 years 2 months) how long you have been actively creating, practicing, or performing music."
* **frequency\_making\_music** - The participant's response to the question: "How frequently do you create, practice, or perform music?" (*Never, Less than once or twice a year, Once or twice a year, Once or twice a month, Once or twice a week, More than once or twice a week*)
* **years\_actively\_singing** - The participant's response to the question: "Estimate (in years and months, e.g. 5 years 2 months) how long you have been actively singing."
* **frequency\_singing** - The participant's response to the question: "How frequently do you sing?" (*Never, Less than once or twice a year, Once or twice a year, Once or twice a month, Once or twice a week, More than once or twice a week*)


### Column descriptions for `original_recordings_license.csv`
* **filename** - The file name of original recordings
* **username** - User name who uploaded the recording to Freesound
* **user_url** URL to the user page on Freesound
* **file_url** URL to the recordings on Freesound
* **freesound_id** Freesound ID of the recording

### Column descriptions for `duplicates.csv`
* **Filename** - The file name of the duplicate recording
* **Category** - Which category the corresponding filename belongs to

## Additional Notes
Of the recordings collected for the dataset, 49 out of 2,985 were collected for multiple classes, if they were appropriate examples for both classes. For example, some cat growl recordings also contained cat hissing sounds; we split such recordings into clips containing just growls or just hisses and included the relevant sound clips in their respective categories. None of the repeated files were used as reference recordings for crowd-worker to imitate. Therefore, all 302 reference recordings are all unique in the dataset. 

A list of sounds shared across categories can be found in the duplicates.csv

## References
[1] Cartwright, M., Pardo, B. VocalSketch: Vocally Imitating Audio Concepts. In *Proceedings of ACM Conference on Human Factors in Computing Systems* (2015). http://dx.doi.org/10.1145/2702123.2702387
