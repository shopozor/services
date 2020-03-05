#! /bin/bash

if [ "$#" -ne "4" ] ; then
  echo "Usage: $0 <base-url> <env-name> <jelastic-k8s-version> <cert-mgr-version>"
  exit 1
fi

BASE_URL=$1
ENV_NAME=$2
JELASTIC_K8S_VERSION=$3
CERT_MANAGER_VERSION=$4

# Expose k8s api through k8s-api subdomain
api_ingress_yaml="k8s-api-ingress.yaml"
api_namespace="default"
# kubectl delete ingress kubernetes-api -n ${api_namespace}
wget -q ${BASE_URL}/manifests/${api_ingress_yaml} -O ${api_ingress_yaml}
sed -i "s/HOSTNAME/${ENV_NAME}.hidora.com/g" ${api_ingress_yaml}
kubectl apply -f ${api_ingress_yaml} -n ${api_namespace}

# TODO: the dashboard needs to have a reference to the k8s-api.HOSTNAME, not HOSTNAME/api
# Transform k8s dashboard ingress from /kubernetes-dashboard path to k8s-dashboard subdomain
dashboard_ingress_yaml="k8s-dashboard-ingress.yaml"
dashboard_namespace="kubernetes-dashboard"
# kubectl delete ingress kubernetes-dashboard -n ${dashboard_namespace}
kubectl apply -f https://raw.githubusercontent.com/jelastic-jps/kubernetes/${JELASTIC_K8S_VERSION}/addons/kubernetes-dashboard-beta.yaml
wget -q ${BASE_URL}/manifests/${dashboard_ingress_yaml} -O ${dashboard_ingress_yaml}
sed -i "s/HOSTNAME/${ENV_NAME}.hidora.com/g" ${dashboard_ingress_yaml}
kubectl apply -f ${dashboard_ingress_yaml} -n ${dashboard_namespace}

# Activate TLS
kubectl create namespace cert-manager
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml
# TODO: not sure the rest of it will work if it is installed before letsencrypt