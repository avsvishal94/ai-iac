import uuid
from pathlib import Path

from generator.aws.vpc import generate_vpc
from generator.aws.eks import generate_eks
from generator.aws.alb import generate_alb
from generator.common.providers import aws_provider
from generator.common.versions import terraform_versions


SUPPORTED_RESOURCES = {
    "aws_vpc": generate_vpc,
    "aws_eks": generate_eks,
    "aws_alb": generate_alb,
}


def generate_terraform(architecture: dict) -> dict:
    """
    Takes validated architecture JSON
    Generates Terraform files on disk
    """

    request_id = str(uuid.uuid4())
    base_path = Path(f"/tmp/ai-iac/{request_id}/terraform")
    base_path.mkdir(parents=True, exist_ok=True)

    blocks = []

    for resource in architecture.get("resources", []):
        resource_type = resource["type"]

        if resource_type not in SUPPORTED_RESOURCES:
            raise ValueError(f"Unsupported resource type: {resource_type}")

        blocks.append(SUPPORTED_RESOURCES[resource_type]())

    # Write main.tf
    (base_path / "main.tf").write_text("\n\n".join(blocks))

    # Write providers.tf
    (base_path / "providers.tf").write_text(aws_provider())

    # Write versions.tf
    (base_path / "versions.tf").write_text(terraform_versions())

    return {
        "request_id": request_id,
        "terraform_path": str(base_path)
    }
