./runTrees.py
echo "Trees Run Complete" | mailx -r "CloudBuild" -s "Trees Run Complete -  `date`" "arjunmuhunthan@gmail.com"
echo "Trees Run Complete" | mailx -r "CloudBuild" -s "Trees Run Complete - `date`" "sp3612@ic.ac.uk"
./runTest.py
echo "Trees Test Complete" | mailx -r "CloudBuild" -s "Trees Test Complete - `date`" "arjunmuhunthan@gmail.com"
echo "Trees Test Complete" | mailx -r "CloudBuild" -s "Trees Test Complete - `date`" "sp3612@ic.ac.uk"
