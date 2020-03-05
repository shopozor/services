#! /bin/bash

if [ "$#" -ne "4" ] ; then
  echo "Usage: $0 <base-url> <env-name> <k8s-dashboard-version> <cert-mgr-version>"
  exit 1
fi

BASE_URL=$1
ENV_NAME=$2
K8S_DASHBOARD_VERSION=$3
CERT_MANAGER_VERSION=$4

# Transform dashboard ingress from /kubernetes-dashboard path to dashboard subdomain
dashboard_ingress_yaml="dashboard-ingress.yaml"
kubectl delete ingress kubernetes-dashboard
wget -q ${BASE_URL}/manifests/${dashboard_ingress_yaml} -O ${dashboard_ingress_yaml}
sed -i "s/HOSTNAME/${ENV_NAME}.hidora.com/g" ${dashboard_ingress_yaml}

# Activate TLS
kubectl create namespace cert-manager
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml
# TODO: not sure the rest of it will work if it is installed before letsencrypt