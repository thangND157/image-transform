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

**3. Phép xoay - Rotation**

Phép xoay quanh tâm một góc cho trước:

*Rotation around the origin at a given angle:*

![image](https://user-images.githubusercontent.com/94043610/173716633-c871c337-9fcb-41f1-8858-83d9c5e4439c.png)

Tính toán trên ma trận:

*Calculation on the matrix:*

![image](https://user-images.githubusercontent.com/94043610/173716657-0c3f5574-7b5a-45a0-ae36-90fe08c74ab8.png)

**4 Phép trượt - Shearing**

