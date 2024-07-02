# Static Website Deployment

## introduciton
This project involves deploying a static website onto a cloud platform, stepping into the role of a DevOps engineer. The website is served using a web server (NGINX or Apache) configured on a cloud instance AWS EC2

## Cloud Platform Setup
1. **Create an Account:**
   - [AWS](https://aws.amazon.com/)

2. **Launch an Instance:**
   - **AWS EC2:**
     - Log in to AWS Management Console.
     - Navigate to EC2 Dashboard.
     - Click on 'Launch Instance'.
     - Select an Amazon Machine Image (AMI) (e.g., Ubuntu Server).
     - Choose an instance type (e.g., t2.micro for free tier).
     - Configure instance details, add storage, and tags.
     - Configure Security Group to allow HTTP (port 80) and SSH (port 22) traffic.
     - Review and launch the instance.

## Web Server Setup
1. **Connect to Your Instance:**
   - Use SSH to connect to your cloud instance.

   ```bash
   ssh -i /path/to/your-key.pem username@instance-public-ip
   
   ```nginx
   sudo yum update -y
   sudo yum install -y nginx

   sudo systemctl start nginx
   sudo systemctl enable nginx

   scp -i /path/to/your-key.pem -r /path/to/your-website-files username@instance-public-ip:/var/www/html/

>> sudo vi /etc/nginx/nginx.conf<<<

## Testing your deployment

Access Your Website:
Open a web browser and navigate to the public IP address of your instance.
Verify that your static website is displayed correctly.

