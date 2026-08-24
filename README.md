# Minh Huy & Thuỳ Dung — Wedding Website

Trang cưới của Minh Huy & Thuỳ Dung, ngày cưới **18/10/2026** (9/9 Âm lịch, Bính Ngọ).

## Cấu trúc

- `index.html` — toàn bộ trang (1 file, không phụ thuộc build tool)
- `images/` — 3 ảnh cưới dùng trong trang

## Chỉnh sửa

Mở `index.html` bằng bất kỳ editor nào. Các phần chính:

- Thông tin ngày cưới / countdown: tìm `2026-10-18T09:00:00+07:00` trong thẻ `<script>`
- Hai họ: section `.families`
- Lịch trình 3 sự kiện: section `.events`
- Ảnh: section `.gallery`, thay file trong `images/` rồi sửa `src` tương ứng

## Xem thử local

```bash
python3 -m http.server 8000
```

rồi mở `http://localhost:8000`.

## Deploy (khi cần public cho khách mời)

Có thể host miễn phí bằng **GitHub Pages**:

1. Vào Settings → Pages của repo này
2. Source: chọn branch `main`, thư mục `/ (root)`
3. Sau vài phút trang sẽ có ở `https://<username>.github.io/<repo-name>/`

Hoặc dùng Netlify/Vercel (kéo thả cả folder này vào là chạy) nếu muốn có tên miền riêng.
