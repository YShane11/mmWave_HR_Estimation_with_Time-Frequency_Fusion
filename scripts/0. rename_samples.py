from pathlib import Path

# ===== 指定多個目標資料夾 =====
target_dirs = [
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/AWR_steady/raw/ECG"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/AWR_steady/raw/mmWave"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/AWR_unsteady/raw/ECG"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/AWR_unsteady/raw/mmWave"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/IWR_steady/raw/ECG_polarH10"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/IWR_steady/raw/mmWave"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/IWR_unsteady/raw/ECG"),
    Path(r"D:/mmwave-heart-rate-monitoring-demo/data/IWR_unsteady/raw/mmWave"),
]

for target_dir in target_dirs:
    if not target_dir.exists():
        print(f"[跳過] 資料夾不存在: {target_dir}")
        continue

    # 抓目前這一層的所有項目（檔案 + 資料夾），依名稱排序
    items = sorted(target_dir.iterdir(), key=lambda p: p.name)

    if not items:
        print(f"[跳過] 沒有項目: {target_dir}")
        continue

    # ===== 第一階段：先改成暫時名稱，避免撞名 =====
    temp_items = []
    for i, item in enumerate(items):
        if item.is_file():
            temp_path = target_dir / f"__temp_rename_{i}__{item.suffix}"
        else:
            temp_path = target_dir / f"__temp_rename_{i}__"

        item.rename(temp_path)
        temp_items.append(temp_path)

    # ===== 第二階段：改成 sample_0, sample_1, ... =====
    for i, temp_path in enumerate(temp_items):
        if temp_path.is_file():
            new_path = target_dir / f"sample_{i}{temp_path.suffix}"
        else:
            new_path = target_dir / f"sample_{i}"

        temp_path.rename(new_path)

    print(f"[完成] {target_dir} 已重新命名 {len(items)} 個項目")