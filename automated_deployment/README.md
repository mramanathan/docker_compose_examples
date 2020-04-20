## Automated Deployment -- Create Infra

- Use ‘terraform’ to spin up a fresh EC2 instance

- Terraform scripts sourced from,
  
  https://github.com/mramanathan/terraform_ansible_aws_examples/tree/master/ec2_ubuntu_docker/

- Update ‘terraform.tfvars’ with values from your AWS account

- Follow these commands to create EC2 instance,

  `$ terraform init`

  `$ terraform plan -out=”ec2.plan”`

  `$ terraform apply “ec2.plan”`


## Automated Deployment -- Install Docker in EC2

- Use ‘ansible’ playbook to install Docker in the EC2 instance

- Source of Ansible playbook,

  https://github.com/mramanathan/terraform_ansible_aws_examples/tree/master/ec2_ubuntu_docker/

- Follow the below procedure to install Docker.

- Update ‘inventory.ini’ with the public IP address of EC2 instance

- Run the `docker_setup.yml` to begin the Docker installation.

  `$ ansible-playbook --key-file <ssh-private-key> --inventory-file inventory.ini docker_setup.yml`

## Automated Deployment -- Deploy "Favorite Cities" app

- Source of Ansible playbook,

  https://github.com/mramanathan/docker_compose_examples/tree/master/automated_deployment/

- Follow these steps to deploy the two tier app,

- Update ‘inventory.ini’ with the public IP address of EC2 instance

- Run the `favorite_cities.yml` to deploy the app.

  `$ ansible-playbook --key-file <ssh-private-key> --inventory-file inventory.ini favorite_cities.yml`
