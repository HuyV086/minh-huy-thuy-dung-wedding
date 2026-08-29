# Wedding Website — Minh Huy & Thuỳ Dung

Trang cưới tĩnh, 1 file, cho đám cưới **Võ Minh Huy & Bùi Việt Thuỳ Dung**, ngày cưới chính **Chủ Nhật 18/10/2026** (9/9 Âm lịch, Bính Ngọ).

## Sự kiện

| Ngày | Sự kiện | Địa điểm |
|---|---|---|
| 18/10/2026, 9h | Lễ Vu Quy / gia tiên | Tư gia, Long Xuyên |
| 18/10/2026, 11h | Tiệc cưới | NH Hoà Bình 2 — Sảnh B, số 8 Lê Hồng Phong, An Giang |
| 31/10/2026, 19h | Tiệc báo hỷ | NH Bách Việt — Sảnh Gold lầu 1, 90 Mạc Đĩnh Chi, Tân Định, Tp.HCM |

Nhà trai: Ông Võ Minh Hùng, Bà Đỗ Thị Kim Liên (Long Xuyên, An Giang).
Nhà gái: Ông Bùi Văn Phiền, Bà Phùng Thị Ánh Loan (Minh Phụng, Tp.HCM).

## Cấu trúc

- `index.html` — toàn bộ trang, không phụ thuộc build tool. Ảnh dùng đường dẫn tương đối tới `images/`, KHÔNG nhúng base64.
- `images/hero.jpg` — ảnh hero (bản hậu kỳ hoàn chỉnh của ảnh bìa album, gốc `IMG_5960_BIA.jpg`).
- `images/album/album-01.jpg` … `album-33.jpg` — toàn bộ 33 ảnh album cưới đã hậu kỳ (nguồn: folder "18.7 HUY MINH VO │ Le Thanh Phuong Bridal_XOG" trong Downloads), resize max 2000px cạnh dài, quality 82, EXIF đã xoay đúng.
- Gallery ("Khoảnh khắc"): masonry layout (CSS `column-count`, responsive 3/2/1 cột), ảnh hiển thị full không crop. Click/tap mở **lightbox riêng của trang** (không phải tab mới) với nút Trước/Sau, đếm số ảnh (`x / 33`), phím mũi tên trái/phải, vuốt trái/phải trên mobile, Esc để đóng. Có chặn nhẹ right-click/kéo-thả ảnh (chỉ cản người dùng thông thường, không chặn được screenshot/DevTools).
- Khi cần thêm/đổi ảnh album: xử lý ảnh gốc bằng Pillow (`ImageOps.exif_transpose` + resize max 2000px + `quality=82`) trước khi bỏ vào `images/album/`, đặt tên tuần tự `album-NN.jpg`, rồi generate lại các `<button class="g-item">` tương ứng trong `index.html` (xem cấu trúc 1 button mẫu trong file).

## Design system

- Palette (lấy từ bảng màu couple tự chọn trong file kế hoạch gốc): Ivory `#FBF6EF`/`#F3E9DD`, Rose đậm `#7C1B27`, Gold `#B8903F`/`#E6C27A`.
- Font: **Cormorant Garamond** (display, tên cô dâu chú rể, số đếm ngược) + **Be Vietnam Pro** (body, hỗ trợ dấu tiếng Việt tốt).
- Single-theme (không có dark mode) — đây là thiệp cưới, cố định 1 mood.
- Reveal-on-scroll dùng IntersectionObserver (`.reveal` class), tôn trọng `prefers-reduced-motion`.

## Deploy

Repo GitHub: **HuyV086/minh-huy-thuy-dung-wedding** (Public — bắt buộc để dùng GitHub Pages free tier).
Live: https://huyv086.github.io/minh-huy-thuy-dung-wedding/

```bash
git add -A && git commit -m "..." && git push
```

GitHub Pages tự rebuild sau ~1 phút. Kiểm tra trạng thái build:
```bash
gh api repos/HuyV086/minh-huy-thuy-dung-wedding/pages/builds/latest --jq .status
```

Xem thử local: `python3 -m http.server 8000` rồi mở `http://localhost:8000`.

## Việc đã lên lịch tự động

Scheduled task **`disable-wedding-site-pages`** sẽ chạy **1/11/2026 09:00** (sau khi cả 2 tiệc kết thúc) để **tắt GitHub Pages** (`gh api -X DELETE repos/.../pages`) — không ai xem được trang nữa, nhưng repo vẫn Public. Nếu user đổi ý (dời ngày, huỷ, hoặc muốn ẩn luôn cả repo), cập nhật/huỷ task này thay vì tạo task mới trùng lặp.

## Nguồn dữ liệu gốc

Toàn bộ nội dung (timeline, ngân sách, khách mời, nhà cung cấp...) được tổng hợp từ Google Drive, folder "Dự án gia đình" → "Đám cưới 10/2026" (tài khoản `huyvm86@gmail.com`), doc "Dự án Đám cưới Minh Huy & Thuỳ Dung — Quản lý tổng" là nguồn tổng hợp mới nhất.
