import subprocess

def run_checkov(path):
    result = subprocess.run(
        ["checkov", "-d", path],
        capture_output=True,
        text=True
    )
    return result.stdout
