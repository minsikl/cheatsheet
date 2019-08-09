variable cmd {
  default   = "echo"
}
resource "null_resource" "example1" {
  provisioner "local-exec" {
    command = "${var.cmd}"
  }
}
