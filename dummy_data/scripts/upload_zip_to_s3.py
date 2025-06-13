import logging
from pathlib import Path

import boto3


def upload_latest_7z_to_s3(
    directory: str = "dummy_data/7z/",
    bucket_name: str = "mojap-land-dev",
    s3_prefix: str = "cps_dummy/",
):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    logger.info("Starting S3 upload script...")

    # Get all .7z files and sort by modification time
    files = sorted(
        Path(directory).glob("*.7z"), key=lambda f: f.stat().st_mtime, reverse=True
    )

    if not files:
        logger.error("❌ No .7z files found in the directory.")
        return False

    latest_file = files[0]
    logger.info(f"✅ Latest .7z file found: {latest_file}")

    s3_key = f"{s3_prefix}{latest_file.name}"
    s3 = boto3.client("s3")

    try:
        s3.upload_file(
            Filename=str(latest_file),
            Bucket=bucket_name,
            Key=s3_key,
        )
        logger.info(
            f" ✅ File {latest_file} successfully uploaded to s3://{bucket_name}/{s3_key}"
        )
        return True
    except Exception as e:
        logger.error(f"❌ Failed to upload file: {e}")
        return False


if __name__ == "__main__":
    upload_latest_7z_to_s3()
