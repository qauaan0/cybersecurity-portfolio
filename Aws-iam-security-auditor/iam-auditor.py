# Setup and Imports

import boto3
client = boto3.client('iam')
import csv
from datetime import datetime, timezone
current_time = datetime.now(timezone.utc)
names_list = client.list_users()

# Generate CSV Report

with open("iam_report.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Groups", "Risk Score", "Risk Level", "Findings"])

# Enumerate IAM Users

    for users in names_list["Users"]:
        username = (users["UserName"])

# User Policies 

        managed_user_policies = client.list_attached_user_policies(UserName=username)
        inline_user_policies = client.list_user_policies(UserName=username)
        managed_user_policy_names = []
        inline_user_policy_names = []

        for policy1 in managed_user_policies["AttachedPolicies"]:
            managed_user_policy_names.append(policy1["PolicyName"])
        for policy2 in inline_user_policies["PolicyNames"]:
            inline_user_policy_names.append(policy2)

# Group Policies

        group_names = []
        group_policies = client.list_groups_for_user(UserName=username)
        managed_group_policy_names = []
        inline_group_policy_names = []

        for groups in group_policies["Groups"]:
            group_names.append(groups["GroupName"])
        
            managed_group_policies = client.list_attached_group_policies(GroupName=groups["GroupName"])
            inline_group_policies = client.list_group_policies(GroupName=groups["GroupName"])

            for gpolicy1 in managed_group_policies["AttachedPolicies"]:
                managed_group_policy_names.append(gpolicy1["PolicyName"])
            for gpolicy2 in inline_group_policies["PolicyNames"]:
                inline_group_policy_names.append(gpolicy2)

# Credential Security

        access_keys = client.list_access_keys(UserName=username)
        mfa = client.list_mfa_devices(UserName=username)
        access_key_age = []

        for keys in access_keys["AccessKeyMetadata"]:
            key_create_date = keys["CreateDate"]
            if keys["Status"] == "Active":
                access_key_age.append((current_time - key_create_date).days)

        mfa_status = len(mfa["MFADevices"]) > 0

# Analyze Findings

        score = 0
        findings = []
        combined_policies = managed_user_policy_names + inline_user_policy_names + managed_group_policy_names + inline_group_policy_names
        high_risk_policies = ["AdministratorAccess", "PowerUserAccess"]
        medium_risk_policies = ["IAMReadOnlyAccess", "ReadOnlyAccess", "SecurityAudit", "AmazonS3ReadOnlyAccess", "LegacyServiceS3Access",]
        low_risk_policies = ["ContractorS3Access"]
        for policy_name in combined_policies:
            if  policy_name in high_risk_policies:
                score += 25
                findings.append(policy_name)
            elif policy_name in medium_risk_policies:
                score += 10
                findings.append(policy_name)
            elif policy_name in low_risk_policies:
                score += 5
                findings.append(policy_name)
        
# Risk Classification and Scoring

        if mfa_status == False:
            score += 20
            findings.append("Missing MFA")
        for key_age in access_key_age:
            if key_age > 90:
                score += 5
                findings.append("Access Key > 90 Days Old")
        if score >= 40:
            risk_level = "High"
            print (risk_level, username, "in group: ", group_names, "with score of: ", score, "\n with reason being: ", findings)
        elif score >= 20:
            risk_level = "Medium"
            print (risk_level, username, "in group: ", group_names, "with score of: ", score, "\n with reason being: ", findings)
        elif score > 0:
            risk_level = "Low"
            print (risk_level, username, "in group: ", group_names, "with score of: ", score, "\n with reason being: ", findings)
        else:
            risk_level = "Safe"
            print (risk_level, username)

        writer.writerow([username, group_names, score, risk_level, findings])
