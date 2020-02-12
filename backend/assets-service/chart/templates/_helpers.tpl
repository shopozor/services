{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "chart.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "chart.labels" -}}
app.kubernetes.io/name: {{ include "chart.name" . }}
helm.sh/chart: {{ include "chart.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Common minio environment variables setup
*/}}
{{- define "minio.envvarsblock" -}}
- name: MINIO_SERVER_ACCESS_KEY
  valueFrom:
    secretKeyRef:
      name: {{ .Values.minio.fullname }}
      key: access-key
- name: MINIO_SERVER_SECRET_KEY
  valueFrom:
    secretKeyRef:
      name: {{ .Values.minio.fullname }}
      key: secret-key
- name: MINIO_SERVER_HOST
  value: {{ .Values.minio.fullname }}
- name: MINIO_SERVER_PORT_NUMBER
  value: {{ .Values.minio.server.port | quote }}
- name: MINIO_ALIAS
  value: {{ .Values.minio.client.alias }}
{{- end -}}

{{/*
Wait for minio init container definition
*/}}
{{- define "wait-for-minio" -}}
- name: wait-for-minio
  image: {{ .Values.minio.client.image }}
  env: {{- include "minio.envvarsblock" . | nindent 4 }}
  command:
    - /bin/sh
    - -c
    - |
      mc config host add ${MINIO_ALIAS} http://${MINIO_SERVER_HOST}:${MINIO_SERVER_PORT_NUMBER} ${MINIO_SERVER_ACCESS_KEY} ${MINIO_SERVER_SECRET_KEY}
{{- end -}}