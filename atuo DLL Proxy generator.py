import os
import pefile
import customtkinter as ctk
from tkinter import filedialog, messagebox

class RustProxyGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rust DLL Proxy Creator - By Seif")
        self.geometry("550x750")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.dll_path = ""
        self._configure_styles()
        self._create_widgets()

    def _configure_styles(self):
        self.primary_color = "#1f538d"
        self.primary_hover = "#14375e"
        self.success_color = "#2fa572"
        self.success_hover = "#106a43"
        self.error_color = "#e74c3c"

    def _create_widgets(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=35, pady=35)

        self._create_header()
        self._create_file_selection()
        self._create_input_fields()
        self._create_action_buttons()
        self._create_footer()

    def _create_header(self):
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 25))

        title = ctk.CTkLabel(
            header_frame,
            text="⚙️ DLL PROXY GENERATOR",
            font=("Orbitron", 32, "bold"),
            text_color=self.primary_color
        )
        title.pack()

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Create Rust DLL Proxies Effortlessly",
            font=("Segoe UI", 11),
            text_color="#888888"
        )
        subtitle.pack(pady=(5, 0))

    def _create_file_selection(self):
        file_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        file_frame.pack(fill="x", pady=(0, 20))

        self.select_btn = ctk.CTkButton(
            file_frame,
            text="📂 SELECT TARGET DLL",
            fg_color=self.primary_color,
            hover_color=self.primary_hover,
            height=50,
            command=self.select_file,
            font=("Segoe UI", 13, "bold"),
            corner_radius=8
        )
        self.select_btn.pack(fill="x")

        self.file_label = ctk.CTkLabel(
            file_frame,
            text="No file selected",
            font=("Segoe UI", 10),
            text_color="#666666"
        )
        self.file_label.pack(pady=(8, 0))

    def _create_input_fields(self):
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_frame.pack(fill="x", pady=20)

        fields = [
            ("📦 Project Name", "proj_name_entry"),
            ("🔗 Proxy DLL Name", "proxy_name_entry"),
            ("📍 Original DLL Name", "orig_name_entry")
        ]

        for label_text, attr_name in fields:
            self._create_input_field(label_text, attr_name)

    def _create_input_field(self, label_text, attr_name):
        label = ctk.CTkLabel(
            self.input_frame,
            text=label_text,
            font=("Segoe UI", 11, "bold"),
            text_color="#ffffff"
        )
        label.pack(anchor="w", padx=3, pady=(10, 4))

        entry = ctk.CTkEntry(
            self.input_frame,
            height=40,
            border_color=self.primary_color,
            border_width=2,
            corner_radius=6,
            font=("Segoe UI", 10)
        )
        entry.pack(fill="x")
        setattr(self, attr_name, entry)

    def _create_action_buttons(self):
        button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(15, 0))

        self.generate_btn = ctk.CTkButton(
            button_frame,
            text="✨ GENERATE PROJECT",
            fg_color=self.success_color,
            hover_color=self.success_hover,
            height=55,
            command=self.generate,
            font=("Segoe UI", 14, "bold"),
            corner_radius=8
        )
        self.generate_btn.pack(fill="x")

    def _create_footer(self):
        footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        footer_frame.pack(fill="x", side="bottom", pady=(20, 0))

        separator = ctk.CTkLabel(
            footer_frame,
            text="━" * 50,
            text_color="#333333"
        )
        separator.pack()

        self.status_label = ctk.CTkLabel(
            footer_frame,
            text="🔄 Status: Waiting for input",
            font=("Segoe UI", 10),
            text_color="#888888"
        )
        self.status_label.pack(pady=(8, 0))

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("DLL Files", "*.dll")])
        if path:
            self.dll_path = path
            filename = os.path.basename(path).replace(".dll", "")
            self.file_label.configure(text=f"✅ Selected: {os.path.basename(path)}", text_color=self.success_color)
            self.proxy_name_entry.delete(0, 'end')
            self.proxy_name_entry.insert(0, filename)
            self.proj_name_entry.delete(0, 'end')
            self.proj_name_entry.insert(0, f"{filename}_proxy")
            if not self.orig_name_entry.get():
                self.orig_name_entry.insert(0, f"{filename}_orig")

    def generate(self):
        project_folder = self.proj_name_entry.get().strip()
        proxy_name = self.proxy_name_entry.get().strip()
        orig_name = self.orig_name_entry.get().strip()

        if not self.dll_path or not proxy_name or not orig_name or not project_folder:
            messagebox.showwarning("⚠️ Missing Info", "Please select a DLL and fill all fields.")
            return

        try:
            pe = pefile.PE(self.dll_path)
            base_dir = os.path.join(os.path.dirname(self.dll_path), project_folder)
            src_dir = os.path.join(base_dir, "src")
            os.makedirs(src_dir, exist_ok=True)

            with open(os.path.join(base_dir, "Forwarded.def"), "w") as f:
                f.write("EXPORTS\n")
                if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
                    for export in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                        if export.name:
                            name = export.name.decode()
                            f.write(f"  {name}={orig_name}.{name} @{export.ordinal}\n")

            with open(os.path.join(base_dir, "Cargo.toml"), "w") as f:
                f.write(f'[package]\nname = "{proxy_name}"\nversion = "0.1.0"\nedition = "2021"\n\n[lib]\nname = "{proxy_name}"\ncrate-type = ["cdylib"]\n')

            with open(os.path.join(base_dir, "build.rs"), "w") as f:
                f.write('fn main() {\n    println!("cargo:rustc-link-arg=/DEF:Forwarded.def");\n}')

            with open(os.path.join(src_dir, "lib.rs"), "w") as f:
                f.write("// by seif\n")

            with open(os.path.join(base_dir, "build.bat"), "w") as f:
                bat_content = f"""@echo off
setlocal
echo ========================================================
echo Checking for Rust/Cargo installation...
echo ========================================================
WHERE cargo >nul 2>nul
IF %ERRORLEVEL% EQU 0 ( goto :Build )
if exist "%USERPROFILE%\\.cargo\\bin\\cargo.exe" (
    set "PATH=%PATH%;%USERPROFILE%\\.cargo\\bin"
    goto :Build
)
echo [ERROR] Rust is NOT installed! Visit https://rustup.rs
pause
exit /b 1
:Build
echo Rust found! Building {proxy_name}.dll...
cd /d "%~dp0"
cargo build --release
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build failed!
    pause
    exit /b 1
)
echo ========================================================
echo SUCCESS! Build complete.
echo Output: "%~dp0target\\release\\{proxy_name}.dll"
echo.
echo Action Required:
echo 1. Rename original "{proxy_name}.dll" to "{orig_name}.dll"
echo 2. Copy the NEW "{proxy_name}.dll" to the same folder.
echo ========================================================
pause"""
                f.write(bat_content)

            self.status_label.configure(text="✅ Status: Project Generated Successfully!", text_color=self.success_color)
            messagebox.showinfo("✅ Done", f"Project generated at:\n{base_dir}")

        except Exception as e:
            self.status_label.configure(text="❌ Status: Error Occurred", text_color=self.error_color)
            messagebox.showerror("❌ Error", str(e))

if __name__ == "__main__":
    app = RustProxyGenerator()
    app.mainloop()