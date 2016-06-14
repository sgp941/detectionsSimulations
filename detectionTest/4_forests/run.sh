python runPatchSize.py
echo "PatchSize Run Complete" | mailx -r "CloudBuild" -s "PatchSize Run Complete -  `date`" "arjunmuhunthan@gmail.com"
echo "PatchSize Run Complete" | mailx -r "CloudBuild" -s "PatchSize Run Complete - `date`" "sp3612@ic.ac.uk"
python runTest.py
echo "PatchSize Test Complete" | mailx -r "CloudBuild" -s "PatchSize Test Complete - `date`" "arjunmuhunthan@gmail.com"
echo "PatchSize Test Complete" | mailx -r "CloudBuild" -s "PatchSize Test Complete - `date`" "sp3612@ic.ac.uk"
