spark-submit\
  --master local\
  --deploy-mode client\
  pi-estimator.py $1 \

res=$?
echo "Job finished with status" res$
exit $res
