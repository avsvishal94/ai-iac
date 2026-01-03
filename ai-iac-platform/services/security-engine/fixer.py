def auto_fix(terraform_code: str) -> str:
    return terraform_code.replace(
        "public_access = true",
        "public_access = false"
    )
