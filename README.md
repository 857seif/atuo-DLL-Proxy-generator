

---

atuo-DLL-Proxy-generator

🦀 Rust DLL Proxy Generator

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

📁 Generated Project Structure
```
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
```
Ordinals
```
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

🔬 Advanced Usage

🔹 Inject Custom Logic
```
Modify src/lib.rs to execute your own code before forwarding:

Logging function calls

Hooking specific APIs

Initializing overlays or tools

Runtime patching

```

---

🔹 Selective Hooking

Instead of forwarding everything blindly, you can:

Intercept specific functions

Override their behavior

Forward only when needed



---

🔹 Chaining Proxies
```
App → Proxy1 → Proxy2 → Original DLL
```
Useful for:

Layered debugging

Multi-stage injection systems

Complex analysis workflows



---

🧪 Real-World Workflow

1. Generate proxy from target DLL


2. Rename original DLL (e.g., original.dll)


3. Place proxy DLL with original name


4. Launch target application


5. Execute custom logic automatically




---
Safety & Design Philosophy

Non-destructive → Never modifies the original DLL

Transparent → Maintains full compatibility

Lightweight → Fast generation process

Developer-focused → Full control without limitations



---

⚡ Performance
```
.def forwarding is handled by the Windows loader → extremely fast
```
No overhead unless you add custom logic

Scales well even with large export tables



---

🧠 Technical Deep Dive

🔹 Why .def?
```
Prevents name mangling issues

Preserves ordinals

Ensures exact export matching

Cleaner than manual pragma exports
```


---

🔹 PE Parsing

The tool reads:

DOS Header

NT Headers

Export Directory


This guarantees accurate extraction without external tools.


---

🔹 Linker Automation

Handled via build.rs, which:

Injects linker arguments

Connects .def with Rust build system

Eliminates manual configuration



---

🧩 Use Cases

```
DLL Proxying / DLL Hijacking

Game Modding & Injection

Reverse Engineering

API Monitoring & Debugging

```

---

🧩 Extensibility Ideas

Plugin system for hooks

Auto hook templates (logging/tracing)

Export filtering (partial proxy generation)

Debugger integration (x64dbg / WinDbg)

GUI enhancements (preview exports, drag & drop)



---

📌 Future Improvements

Better error handling for malformed PE files

Export viewer inside GUI

One-click build & inject

Cross-platform analysis support

Advanced research integrations



---

⚠️ Troubleshooting

Architecture Mismatch
Ensure Rust target matches the DLL (x64 or x86)

Missing Dependencies
Install MSVC Build Tools

Permission Issues
Ensure access to protected directories



---

🤝 Contributing

Contributions are welcome!

Improve parsing logic

Enhance GUI

Add features

Fix edge cases



---

Disclaimer

This project is intended for educational and research purposes only.
Always respect software licenses and use responsibly.


---
Final Note

This tool is designed to eliminate repetitive low-level work and let you focus on what actually matters:

analysis, hooking, and custom logic.


---
