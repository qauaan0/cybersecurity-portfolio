# AWS IAM Security Auditor Write-Up

## Overview
This tool audits IAM users in an AWS environment and determines their risk through missing MFA, stale access keys, and overprivileged policies. These are common security risks but often go unnoticed until an incident. Manually auditing IAM doesn't scale past a handful of users, so this automates the review and outputs a CSV risk report.

I tested this against IAM users provisioned within my personal AWS free tier account.

## Architecture / How It Works
Refer to the [IAM Auditor Flowchart](./iam-auditor-flowchart.png) within this folder to see the architecture.

## Security Checks 
Scoring Methodology: Risk scores are cumulative. Users can accrue points from multiple findings, since combined risks (an overprivileged policy and no MFA) represent greater overall exposure. Weights were assigned based on my own judgment of relative severity; for example, full administrative access poses more immediate risk than a single stale access key.

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
The auditor generates a CSV report summarizing each IAM user's group membership, calculated risk score, risk level, and detected security findings.

<img width="894" height="195" alt="image" src="https://github.com/user-attachments/assets/7c726080-18e7-422c-a711-942e9c72edfd" />

**Note:** 'LegacyServiceS3Access' and 'ContractorS3Access' are custom test policies. 

## Technologies Used
- Python
- Boto3
- AWS IAM
- CSV

## What I Learned
- Reading documentation before working with new technologies is extremely valuable. Documentation provides exact required parameters, expected input types, and API response structures.
- Logic errors can pass testing silently if test data doesn't cover any edge cases. Testing against different IAM configurations helped me identify issues that weren't immediately obvious.
- Breaking the project into smaller steps made troubleshooting API calls and Python logic much easier.

## Future Improvements 
- Add pagination to support larger IAM environments
- Detect inactive access keys
- Detect wildcard permissions
- Align my risk scoring with official framework like CIS or AWS Security Hub
