DIST = "storage/emulated/0/Music"
echo $DIST 
adb shell 'cd ${DIST} && for f in *\ *; do mv "$f" "${f// /_}"; done'
python3 adb-sync.py --reverse "storage/emulated/0/Music/University_of_North_Texas_One_O'Clock_Lab_Band_Radio" ~/Music
