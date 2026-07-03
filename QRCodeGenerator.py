import qrcode

def generate_qr(text, output_path):
    img = qrcode.make(text)
    img.save(output_path)

def main():
    text = input("Text or URL to encode: ")
    output_path = input("Output image path (e.g. qr.png): ")
    generate_qr(text, output_path)
    print(f"QR code saved to {output_path}")

if __name__ == "__main__":
    main()
