source:
https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v=vs.85)

cat books.xml | xq
cat books.xml | xq '.catalog.book[].author'

source:
http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/
http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/www/repository.html#pir

date;cat SwissProt.xml | xq > SwissProt.json;date
~40s for 115MB file

date;cat psd7003.xml | xq > psd7003.json;date
~230s for 717MB file

jq -c '.ProteinDatabase.ProteinEntry[]' psd7003.json

jq -c '.ProteinDatabase.ProteinEntry[]' psd7003.json > ProteinEntry.json

clear;date;cat psd7003.xml | xq | jq -c '.ProteinDatabase.ProteinEntry[]' > ProteinEntry.json;date

wc -l ProteinEntry.json

source:
https://www.ashbyhq.com/blog/engineering/jq-and-yq
