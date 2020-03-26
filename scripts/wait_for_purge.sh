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

echo "Waiting for deployments to be purged"
for iteration in `seq 1 $TIMEOUT`; do
  status=$(kubectl get -n $NAMESPACE deployments)
  if [ -z "$status" ] ; then
    echo "Purge successful" && exit 0
  else
    sleep ${DELTA_T}
  fi
done

echo "Deployments purge timed out" && exit 1