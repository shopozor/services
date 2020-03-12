#! /bin/bash

if [ "$#" -ne "1" ] ; then
  echo "Usage: $0 <cert-mgr-version>"
  exit 1
fi

CERT_MANAGER_VERSION=$1

# Install cert-manager
kubectl create namespace cert-manager
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml