# MarkItDown - Universal Document Converter

## 📖 Overview

MarkItDown is a powerful OOMOL workflow package that transforms various document formats into clean, readable Markdown text. Whether you're dealing with PDFs, Word documents, PowerPoint presentations, Excel files, images, or even audio files, MarkItDown can convert them into structured Markdown format that's easy to read, edit, and process.

## 🎯 What Can You Do With MarkItDown?

### Document Types Supported
- **PDF Documents** - Convert research papers, reports, and books
- **Microsoft Office Files** - Word documents (.docx), PowerPoint slides (.pptx), Excel sheets (.xlsx)
- **Images** - Extract text from screenshots, scanned documents, and photos
- **Audio Files** - Transcribe audio content to text
- And many more formats supported by Microsoft's MarkItDown library

### Perfect For
- **Content Creators** - Convert presentations and documents for blog posts
- **Researchers** - Extract text from academic papers for analysis
- **Business Users** - Transform reports and presentations into shareable formats
- **Students** - Convert lecture materials and reading assignments
- **Anyone** who needs to work with text from various document formats

## 🧩 Available Blocks

### MarkItDown Converter Block
**What it does:** The core conversion engine that transforms your files into Markdown

**Features:**
- **Smart File Processing** - Automatically detects and processes different file types
- **Plugin Support** - Enhanced processing capabilities through plugins
- **AI Enhancement** - Uses language models for improved text extraction and formatting
- **Flexible Model Selection** - Choose from various AI models for optimal results

**Input Options:**
- Select any supported file from your computer
- Enable or disable plugin processing
- Choose whether to use AI enhancement
- Select your preferred language model (default: Kimi K2)

**Outputs:**
- Clean Markdown text content
- Success/failure status
- Error messages (if any issues occur)

## 🚀 How to Use

### Basic Workflow
1. **Add the MarkItDown Converter block** to your OOMOL workflow
2. **Select your input file** using the file picker
3. **Configure options** (plugins, AI enhancement, model selection)
4. **Connect a preview block** to see your converted Markdown
5. **Run the workflow** to get your converted content

### Configuration Options

#### File Input
Simply click the file selector and choose any supported document from your computer.

#### Plugin Processing
- **Enabled** (Default): Uses specialized plugins for better format handling
- **Disabled**: Basic conversion without additional processing

#### AI Enhancement
- **Enabled** (Default): Uses artificial intelligence for improved text extraction
- **Disabled**: Standard conversion without AI assistance

#### Model Selection
Choose from available language models:
- **Kimi K2** (Default): Balanced performance and accuracy
- **Other models**: Available based on your OOMOL setup

## 💡 Example Use Cases

### 1. Content Repurposing
Convert your PowerPoint presentation into a Markdown blog post:
- Input: `presentation.pptx`
- Output: Structured Markdown with headings and content
- Use for: Website content, documentation, articles

### 2. Research Document Processing
Extract text from academic papers:
- Input: `research_paper.pdf`
- Output: Clean text for analysis or summarization
- Use for: Literature reviews, note-taking, content analysis

### 3. Image Text Extraction
Get text from screenshots or scanned documents:
- Input: `screenshot.png` or `scanned_doc.jpg`
- Output: Extracted and formatted text
- Use for: Digitizing printed materials, processing screenshots

### 4. Audio Transcription
Convert spoken content to written text:
- Input: `meeting_recording.mp3`
- Output: Transcribed text in Markdown format
- Use for: Meeting notes, interview transcripts, content creation

## 🔧 Technical Details

### System Requirements
- Python 3.10 or higher (up to 3.12)
- OOMOL platform environment
- Internet connection (for AI-enhanced processing)

### Dependencies
- Microsoft MarkItDown library (v0.14.0+)
- OpenAI API (for AI enhancement)
- Additional plugins for enhanced format support

## 🤝 Getting Started

1. **Install** the MarkItDown package in your OOMOL environment
2. **Create a new workflow** or add to an existing one
3. **Drag the MarkItDown Converter block** onto your canvas
4. **Connect input and output blocks** as needed
5. **Configure your settings** and run your first conversion

## 📊 Output Quality

The quality of conversion depends on:
- **Source file quality** - Higher quality inputs produce better results
- **AI enhancement settings** - Enable for more accurate text extraction
- **Plugin usage** - Enables format-specific optimizations
- **Model selection** - Different models may excel with different content types

## 🆘 Troubleshooting

**File not converting properly?**
- Check if the file format is supported
- Try enabling plugins and AI enhancement
- Ensure the file isn't corrupted or password-protected

**Poor text quality?**
- Enable AI enhancement for better results
- Try a different language model
- Check if the source document has good text quality

## 📈 Version Information

- **Current Version**: 0.0.1
- **Repository**: [GitHub - oomol-flows/markitdown](https://github.com/oomol-flows/markitdown.git)
- **Author**: alwaysmavs

---

*Ready to transform your documents? Install MarkItDown and start converting your files to Markdown today!*