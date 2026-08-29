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
- Gallery ("Khoảnh khắc"): trình bày dạng **tạp chí ảnh cưới (magazine reader)**, KHÔNG hiện hết 33 ảnh cùng lúc. Trên trang chính chỉ có 1 thẻ bìa tạp chí (`.mag-teaser`, dùng `images/hero.jpg`) — bấm vào mở overlay toàn màn hình (`#magReader`) cho xem lần lượt từng trang kiểu lật tạp chí thật.
  - Cấu trúc dữ liệu: mảng `CHAPTERS` trong `<script>` (3 chương: Ba Son 9 ảnh, Diamond Plaza 10 ảnh, Bảo Tàng 14 ảnh — mỗi chương có `roman`, `title`, `subtitle`, `spreads` là mảng object `{imgs:[...], cap:'...'}` theo số thứ tự global 1–33 tương ứng `images/album/album-NN.jpg`. `cap` là câu trích dẫn ngắn hiển thị dưới ảnh trên trang đó (có thể để trống nếu không cần).
  - Khi ghép nhiều ảnh vào 1 trang (`imgs` có ≥2 phần tử), LUÔN đảm bảo trang đó có ít nhất 1 ảnh có mặt cả cô dâu lẫn chú rể — không ghép 2 ảnh solo-1-người (dù khác người) vào chung 1 trang, sẽ đọc như "mất" người còn lại khỏi trang đó.
  - Mỗi lần mở, JS build danh sách `PAGES` phẳng: 1 trang bìa (có mục lục 3 chương, bấm vào nhảy thẳng tới trang tiêu đề chương) + với mỗi chương: 1 trang tiêu đề (roman số + tên chương + câu mô tả) + các trang ảnh (spread) render theo layout `solo` / `solo-landscape` / `duo` / `trio` tuỳ số ảnh và tỷ lệ khung hình (mảng `LANDSCAPE` liệt kê ảnh nào nằm ngang: 4, 6, 23, 26, 29).
  - Chỉ ảnh của trang hiện tại mới có trong DOM (ảnh trang trước/sau được preload ngầm bằng `new Image()`, không chèn vào DOM) — tránh tải hết 33 ảnh cùng lúc.
  - Điều hướng: nút Trước/Sau, click vùng trái/phải màn hình (click-zone), phím mũi tên, vuốt trái/phải trên mobile, ESC đóng. Có thanh tiến độ + "Trang X / 25 · [Chương]" ở góc trên. Chặn nhẹ right-click/kéo-thả ảnh như cũ.
  - Khi cần đổi/thêm ảnh: xử lý ảnh gốc bằng Pillow (`ImageOps.exif_transpose` + resize max 2000px + `quality=82`) → `images/album/album-NN.jpg`, rồi sửa mảng `CHAPTERS`/`spreads`/`LANDSCAPE` trong `<script>` cho khớp (không cần đụng HTML, toàn bộ trang tạp chí là JS-driven).

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
