"""
OSINT Recon Dashboard - Tkinter Prototype (Lite Version)

This is a small, standalone Tkinter proof-of-concept built to compare
against the main Streamlit dashboard. It intentionally covers only two
modules (WHOIS + DNS) to demonstrate the Tkinter approach without
duplicating the full project.

The main, full-featured submission is the Streamlit app (app.py).
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import json

from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_records


class OsintLiteDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OSINT Dashboard - Tkinter Prototype")
        self.geometry("700x500")

        self._build_input_area()
        self._build_tabs()

    def _build_input_area(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="x")

        ttk.Label(frame, text="Domain:").pack(side="left")
        self.domain_entry = ttk.Entry(frame, width=35)
        self.domain_entry.pack(side="left", padx=5)

        self.scan_btn = ttk.Button(frame, text="Scan", command=self.run_scan)
        self.scan_btn.pack(side="left", padx=5)

        self.status_label = ttk.Label(self, text="")
        self.status_label.pack(anchor="w", padx=10)

    def _build_tabs(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.whois_text = self._make_tab("WHOIS")
        self.dns_text = self._make_tab("DNS")

    def _make_tab(self, label):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=label)
        text_widget = scrolledtext.ScrolledText(frame, wrap="word")
        text_widget.pack(fill="both", expand=True)
        return text_widget

    def run_scan(self):
        domain = self.domain_entry.get().strip()
        if not domain:
            self.status_label.config(text="Please enter a domain.")
            return

        self.status_label.config(text="Scanning...")
        self.update()  # force the label to redraw before the lookups run

        whois_data = get_whois_info(domain)
        dns_data = get_dns_records(domain)

        self.whois_text.delete("1.0", tk.END)
        self.whois_text.insert(tk.END, json.dumps(whois_data, indent=2, default=str))

        self.dns_text.delete("1.0", tk.END)
        self.dns_text.insert(tk.END, json.dumps(dns_data, indent=2, default=str))

        self.status_label.config(text="Scan complete.")


if __name__ == "__main__":
    app = OsintLiteDashboard()
    app.mainloop()
