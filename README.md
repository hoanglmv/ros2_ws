# 🚀 ROS 2 (Humble) Colcon Workspace - Cẩm Nang Toàn Diện Cho Người Mới Bắt Đầu

Chào mừng bạn đến với **`ros2_ws`**! Đây là dự án không gian làm việc (Colcon Workspace) hoàn chỉnh, được thiết kế chuyên biệt để giúp người mới tiếp cận hệ điều hành robot **ROS 2 (Robot Operating System 2)** từ con số 0.

Dự án này đã được biên dịch sẵn, bao gồm đầy đủ mã nguồn Python chuẩn mực mô phỏng điều khiển cánh tay robot (**OpenArm**), tích hợp toàn bộ các tính năng cốt lõi: **Node, Topic, Service, Action, Parameter, QoS và Launch System**.

---

## 📑 Mục Lục
1. [ROS 2 Là Gì & Điểm Khác Biệt Cốt Lõi](#1-ros-2-là-gì--điểm-khác-biệt-cốt-lõi)
2. [Cấu Trúc Colcon Workspace](#2-cấu-trúc-colcon-workspace)
3. [Cẩm Nang Lệnh `colcon build` (Chi Tiết Từ A - Z)](#3-cẩm-nang-lệnh-colcon-build-chi-tiết-từ-a---z)
   - [A. Colcon Build Là Gì & Cách Hoạt Động](#a-colcon-build-là-gì--cách-hoạt-động)
   - [B. Cú Pháp Chuẩn & Ý Nghĩa Cờ `--symlink-install`](#b-cú-pháp-chuẩn--ý-nghĩa-cờ---symlink-install)
   - [C. Các Cờ Tham Số Nâng Cao Thường Dùng](#c-các-cờ-tham-số-nâng-cao-thường-dùng)
   - [D. Khi Nào Cần Build Lại & Khi Nào Không Cần?](#d-khi-nào-cần-build-lại--khi-nào-không-cần)
   - [E. Quy Trình Clean Build (Dọn Dẹp Triệt Để Khi Gặp Lỗi)](#e-quy-trình-clean-build-dọn-dẹp-triệt-để-khi-gặp-lỗi)
4. [Quy Tắc Vàng Về Nạp Môi Trường (Source Environment)](#4-quy-tắc-vàng-về-nạp-môi-trường-source-environment)
5. [Giải Thích Toàn Diện Các Khái Niệm Quan Trọng](#5-giải-thích-toàn-diện-các-khái-niệm-quan-trọng)
   - [A. Node (Nút tính toán độc lập)](#a-node-nút-tính-toán-độc-lập)
   - [B. Topic & Message (Truyền tin 1 chiều liên tục)](#b-topic--message-truyền-tin-1-chiều-liên-tục)
   - [C. Service (Giao tiếp Yêu cầu - Phản hồi 1-1)](#c-service-giao-tiếp-yêu-cầu---phản-hồi-1-1)
   - [D. Action (Tác vụ dài hạn có Feedback & Huỷ ngang)](#d-action-tác-vụ-dài-hạn-có-feedback--huỷ-ngang)
   - [E. Parameter (Tham số cấu hình động lúc runtime)](#e-parameter-tham-số-cấu-hình-động-lúc-runtime)
   - [F. QoS (Quality of Service - Chất lượng dịch vụ mạng)](#f-qos-quality-of-service---chất-lượng-dịch-vụ-mạng)
   - [G. Launch File (Hệ thống khởi chạy tự động)](#g-launch-file-hệ-thống-khởi-chạy-tự-động)
6. [Bảng Tra Cứu Lệnh Dòng Lệnh (CLI Cheat-Sheet Đầy Đủ)](#6-bảng-tra-cứu-lệnh-dòng-lệnh-cli-cheat-sheet-đầy-đủ)
7. [Hướng Dẫn Thực Hành Step-by-Step (Từng Bước Chi Tiết)](#7-hướng-dẫn-thực-hành-step-by-step-từng-bước-chi-tiết)
   - [Bước 1: Nạp môi trường & Build Workspace](#bước-1-nạp-môi-trường--build-workspace)
   - [Bước 2: Thực hành Node & Topic (Publisher & Subscriber)](#bước-2-thực-hành-node--topic-publisher--subscriber)
   - [Bước 3: Thực hành Service Server & Service Client](#bước-3-thực-hành-service-server--service-client)
   - [Bước 4: Thực hành Action Server & Action Client (Tiến độ thời gian thực)](#bước-4-thực-hành-action-server--action-client-tiến-độ-thời-gian-thực)
   - [Bước 5: Thực hành Đọc & Cập Nhật Parameter Động](#bước-5-thực-hành-đọc--cập-nhật-parameter-động)
   - [Bước 6: Thực hành Chạy Hệ Thống Bằng Launch File & Cấu Hình YAML](#bước-6-thực-hành-chạy-hệ-thống-bằng-launch-file--cấu-hình-yaml)
8. [Các Lỗi Thường Gặp (Troubleshooting) & Cách Xử Lý Nhanh](#8-các-lỗi-thường-gặp-troubleshooting--cách-xử-lý-nhanh)

---

## 1. ROS 2 Là Gì & Điểm Khác Biệt Cốt Lõi

**ROS 2 (Robot Operating System 2)** không phải là một hệ điều hành độc lập như Windows hay Ubuntu, mà là một **bộ khung phần mềm trung gian (Middleware Framework)** cung cấp:
- Giao thức truyền thông điệp phân tán giữa các bộ phận của robot.
- Trình điều khiển phần cứng (Cảm biến, Động cơ, Camera, Lidar).
- Các gói thư viện thuật toán chuẩn (SLAM, Navigation 2, MoveIt 2).
- Các công cụ trực quan hóa (Rviz2, Rqt).

### Điểm khác biệt vượt trội của ROS 2 so với ROS 1:
1. **Không còn nút trung tâm (`roscore`)**: ROS 2 dựa trên chuẩn công nghiệp **DDS (Data Distribution Service)**, các Node tự động tìm thấy nhau (Zero-configuration discovery). Nếu một node bị sập, toàn bộ hệ thống còn lại vẫn hoạt động bình thường.
2. **Hỗ trợ thời gian thực (Real-time)**: Tối ưu cho các tác vụ điều khiển động cơ yêu cầu độ trễ cực thấp.
3. **Đa nền tảng**: Chạy tốt trên Linux (Ubuntu), Windows, macOS và cả vi điều khiển nhỏ (micro-ROS trên ESP32, STM32).
4. **Bảo mật mạng (SROS 2)**: Tích hợp mã hóa TLS/DDS Security chống nghe lén và điều khiển trái phép.

---

## 2. Cấu Trúc Colcon Workspace

Một không gian làm việc Colcon Workspace tiêu chuẩn phân chia mã nguồn và sản phẩm biên dịch thành 4 thư mục rõ ràng:

```text
ros2_ws/
├── src/                                  # [1. Source Space] Mã nguồn các package do bạn viết
│   ├── openarm_demo_py/                  # Package Python: Node, Topic, Service, Action, Param
│   │   ├── package.xml                   # File chứng minh thư manifest của package
│   │   ├── setup.py                      # Đăng ký lệnh thực thi (console_scripts)
│   │   ├── setup.cfg                     # Cấu hình cài đặt thư viện
│   │   └── openarm_demo_py/              # Module Python chứa logic
│   │       ├── __init__.py
│   │       ├── topic_publisher.py        # Publisher: /joint_states và /arm_status
│   │       ├── topic_subscriber.py       # Subscriber: nhận dữ liệu, xử lý an toàn
│   │       ├── service_server.py         # Service Server: /set_arm_power & /calc_target_pos
│   │       ├── service_client.py         # Service Client: gửi yêu cầu bất đồng bộ
│   │       ├── param_demo.py             # Parameters: khai báo, bắt sự kiện thay đổi
│   │       ├── action_server.py          # Action Server: /execute_trajectory (Feedback & Cancel)
│   │       └── action_client.py          # Action Client: theo dõi tiến độ thời gian thực
│   │
│   └── openarm_bringup/                  # Package Khởi chạy (Launch) & File cấu hình
│       ├── package.xml
│       ├── setup.py
│       ├── config/
│       │   └── arm_params.yaml           # File cấu hình tham số YAML
│       └── launch/
│           ├── arm_pub_sub.launch.py     # File khởi động nhiều node cùng lúc
│           └── full_system.launch.py     # File nạp cấu hình YAML tự động
│
├── build/                                # [2. Build Space] Thư mục chứa file tạm khi build
├── install/                              # [3. Install Space] Thành phẩm sau khi build (chứa setup.bash)
└── log/                                  # [4. Log Space] Nhật ký ghi lại tiến trình build
```

---

## 3. Cẩm Nang Lệnh `colcon build` (Chi Tiết Từ A - Z)

### A. Colcon Build Là Gì & Cách Hoạt Động?
`colcon` (viết tắt của **COLlective CONstruction**) là công cụ biên dịch chính thức của ROS 2 (thay thế cho `catkin_make` trong ROS 1).
Khi bạn gõ lệnh `colcon build`, công cụ này sẽ:
1. Quét toàn bộ thư mục `src/` để tìm tất cả các thư mục con có chứa file `package.xml`.
2. Phân tích đồ thị phụ thuộc (Dependency Graph) để biết package nào cần được build trước, package nào build sau.
3. Sử dụng đa luồng CPU để build đồng thời nhiều package độc lập.
4. Gom tất cả các file thực thi, file thư viện, file launch vào thư mục `install/` và tạo sẵn script `setup.bash`.

---

### B. Cú Pháp Chuẩn & Ý Nghĩa Cờ `--symlink-install`

Lệnh build tiêu chuẩn bạn **luôn luôn nên dùng**:
```bash
colcon build --symlink-install
```

> 🌟 **Tại sao cờ `--symlink-install` lại cực kỳ quan trọng?**
> - **Nếu KHÔNG có `--symlink-install`:** Mỗi lần bạn gõ `colcon build`, colcon sẽ **copy nguyên văn** các file code `.py`, file launch `.py`, file cấu hình `.yaml` từ `src/` sang thư mục `install/`. Khi bạn mở file code trong `src/` ra chỉnh sửa, những sửa đổi đó **sẽ KHÔNG có hiệu lực** cho đến khi bạn chạy lại `colcon build`!
> - **Khi CÓ `--symlink-install`:** Thay vì copy, colcon sẽ tạo một **liên kết mềm (Symbolic Link)** từ `install/` trỏ ngược về file gốc trong `src/`. Nhờ đó, mỗi lần bạn sửa code Python hoặc sửa file launch, bạn chỉ cần nhấn **Ctrl + S (Lưu file)** là code mới có tác dụng ngay lập tức, **KHÔNG CẦN BUILD LẠI**!

---

### C. Các Cờ Tham Số Nâng Cao Thường Dùng

| Lệnh colcon | Mục đích sử dụng |
| :--- | :--- |
| `colcon build --symlink-install` | Build toàn bộ workspace và tạo liên kết mềm (khuyên dùng hàng ngày). |
| `colcon build --packages-select <pkg_name> --symlink-install` | **Chỉ build duy nhất 1 package chỉ định.** Tiết kiệm thời gian cực lớn khi workspace của bạn có hàng chục package. |
| `colcon build --packages-up-to <pkg_name> --symlink-install` | Build package chỉ định kèm theo tất cả các package mà nó phụ thuộc vào. |
| `colcon build --packages-ignore <pkg_name>` | Bỏ qua không build một package nào đó (ví dụ package đang bị lỗi dở dang). |
| `colcon build --parallel-workers 2` | **Giới hạn số luồng build đồng thời.** Cực kỳ hữu ích khi chạy trên máy yếu hoặc Raspberry Pi để tránh bị tràn RAM (Out of Memory). |
| `colcon build --continue-on-error` | Nếu một package bị lỗi, colcon vẫn tiếp tục build nốt các package còn lại thay vì dừng ngay lập tức. |

**Ví dụ thực tế:** Chỉ muốn build lại package `openarm_demo_py`:
```bash
colcon build --packages-select openarm_demo_py --symlink-install
```

---

### D. Khi Nào Cần Build Lại & Khi Nào Không Cần?

Nếu bạn đã build với cờ `--symlink-install`, hãy áp dụng bảng quy tắc sau:

| Hành động của bạn | Cần chạy lại `colcon build` không? |
| :--- | :---: |
| Chỉnh sửa nội dung logic bên trong file Python có sẵn (`.py`) | ❌ **KHÔNG CẦN** (Chỉ cần lưu file là xong) |
| Chỉnh sửa nội dung file cấu hình YAML (`.yaml`) | ❌ **KHÔNG CẦN** |
| Tạo một file Python mới và đăng ký thêm vào `setup.py` | ✅ **CẦN BUILD LẠI** |
| Thêm thư viện/phụ thuộc mới vào file `package.xml` | ✅ **CẦN BUILD LẠI** |
| Thêm file launch mới vào thư mục `launch/` | ✅ **CẦN BUILD LẠI** |
| Viết hoặc sửa code C++ (`.cpp`, `.hpp`) | ✅ **BẮT BUỘC BUILD LẠI** |

---

### E. Quy Trình Clean Build (Dọn Dẹp Triệt Để Khi Gặp Lỗi)

Trong quá trình phát triển, đôi khi bạn đổi tên file, xoá package hoặc sửa cấu hình khiến cache biên dịch cũ bị xung đột và báo lỗi khó hiểu. Khi đó, hãy thực hiện **Clean Build**:

```bash
# 1. Đi về thư mục gốc workspace:
cd ~/Project/OpenArm/Demos/ROS2_WS

# 2. Xóa sạch 3 thư mục do colcon tự sinh ra:
rm -rf build/ install/ log/

# 3. Biên dịch lại từ đầu:
colcon build --symlink-install

# 4. Nạp lại môi trường:
source install/setup.bash
```

---

## 4. Quy Tắc Vàng Về Nạp Môi Trường (Source Environment)

Mỗi khi bạn mở một **cửa sổ Terminal mới**, bạn **bắt buộc** phải nạp 2 script môi trường sau trước khi chạy lệnh:

```bash
# 1. Nạp ROS 2 hệ thống (Underlay):
source /opt/ros/humble/setup.bash

# 2. Nạp các package trong workspace của bạn (Overlay):
source install/setup.bash
```

> 💡 **Mẹo:** Bạn có thể thêm dòng `source /opt/ros/humble/setup.bash` vào file `~/.bashrc` để không phải gõ lại mỗi lần mở máy:
> ```bash
> echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
> ```

---

## 5. Giải Thích Toàn Diện Các Khái Niệm Quan Trọng

### A. Node (Nút tính toán độc lập)
* **Khái niệm:** Node là một tiến trình thực thi độc lập (Microservice). Mỗi node đảm nhận đúng một nhiệm vụ duy nhất (Ví dụ: 1 node đọc camera, 1 node điều khiển góc quay motor, 1 node hiển thị UI).
* **Vòng đời:** Khởi tạo (`rclpy.init()`) $\rightarrow$ Khởi tạo class node $\rightarrow$ Lắng nghe / chạy vòng lặp xử lý (`rclpy.spin()`) $\rightarrow$ Dọn dẹp & giải phóng (`rclpy.shutdown()`).

### B. Topic & Message (Truyền tin 1 chiều liên tục)
* **Khái niệm:** Giao thức truyền tin bất đồng bộ theo mô hình **Publish / Subscribe (Xuất bản / Đăng ký nhận)**. 
* **Đặc điểm:** Không quan tâm người nhận là ai; 1 Topic có thể có nhiều Publisher và nhiều Subscriber.
* **Khi nào nên dùng?** Khi dữ liệu mang tính chu kỳ liên tục, mất một vài gói tin không làm sập hệ thống (Ví dụ: Toạ độ góc khớp tay máy `/joint_states`, hình ảnh camera, đám mây điểm Lidar).

### C. Service (Giao tiếp Yêu cầu - Phản hồi 1-1)
* **Khái niệm:** Mô hình giao tiếp đồng bộ hoặc bất đồng bộ **Client / Server (2 chiều)**. Client gửi 1 yêu cầu (Request), Server xử lý và trả về 1 phản hồi (Response).
* **Đặc điểm:** 1 Service chỉ có 1 Server phục vụ, nhưng có thể có nhiều Client gọi tới.
* **Khi nào nên dùng?** Khi bạn cần xác nhận chắc chắn hành động đã thành công hay chưa, hoặc chỉ kích hoạt khi có sự kiện (Ví dụ: Bật/tắt nguồn motor `/set_arm_power`, hiệu chuẩn toạ độ Home, đổi chế độ).

### D. Action (Tác vụ dài hạn có Feedback & Huỷ ngang)
* **Khái niệm:** Giao thức giao tiếp cao cấp nhất trong ROS 2, gồm 3 phần:
  1. **Goal (Mục tiêu):** Client gửi lệnh yêu cầu Server thực hiện mục tiêu.
  2. **Feedback (Tiến độ):** Trong khi đang thực hiện, Server liên tục gửi cập nhật trạng thái về Client.
  3. **Result (Kết quả):** Khi mục tiêu hoàn tất, Server trả về kết quả cuối cùng.
  * *Hỗ trợ Huỷ ngang (Cancel / Preempt):* Client có thể gửi lệnh huỷ bất kỳ lúc nào nếu gặp chướng ngại vật khẩn cấp.
* **Khi nào nên dùng?** Cho các tác vụ tốn nhiều thời gian (Ví dụ: Di chuyển cánh tay theo quỹ đạo 6 điểm, điều hướng xe tự hành từ phòng khách sang nhà bếp).

### E. Parameter (Tham số cấu hình động lúc runtime)
* **Khái niệm:** Các biến cấu hình lưu trữ trực tiếp bên trong từng Node (Ví dụ: `max_speed`, `robot_name`, `wheel_radius`).
* **Đặc điểm:** Cho phép xem và thay đổi giá trị trong thời gian thực bằng CLI hoặc file YAML mà **không cần phải tắt hay khởi động lại Node**. Có thể cài đặt hàm callback để chặn các giá trị vượt ngưỡng an toàn.

### F. QoS (Quality of Service - Chất lượng dịch vụ mạng)
* **Khái niệm:** Cơ chế của mạng DDS cho phép bạn cấu hình mức độ ưu tiên truyền tin:
  - **Reliability:**
    - `RELIABLE`: Đảm bảo gói tin không bị mất (phù hợp cho lệnh điều khiển, vị trí khớp).
    - `BEST_EFFORT`: Bỏ qua gói tin cũ để ưu tiên tốc độ mới nhất (phù hợp camera, lidar).
  - **History & Depth:** Lưu trữ bao nhiêu tin nhắn gần nhất (`KEEP_LAST`, độ sâu hàng đợi depth=10).

### G. Launch File (Hệ thống khởi chạy tự động)
* **Khái niệm:** Các file viết bằng Python (`.launch.py`) mô tả cách khởi động cả một cụm nhiều Node, thiết lập thông số, đổi tên topic (remapping) và nạp file YAML cấu hình chỉ bằng **một câu lệnh duy nhất**.

---

## 6. Bảng Tra Cứu Lệnh Dòng Lệnh (CLI Cheat-Sheet Đầy Đủ)

| Nhóm lệnh | Cú pháp lệnh | Giải thích chức năng |
| :--- | :--- | :--- |
| **Workspace** | `colcon build --symlink-install` | Biên dịch toàn bộ workspace, tạo symlink cho Python |
| | `colcon build --packages-select <pkg>` | Chỉ biên dịch duy nhất 1 package chỉ định |
| | `source /opt/ros/humble/setup.bash` | Nạp ROS 2 hệ thống vào terminal hiện tại |
| | `source install/setup.bash` | Nạp các package trong workspace của bạn |
| **Node** | `ros2 pkg executables <tên_pkg>` | Liệt kê các node thực thi có sẵn trong package |
| | `ros2 node list` | Liệt kê các node **đang chạy thực tế** trong RAM |
| | `ros2 node info <tên_node>` | Xem chi tiết Publisher, Subscriber, Service của Node |
| **Topic** | `ros2 topic list` | Xem danh sách các topic đang hoạt động |
| | `ros2 topic list -t` | Xem danh sách topic kèm kiểu dữ liệu (Message Type) |
| | `ros2 topic echo <tên_topic>` | In trực tiếp dữ liệu truyền trên topic ra terminal |
| | `ros2 topic hz <tên_topic>` | Đo tần số gửi tin thực tế (Hz / FPS) |
| | `ros2 topic info <tên_topic>` | Xem số lượng Publisher và Subscriber đang kết nối |
| | `ros2 topic pub <topic> <type> "<data>"` | Tự phát một bản tin từ dòng lệnh lên topic |
| **Service** | `ros2 service list` | Xem danh sách các service đang mở |
| | `ros2 service type <tên_service>` | Xem kiểu dữ liệu của service |
| | `ros2 interface show <kiểu_srv>` | Xem cấu trúc Request và Response |
| | `ros2 service call <srv> <type> "<data>"` | Gửi yêu cầu gọi service trực tiếp từ terminal |
| **Parameter**| `ros2 param list` | Xem danh sách toàn bộ tham số của các node |
| | `ros2 param get <node> <param>` | Lấy giá trị hiện tại của tham số |
| | `ros2 param set <node> <param> <value>` | Đổi giá trị tham số trong thời gian thực |
| | `ros2 param dump <node>` | Xuất các giá trị tham số của node ra file YAML |
| **Action** | `ros2 action list` | Liệt kê các Action Server đang hoạt động |
| | `ros2 action info <tên_action>` | Xem thông tin chi tiết của Action |
| | `ros2 action send_goal <act> <type> "<goal>" --feedback` | Gửi mục tiêu và theo dõi tiến độ Feedback |

---

## 7. Hướng Dẫn Thực Hành Step-by-Step (Từng Bước Chi Tiết)

### Bước 1: Nạp Môi Trường & Build Workspace

Mở một cửa sổ Terminal mới và di chuyển vào workspace:
```bash
cd ~/Project/OpenArm/Demos/ROS2_WS

# 1. Nạp ROS 2 nền tảng:
source /opt/ros/humble/setup.bash

# 2. Biên dịch toàn bộ các gói:
colcon build --symlink-install

# 3. Nạp gói vừa build vào terminal:
source install/setup.bash
```
> **Kết quả mong đợi:** Terminal báo `Summary: 2 packages finished`.

---

### Bước 2: Thực Hành Node & Topic (Publisher & Subscriber)

#### A. Khởi chạy Publisher (Chạy ngầm):
```bash
ros2 run openarm_demo_py arm_publisher &
```
*(Nếu muốn chạy ở màn hình chính xem log phát toạ độ khớp liên tục, bạn bỏ dấu `&` đi).*

#### B. Kiểm tra hoạt động của Node & Topic:
```bash
# 1. Kiểm tra node đang chạy:
ros2 node list
# -> Hiện: /arm_joint_publisher

# 2. Kiểm tra các topic đang được phát:
ros2 topic list
# -> Hiện: /arm_status và /joint_states

# 3. Đo tần số phát toạ độ khớp:
ros2 topic hz /joint_states
# -> Báo trung bình: average rate: 2.000 Hz

# 4. "Nghe" trực tiếp dữ liệu góc khớp robot đang xoay hình sin:
ros2 topic echo /joint_states
```
*(Bấm `Ctrl + C` để dừng in dữ liệu).*

#### C. Chạy Subscriber để nhận dữ liệu:
Mở một terminal khác (đã source môi trường) và chạy:
```bash
ros2 run openarm_demo_py arm_subscriber
```
> **Kết quả:** Subscriber sẽ tự động bắt sóng cả 2 topic `/arm_status` và `/joint_states`, sau đó in log toạ độ 4 khớp robot (`joint_base`, `joint_shoulder`, `joint_elbow`, `joint_wrist`).

---

### Bước 3: Thực Hành Service Server & Service Client

#### A. Khởi chạy Service Server:
```bash
ros2 run openarm_demo_py arm_service_server &
```

#### B. Kiểm tra danh sách Service:
```bash
ros2 service list
# Sẽ có: /set_arm_power và /calc_target_pos
```

#### C. Gọi Service từ Terminal (Bật/Tắt nguồn tay máy):
```bash
# Bật nguồn motor tay máy:
ros2 service call /set_arm_power example_interfaces/srv/SetBool "{data: true}"
# -> Trả về: success=True, message='Nguồn động cơ tay máy ĐÃ ĐƯỢC BẬT (Motors Enabled).'

# Tắt nguồn motor:
ros2 service call /set_arm_power example_interfaces/srv/SetBool "{data: false}"
# -> Trả về: success=True, message='Nguồn động cơ tay máy ĐÃ ĐƯỢC NGẮT (Motors Disabled).'
```

#### D. Gọi Service bằng Python Client:
```bash
ros2 run openarm_demo_py arm_service_client true
```

---

### Bước 4: Thực Hành Action Server & Action Client (Tiến Độ Thời Gian Thực)

#### A. Khởi chạy Action Server:
```bash
ros2 run openarm_demo_py arm_action_server &
```

#### B. Gửi Goal từ Terminal kèm theo dõi Feedback:
Gửi lệnh yêu cầu thực hiện chuỗi quỹ đạo 6 bước:
```bash
ros2 action send_goal /execute_trajectory example_interfaces/action/Fibonacci "{order: 6}" --feedback
```
> **Kết quả:** Terminal sẽ hiển thị từng bước tiến độ:
> - `Feedback: sequence=[0, 1, 1]`
> - `Feedback: sequence=[0, 1, 1, 2]`
> - ...
> - `Result: sequence=[0, 1, 1, 2, 3, 5, 8]`
> - `Goal reached successfully!`

#### C. Chạy Action Client viết bằng Python:
```bash
ros2 run openarm_demo_py arm_action_client 5
```

---

### Bước 5: Thực Hành Đọc & Cập Nhật Parameter Động

#### A. Khởi chạy Node Quản Lý Tham Số:
```bash
ros2 run openarm_demo_py arm_param_demo &
```
Node này tự động in giá trị các tham số mỗi 3 giây một lần.

#### B. Xem danh sách và đọc giá trị:
```bash
ros2 param list /arm_param_demo
ros2 param get /arm_param_demo max_speed
# -> Double value is: 1.0
```

#### C. Cập nhật tham số trong thời gian thực:
```bash
# 1. Cập nhật giá trị hợp lệ (0.0 < max_speed <= 2.0):
ros2 param set /arm_param_demo max_speed 1.8
# -> Trả về: Set parameter(s) successfully

# 2. Thử đặt giá trị vi phạm giới hạn an toàn (> 2.0):
ros2 param set /arm_param_demo max_speed 3.5
# -> Node sẽ TỪ CHỐI và cảnh báo: 'max_speed phải nằm trong khoảng (0.0, 2.0]!'
```

---

### Bước 6: Thực Hành Chạy Hệ Thống Bằng Launch File & Cấu Hình YAML

Thay vì phải mở 4 - 5 terminal để chạy từng Node riêng lẻ, bạn chỉ cần dùng **1 lệnh Launch**:

#### A. Khởi chạy đồng thời Publisher và Subscriber:
```bash
ros2 launch openarm_bringup arm_pub_sub.launch.py
```
> Bạn có thể truyền trực tiếp thông số cấu hình trên dòng lệnh:
> ```bash
> ros2 launch openarm_bringup arm_pub_sub.launch.py robot_name:=OpenArm_Titan publish_rate_hz:=5.0
> ```

#### B. Khởi chạy toàn bộ hệ sinh thái nạp thông số từ file YAML:
File cấu hình tại [`src/openarm_bringup/config/arm_params.yaml`](file:///home/myvh/Project/OpenArm/Demos/ROS2_WS/src/openarm_bringup/config/arm_params.yaml) chứa sẵn cấu hình tham số. Chạy lệnh:
```bash
ros2 launch openarm_bringup full_system.launch.py
```
Toàn bộ Publisher, Subscriber và Service Server sẽ tự động được khởi tạo cùng với các tham số chuẩn!

---

## 8. Các Lỗi Thường Gặp (Troubleshooting) & Cách Xử Lý Nhanh

### ❌ Lỗi 1: `Package 'openarm_demo_py' not found`
* **Nguyên nhân:** Cửa sổ Terminal hiện tại chưa được nạp thông tin đường dẫn sau khi build.
* **Cách sửa:** Gõ lệnh:
  ```bash
  source install/setup.bash
  ```

### ❌ Lỗi 2: `ros2 node list` không in ra gì (No output)
* **Nguyên nhân:** Lệnh này chỉ quét các tiến trình Node **đang chạy trong RAM**. Bạn chưa chạy node nào bằng `ros2 run` hoặc `ros2 launch`.
* **Cách sửa:** Chạy thử 1 node trước (`ros2 run openarm_demo_py arm_publisher &`), sau đó gõ lại `ros2 node list`.

### ❌ Lỗi 3: `Unknown topic '/joint_states'`
* **Nguyên nhân:** Topic trong ROS 2 là động (Dynamic). Khi Node phát bị tắt (`pkill` hoặc `Ctrl+C`), Topic đó sẽ tự động biến mất khỏi mạng.
* **Cách sửa:** Bật lại Node phát trước khi dùng lệnh `ros2 topic echo` hoặc `ros2 topic info`.

### ❌ Lỗi 4: Sửa code Python nhưng chạy lại không thấy thay đổi
* **Nguyên nhân:** Khi build quên gắn cờ `--symlink-install`.
* **Cách sửa:** Chạy lại lệnh build đúng chuẩn:
  ```bash
  colcon build --symlink-install
  ```

---

## 👨‍💻 Tác Giả & Đóng Góp
- **Tác giả:** [hoanglmv](https://github.com/hoanglmv)
- **Repository:** [https://github.com/hoanglmv/ros2_ws](https://github.com/hoanglmv/ros2_ws)
- **Mã nguồn:** Giấy phép mã nguồn mở Apache-2.0.
