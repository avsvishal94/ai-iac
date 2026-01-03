from jinja2 import Template

def generate_vpc(cidr):
    template = Template("""
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  cidr   = "{{ cidr }}"
}
""")
    return template.render(cidr=cidr)
