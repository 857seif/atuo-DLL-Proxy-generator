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