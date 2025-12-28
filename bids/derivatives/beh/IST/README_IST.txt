Preprocessed Information Search Task (IST) data

(Preprocessing was done by Jesse Niebaum; no preprocessing code available in the project directory)

Includes: 
- A trial-level dataframe (IST_Full.csv), which contains all primary variables for all individual trials + effort condition. 
- A condition x subject level dataframe (IST_Condition.csv), which is long-wise with 3 values for each subject for each effort condition (low, medium, high).
- A subject-level dataframe (IST_Participant.csv), which contains the effort condition-level means for all primary variables for each participant. The effort level is denoted at the end of each variable (e.g., "boxesFlipped_low", "boxesFlipped_medium", etc.).

For all files, pNew is the updated calculation of the p(correct) variable used in past work (e.g. http://dx.doi.org/10.1037/dev0001397). 
Because testing was done in person and individually, there are far fewer no-sample trials compared with the prior paper testing in groups (only 4 no-sample trials here)--so, this variable isn't meaningful. Similarly, discrimination errors, where a participant does not select the majority color (via mistake or intentionally ignoring task instructions) were quite low in this dataset compared with all prior work. Participants generally did well. 