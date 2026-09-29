"""Telecharge et concatene les pages Zephyr kernel pour tests."""

from __future__ import annotations

import os
import urllib.request
from pathlib import Path

urls = [
    "https://docs.zephyrproject.org/latest/kernel/services/index.html",
    "https://docs.zephyrproject.org/latest/kernel/services/threads/index.html",
    "https://docs.zephyrproject.org/latest/kernel/services/scheduling/index.html",
    "https://docs.zephyrproject.org/latest/kernel/services/synchronization/semaphores.html",
    "https://docs.zephyrproject.org/latest/kernel/services/synchronization/mutexes.html",
    "https://docs.zephyrproject.org/latest/kernel/services/threads/workqueue.html",
    "https://docs.zephyrproject.org/latest/kernel/services/timing/timers.html",
    "https://docs.zephyrproject.org/latest/kernel/services/interrupts.html",
    "https://docs.zephyrproject.org/latest/kernel/services/message_queues.html",
    "https://docs.zephyrproject.org/latest/kernel/memory_management/index.html",
]

out_dir = Path(__file__).resolve().parents[1] / "data"
out_dir.mkdir(exist_ok=True)
out_path = out_dir / "zephyr_kernel.html"

with open(out_path, "w", encoding="utf-8") as f:
    f.write("<html><body>\n")
    for i, url in enumerate(urls, 1):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                html = r.read().decode("utf-8", errors="ignore")
            f.write(f'<section id="zephyr_page_{i}">\n')
            f.write(html)
            f.write("\n</section>\n")
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Failed {url}: {e}")
    f.write("</body></html>\n")

print(f"Saved to {out_path}")
