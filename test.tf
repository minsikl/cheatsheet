variable cmd {
  default   = ""
}
resource "null_resource" "example1" {
  provisioner "local-exec" {
    command = "${var.cmd}"
  }
}
