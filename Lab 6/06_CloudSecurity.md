# Cloud Security

## Level 1

    `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/86267756-f5b4-4057-9c2c-4f1d59c7ae33">
   
    `unzip awscliv2.zip`

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/765915d2-0bee-47bc-aae6-05dff063816d">

    `sudo ./aws/install`

After installing the AWS CLI, we can check if it was installed correctly by running the `aws --version` command.

We can access the S3 bucket containing the content for the flaws.cloud website using the AWS CLI by running the following command:
    
    `aws s3 ls s3://flaws.cloud/ --no-sign-request --region us-west-2`

We can see that a file named `secret-dd02c7c.html` is located in the bucket and looks interesting.

We can navigate to the secret page by visiting [http://flaws.cloud/secret-dd02c7c.html](http://flaws.cloud/secret-dd02c7c.html) in a web browser.

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/38237e20-7e13-48fd-a69f-944c4fdc0894">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/f86a2a7d-49bd-40ff-a74d-846fc9876289">

### Vulnerabilities

1. Exposed S3 bucket: The S3 bucket "flaws.cloud" is exposed to the internet, allowing anyone to access its contents without authentication.
2. Lack of encryption: The contents of the S3 bucket are not encrypted, which makes it easier for attackers to intercept and read sensitive information.
3. Accessible HTML file: The file "secret-dd02c7c.html" is accessible to anyone who knows the URL, which can lead to the disclosure of sensitive information.

### Potential Business Implications

1. Loss of customer trust: If sensitive information is leaked due to these vulnerabilities, customers may lose trust in the company's ability to protect their data.
2. Legal and regulatory penalties: Depending on the nature of the exposed data, the company may be liable for legal and regulatory penalties.
3. Financial loss: The loss of customer trust and legal penalties can result in financial loss for the company.

### Possible Solutions

1. Restrict access to the S3 bucket: The S3 bucket should be properly secured with access controls to restrict access only to authorized users.
2. Implement encryption: The contents of the S3 bucket should be encrypted to protect against interception and unauthorized access.
3. Remove or secure the HTML file: The file should be removed or secured with authentication to prevent unauthorized access.

To address the vulnerabilities in level 1, the company could use AWS IAM to create users with limited permissions and assign them to appropriate groups with specific access levels. The S3 bucket should be configured to allow access only to authorized users, and the contents of the bucket should be encrypted using AWS S3 encryption. Finally, the HTML file should be removed or secured with authentication to prevent unauthorized access. By implementing these solutions, the company can mitigate the potential business implications of these vulnerabilities and protect their customers' sensitive information.

## Level 2

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/625a1218-6cb3-40da-a745-a376d12cb445">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/38f2deed-6dca-452f-b930-f276d39418ad">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/55e1a588-12c5-4e34-a5b2-6c5d8a36df9f">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/41752a7b-abab-4256-8cd7-32a9ec1201b1">

- The user should see that the bucket `flaws.cloud` is listed. This bucket is accessible to anyone with the URL, as shown by the URL [https://flaws.cloud.s3.amazonaws.com/](https://flaws.cloud.s3.amazonaws.com/) being accessible.
- The user needs to create an IAM user in the AWS account and configure the AWS CLI to use that user's credentials. This allows the user to access the S3 bucket associated with the Level 2 challenge.
- Within the AWS Dashboard, the user should search for IAM and add a new user under the "Users" section. They should create a username and select an access key.
- The user should then attach the user to a group with the necessary permissions, in this case, "AdminS3", which can be created with the "Create Group" button.
- Once the user is created, the Secret Access Key will be displayed. It's important to note that this key will only be displayed at this point, and if it's lost, it will need to be regenerated.
- The user should then configure the AWS CLI on their local machine using the `aws configure` command. They will be prompted to enter their AWS Access Key ID, Secret Access Key, region (in this case, `us-east-1`), and default output format (in this case, `json`).

### Vulnerabilities

- Insecure S3 Bucket: The S3 bucket "level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud" has been modified to grant public access to everyone who has the URL, making it vulnerable to unauthorized access and data exfiltration.
- AWS Access Key Exposure: An AWS access key was accidentally left in a public S3 bucket, making it easily accessible to attackers. This could result in unauthorized access to the AWS account, leading to the theft of sensitive information, data loss or even complete compromise of the account.

### Potential Business Implications

- Data theft or loss: The unauthorized access to the S3 bucket and AWS account can lead to the theft or loss of sensitive data, which can have a significant impact on the business.
- Reputation damage: The exposure of confidential data can damage the reputation of the business and lead to a loss of customer trust.
- Legal and regulatory penalties: The exposure of sensitive information can lead to legal and regulatory penalties, such as fines and lawsuits.

### Potential Solutions

- Secure the S3 Bucket: The S3 bucket should be secured by modifying its access control list (ACL) to prevent public access, and only allow access to authorized users. The bucket should also be encrypted to ensure the confidentiality of the data.
- Rotate Access Keys: The exposed AWS access key should be revoked and replaced with a new access key. Access keys should also be regularly rotated to minimize the risk of exposure.
- Implement IAM Best Practices: Best practices such as the principle of least privilege, multi-factor authentication (MFA), and monitoring of IAM activity should be implemented to secure the AWS account.
- Regular Security Audits: Regular security audits and vulnerability assessments should be conducted to identify any vulnerabilities or weaknesses in the security posture and take corrective measures promptly.
- By implementing these solutions, the business can mitigate the risk of unauthorized access to its sensitive data and avoid potential damage to its reputation and financial losses.

## Level 3

The user can find the AWS key by accessing the S3 bucket using the URL [https://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud.s3.amazonaws.com/] (https://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud.s3.amazonaws.com/). This reveals that the bucket contains a git config file.

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/1ff6eee9-a821-46f7-8754-d4caa1bdd1e3">

To download the entire S3 bucket locally, the user can use the command `aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region us-west-2`.

The user can checkout the git commit using the command `git checkout b64c8dcfa8a39af06521cf4cb7cdce5f0ca9e526`. This reveals the existence of an `access_keys.txt` file.

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/0478950d-25c9-4b10-a186-655b9cb52267">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/de2caf9a-2d41-4074-bbdd-548b4451cdfc">

The `access_keys.txt` file contains the access key and secret access key, which are required to authenticate with AWS. The access key is `AKIAJ366LIPB4IJKT7SA`, and the secret access key is `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`.

The user can configure a new AWS profile using the command `aws configure --profile flaws`. After entering the access key, secret access key, region, and default output format, the user can list the files in the S3 bucket using the command `aws --profile flaws s3 ls`.

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/cba52835-e545-4c91-ac5f-64927bac8e2d">

<img width="600" alt="image" src="https://github.com/gabizzle/Penetration-Testing/assets/67624149/19a9ad5c-ebe7-4a2e-a88a-578dc5a39f11">

### Vulnerabilities

1. Exposure to Authenticated AWS Users: The S3 bucket is set to allow access to any authenticated AWS user. This can lead to unauthorized access to sensitive information stored in the bucket by an authenticated user with malicious intent.
2. Git Repository Access: The S3 bucket contains a Git repository that can be accessed by anyone with access to the bucket, potentially allowing unauthorized access to sensitive information.

### Potential Business Implications

1. Loss of confidential data: Unauthorized access to sensitive information can lead to a loss of confidential data, which can be damaging to the business and may result in legal and regulatory penalties.
2. Reputation damage: A data breach can damage the reputation of the business, leading to a loss of customer trust and revenue.

### Possible Solutions

1. Restrict Access: The S3 bucket should be configured to only allow access to authorized users and not to any authenticated AWS user.
2. Secure Git Repository: The Git repository should be secured with access controls, such as requiring authentication and authorization, and encryption to prevent unauthorized access.
3. Regular Security Audits: Regular security audits should be conducted to identify vulnerabilities and ensure that appropriate security measures are in place to protect sensitive information.

By implementing these solutions, the business can mitigate the risk of data breaches, loss of confidential data, and reputation damage, thereby maintaining customer trust and avoiding financial losses.
