from pathlib import Path
import shutil

from tqdm import tqdm


def main():
    root_dir = Path("/data/yangming/datasets/scannet_v2")

    exts = [
        "_vh_clean_2.ply",
        "_vh_clean_2.labels.ply",
        "_vh_clean_2.0.010000.segs.json",
        ".aggregation.json",
    ]

    for split in ["train", "val"]:
        print("split:", split)
        with open(f"scannetv2_{split}.txt") as f:
            scan_ids = f.readlines()

        for scan_id in tqdm(scan_ids):
            scan_id = scan_id.strip()
            for ext in exts:
                file_name = scan_id + ext
                shutil.copy(root_dir / "scans"/ scan_id / file_name, Path(split) / file_name)


if __name__ == "__main__":
    main()
