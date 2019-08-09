variable cmd {
  description = "test"
  default   = ""
}
resource "null_resource" "example1" {
  provisioner "local-exec" {
    command = "${var.cmd}"
  }
}
