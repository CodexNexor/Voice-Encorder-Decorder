import base64
from pathlib import Path

def decode_code_to_audio(code: str, output_audio_file: str) -> None:
    try:
        audio_bytes = base64.b64decode(code.encode("ascii"))
    except Exception as e:
        raise ValueError(f"Invalid code! Could not decode: {e}")

    Path(output_audio_file).write_bytes(audio_bytes)
    print(f"\nAudio successfully restored and saved as: {output_audio_file}")


def main():
    print("=== Secret Code to Audio Decoder ===")

    choice = input("Do you want to: \n1) Paste the code \n2) Load code from a .txt file\nChoose 1 or 2: ").strip()

    if choice == "1":
        print("\nPaste your secret code below:")
        code = input("Code: ").strip()

    elif choice == "2":
        file_path = input("Enter path of the .txt file: ").strip()
        code = Path(file_path).read_text(encoding="utf-8").strip()

    else:
        print("Invalid option! Choose 1 or 2.")
        return

    output_audio = input("Enter output audio filename (example: recovered.mp3): ").strip()

    decode_code_to_audio(code, output_audio)


if __name__ == "__main__":
    main()
