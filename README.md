
# Rust DLL Proxy Generator

A lightweight yet powerful tool designed to automate the creation of DLL Proxy projects using Rust. This tool removes the manual complexity of building proxy DLLs by automatically extracting exports and generating a fully functional Rust project ready for compilation.


---

🚀 Overview

Creating a DLL Proxy manually is often tedious and error-prone, especially when dealing with large export tables. This tool simplifies the entire workflow by:

Parsing the target DLL

Extracting all exported functions

Generating a complete Rust project

Setting up forwarding automatically


The result is a ready-to-build proxy DLL that can intercept and forward function calls seamlessly.


---

✨ Features

Automated Project Generation
Generates a complete Rust project structure (Cargo.toml, src/, etc.)

Export Extraction
Parses the target DLL and generates a .def file based on its export table

Build Integration
Includes a build.rs script to properly pass linker arguments

Simple GUI
Easy-to-use interface for selecting DLLs and configuring project details

Architecture Detection
Automatically supports both x86 and x64 binaries

Safe by Design
The original DLL is never modified — only read for export extraction



---

⚙️ How It Works

1. Select Target DLL
Choose the original DLL (e.g., steam_api64.dll)


2. Configure 

Project Name

Proxy DLL Name

Original DLL Name (renamed version)



3. Generate Project
The tool creates a fully structured Rust project ready to build




---
```

📁 Generated Project Structure

your_generated_proxy/
│
├── src/
│   └── lib.rs        # Main proxy logic (editable)
│
├── Forwarded.def     # Export forwarding definitions
├── Cargo.toml        # Rust project configuration
├── build.rs          # Linker integration script

```
---

🔧 Build Instructions
```
cd your_generated_proxy
cargo build --release
```
Or simply run:
```
build.bat
```
> ⚠️ Requires Rust (cargo) and MSVC Build Tools installed




---

🧠 Core Concepts

1. Export Extraction Logic

The tool parses the Portable Executable (PE) structure of the DLL and extracts:

Function Names

Ordinals

Entry Points


This ensures full compatibility with the original DLL, even for edge cases.


---

2. Automatic Function Forwarding

Each exported function is mapped inside the .def file using:

FunctionName=OriginalDllName.FunctionName

This allows:

The proxy DLL to load first

Execution of custom logic (e.g., inside DllMain)

Seamless forwarding to the original DLL



---

3. Rust Build Integration

The generated build.rs ensures proper linking:
```
fn main() {
    println!("cargo:rustc-link-arg=/DEF:Forwarded.def");
}
```
This bridges Rust with the Windows linker (link.exe) and enables automatic export forwarding without manual configuration.


---

💡 Why Use This Tool?

Speed
Avoid writing hundreds of export forwarding lines manually

Automation
One-click generation instead of a multi-step manual process

Rust Power
Use a modern, memory-safe language for low-level Windows internals

Flexibility
Easily inject custom logic into src/lib.rs



---

🧩 Use Cases

DLL Proxying / DLL Hijacking

Game Modding & Injection

Reverse Engineering

API Monitoring & Debugging



---

⚠️ Troubleshooting

Architecture Mismatch
Ensure Rust target matches the DLL (x64 or x86)

Missing Dependencies
Install MSVC Build Tools (required for linking)

Permission Issues
Make sure you have access if working inside protected folders



---

⚖️ Disclaimer

This project is intended for educational and research purposes only.
Always respect software licenses and use responsibly.


---
Final Note

This tool is designed to eliminate repetitive low-level work and let you focus on what actually matters:
analysis, hooking, and custom logic.


---
