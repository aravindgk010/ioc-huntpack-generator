import argparse
from pathlib import Path

from ioc_extractor.extractor import extract_iocs
from ioc_extractor.normalizer import normalize_iocs
from ioc_extractor.reporter import (
    write_json_report,
    build_markdown_report,
    write_markdown_report,
)


def read_input_file(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def ensure_output_dir(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Extract IOCs from a text file and prepare them for reporting."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input text file",
    )
    parser.add_argument(
        "--output",
        default="results",
        help="Directory to store generated reports",
    )

    args = parser.parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output)

    ensure_output_dir(output_dir)

    text = read_input_file(input_path)
    raw_iocs = extract_iocs(text)
    normalized_iocs = normalize_iocs(raw_iocs)

    json_output_path = output_dir / "ioc_report.json"
    markdown_output_path = output_dir / "ioc_report.md"

    write_json_report(normalized_iocs, json_output_path)

    markdown_report = build_markdown_report(normalized_iocs, input_path.name)
    write_markdown_report(markdown_report, markdown_output_path)

    print("\n[+] Extracted IOCs:\n")
    for ioc_type, values in normalized_iocs.items():
        print(f"{ioc_type.upper()}:")
        if values:
            for value in values:
                print(f"  - {value}")
        else:
            print("  - None found")
        print()

    print("[+] Reports generated successfully:")
    print(f"  - JSON: {json_output_path}")
    print(f"  - Markdown: {markdown_output_path}")


if __name__ == "__main__":
    main()