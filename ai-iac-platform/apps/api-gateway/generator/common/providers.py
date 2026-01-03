def aws_provider(region: str = "ap-south-1") -> str:
    return f"""
provider "aws" {{
  region = "{region}"
}}
""".strip()
