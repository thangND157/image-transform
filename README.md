# Biến đổi hình học ảnh - Geometric transformation

Thiết kế một ứng dựng có thể thực hiện các phép biến đổi hình học ảnh.

Designing an application that can perform geometry transformations of image.

## Lý thuyết - Theory

**1. Phép tỉ lệ - Scaling**

Phép tỉ lệ làm giãn chiều rộng n lần, giãn chiều cao m lần:

*Scaling stretches the width n times, stretches the height m times:*

![image](https://user-images.githubusercontent.com/94043610/173715439-4bef083a-4a75-401c-9241-38f83730d199.png)

Tính toán trên ma trận:

*Calculation on the matrix:*

![image](https://user-images.githubusercontent.com/94043610/173715464-8f01a031-65b7-4f09-99db-fd216405694c.png)

**2. Phép tịnh tiến - Translation**

Phép tịnh tiến làm điểm ảnh dời đi đoạn dx (trục x) và dy (trục y):

*Translation moves the pixel by dx (x-axis) and dy (y-axis):*

![image](https://user-images.githubusercontent.com/94043610/173715904-6efb5661-1854-4bb2-b40f-22e7c8b3bd59.png)

Tính toán trên ma trận:

*Calculation on the matrix:*

![image](https://user-images.githubusercontent.com/94043610/173715932-887087e0-5688-4547-9ba0-64df6c47b6c2.png)
$$ ={\left\lbrack \matrix{2 & 3 \cr 4 & 5} \right\rbrack} $$

**3. Phép xoay - Rotation**

Phép xoay quanh tâm một góc cho trước:

*Rotation around the origin at a given angle:*

![image](https://user-images.githubusercontent.com/94043610/173716633-c871c337-9fcb-41f1-8858-83d9c5e4439c.png)

Tính toán trên ma trận:

*Calculation on the matrix:*

![image](https://user-images.githubusercontent.com/94043610/173716657-0c3f5574-7b5a-45a0-ae36-90fe08c74ab8.png)

**4 Phép trượt - Shearing**

Phép trượt thay đổi độ dài đường chéo khi dời điểm ảnh theo trục x hoặc y một đoạn:

*Shearing changes the diagonal length when moving pixels along the x or y-axis by a distance:*

![image](https://user-images.githubusercontent.com/94043610/173717122-56f203d8-02c9-4c60-960a-146239ae0e03.png)

Tính toán trên ma trận:

*Calculation on the matrix:*

![image](https://user-images.githubusercontent.com/94043610/173717159-688dd0c5-c8f9-46b5-8eb8-78bcb78c53d7.png)

## Kết quả - Results

Kết quả từ chương trình được so sánh với kết quả từ các hàm có sẵn của OpenCV.

*Results from the program are compared with results from the built-in functions of OpenCV.*

**1. Phép tỉ lệ - Scaling**

![image](https://user-images.githubusercontent.com/94043610/173717872-d584c134-00c8-4cad-b3d9-8e73ef911967.png)

**2. Phép tịnh tiến - Translation**

![image](https://user-images.githubusercontent.com/94043610/173717994-ebefe67e-5007-4805-a32b-8c22af3034d1.png)

**3. Phép xoay - Rotation**

![image](https://user-images.githubusercontent.com/94043610/173718085-05a06370-fa33-4705-b244-44d06bfada80.png)

**4 Phép trượt - Shearing**

![image](https://user-images.githubusercontent.com/94043610/173718123-18dc1a3f-ea85-4be8-9503-5a17202af710.png)

**Các phép biến đổi liên quan tới số thập phân (phép tỉ lệ và phép xoay) sẽ bị sai lệch do không thực hiện nội suy điểm ảnh.**

**Transformations involving floating point numbers (scaling and rotation) will be wrong because pixel interpolation is not performed.**

## More

Nogài ra file `img_trans.py` còn có thêm 2 phép biến đổi là Affine và biến đổi phối cảnh.

In addition, file `img_trans.py` have 2 more transformations: Affine and Perspective.
