from pathlib import Path
import subprocess, json

def extract_enem_batch(pdf_dir="dados/provas_pdf",
                       out_dir="dados/provas_json",
                       overwrite=False,
                       minimal=False):
    """
    Run `python -m enem` on every *.pdf in `pdf_dir` and drop the
    extractor’s output in `out_dir/<pdf_stem>/`.

    Returns a list of paths to the resulting data.json files.
    """
    pdf_dir, out_dir = Path(pdf_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    data_files = []
    for pdf in sorted(pdf_dir.glob("*.pdf")):
        dest = out_dir / pdf.stem          # e.g. dados/provas_json/ENEM2019
        if dest.exists() and not overwrite:
            print(f"✔  {pdf.name} already extracted — skipping")
            data_files.append(dest / "data.json")
            continue

        cmd = ["python", "-m", "enem", str(pdf), "-o", str(out_dir)]
        if minimal:
            cmd += ["-m", "true"]          # only questions/answers, if you want
        try:
            subprocess.run(cmd, check=True)
            data_files.append(dest / "data.json")
            print(f"✅  {pdf.name} → {dest}")
        except subprocess.CalledProcessError as e:
            print(f"❌  {pdf.name}: {e.stderr or e}")

    return data_files

extract_enem_batch()