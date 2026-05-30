"""
Build Text2LLM as a standalone Windows executable
"""
import PyInstaller.__main__
import os
import sys

print("=" * 70)
print("Building Text2LLM Executable")
print("=" * 70)

APP_NAME = "Text2LLM"
VERSION = "2.0"
ICON = "icon.ico" 

# Check if icon exists
if not os.path.exists(ICON):
    print(f"⚠️  No icon found. Building without icon.")
    icon_param = []
else:
    icon_param = [f'--icon={ICON}']
    print(f"✅  Using icon: {ICON}")

print(f"\n🔨 Building {APP_NAME} v{VERSION}...")
print("   This will take 3-5 minutes...\n")

# Build configuration
build_params = [
    'main_launcher.py',                    # Entry point
    f'--name={APP_NAME}',                  # Executable name
    '--onefile',                           # Single .exe file
    '--windowed',                          # No console window
    '--clean',                             # Clean build
    '--noconfirm',                         # Don't ask for confirmation
    
    # Add Python files as data
    '--add-data=setup_wizard.py;.',
    '--add-data=book_rag_gui.py;.',
    '--add-data=ollama_book_rag.py;.',
    
    # Hidden imports (modules not auto-detected)
    '--hidden-import=tkinter',
    '--hidden-import=tkinter.ttk',
    '--hidden-import=tkinter.filedialog',
    '--hidden-import=tkinter.scrolledtext',
    '--hidden-import=tkinter.messagebox',
    '--hidden-import=PIL',
    '--hidden-import=PIL.Image',
    '--hidden-import=numpy',
    '--hidden-import=PyPDF2',
    '--hidden-import=requests',
    '--hidden-import=pickle',
    '--hidden-import=threading',
    '--hidden-import=pathlib',
    '--hidden-import=datetime',
    '--hidden-import=hashlib',
    '--hidden-import=json',
    '--hidden-import=time',
    '--hidden-import=re',
    
    # Collect all submodules
    '--collect-all=tkinter',
    '--collect-all=PyPDF2',
    
    # Don't use UPX compression (more compatible)
    '--noupx',
] + icon_param

# Run PyInstaller
try:
    print("📦 Running PyInstaller...\n")
    PyInstaller.__main__.run(build_params)
    
    print("\n" + "=" * 70)
    print("✅ BUILD COMPLETE!")
    print("=" * 70)
    
    exe_path = f"dist/{APP_NAME}.exe"
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"\n📍 Location: {exe_path}")
        print(f"📊 Size: {size_mb:.1f} MB")
    
    print("\n✨ Enhanced Features:")
    print("   🧠 Chain-of-Thought Reasoning")
    print("   📊 Confidence Scoring")
    print("   💬 Multi-Turn Conversations")
    print("   ⚡ llama3.2:3b Model Support")
    
    print("\n📦 Package Details:")
    print("   • Single executable file")
    print("   • No Python installation needed")
    print("   • Double-click to run")
    print("   • Works on any Windows 10/11 PC")
    print("   • Requires Ollama (auto-setup wizard)")
    
    print("\n🧪 To test:")
    print(f"   cd dist")
    print(f"   {APP_NAME}.exe")
    
    print("\n📤 To distribute:")
    print(f"   1. Share: dist/{APP_NAME}.exe")
    print(f"   2. Users need: Ollama with llama3.2:3b")
    print(f"   3. Setup wizard handles installation")
    
    print("\n📋 Requirements for users:")
    print("   • Windows 10/11")
    print("   • 8GB RAM (16GB recommended)")
    print("   • 6GB disk space")
    print("   • Internet (for initial Ollama setup)")
    
    print("\n💡 Pro tip:")
    print("   Create a README.txt with installation instructions:")
    print("   1. Download Text2LLM.exe")
    print("   2. Double-click to run")
    print("   3. Follow setup wizard")
    print("   4. Install Ollama when prompted")
    print("   5. Wait for models to download (~2.5 GB)")
    print("   6. Start using Text2LLM!")
    
    print("=" * 70 + "\n")
    
    # Create a simple README
    readme_path = "dist/README.txt"
    try:
        with open(readme_path, 'w') as f:
            f.write(f"""Text2LLM v{VERSION}
{'=' * 50}

AI-Powered Book Assistant with Advanced Features

WHAT'S NEW IN v2.0:
  🧠 Chain-of-Thought Reasoning - See how AI thinks
  📊 Confidence Scoring - Know when to trust answers
  💬 Multi-Turn Conversations - Natural follow-ups
  ⚡ llama3.2:3b Model - Responses

INSTALLATION:
1. Double-click Text2LLM.exe
2. Follow the setup wizard
3. Install Ollama when prompted (free, from ollama.com)
4. Wait for AI models to download (~2.5 GB)
5. Start using Text2LLM!

SYSTEM REQUIREMENTS:
- Windows 10 or Windows 11
- 8GB RAM minimum (16GB recommended)
- 6GB free disk space
- Internet connection (for setup only)

FEATURES:
✓ Upload any PDF book or document
✓ Ask questions in plain English
✓ Get answers with reasoning and confidence
✓ Natural follow-up questions
✓ 100% private - works offline after setup
✓ No data leaves your computer

USAGE:
1. Click "Load PDF Book"
2. Select your PDF file
3. Wait for indexing (first time only, 10-15 min)
4. Ask questions!

PERFORMANCE:
- First query: 40-60 seconds (loading model)
- Subsequent queries: 40-60 seconds
- Indexing: 10-15 minutes per book (one-time)
- Cache: Permanent (books never re-indexed)

TROUBLESHOOTING:
- If Ollama error: Install from https://ollama.com
- If model error: Run "ollama pull llama3.2:3b"
- If slow: Close other applications, need 8GB+ RAM
- Clear cache: Tools → Clear Cache

PRIVACY:
- 100% local processing
- No internet after setup
- No data collection
- No tracking

SUPPORT:
- Issues: Check Tools → Cache Location
- Models: Run "ollama list" to verify
- Cache: Located in AppData\\Roaming\\Text2LLM

© 2025 Text2LLM Enhanced
""")
        print(f"✅ Created README: {readme_path}\n")
    except Exception as e:
        print(f"⚠️  Could not create README: {e}\n")

except Exception as e:
    print("\n" + "=" * 70)
    print("❌ BUILD FAILED!")
    print("=" * 70)
    print(f"Error: {e}")
    print("\nCommon issues:")
    print("  • PyInstaller not installed: pip install pyinstaller")
    print("  • Missing dependencies: pip install -r requirements.txt")
    print("  • File in use: Close Text2LLM and try again")
    print("=" * 70 + "\n")
    sys.exit(1)
