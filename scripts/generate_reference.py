#!/usr/bin/env -S uv run python
"""Generate reference swagger2.json file."""

import json
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
app_path = project_root / "src" / "openapi_server"
sys.path.insert(0, str(app_path))

from main import app


def main():
    """Generate reference swagger2.json file."""
    # Get swagger2 spec
    spec = app.swagger2()

    # Create reference directory
    ref_dir = project_root / "tests" / "reference"
    ref_dir.mkdir(parents=True, exist_ok=True)

    # Write reference file
    ref_file = ref_dir / "swagger2.json"
    with open(ref_file, 'w') as f:
        json.dump(spec, f, indent=2, sort_keys=True)

    print(f"✅ Generated {ref_file}")

if __name__ == "__main__":
    main()
