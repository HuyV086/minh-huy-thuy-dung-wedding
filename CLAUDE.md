# Wedding Website — Minh Huy & Thùy Dung

Trang cưới tĩnh, 1 file, cho đám cưới **Võ Minh Huy & Bùi Việt Thùy Dung**, ngày cưới chính **Chủ Nhật 18/10/2026** (9/9 Âm lịch, Bính Ngọ).

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
  - Cấu trúc dữ liệu: mảng `CHAPTERS` trong `<script>` (3 chương: Ba Son 9 ảnh, Diamond Plaza 10 ảnh, Bảo Tàng 14 ảnh — mỗi chương có `roman`, `title`, `subtitle`, `spreads` là mảng object `{imgs:[...], cap:{...}}` theo số thứ tự global 1–33 tương ứng `images/album/album-NN.jpg`. `cap` là câu trích dẫn ngắn hiển thị dưới ảnh trên trang đó (có thể để trống nếu không cần). `title`/`subtitle`/`cap` đều là object `{vi:'...', en:'...'}` (xem mục Đa ngôn ngữ bên dưới).
  - Khi ghép nhiều ảnh vào 1 trang (`imgs` có ≥2 phần tử), LUÔN đảm bảo trang đó có ít nhất 1 ảnh có mặt cả cô dâu lẫn chú rể — không ghép 2 ảnh solo-1-người (dù khác người) vào chung 1 trang, sẽ đọc như "mất" người còn lại khỏi trang đó.
  - Mỗi lần mở, JS build danh sách `PAGES` phẳng: 1 trang bìa (có mục lục 3 chương, bấm vào nhảy thẳng tới trang tiêu đề chương) + với mỗi chương: 1 trang tiêu đề (roman số + tên chương + câu mô tả) + các trang ảnh (spread) render theo layout `solo` / `solo-landscape` / `duo` / `trio` tuỳ số ảnh và tỷ lệ khung hình (mảng `LANDSCAPE` liệt kê ảnh nào nằm ngang: 4, 6, 23, 26, 29).
  - Chỉ ảnh của trang hiện tại mới có trong DOM (ảnh trang trước/sau được preload ngầm bằng `new Image()`, không chèn vào DOM) — tránh tải hết 33 ảnh cùng lúc.
  - Điều hướng: nút Trước/Sau, click vùng trái/phải màn hình (click-zone), phím mũi tên, vuốt trái/phải trên mobile, ESC đóng. Có thanh tiến độ + "Trang X / 25 · [Chương]" ở góc trên. Chặn nhẹ right-click/kéo-thả ảnh như cũ.
  - Khi cần đổi/thêm ảnh: xử lý ảnh gốc bằng Pillow (`ImageOps.exif_transpose` + resize max 2000px + `quality=82`) → `images/album/album-NN.jpg`, rồi sửa mảng `CHAPTERS`/`spreads`/`LANDSCAPE` trong `<script>` cho khớp (không cần đụng HTML, toàn bộ trang tạp chí là JS-driven).

## Đa ngôn ngữ (VI/EN)

- Nút chuyển ngôn ngữ (`#langToggle`, VI/EN) cố định góc trên-phải, mặc định **tiếng Việt**, lưu lựa chọn vào `localStorage('lang')` để nhớ giữa các lần ghé.
- Nội dung tĩnh (hero, gia đình, sự kiện, gallery teaser, footer, aria-label): gắn `data-i18n="key"` (hoặc `data-i18n-aria="key"` cho thuộc tính aria-label) trên element, bản dịch nằm trong object `STATIC_I18N` ở cuối `<script>`. Thêm text tĩnh mới → thêm attribute + 1 dòng trong `STATIC_I18N`.
- Nội dung tạp chí (JS-driven): `CHAPTERS[i].title`, `.subtitle`, và mỗi `spreads[j].cap` là object `{vi, en}` thay vì string. `MAG_STRINGS.vi/.en` chứa các chữ khung cố định (Trang/Page, Chương/Chapter, Bìa/Cover...). Khi đổi ngôn ngữ lúc đang mở album, trang hiện tại được render lại tại chỗ (event `langchange`) — không nhảy về trang bìa.
- Bản dịch tiếng Anh của các quote trong tạp chí là dịch thoát ý (không dịch từng chữ) để giữ giọng văn tự nhiên.

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

## Album ảnh/video (album.html)

Trang riêng `album.html` dùng chung repo/Pages với trang thiệp nhưng **độc lập, không có link qua lại với `index.html`** — mục đích là nơi lưu giữ lâu dài cho người thân/bạn bè xem lại, không gắn với trang thiệp nữa. Dữ liệu ở `data/media.json`, nguồn ảnh/video thật thả vào `album-media/<chương>/` rồi chạy `python3 scripts/build_album_manifest.py`. Xem chi tiết cấu trúc chương trong `album-media/README.md` và danh sách `CHAPTERS` trong `scripts/build_album_manifest.py`.

Trước đây có `album-admin.html` (công cụ client-side để sắp xếp/đổi tên/xoá ảnh, export `media.json` qua tải file) nhưng **đã bị xoá khỏi repo** vì user tự sắp xếp ảnh trực tiếp trên máy rồi mới thả vào `album-media/`, không cần admin nữa — và vì trang này public trên GitHub Pages (không yêu cầu đăng nhập) nên xoá luôn để không ai vô tình truy cập được.

**Giao diện**: mỗi chương là 1 hàng "cuốn album" thu gọn (bìa nhỏ + tên + số mục/"Sắp cập nhật"), bấm vào hàng để bung accordion thành lưới thumbnail (ảnh vuông 3:4). Bấm thumbnail mở lightbox xem từng ảnh/video, có nút **Tải về** (`<a download>`) cạnh số đếm. Chỉ 1 album mở cùng lúc. Bấm chip ở đầu trang sẽ tự mở + cuộn tới đúng album. Ảnh lazy-load qua `IntersectionObserver` thủ công (không dùng `loading="lazy"` gốc — xem lịch sử sửa lỗi "ảnh bị lỗi" nếu cần).

Trạng thái nội dung hiện tại (thứ tự chương đúng như hiển thị trên trang):
1. **Ngoại cảnh** (33 ảnh, có chú thích thật)
2. **Đính hôn** (114 ảnh)
3. **Vu quy** (69 ảnh)
4. **Tân hôn** (122 ảnh — gồm cả ảnh từng ở chương "Gia tiên" cũ, đã gộp vào đây rồi xoá chương Gia tiên vì dư thừa)
5. **Hoà Bình 2** (220 ảnh — tên cũ "Nhà hàng", đã đổi tên cả chương lẫn folder `album-media/5-hoa-binh-2/`)
6. **Photobooth 18/10** (89 ảnh)
7. **Bách Việt** (trống, "Sắp cập nhật" — tên cũ "Báo hỷ", đã đổi tên cả chương lẫn folder `album-media/7-bach-viet/`)
8. **Photobooth 31/10** (trống, "Sắp cập nhật" — chờ ảnh sau sự kiện 31/10)
9. **Video** (2 clip nén 720p ~85MB/clip bằng ffmpeg two-pass vì bản gốc 204MB/449MB vượt giới hạn 100MB của GitHub; bản gốc full-quality giữ ở `Video goc/` tại root repo, đã gitignore. Có cover riêng `images/chapters/video/cover.jpg`)
10. **Hậu trường** (165 ảnh)

`album-media/11-chua-xac-dinh/` vẫn còn 30 ảnh nhưng **không nằm trong `CHAPTERS`** của script → không bao giờ hiện lên web, chỉ là nơi user tự tham khảo/điều chỉnh riêng.

Lưu ý khi chạy lại `scripts/build_album_manifest.py`:
- Script build lại TOÀN BỘ nội dung 1 chương từ folder `album-media/` tương ứng — chương nào folder trống thì giữ nguyên dữ liệu cũ (không xoá), chương nào có file thì rebuild từ đầu (mất hết mục không có file gốc tương ứng trong folder, kể cả video thêm tay).
- Field `cover` của 1 chương được giữ nguyên qua các lần rebuild nếu nó vẫn là 1 trong các mục hiện tại CỦA chương đó, HOẶC là file ảnh riêng vẫn còn tồn tại trên đĩa (dùng cho trường hợp đặt cover thủ công ở ngoài `items`, như chương Video) — nếu không sẽ tự lấy ảnh đầu tiên làm cover.
- `album-media/` + `images/chapters/` + `videos/` cộng lại hiện hơn 700MB đã commit vào repo (ảnh nén quality 82, max 2000px/cạnh; video nén 720p) — biết trước nếu thấy repo nặng lên nhiều.

## Việc đã lên lịch tự động

Không còn task tự tắt GitHub Pages — đã huỷ (trước đó có task `disable-wedding-site-pages` định tắt Pages ngày 1/11/2026, nhưng vì `album.html` cần chạy lâu dài nên đã huỷ, giữ Pages bật vĩnh viễn). Đừng tạo lại task kiểu này trừ khi user yêu cầu rõ ràng.

## Nguồn dữ liệu gốc

Toàn bộ nội dung (timeline, ngân sách, khách mời, nhà cung cấp...) được tổng hợp từ Google Drive, folder "Dự án gia đình" → "Đám cưới 10/2026" (tài khoản `huyvm86@gmail.com`), doc "Dự án Đám cưới Minh Huy & Thùy Dung — Quản lý tổng" là nguồn tổng hợp mới nhất.
