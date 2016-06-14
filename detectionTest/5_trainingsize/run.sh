./runTrainingSize.py
echo "TrainingSize Run Complete" | mailx -r "CloudBuild" -s "TrainingSize Run Complete -  `date`" "arjunmuhunthan@gmail.com"
echo "TrainingSize Run Complete" | mailx -r "CloudBuild" -s "TrainingSize Run Complete - `date`" "sp3612@ic.ac.uk"
./runTest.py
echo "TrainingSize Test Complete" | mailx -r "CloudBuild" -s "TrainingSize Test Complete - `date`" "arjunmuhunthan@gmail.com"
echo "TrainingSize Test Complete" | mailx -r "CloudBuild" -s "TrainingSize Test Complete - `date`" "sp3612@ic.ac.uk"
