from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import messagebox


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


class RecordGui:
    def __init__(self, root: tk.Tk, base_dir: Path, url: str):
        self.root = root
        self.base_dir = base_dir
        self.url = url
        self.helper_script = base_dir / "record_with_id.py"

        self.root.title("Playwright Recorder Launcher")
        self.root.geometry("520x210")
        self.root.resizable(False, False)

        pad = {"padx": 10, "pady": 8}

        tk.Label(root, text="Page Name").grid(row=0, column=0, sticky="w", **pad)
        self.page_name_var = tk.StringVar()
        tk.Entry(root, textvariable=self.page_name_var, width=55).grid(
            row=0, column=1, **pad
        )

        tk.Label(root, text="Test Objective").grid(row=1, column=0, sticky="w", **pad)
        self.test_objective_var = tk.StringVar()
        tk.Entry(root, textvariable=self.test_objective_var, width=55).grid(
            row=1, column=1, **pad
        )

        tk.Label(root, text=f"URL: {self.url}", fg="gray30").grid(
            row=2, column=0, columnspan=2, sticky="w", padx=10, pady=6
        )

        btn_row = tk.Frame(root)
        btn_row.grid(row=3, column=0, columnspan=2, pady=16)

        tk.Button(
            btn_row,
            text="Start Recording",
            width=18,
            command=self.start_recording,
        ).pack(side="left", padx=8)
        tk.Button(btn_row, text="Close", width=10, command=self.root.destroy).pack(
            side="left", padx=8
        )

    def start_recording(self) -> None:
        page_name = self.page_name_var.get().strip()
        objective = self.test_objective_var.get().strip()

        if not page_name:
            messagebox.showerror("Missing Input", "Please enter Page Name.")
            return
        if not objective:
            messagebox.showerror("Missing Input", "Please enter Test Objective.")
            return

        test_id = self.build_test_id(page_name)
        scenario = objective

        cmd = [
            "python3",
            str(self.helper_script),
            test_id,
            self.url,
            "--page-name",
            page_name,
            "--test-object",
            objective,
            "--scenario",
            scenario,
            "--no-prompt",
        ]

        try:
            # Launch recorder flow in a child process and return immediately.
            subprocess.Popen(cmd, cwd=str(self.base_dir))
        except OSError as exc:
            messagebox.showerror("Launch Failed", f"Could not start recorder: {exc}")
            return

        messagebox.showinfo(
            "Recorder Started",
            f"Started Playwright recorder.\n\nTest ID: {test_id}\nURL: {self.url}",
        )

    @staticmethod
    def build_test_id(page_name: str) -> str:
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"TC_{slugify(page_name).upper()}_{stamp}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tiny GUI launcher for Playwright recording with metadata."
    )
    parser.add_argument(
        "--url",
        default="http://novel.hctestedu.com/",
        help="Target URL for recording.",
    )
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    root = tk.Tk()
    RecordGui(root=root, base_dir=base_dir, url=args.url)
    root.mainloop()


if __name__ == "__main__":
    main()
