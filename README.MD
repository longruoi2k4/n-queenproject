N-Queen Problem Stimulation

Thuật toán giải bải toán tham khảo tại video: 

Tổng quan
Chương trình này là một công cụ hiển thị đồ họa cho bài toán N-Queens sử dụng thư viện Pygame. Bài toán N-Queens trong đó bạn cần đặt N quân hậu trên bàn cờ kích thước N×N sao cho không có hai quân hậu nào đe dọa nhau. Trình hiển thị này cung cấp một biểu diễn đồ họa cho quá trình tìm giải.

Hai biến có thể tùy chỉnh
Biến ROW: số lượng quân hậu trên bàn cờ.
Biến Speed: chỉ thời gian delay sau mỗi lần vẽ lại bảng

Trạng thái của các ô cờ(Spot) được thể hiện qua màu sắc:
-Trắng, đen: Màu mặc định, đại diện cho một vị trí trống trên bàn cờ.
-Vàng: Chỉ ra rằng có một quân hậu được đặt ở vị trí đó.
-Xanh lá cây: Đại diện cho một vị trí trống nơi có thể đặt quân hậu.
-Đỏ: Chỉ một chướng ngại vật, biểu thị mối đe doạ của một quân hậu.
-Xanh dương: Đánh dấu quá trình kiểm tra trong quá trình thực thi thuật toán.


Chi tiết thực hiện

Bàn cờ được biểu diễn bằng một lưới các điểm sử dụng lớp Spot.
Hàm make_grid khởi tạo lưới bàn cờ.
Hàm algorithm thực thi thuật toán N-Queens, và hàm solveNQUtil là một phương pháp quay lui đệ quy để tìm giải.
Hàm draw cập nhật cửa sổ Pygame để hiển thị các thay đổi trên bàn cờ trong quá trình thực thi thuật toán.
Ngoài ra có thêm một số chức năng như tùy trình số hàng, tốc độ và hiển thị luôn kết quả bài toán.
