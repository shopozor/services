#! /bin/bash

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

deployment_names=$(kubectl get deployments -o jsonpath='{.items[*].metadata.name}' -n $NAMESPACE)
nb_deployments=$(echo ${deployment_names} | wc -w)

echo "Waiting for deployments to be done"
for iteration in `seq 1 $TIMEOUT`; do
  nb_success=0
  for name in $deployment_names ; do
    status=$(kubectl rollout status deployment $name --namespace $NAMESPACE --watch=false | grep "success" | wc -l)
    if [ "$status" -eq "1" ] ; then
      echo "Deployment $name rolled out."
    fi
    nb_success=$(($nb_success + $status))
  done
  if [ "$nb_success" -eq "$nb_deployments" ] ; then
    echo "Deployments rolled out successfully"
    exit 0
  else
    echo "Iteration $iteration"
    sleep ${DELTA_T}
  fi
done

for name in $deployment_names ; do
  status=$(kubectl rollout status deployment $name --namespace $NAMESPACE --watch=false | grep "success" | wc -l)
  if [ "$status" -eq "0" ] ; then
    echo "Failed to roll out deployment $name."
  fi
done
echo "Deployments timed out" && exit 1