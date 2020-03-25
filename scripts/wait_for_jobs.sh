#! /bin/sh

if [ "$#" -lt "1" ] ; then
  echo "Usage: $0 namespace [timeout_iterations] [delta_iterations_in_sec]"
  echo "Default: "
  echo " - timeout_iterations     : 300"
  echo " - delta_iterations_in_sec:   5"
  exit 1
fi

NAMESPACE=$1
TIMEOUT=${2:-300}
DELTA_T=${3:-5}

job_names=$(kubectl get jobs -o jsonpath='{.items[*].metadata.name}' -n $NAMESPACE)
nb_jobs=$(echo ${job_names} | wc -w)

echo "Waiting for jobs to be done"
for iteration in `seq 1 $TIMEOUT`; do
  nb_success=0
  for name in $job_names ; do
    status=$(kubectl get job $name --namespace $NAMESPACE -o jsonpath='{.status.succeeded}')
    # when status == 1, then the corresponding job is successful
    # maybe we could just put that information in some kind of arrays and just display the new successful job
    nb_success=$(($nb_success + $status))
  done
  if [ "$nb_success" -eq "$nb_jobs" ] ; then
    echo "Jobs rolled out successfully" && exit 0
  else
    sleep ${DELTA_T}
  fi
done

for name in $job_names ; do
  status=$(kubectl get job $name --namespace $NAMESPACE -o jsonpath='{.status.succeeded}')
  if [ "$status" -eq "0" ] ; then
    echo "Failed to roll out job $name."
  fi
done
echo "Jobs timed out" && exit 1