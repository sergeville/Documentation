#!/usr/bin/env python3
"""Minutes dashboard server — auto-discovers minutes-*.md files in this directory.

Serves:
  /api/minutes   JSON list of all minutes files, parsed from filename + header
  /*             static files (index.html, md files, etc.)
"""
import http.server
import json
import re
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = 8899

# Filename convention: minutes-YYYY-MM-DD-HHMM-topic-slug.md
FILENAME_RE = re.compile(
    r"^minutes-(\d{4}-\d{2}-\d{2})-(\d{2})(\d{2})-(.+)\.md$"
)


def _extract_field(body: str, label: str) -> str | None:
    """Look for `**Label:** value` in the first ~20 lines."""
    pattern = rf"\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$"
    for line in body.splitlines()[:25]:
        m = re.match(pattern, line.strip())
        if m:
            return m.group(1).strip()
    return None


def _first_heading(body: str) -> str | None:
    for line in body.splitlines()[:5]:
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _first_paragraph(body: str, skip_lines: int = 1) -> str:
    """First non-empty non-meta paragraph, truncated."""
    paras = []
    current = []
    for line in body.splitlines()[skip_lines:]:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("---") or s.startswith("**"):
            if current:
                paras.append(" ".join(current))
                current = []
            continue
        current.append(s)
        if paras:
            break
    if current and not paras:
        paras.append(" ".join(current))
    text = paras[0] if paras else ""
    return text[:280] + ("…" if len(text) > 280 else "")


def _slug_to_title(slug: str) -> str:
    return " ".join(w.capitalize() for w in slug.replace("_", "-").split("-"))


def scan_minutes() -> list[dict]:
    out = []
    for path in ROOT.glob("minutes-*.md"):
        m = FILENAME_RE.match(path.name)
        if not m:
            continue
        date, hh, mm, slug = m.group(1), m.group(2), m.group(3), m.group(4)
        try:
            body = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            body = ""

        heading = _first_heading(body) or ""
        # Strip common prefixes like "Session Minutes — " to get real topic
        topic = heading
        for prefix in ("Session Minutes — ", "Meeting Minutes — ", "Session Minutes -- ", "Meeting Minutes -- "):
            if topic.startswith(prefix):
                topic = topic[len(prefix):].strip()
                break
        # If topic is just a date/time stamp, derive from slug
        if not topic or re.match(r"^\d{4}-\d{2}-\d{2}", topic):
            topic = _slug_to_title(slug)
        # Prefer explicit Theme / Topic field if present
        theme = _extract_field(body, "Theme") or _extract_field(body, "Topic")
        if theme:
            topic = theme

        agent = (
            _extract_field(body, "Agent")
            or _extract_field(body, "Facilitator")
            or "Unknown"
        )
        summary = _first_paragraph(body, skip_lines=1)

        out.append({
            "date": date,
            "time": f"{hh}:{mm}",
            "agent": agent,
            "topic": topic,
            "file": path.name,
            "summary": summary,
            "mtime": path.stat().st_mtime,
        })

    # Newest first: sort by date desc, then time desc
    out.sort(key=lambda x: (x["date"], x["time"]), reverse=True)
    return out


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.rstrip("/") == "/api/minutes":
            try:
                data = scan_minutes()
                payload = json.dumps(data).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(payload)
            except Exception as e:
                self.send_error(500, f"Scan failed: {e}")
            return
        super().do_GET()

    def log_message(self, format, *args):  # quiet
        return


def main():
    import os
    os.chdir(ROOT)
    with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print(f"minutes_server.py listening on :{PORT} (root={ROOT})")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
