resource "aws_s3_bucket" "trading_bucket" {
  bucket = "${var.bucket_name}"
  acl = "${var.acl_value}"

  tags = {
    Name        = "${var.bucket_name}"
    Environment = "dev"
  }
}