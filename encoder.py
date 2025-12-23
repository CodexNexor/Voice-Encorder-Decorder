import base64
from pathlib import Path

def encode_audio_to_code(input_file: str, output_text_file: str | None = None) -> str:
    audio_path = Path(input_file)

    if not audio_path.exists():
        raise FileNotFoundError(f"Input file not found: {audio_path}")

    audio_bytes = audio_path.read_bytes()
    encoded_code = base64.b64encode(audio_bytes).decode("ascii")

    if output_text_file:
        Path(output_text_file).write_text(encoded_code, encoding="utf-8")
        print(f"\nSecret code saved to: {output_text_file}")
    else:
        print("\nYour Secret Code:\n")
        print(encoded_code)

    return encoded_code


def main():
    print("=== Audio to Secret Code Encoder ===")

    # Ask user for audio file path
    input_path = input("Enter path of your audio file (mp3/wav/etc.): ").strip()

    # Ask where to save output
    save_option = input("Save secret code to .txt file? (y/n): ").strip().lower()

    if save_option == "y":
        output_file = input("Enter output .txt filename: ").strip()
        encode_audio_to_code(input_path, output_file)
    else:
        encode_audio_to_code(input_path, None)


if __name__ == "__main__":
    main()
