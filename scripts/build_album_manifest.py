#!/usr/bin/env python3
"""Quét album-media/<chuong>/ và cập nhật data/media.json cho trang album.html.

Chương nào trong album-media/ còn trống (chỉ có .gitkeep) sẽ được GIỮ NGUYÊN
trong media.json (không đụng tới mock data hiện có). Chương nào có ảnh/video
thật sẽ được build lại từ đầu từ nội dung trong folder đó.

Chạy: python3 scripts/build_album_manifest.py
"""
import json
import shutil
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
MEDIA_SRC = ROOT / "album-media"
IMAGES_OUT = ROOT / "images" / "chapters"
VIDEOS_OUT = ROOT / "videos"
MANIFEST = ROOT / "data" / "media.json"

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".heic", ".heif"}
VIDEO_EXT = {".mp4", ".mov", ".m4v"}

# (ten folder trong album-media/, id chuong, ten hien thi)
CHAPTERS = [
    ("1-ngoai-canh", "ngoai-canh", "Ngoại cảnh"),
    ("2-dinh-hon", "dinh-hon", "Đính hôn"),
    ("3-vu-quy", "vu-quy", "Vu quy"),
    ("4-tan-hon", "tan-hon", "Tân hôn"),
    ("5-nha-hang", "nha-hang", "Nhà hàng"),
    ("10-photobooth-18-10", "photobooth-18-10", "Photobooth 18/10"),
    ("12-photobooth-31-10", "photobooth-31-10", "Photobooth 31/10"),
    ("7-bao-hy", "bao-hy", "Báo hỷ"),
    ("6-hau-truong", "hau-truong", "Hậu trường"),
    ("8-video", "video", "Video"),
    ("11-chua-xac-dinh", "chua-xac-dinh", "Chưa xác định sau"),
]

MAX_EDGE = 2000
QUALITY = 82


def list_source_files(folder: Path):
    files = [
        f for f in sorted(folder.iterdir())
        if f.is_file() and not f.name.startswith(".")
    ]
    return files


def process_image(src: Path, dst: Path):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > MAX_EDGE:
            scale = MAX_EDGE / max(w, h)
            im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        dst.parent.mkdir(parents=True, exist_ok=True)
        im.save(dst, "JPEG", quality=QUALITY)


def build_chapter_items(folder_name, chapter_id, existing_by_source):
    folder = MEDIA_SRC / folder_name
    files = list_source_files(folder) if folder.is_dir() else []
    if not files:
        return None  # chương trống -> không đụng tới, giữ nguyên mock/data cũ

    items = []
    img_i = 0
    for f in files:
        ext = f.suffix.lower()
        prev = existing_by_source.get(f.name, {})
        if ext in IMAGE_EXT:
            img_i += 1
            out_name = f"{img_i:02d}.jpg"
            out_path = IMAGES_OUT / chapter_id / out_name
            process_image(f, out_path)
            items.append({
                "type": "image",
                "src": f"images/chapters/{chapter_id}/{out_name}",
                "caption": prev.get("caption", ""),
                "sourceFile": f.name,
            })
        elif ext in VIDEO_EXT:
            out_dir = VIDEOS_OUT / chapter_id
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f.name
            shutil.copy2(f, out_path)
            items.append({
                "type": "video",
                "src": f"videos/{chapter_id}/{f.name}",
                "caption": prev.get("caption", ""),
                "sourceFile": f.name,
            })
        else:
            print(f"  (bỏ qua, không nhận diện được loại file: {f.name})")
    return items


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"chapters": []}
    existing_chapters = {c["id"]: c for c in manifest.get("chapters", [])}

    new_chapters = []
    for folder_name, chapter_id, title in CHAPTERS:
        existing = existing_chapters.get(chapter_id, {})
        existing_by_source = {
            item.get("sourceFile"): item
            for item in existing.get("items", [])
            if item.get("sourceFile")
        }
        items = build_chapter_items(folder_name, chapter_id, existing_by_source)
        if items is None:
            if existing:
                print(f"- {title}: trống trong album-media/, giữ nguyên {len(existing.get('items', []))} mục cũ.")
                new_chapters.append(existing)
            else:
                print(f"- {title}: trống, chưa có dữ liệu cũ, bỏ qua.")
            continue

        cover = existing.get("cover")
        cover_still_valid = any(it["src"] == cover for it in items)
        new_chapters.append({
            "id": chapter_id,
            "title": title,
            "cover": cover if cover_still_valid else (items[0]["src"] if items else None),
            "items": items,
        })
        print(f"- {title}: build lại {len(items)} mục từ album-media/{folder_name}/")

    manifest["chapters"] = new_chapters
    manifest.pop("note", None)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nĐã cập nhật {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
