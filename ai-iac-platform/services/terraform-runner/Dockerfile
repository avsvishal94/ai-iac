FROM hashicorp/terraform:1.6

WORKDIR /workspace

# Install system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    pipx \
    bash

# Ensure pipx binaries are on PATH
ENV PATH="/root/.local/bin:$PATH"

# Install Checkov via pipx (PEP 668 compliant)
RUN pipx install checkov

# Keep container running
ENTRYPOINT ["sleep", "infinity"]
