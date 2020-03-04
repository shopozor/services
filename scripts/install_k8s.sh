#! /bin/bash

# TODO: this is not necessary when we work with devspace!
kubectl create namespace dev
kubectl create namespace staging
kubectl create namespace pre-production
kubectl create namespace production