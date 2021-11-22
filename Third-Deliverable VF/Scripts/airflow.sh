#! /bin/bash
aws sts get-caller-identity
aws eks --region us-west-2 update-kubeconfig --name airflow-eks-data-bootcamp

export NFS_SERVER=$(terraform output -raw efs)


helm repo remove nfs-subdir-external-provisioner
helm repo remove apache-airflow

kubectl delete namespace storage
kubectl delete namespace airflow


kubectl create namespace storage
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/

kubectl create namespace airflow
helm repo add apache-airflow https://airflow.apache.org
helm install airflow -f airflow-values.yaml apache-airflow/airflow --namespace airflow
kubectl get pods -n airflow
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow  