# Lab 5 — Lê Quang Khải — 2A202603237

Bài thực hành MOT tracking trên 150 frame của MOT17-09, đề B. Nhãn được học viên gán và sửa thủ công trong CVAT local.

## File bài nộp

- [Báo cáo cá nhân](report/individual/2A202603237_LeQuangKhai.md).
- [MOT 1.1](src/exports/LeQuangKhai_mot.zip), chứa `gt/gt.txt` và `gt/labels.txt`.
- [CVAT for video 1.1](src/exports/LeQuangKhai_cvat_video.zip), chứa `annotations.xml`.
- [Ảnh trước che — frame 20](report/individual/images/che_1_truoc.png).
- [Ảnh giữa che — frame 42](report/individual/images/che_2_giua.png).
- [Ảnh sau che — frame 60](report/individual/images/che_3_sau.png).

## Kết quả tự kiểm

12 track, 849 box, 104 keyframe có box; không có Shape rời. Job CVAT đã completed. Hai ZIP không kèm ảnh gốc. Bản CVAT đang lưu đã được đối chiếu với các keyframe trong XML xuất.

Theo xác nhận của học viên, mentor cho phép số người được gán linh hoạt. Tool có tùy chọn riêng cho ngoại lệ này; các kiểm tra khác được giữ nguyên:

```bash
python3 src/check_submission.py --mot src/exports/LeQuangKhai_mot.zip --cvat src/exports/LeQuangKhai_cvat_video.zip --allow-any-track-count
```

Kết quả: **0 lỗi, 1 cảnh báo**. Cảnh báo còn lại là XML track 9 có 3 keyframe trên 5 frame nhìn thấy (60 keyframe/100 frame); báo cáo có số liệu và nhận xét. Tool không tính MOTA/IDF1 hoặc thay thế kiểm tra nhãn bằng mắt. Những giới hạn của ghi chép xem trước, frame lỗi và thời gian riêng từng người được nêu rõ trong báo cáo.

## Quy định và nguồn

Đề gốc và tài liệu: [VinUni-AI20k/K5-L2-MOTTracking](https://github.com/VinUni-AI20k/K5-L2-MOTTracking), [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [SUBMISSION.md](SUBMISSION.md), [RULES.md](RULES.md).

Nguồn dữ liệu và ảnh minh chứng: MOT17, MOTChallenge (Milan et al., 2016), CC BY-NC-SA 3.0. Bộ bài không nộp ảnh frame/video hoặc ground truth gốc. Báo cáo mục 7 mô tả phạm vi hỗ trợ AI; không dùng model sinh box/track ID để nộp.
