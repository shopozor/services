#! /bin/bash

if [ "$#" -ne "3" ] ; then
  echo "Usage: $0 <base-url> <cert-mgr-version> <cert-mgr-email>"
  exit 1
fi

BASE_URL=$1
CERT_MANAGER_VERSION=$2
CERT_MANAGER_EMAIL=$3

# Install cert-manager
kubectl create namespace cert-manager
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml

# Install certification issuers
wget ${BASE_URL}/manifests/staging_issuer.yaml -O staging_issuer.yaml
wget ${BASE_URL}/manifests/prod_issuer.yaml -O prod_issuer.yaml
sed -i "s/EMAIL_ADDRESS/${CERT_MANAGER_EMAIL}/g" staging_issuer.yaml
kubectl create -f staging_issuer.yaml
sed -i "s/EMAIL_ADDRESS/${CERT_MANAGER_EMAIL}/g" prod_issuer.yaml
kubectl create -f prod_issuer.yaml