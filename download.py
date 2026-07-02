import subprocess
from pathlib import Path

# Cartella dello script
SCRIPT_DIR = Path(__file__).parent

LINKS_FILE = SCRIPT_DIR / "links.txt"
OUTPUT_DIR = SCRIPT_DIR

if not LINKS_FILE.exists():
    print("❌ File links.txt non trovato!")
    exit(1)

# Legge tutti i link
with open(LINKS_FILE, "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

total = len(links)

while links:
    link = links[0]

    print(f"\n[{total - len(links) + 1}/{total}] Download:")
    print(link)

    command = [
        "yt-dlp",
        "-f", "ba",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--download-archive", str(SCRIPT_DIR / "downloaded.txt"),
        "-o", str(OUTPUT_DIR / "%(title)s.%(ext)s"),
        link
    ]

    result = subprocess.run(command)

    if result.returncode == 0:
        print("✅ Download completato.")

        # Rimuove il link appena scaricato
        links.pop(0)

        # Aggiorna il file links.txt
        with open(LINKS_FILE, "w", encoding="utf-8") as f:
            for l in links:
                f.write(l + "\n")
    else:
        print("❌ Errore durante il download.")
        print("Il link rimane nel file per poter riprovare.")
        break

print("\n🏁 Operazione terminata.")