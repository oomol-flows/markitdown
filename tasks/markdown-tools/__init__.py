#region generated meta
import typing
from oocana import LLMModelOptions
class Inputs(typing.TypedDict):
    input_file: str
    enable_plugins: bool | None
    llm_enhanced: bool | None
    llm_model: LLMModelOptions
class Outputs(typing.TypedDict):
    markdown_content: typing.NotRequired[str]
    success: typing.NotRequired[bool]
    error_message: typing.NotRequired[str | None]
#endregion

from oocana import Context
import os
from pathlib import Path

def main(params: Inputs, context: Context) -> Outputs:
    """
    Convert various file formats to Markdown using MarkItDown library

    Args:
        params: Input parameters including file path and options
        context: OOMOL context object

    Returns:
        Dictionary containing converted markdown content and status
    """

    try:
        # Import MarkItDown (will fail if not installed)
        from markitdown import MarkItDown

        # Validate input file
        input_file_path = params["input_file"]
        if not input_file_path or not os.path.exists(input_file_path):
            raise ValueError(f"Input file not found: {input_file_path}")

        # Get file size for validation (optional limit)
        file_size = os.path.getsize(input_file_path)
        max_size_mb = 100  # 100MB limit
        if file_size > max_size_mb * 1024 * 1024:
            raise ValueError(f"File size ({file_size / (1024*1024):.1f}MB) exceeds limit of {max_size_mb}MB")

        # Initialize MarkItDown with optional parameters
        enable_plugins = params.get("enable_plugins", False) or False
        llm_enhanced = params.get("llm_enhanced", False) or False
        llm_model_options = params.get("llm_model")

        # Create MarkItDown instance with LLM integration if requested
        if llm_enhanced and llm_model_options:
            try:
                # Use OpenAI client with OOMOL provided configuration
                from openai import OpenAI

                # Get OOMOL provided base_url and api_key
                base_url = context.oomol_llm_env.get("base_url")
                api_key = context.oomol_llm_env.get("api_key")

                if not api_key:
                    raise ValueError("No API key provided by OOMOL")

                # Create OpenAI client with OOMOL configuration
                openai_client = OpenAI(
                    base_url=base_url,
                    api_key=api_key
                )

                model_name = llm_model_options.get("model", "deepseek-chat")
                md = MarkItDown(
                    llm_client=openai_client,
                    llm_model=model_name,
                    enable_plugins=enable_plugins
                )
                context.preview({
                    "type": "text",
                    "data": f"Using LLM-enhanced conversion with {model_name} model via OOMOL"
                })
            except Exception as llm_error:
                # Fall back to basic mode if LLM setup fails
                context.preview({
                    "type": "text",
                    "data": f"OpenAI client setup failed ({str(llm_error)}), falling back to basic conversion"
                })
                md = MarkItDown(enable_plugins=enable_plugins)
        else:
            md = MarkItDown(enable_plugins=enable_plugins)

        # Convert the file
        result = md.convert(input_file_path)

        if not result or not hasattr(result, 'text_content'):
            raise ValueError("Conversion failed - no content returned")

        markdown_content = result.text_content

        if not markdown_content or markdown_content.strip() == "":
            raise ValueError("Conversion resulted in empty content")

        # Preview the converted markdown (first 1000 characters)
        preview_content = markdown_content[:1000]
        if len(markdown_content) > 1000:
            preview_content += "\n\n... (content truncated for preview)"

        context.preview({
            "type": "markdown",
            "data": preview_content
        })

        # Log conversion success
        file_path = Path(input_file_path)
        print(f"Successfully converted: {file_path.name} ({file_size / 1024:.1f} KB)")

        return {
            "markdown_content": markdown_content,
            "success": True,
            "error_message": None
        }

    except ImportError as e:
        error_msg = "MarkItDown library not installed. Please install with: pip install 'markitdown[all]'"
        print(f"Import error: {error_msg}")
        raise ValueError(error_msg)

    except Exception as e:
        error_msg = f"Conversion failed: {str(e)}"
        print(f"Conversion error: {error_msg}")
        raise ValueError(error_msg)