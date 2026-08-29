# AWS IAM Security Auditor Write-Up

## Overview
This project is a Python-based AWS IAM auditing tool that uses Boto3 to identify potential security vulnerabilities. 
This tool scans everyone users for their permissions, MFA, and access keys.

## Purpose
Poor IAM hygiene is far too common in IAM environments despite being relatively simple to bolster. 
This project explores how IAM security reviews can be automated with Python.

## Architecture / How It Works
Refer to the [IAM Auditor Flowchart](./iam-auditor-flowchart.png) within this folder to see the architecture.

## Security Checks 
| Finding | Risk Score |
|---|---:|
| High-risk policy | +25 |
| Medium-risk policy | +10 |
| Low-risk policy | +5 |
| Missing MFA | +20 |
| Access key older than 90 days | +5 |

### Risk Levels

| Score | Risk Level |
|---|---|
| 40+ | High |
| 20–39 | Medium |
| 1–19 | Low |
| 0 | Safe |

## Example Findings
(with a simulated AWS environment)
<img width="894" height="195" alt="image" src="https://github.com/user-attachments/assets/7c726080-18e7-422c-a711-942e9c72edfd" />

