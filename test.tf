variable cmd1 {
  description = "test1"
  default   = ""
}
variable cmd2 {
  description = "test2"
  default   = ""
}
variable cmd3 {
  description = "test3"
  default   = ""
}
resource "null_resource" "example1" {
  provisioner "local-exec" {
    command = "${var.cmd1} ${var.cmd2} ${var.cmd3}"
  }
}
