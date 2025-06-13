import logging
import os
from datetime import datetime
from typing import Optional

import py7zr


def get_archive_name(
    archive_prefix: Optional[str], timestamp: str, password: Optional[str]
) -> str:
    """
    Construct the final archive name with optional prefix.

    Args:
        archive_prefix (Optional[str]): Custom prefix for the archive.
        timestamp (str): Timestamp string.
        password (Optional[str]): If present, will prefix with "corrupt_".

    Returns:
        str: Final archive filename.
    """

    base_name = "dummy_data"

    if not get_archive_name:
        logging.info("No archive prefix provided, using default name.")
        return f"{base_name}_{timestamp}.7z"

    elif archive_prefix:
        logging.info(f"Using provided archive prefix: {archive_prefix}")
        return f"{archive_prefix}_{base_name}_{timestamp}.7z"


def zip_folder(
    source_dir: str,
    output_dir: str = "dummy_data/7z",
    password: Optional[str] = None,
    archive_prefix: Optional[str] = None,
) -> str:
    """
    Compress a folder into a .7z archive with a timestamped name.

    Args:
        source_dir (str): Folder to compress.
        output_dir (str): Where to save the archive.
        password (Optional[str]): Password for encryption.
        archive_name (Optional[str]): Custom name for archive (without extension).

    Returns:
        str: Path to the created archive.
    """
    logging.info("Starting folder compression...")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_name = get_archive_name(archive_prefix, timestamp, password)
    output_path = os.path.join(output_dir, final_name)

    logging.info(f"Creating archive: {output_path}")
    with py7zr.SevenZipFile(output_path, mode="w", password=password) as archive:
        archive.writeall(path=source_dir, arcname="dummy")

    logging.info(f"Archive created successfully: {output_path}")
    return output_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    success_path = zip_folder(source_dir="dummy_data/raw_data", archive_prefix="clean")

    wrong_password = zip_folder(
        source_dir="dummy_data/raw_data",
        password="junk123",
        archive_prefix="wrong_password",
    )

    logging.info("Archives created at:\n- %s\n- %s", success_path, wrong_password)
