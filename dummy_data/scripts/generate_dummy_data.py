# data_generator.py

import logging
import random
import typing as t
from pathlib import Path

import pandas as pd
from faker import Faker

logging.basicConfig(level=logging.INFO)

faker = Faker("en_GB")  # For UK-style city names


# Common data generator
def generate_data(num_rows: int = 100) -> t.Dict[str, t.List]:
    months = (
        pd.date_range("2023-01-01", "2025-12-01", freq="MS").strftime("%B %Y").tolist()
    )
    return {
        "Month": random.choices(months, k=num_rows),
        "Year": [random.randint(2023, 2025) for _ in range(num_rows)],
        "ID": [random.randint(1000, 9999) for _ in range(num_rows)],
        "Offence": random.choices(
            ["Theft", "Assault", "Fraud", "Burglary", "Drug Offense"], k=num_rows
        ),
        "Area": [faker.city() for _ in range(num_rows)],
        "CourtType": random.choices(["Crown Court", "Magistrates' Court"], k=num_rows),
        "Outcome": random.choices(
            [
                "Guilty",
                "Not Guilty",
                "Dismissed",
                "Sentenced",
                "Community Service",
                "Fine",
            ],
            k=num_rows,
        ),
        "Gender": random.choices(["Male", "Female"], k=num_rows),
        "Age": [random.randint(18, 80) for _ in range(num_rows)],
        "Ethnicity": random.choices(
            ["White", "Black", "Asian", "Mixed", "Other"], k=num_rows
        ),
    }


casetype_map = {
    "post_charge": ["Criminal", "Civil"],
    "postcharge_cfs": ["Family", "Housing", "Immigration"],
    "pre_charge": ["Traffic", "Environmental", "Public Order", "Health and Safety"],
}

charge_type_fixed = {
    "post_charge": "postcharge",
    "postcharge_cfs": "postcharge_cfs",
    "pre_charge": "pre_charge",
}


def generate_dataset(dataset_key: str, num_rows: int) -> pd.DataFrame:
    logging.info(f"Generating dataset for {dataset_key} with {num_rows} rows")
    data = generate_data(num_rows)
    data["Casetype"] = random.choices(casetype_map[dataset_key], k=num_rows)
    if dataset_key in charge_type_fixed:
        data["ChargeType"] = [charge_type_fixed[dataset_key]] * num_rows
    return pd.DataFrame(data)


def save_datasets(output_dir: Path, num_rows: int = 100):
    logging.info("Creating output directory for dummy datasets")
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Generating dummy datasets with {num_rows} rows each")
    post_charge_data = generate_dataset("post_charge", num_rows)
    postcharge_cfs_data = generate_dataset("postcharge_cfs", num_rows)
    pre_charge_data = generate_dataset("pre_charge", num_rows)

    logging.info("Saving datasets to CSV files")
    post_charge_data.to_csv(output_dir / "post_charge_data.csv", index=False)
    postcharge_cfs_data.to_csv(output_dir / "postcharge_cfs_data.csv", index=False)
    pre_charge_data.to_csv(output_dir / "pre_charge_data.csv", index=False)

    logging.info(f"Dummy datasets created and saved successfully at {output_dir}")


# Optional: allow this to run as a standalone script too
if __name__ == "__main__":
    save_datasets(Path("dummy_data/raw_data"))
