# album-media — nguồn ảnh/video cho trang Album

Thả ảnh/video đã chọn vào đúng folder chương dưới đây. Tên file không quan trọng, cứ copy nguyên tên gốc — khi dựng trang sẽ xử lý (resize, đặt thứ tự) dựa trên thứ tự file trong mỗi folder (có thể đổi lại bằng Admin sau).

| Folder | Chương |
|---|---|
| `1-ngoai-canh/` | Ngoại cảnh |
| `2-dinh-hon/` | Đính hôn |
| `3-vu-quy/` | Vu quy |
| `4-tan-hon/` | Tân hôn |
| `5-nha-hang/` | Nhà hàng |
| `10-photobooth-18-10/` | Photobooth 18/10 |
| `12-photobooth-31-10/` | Photobooth 31/10 |
| `7-bao-hy/` | Báo hỷ |
| `6-hau-truong/` | Hậu trường |
| `8-video/` | Video |
| `11-chua-xac-dinh/` | Chưa xác định sau |

Video (clip) cứ thả thẳng vào folder chương tương ứng cùng với ảnh — trang sẽ tự nhận diện theo phần mở rộng file (`.jpg/.png` vs `.mp4/.mov`).

## Lịch sử xử lý ảnh ngày 18/10

Ảnh thô gốc từ photographer (`Hinh dam cuoi 18:10/`, `Photobooth 18:10/` ở thư mục gốc repo, KHÔNG commit vì quá nặng ~5GB) ban đầu được phân loại tự động theo giờ chụp EXIF vào 1 chương "Gia tiên" tạm thời. User đã tự review toàn bộ, gộp "Gia tiên" vào `4-tan-hon/` (xoá chương Gia tiên vì dư thừa), bớt/thêm lại ảnh giữa các chương, và đưa ảnh chưa chắc chắn vào `11-chua-xac-dinh/` — số lượng file trong mỗi folder hiện tại là kết quả cuối sau khi user tự sắp xếp, không còn khớp với số liệu phân loại tự động ban đầu nữa.
