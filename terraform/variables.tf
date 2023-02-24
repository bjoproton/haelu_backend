variable "region" {
  description = "Default region"
  type = string
  default = "eu-west-1"
}

variable "ami" {
  description = "AWS AMI"
  type = string
  default = "ami-096800910c1b781ba"
}

variable "instance_type" {
  description = "AWS IT"
  type = string
  default = "t2.micro"
}

variable "domain" {
  description = "domain"
  type = string
}