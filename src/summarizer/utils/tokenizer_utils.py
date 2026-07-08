from typing import List
from ensure import ensure_annotations
from transformers import AutoTokenizer, PreTrainedTokenizerBase


@ensure_annotations
def load_tokenizer(model_name: str) -> PreTrainedTokenizerBase:
    """
    Load a Hugging Face tokenizer.

    Args:
        model_name (str): Hugging Face model name.

    Returns:
        PreTrainedTokenizerBase: Loaded tokenizer.
    """

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return tokenizer


@ensure_annotations
def count_tokens(text: str,tokenizer: PreTrainedTokenizerBase) -> int:
    """
    Count the number of tokens in the text.

    Args:
        text (str): Input text.
        tokenizer: Hugging Face tokenizer.

    Returns:
        int: Number of tokens.
    """

    tokens = tokenizer.encode(
        text,
        add_special_tokens=True
    )

    return len(tokens)


@ensure_annotations
def is_text_too_long(text: str,tokenizer: PreTrainedTokenizerBase,max_tokens: int) -> bool:
    """
    Check whether text exceeds the maximum token limit.

    Args:
        text (str): Input text.
        tokenizer: Hugging Face tokenizer.
        max_tokens (int): Maximum allowed tokens.

    Returns:
        bool: True if text exceeds limit.
    """

    return count_tokens(text, tokenizer) > max_tokens


@ensure_annotations
def truncate_text(text: str,tokenizer: PreTrainedTokenizerBase, max_tokens: int) -> str:
    """
    Truncate text to the specified number of tokens.

    Args:
        text (str): Input text.
        tokenizer: Hugging Face tokenizer.
        max_tokens (int): Maximum tokens.

    Returns:
        str: Truncated text.
    """

    tokenized = tokenizer(
        text,
        truncation=True,
        max_length=max_tokens,
        return_tensors=None
    )

    truncated_text = tokenizer.decode(
        tokenized["input_ids"],
        skip_special_tokens=True
    )

    return truncated_text


@ensure_annotations
def split_into_token_chunks(text: str,tokenizer: PreTrainedTokenizerBase, chunk_size: int = 450,overlap: int = 50) -> List[str]:
    """
    Split text into overlapping token chunks.

    Example

        chunk1: tokens 1-450

        chunk2: tokens 401-850

        chunk3: tokens 801-1250

    Args:
        text (str): Input text.
        tokenizer: Hugging Face tokenizer.
        chunk_size (int): Tokens per chunk.
        overlap (int): Overlap between chunks.

    Returns:
        List[str]: List of text chunks.
    """

    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size."
        )

    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunks = []

    step = chunk_size - overlap

    for start in range(0, len(token_ids), step):

        end = start + chunk_size

        chunk_ids = token_ids[start:end]

        chunk_text = tokenizer.decode(
            chunk_ids,
            skip_special_tokens=True
        )

        chunks.append(chunk_text)

        if end >= len(token_ids):
            break

    return chunks


@ensure_annotations
def merge_chunks(chunks: List[str]) -> str:
    """
    Merge multiple text chunks into one string.

    Args:
        chunks (List[str]): List of chunks.

    Returns:
        str: Combined text.
    """

    return "\n\n".join(chunks)