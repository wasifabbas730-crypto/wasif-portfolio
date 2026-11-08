with open(r"C:\Users\Dr.C\.gemini\antigravity\scratch\wasif-portfolio\index.html", "r", encoding="utf-8") as f:
    content = f.read()

checks = [
    ("Title tag", "<title>Syed Wasif Abbas Rizvi" in content),
    ("Three.js script", "three.min.js" in content),
    ("Wave canvas container", 'id="wave-canvas-container"' in content),
    ("Header certs button", 'id="btn-header-open-certs"' in content),
    ("Hero certs button", 'id="btn-hero-open-certs"' in content),
    ("Dock certs button", 'id="btn-dock-open-certs"' in content),
    ("Certs modal", 'id="certs-modal"' in content),
    ("Diploma preview modal", 'id="cert-preview-modal"' in content),
    ("Interactive terminal", 'id="terminal-input"' in content),
    ("Wave HUD sliders", 'id="slider-wave-speed"' in content),
    ("Base64 wave texture", "data:image/jpeg;base64," in content),
    ("Projects Verity", "Verity — Loan Underwriting Desk" in content),
    ("Projects EstatePredict", "EstatePredict Home Valuation" in content),
    ("Projects ParkGuard", "ParkGuard Parking & Barcode System" in content),
    ("Aetherfall Interactive", "Aetherfall Interactive Inc" in content),
    ("Web Audio API Synthesizer", "AudioContext" in content),
]

all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

if all_passed:
    print("\nALL VERIFICATION CHECKS PASSED PERFECTLY!")
