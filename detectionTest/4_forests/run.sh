python runForests.py
echo "Forests Run Complete" | mailx -r "CloudBuild" -s "Forests Run Complete -  `date`" "arjunmuhunthan@gmail.com"
echo "Forests Run Complete" | mailx -r "CloudBuild" -s "Forests Run Complete - `date`" "sp3612@ic.ac.uk"
python runTest.py
echo "Forests Test Complete" | mailx -r "CloudBuild" -s "Forests Test Complete - `date`" "arjunmuhunthan@gmail.com"
echo "Forests Test Complete" | mailx -r "CloudBuild" -s "Forests Test Complete - `date`" "sp3612@ic.ac.uk"
