# album-media — nguồn ảnh/video cho trang Album

Thả ảnh/video đã chọn vào đúng folder chương dưới đây. Tên file không quan trọng, cứ copy nguyên tên gốc — khi dựng trang sẽ xử lý (resize, đặt thứ tự) dựa trên thứ tự file trong mỗi folder (có thể đổi lại bằng Admin sau).

| Folder | Chương |
|---|---|
| `1-ngoai-canh/` | Ngoại cảnh |
| `2-dinh-hon/` | Đính hôn |
| `3-vu-quy/` | Vu quy |
| `4-tan-hon/` | Tân hôn |
| `5-hoa-binh-2/` | Hoà Bình 2 |
| `6-photobooth-18-10/` | Photobooth 18/10 |
| `7-bach-viet/` | Bách Việt |
| `8-photobooth-31-10/` | Photobooth 31/10 |
| `9-video/` | Video |
| `10-hau-truong/` | Hậu trường |

Thứ tự folder ở trên = thứ tự chương hiển thị trên trang (do danh sách `CHAPTERS` trong `scripts/build_album_manifest.py` quyết định, không phải do tên folder).

Video (clip) cứ thả thẳng vào folder chương tương ứng cùng với ảnh — trang sẽ tự nhận diện theo phần mở rộng file (`.jpg/.png` vs `.mp4/.mov`).

### `11-chua-xac-dinh/` — folder nội bộ, KHÔNG hiển thị trên web

Folder này vẫn còn 30 ảnh để chủ nhân tự tham khảo/điều chỉnh sau, nhưng không nằm trong danh sách `CHAPTERS` của script nên sẽ không bao giờ được build lên trang. Khi đã quyết định ảnh nào dùng, chuyển ảnh đó sang chương phù hợp rồi chạy lại script.

## Lịch sử xử lý ảnh ngày 18/10

Ảnh thô gốc từ photographer (`Hinh dam cuoi 18:10/`, `Photobooth 18:10/` ở thư mục gốc repo, KHÔNG commit vì quá nặng ~5GB) ban đầu được phân loại tự động theo giờ chụp EXIF vào 1 chương "Gia tiên" tạm thời. User đã tự review toàn bộ, gộp "Gia tiên" vào `4-tan-hon/` (xoá chương Gia tiên vì dư thừa), bớt/thêm lại ảnh giữa các chương, và đưa ảnh chưa chắc chắn vào `11-chua-xac-dinh/` — số lượng file trong mỗi folder hiện tại là kết quả cuối sau khi user tự sắp xếp, không còn khớp với số liệu phân loại tự động ban đầu nữa.

## Đổi tên & sắp xếp lại thứ tự (vòng sau)

"Nhà hàng" đổi tên thành "Hoà Bình 2" (folder `5-nha-hang/` → `5-hoa-binh-2/`), "Báo hỷ" đổi tên thành "Bách Việt" (folder `7-bao-hy/` → `7-bach-viet/`). Thứ tự chương trên trang cũng được sắp lại theo yêu cầu: Ngoại cảnh → Đính hôn → Vu quy → Tân hôn → Hoà Bình 2 → Photobooth 18/10 → Bách Việt → Photobooth 31/10 → Video → Hậu trường.
