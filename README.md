# index-pdf
A short python script to quickly index a HUGE pdf file based on regex

#### Requires PyPDF2 and tkinter
>pip3 install PyPDF2

>apt install tk

#### Usuage: 
1. Put search.py in folder containing all PDF's and run it
1. Enter search query
1. Select pdf files, you can select multiple pdf's
1. Click on search 
1. *The initial building of index will be slow*, after the document is indexed, search is fast

### Note: The program might not respond for a few minutes, do not *PANIC*
  * If documents have been modified, you will need to delete <document_name>.pdf.index files
  * Change the regex pattern according to your needs, By default search is for sentence_case
  (First Letter Is Capital)
  * I do not intend on maintaining this project as it is just a quick script I wrote to solve a common annoyance.
  However, feel free to provide feedback/feature requests
