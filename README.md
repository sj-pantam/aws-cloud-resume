# AWS Cloud Resume Challenge

## Overview

This repository showcases my solution to the Cloud Resume Challenge, a project designed to build and demonstrate core cloud computing skills.

You can view the live project [here](https://www.sujanspage.com/).

## Architecture

Below is the architecture I implemented for this project:

![Architecture Diagram](https://github.com/sj-pantam/aws-cloud-resume/blob/main/aws-resume-Page-1.drawio.png) <!-- You can link to your diagram image here -->

### AWS Services Utilized

- **S3**: For hosting the static website.
- **AWS CloudFront**: To distribute content globally with low latency.
- **AWS Certificate Manager (ACM)**: For managing SSL/TLS certificates to secure the website.
- **AWS Lambda**: To handle backend logic and integrate with DynamoDB.
- **DynamoDB**: For storing visitor count data.
- **GitHub Actions**: For automating the CI/CD pipeline.
- **Terraform**: To automate infrastructure provisioning and management.
