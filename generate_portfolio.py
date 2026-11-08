import os

b64_path = r"C:\Users\Dr.C\.gemini\antigravity\scratch\wasif-portfolio\wave_b64.txt"
with open(b64_path, 'r', encoding='utf-8') as f:
    wave_b64 = f.read().strip()

template_path = r"C:\Users\Dr.C\.gemini\antigravity\scratch\wasif-portfolio\template.html"
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

output_html = template.replace("__WAVE_B64_PLACEHOLDER__", wave_b64)

output_path = r"C:\Users\Dr.C\.gemini\antigravity\scratch\wasif-portfolio\index.html"
with open(output_path, "w", encoding="utf-8") as out:
    out.write(output_html)

print(f"Generated index.html successfully at {output_path} (Size: {os.path.getsize(output_path)} bytes)")
