This game currently only works with otree version 2.2.3 due to the old django design.
please install with
pip3 install -U "otree==2.2.3"

Demo-version af spillet "Bad Influence"

Der er kun een stor gruppe i et stort netværk, defineret i Subsession.creating_session.
Netværket er designet vha "preferential attachement" metoden, dvs. på en sådan måde at
der er få spillere som har mange venner og mange spillere som har få venner. Jeg tænker
at det minimale antal af venner for en spiller skal være 2 eller 3 (Constants.num_initial_friends=3). Hver spiller kan kun se sit eget ego-netværk og chatte med sine venner individuelt. Spilleren kan så vælge rød eller blå, og man kan se graden af konsensus i i hele gruppen i en progress-bar.


Opsætning på circleCI og rancher:
Efter standard git add ., git commit -m, git pull og git push, skriv:

./set_tag [tag of docker image] [tag description]

f.eks.:
./set_tag bad_influence_version_X "blah blah beskrivelse"

Det sætter et tag og tjekker om der er uncommitted changes (hvis ja, så pushes automatisk).
Så går circleCI i gang med at lave et build (tjek hvor lang tid det varer på https://circleci.com/bb/cibs).
Vent ca. 5 minutter indtil circleCI har bygget buildet. Dernæst skriv:

./up [tag of docker image] [subdomain, e.g test if running on test.cibs.mef.sc.ku.dk]

F.eks.:
./up bad_influence_version_X test

(HVIS DU IKKE HAR SAT RANCHER OP ENDNU:)
Gå til https://cibs-adm.mef.sc.ku.dk/
Login: robin/rancher+p
Nederste højre hjørne: download rancher CLI
Save, extract, føj rancher.exe til PATH
Naviger til den otree-folder du vil sætte op
Skriv rancher config
Enter url (min er   https://cibs-adm.mef.sc.ku.dk/v2-beta )
Enter access key ved at tryppe på “Ad account API key” på https://cibs-adm.mef.sc.ku.dk/env/1a141/api/keys
Skriv beskrivelse (f.eks. robinskey2019) og
gem dine keys (se schrivener)
Så, nu kører rancher på din computer.)
