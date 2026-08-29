# AWS IAM Security Auditor Write-Up

## Overview
This project is a Python-based AWS IAM auditing tool that uses Boto3 to identify potential security vulnerabilities. 
This tool scans everyone users for their permissions, MFA, and access keys.

## Purpose
Poor IAM hygiene is far too common in IAM environments despite being relatively simple to bolster. 
This project explores how IAM security reviews can be automated with Python.

## Architecture / How It Works
Refer to [View the IAM Auditor Flowchart](./iam-auditor-flowchart.png) within this folder

## Security Checks 
| Finding | Risk Score |
|---|---:|
| High-risk policy | +25 |
| Medium-risk policy | +10 |
| Low-risk policy | +5 |
| Missing MFA | +20 |
| Access key older than 90 days | +5 |
