def generate_alb(name: str = "generated-alb") -> str:
    return f"""
module "alb" {{
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 9.0"

  name               = "{name}"
  load_balancer_type = "application"

  vpc_id  = module.vpc.vpc_id
  subnets = module.vpc.public_subnets
}}
""".strip()
