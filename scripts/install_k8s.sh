#! /bin/bash

if [ "$#" -ne "3" ] ; then
  echo "Usage: $0 <base-url> <cert-mgr-version> <cert-mgr-email>"
  exit 1
fi

BASE_URL=$1
CERT_MANAGER_VERSION=$2
CERT_MANAGER_EMAIL=$3

installIssuer() {
  local name=$1
  wget ${BASE_URL}/manifests/${name}.yaml -O ${name}.yaml
  sed -i "s/EMAIL_ADDRESS/${CERT_MANAGER_EMAIL}/g" ${name}.yaml
  kubectl create -f ${name}.yaml
}

# Install cert-manager
kubectl create namespace cert-manager
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml

# Install certification issuers
installIssuer staging_issuer
installIssuer prod_issuer