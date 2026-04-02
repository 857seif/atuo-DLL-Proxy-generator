# atuo-DLL-Proxy-generator
Rust DLL Proxy Generator
​A lightweight tool designed to automate the creation of DLL Proxies using the Rust programming language. This tool simplifies the process of generating a proxy project by automatically extracting exports and setting up the necessary build files.
​Features
​Automated Project Generation: Creates a complete Rust project structure (Cargo.toml, src, etc.).
​Export Extraction: Automatically generates the .def file based on the target DLL's export table.
​Build Integration: Includes a build.rs script to handle linker arguments for the proxying process.
​User Interface: A simple GUI for selecting files and configuring project names.
​How It Works
​Select Target: Choose the original DLL (e.g., steam_api64.dll).
​Configure: Set the Project Name, Proxy DLL Name, and the Original DLL Name (the renamed original).
​Generate: Click "Generate Project" to create the source folder.
​Project Structure (Generated)
​Once generated, the output folder will contain:
​src/: Main Rust source files.
​Forwarded.def: Export definitions for forwarding calls.
​Cargo.toml: Project configuration and dependencies.
​build.rs: Build script for linking the .def file.
​Usage
​After generating the project, you can build it using the Rust compiler:
```
cd your_generated_proxy
cargo build --release
```
or you can run the build.bat 
but you should have cargo 😄

Technical Details
​Target Architecture: Automatically detects and generates proxies for x64 and x86 binaries.
​Linker Flags: Utilizes custom linker arguments within build.rs to ensure proper .def file integration.
​Binary Safety: The generator does not modify the original DLL; it only reads the export table to ensure binary integrity.
​Why use this?
​Speed: Skip writing hundreds of pragma comment lines manually.
​Rust Power: Benefit from Rust's safety and modern tooling while performing low-level DLL hijacking or proxying tasks.
​Customization: Easily inject your own logic into the generated src/lib.rs while the proxy handles the rest.

Detailed Component Breakdown
1. Export Extraction Logic
The tool parses the Portable Executable (PE) structure of the target DLL to identify the Export Directory. It extracts:
 * Function Names: For named exports.
 * Ordinals: To maintain compatibility with non-named exports.
 * Entry Points: Ensuring the proxy points to the correct addresses.
2. Automated Module Forwarding
The generated .def file uses the following syntax for every exported function:
FunctionName=OriginalDllName.FunctionName
This tells the Windows Loader to redirect calls to the original DLL (which you should rename according to your configuration) while allowing your proxy DLL to execute its own code first (e.g., in DllMain).
3. Rust Build Script (build.rs) Integration
To bridge the gap between Rust and the Windows Linker, the tool generates a build.rs that includes:
fn main() {
    println!("cargo:rustc-link-arg=/DEF:Forwarded.def");
}

This ensures that the Forwarded.def file is correctly passed to link.exe during the compilation process, enabling seamless proxying without manual linker configuration.
Troubleshooting & Common Issues
 * Architecture Mismatch: Ensure that the Rust target (x86_64-pc-windows-msvc or i686-pc-windows-msvc) matches the architecture of the original DLL.
 * Missing Dependencies: The generated project requires the MSVC Build Tools to be installed, as it relies on the Windows Linker for .def file processing.
 * Privilege Issues: If the target DLL is located in Program Files, ensure the proxying process (and the game/app) has the necessary read/write permissions.

This project is for educational and research purposes only. Use responsibly and respect software licenses.
