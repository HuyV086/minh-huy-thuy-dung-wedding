# album-media — nguồn ảnh/video cho trang Album

Thả ảnh/video đã chọn vào đúng folder chương dưới đây. Tên file không quan trọng, cứ copy nguyên tên gốc — khi dựng trang sẽ xử lý (resize, đặt thứ tự) dựa trên thứ tự file trong mỗi folder (có thể đổi lại bằng Admin sau).

| Folder | Chương |
|---|---|
| `1-ngoai-canh/` | Ngoại cảnh |
| `2-dinh-hon/` | Đính hôn |
| `3-vu-quy/` | Vu quy |
| `9-gia-tien/` | Gia tiên |
| `4-tan-hon/` | Tân hôn |
| `5-nha-hang/` | Nhà hàng |
| `10-photo-booth/` | Photo booth |
| `7-bao-hy/` | Báo hỷ |
| `6-hau-truong/` | Hậu trường |
| `8-video/` | Video |
| `11-chua-xac-dinh/` | Chưa xác định sau |

Video (clip) cứ thả thẳng vào folder chương tương ứng cùng với ảnh — trang sẽ tự nhận diện theo phần mở rộng file (`.jpg/.png` vs `.mp4/.mov`).

## Ảnh ngày 18/10 (Hinh dam cuoi 18:10 + Photobooth 18:10)

Hai folder gốc `Hinh dam cuoi 18:10/` và `Photobooth 18:10/` ở thư mục gốc repo (KHÔNG commit, quá nặng ~5GB) là ảnh thô photographer giao. Đã phân loại + nén theo giờ chụp (EXIF `DateTimeOriginal`) vào các folder trên:

- 05h–06h30 → `6-hau-truong/`
- 06h30–07h30 → `3-vu-quy/`
- 07h30–10h → `9-gia-tien/`
- 10h trở đi → `5-nha-hang/`
- Không đọc được EXIF giờ chụp → `11-chua-xac-dinh/`
- Toàn bộ `Photobooth 18:10/` → `10-photo-booth/` (không chia giờ)

Ranh giới giờ có thể lệch vài ảnh ở mép khung giờ — user sẽ tự review và sắp xếp lại qua Admin, không cần phân loại lại từ ảnh gốc trừ khi có ảnh mới.
