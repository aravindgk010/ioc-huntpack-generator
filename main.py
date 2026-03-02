import argparse
from pathlib import Path

from ioc_extractor.extractor import extract_iocs
from ioc_extractor.normalizer import normalize_iocs


def read_input_file(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Extract IOCs from a text file and prepare them for reporting."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input text file",
    )

    args = parser.parse_args()
    input_path = Path(args.input)

    text = read_input_file(input_path)
    raw_iocs = extract_iocs(text)
    normalized_iocs = normalize_iocs(raw_iocs)

    print("\n[+] Extracted IOCs:\n")
    for ioc_type, values in normalized_iocs.items():
        print(f"{ioc_type.upper()}:")
        if values:
            for value in values:
                print(f"  - {value}")
        else:
            print("  - None found")
        print()


if __name__ == "__main__":
    main()